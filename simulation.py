#TODO: Make command list a property of the SimState

import random
import string
import time
import copy

import classes
from classes import workclass
from classes import robotclass
from displays import *
from displays import sim


errorCMD = ["\nERROR: Robot does not exist or command was mistyped.",
            "Please try again."]
errorMaxRobots = ["\nERROR: Maximum robot capacity exceeded.",
                  "Please remove one or more robots from destination before adding more."]


def init_robots(workplace_to_be):
    robots = []
    if workplace_to_be.robots_are_old:
        id = random.randint(337, 742)
        for i in range(workplace_to_be.number_of_robots):
            age = random.randint(5, 20)
            strength = (random.randint(50, 150)/10) - age/5.0
            battery = (random.randint(90, 150)/10) - age/5.0
            utility = random.randint(1, 10)
            cost = random.randint(35, 150)
            breakdowns = random.choice(workplace_to_be.breakdown_chance)

            robots.append(robotclass.LaborRobot(id, age, strength, battery,
                                                utility, cost, breakdowns))
            id += random.randint(4, 10)
    else:
        id = random.randint(925, 986)
        for i in range(workplace_to_be.number_of_robots):
            age = 0
            strength = random.randint(70, 190)/10
            battery = random.randint(100, 160)/10
            utility = random.randint(1, 10)
            cost = random.randint(55, 180)

            robots.append(robotclass.LaborRobot(id, age, strength, battery,
                                                utility, cost))
            id += 1
    
    return robots


def build_cmd_list(workplaces):
    cmd_list = ['UPDATE', 'RUN']
    for workplace in workplaces:
        cmd_list.append(workplace.cmd)
    return cmd_list


def placement_phase(sim_state):
    sim.placement_display(sim_state)
    cmd_list = build_cmd_list(sim_state.workplaces)
    
    command = [None]
    while command[0] != 'RUN':
        sim.placement_cmd(sim_state.workplaces)
        input = raw_input("\nPlease choose an option from above:")
        command = input.upper().split()
        command.append(' ')
        
        if command[0] not in cmd_list:
            print_text(errorCMD)
        elif command[0] == 'UPDATE':
            sim.placement_display(sim_state)
        elif command[0] == 'RUN':
            break
        else:
            for workplace in sim_state.workplaces:
                if command[0] == workplace.cmd:
                    id = int(command[1])
                    old_home = workplace
                
                    found = False
                    while not found:
                        for other in sim_state.workplaces:
                            if other is workplace:
                                continue
                            else:
                                for robot in other.robots:
                                    if robot.id == id:
                                        old_home = other
                                        found = True
                                        break
                        #Robot not found anywhere; break loop w/o changing oldHome.
                        break
                    
                    if old_home == workplace:
                        print_text(errorCMD)
                    else:
                        move = old_home.removeRobot(id)
                        try:
                            workplace.add_robot(move)
                            print "\nSUCCESS. Robot #{} moved from {} to {}.".format(id,
                                                                                     old_home.name,
                                                                                     workplace.name)
                        except workclass.TooManyRobots:
                            old_home.add_robot(move)
                            print_text(errorMaxRobots)


def calculation_phase(sim_state):
    sim_state.phase = 'CALCULATION'
    for i in range(sim_state.weeks):
        for workplace in sim_state.workplaces:
            workplace.update()
        sim.calc_status(i, sim_state.weeks)
        

def results_phase(sim_state):
    sim_state.phase = 'SIMULATION RESULTS'
    sim.print_key(sim_state)
    for workplace in sim_state.workplaces:
        sim.results(workplace, sim_state.weeks)

    restart = True
    done_yet = False
    while not done_yet:
        sim.end_menu()
        input = raw_input("\nPlease choose an option from above:")
        command = input.upper().split()
        command.append(' ')
        
        if command[0] == 'RESTART':
            done_yet = True
        elif command[0] == 'DECOM':
            id_nums = []
            for workplace in sim_state.workplaces:
                for robot in workplace.robots:
                    id_nums.append(robot.id)
                
            for i in range(sim_state.robots_to_discard_num):
                extant = False
                while not extant:
                    input = raw_input("Enter ID of robot #{} to be decommissioned:".format(i+1))
                    try:
                        if int(input) in id_nums:
                            extant = True
                        else:
                            print_text(errorID)
                    except ValueError:
                        input = ' '
                        print_text(errorID)
            print '\nSIMULATION COMPLETE\n'
            restart = False
            done_yet = True
        else:
            print_text(errorCMD)
    
    return restart


def run_sim(workplaces_to_be, robots_to_discard_num, sim_name="SIMULATION"):
    workplaces = []
    for i in workplaces_to_be:
        robots = init_robots(i)
        workplaces.append(i.constructor(i.number_of_robots, copy.deepcopy(robots),
                                        i.name, i.cmd))
    
    sim_running = True
    while sim_running:
        sim_state = classes.SimState(robots_to_discard_num, copy.deepcopy(workplaces),
                                    sim_name)
        
        placement_phase(sim_state)
        calculation_phase(sim_state)
        sim_running = results_phase(sim_state)

if __name__ == '__main__':
    workplaces_to_be = []
    workplaces_to_be.append(workclass.WorkplaceToBe(7, True, workclass.Farm,
                                                    "FARM", "FARM"))
    workplaces_to_be.append(workclass.WorkplaceToBe(5, True, workclass.Factory,
                                                    "FACTORY", "FACT"))
    workplaces_to_be.append(workclass.WorkplaceToBe(2, False, workclass.Unassigned,
                                                    "UNASSIGNED", "NONE"))
    run_sim(workplaces_to_be, 2, "TEST #1")
