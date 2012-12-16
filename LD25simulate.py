import random
import string
from LD25class import *
from LD25display import *

BREAKDOWN_CHANCE = [0, 0, 1, 1, 2, 3]
WEEKS_NUM = 104

def initRobots(number, old):
    """
    Returns a list of LaborRobot objects with randomized attributes.
    
    number: Number of robot objects to create (a positive int).
    old: A bool indicating whether or not the robots are old robots.
    """
    robots = []
    
    if old:
        id = random.randint(337, 742)
        for i in range(number):
            age = random.randint(5, 20)
            strength = (random.randint(50, 150)/10) - age/5.0
            battery = (random.randint(90, 150)/10) - age/5.0
            utility = random.randint(1, 10)
            cost = random.randint(35, 150)
            breakdowns = random.choice(BREAKDOWN_CHANCE)
            
            robots.append(LaborRobot(id, age, strength, battery, utility,
                                     cost, breakdowns))
            id += random.randint(4, 10)
    else:
        id = random.randint(925, 986)
        for i in range(number):
            age = 0
            strength = random.randint(70, 190)/10
            battery = random.randint(100, 160)/10
            utility = random.randint(1, 10)
            cost = random.randint(55, 180)
            
            robots.append(LaborRobot(id, age, strength, battery, utility,
                                     cost))
            id += 1
    
    return robots


def runSim(oldRobots, newRobots, simName="Simulation"):
    """
    Runs the robot simulation with the given parameters.
    
    oldRobots: Number of robots in operation at the site (a non-negative int).
    newRobots: Number of incoming brand new robots to fit in (a positive int).
    numWorks: Number of workplaces (a positive int).
    simName: Name of current simulation.
    """
    #Initialization.
    oldRobotL = initRobots(oldRobots, True)
    newRobotL = initRobots(newRobots, False)
        
    farmRobots = oldRobots/random.randint(2, 4)
    factoryRobots = oldRobots - farmRobots
    
    unassigned = Unassigned(newRobotL[:])
    farm = Farm(farmRobots, random.randint(1, 7), oldRobotL[:farmRobots])
    factory = Factory(factoryRobots, random.randint(1,7), oldRobotL[farmRobots:])
    
    rerun = True
    
    while rerun:
        #Robot placements.
        pDisplay(unassigned, farm, factory, simName)
    
        command = [False]
    
        while command[0] != 'run':
            pCommand()
            input = raw_input("\nPlease choose an option from above:")
            command = input.lower().split()
            command.append(' ')
    
            if command[0] == 'farm':
                id = int(command[1])
                oldHome = farm
            
                for robot in factory.robots():
                    if robot.idNum() == id:
                        oldHome = factory
                        break
                    
                if oldHome == farm:
                    for robot in unassigned.robots():
                        if robot.idNum() == id:
                            oldHome = unassigned
                            break
            
                move = oldHome.rem(id)
                try:
                    farm.addRobo(move)
                except TooManyRobots:
                    oldHome.addRobo(move)
                    print "ERROR: Farm already contains max number of robots."
                    print "Please remove robots from farm before adding more."
            elif command[0] == 'factory':
                id = int(command[1])
                oldHome = factory
            
                for robot in farm.robots():
                    if robot.idNum() == id:
                        oldHome = farm
                        break
            
                if oldHome == factory:
                    for robot in unassigned.robots():
                        if robot.idNum() == id:
                            oldHome = unassigned
                            break
            
                move = oldHome.rem(id)
                try:
                    factory.addRobo(move)
                except TooManyRobots:
                    oldHome.addRobo(move)
                    print "ERROR: Factory already contains max number of robots."
                    print "Please remove robots from farm before adding more."
            elif command[0] == 'none':
                id = int(command[1])
                oldHome = unassigned
            
                for robot in factory.robots():
                    if robot.idNum() == id:
                        oldHome = factory
                        break
                if oldHome == unassigned:
                    for robot in farm.robots():
                        if robot.idNum() == id:
                            oldHome = farm
                            break
            
                move = oldHome.rem(id)
                unassigned.addRobo(move)
            elif command[0] == 'update':
                pDisplay(unassigned, farm, factory, simName)
            elif command[0] == 'run':
                break
            else:
                print "Invalid command. Please try again."

        #Run simulation.
        for i in range(WEEKS_NUM):
            factory.update()
            farm.update()
            sStatus(i, WEEKS_NUM)
    
        #Display results.
        keyAndTitle(1, simName)
        rWork(farm, 0, WEEKS_NUM, simName)
        rWork(factory, 1, WEEKS_NUM, simName)

        choice = raw_input("Rerun simulation?")
