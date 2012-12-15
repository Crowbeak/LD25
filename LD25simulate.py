import random
import string
from LD25class import *
from LD25display import *

BREAKDOWN_CHANCE = [0, 0, 1, 1, 2, 3]

def initRobots(number, old, robots=[]):
    """
    Returns a list of LaborRobot objects with randomized attributes.
    
    number: Number of robot objects to create (a positive int).
    old: A bool indicating whether or not the robots are old robots.
    """
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
    robots = initRobots(oldRobots, True)
    robots = initRobots(newRobots, False, robots[:])
        
    farmRobots = oldRobots/random.randint(2, 4)
    factoryRobots = oldRobots - farmRobots
    
    unassigned = Unassigned(robots)
    farm = Farm(farmRobots, random.randint(1, 7))
    factory = Factory(factoryRobots, random.randint(1,7))
    
    #Placement
    pDisplay(simName, unassigned, farm, factory)
    
    command = [False]
    
    while command[0] != 'run':
        pCommand()
        comm = raw_input("\nPlease choose an option from above:")
        command = comm.lower().split()
    
        if command[0] == 'farm':
            moved = False
            temp = factory.robots()
            for i in range(len(temp)):
                if temp[i].idNum() == int(command[1]):
                    farm.add(factory.remove(int(command[1])))
                    moved = True
                    break
            if not moved:
                temp = unassigned.robots()
                for i in range(len(temp)):
                    if temp[i].idNum() == int(command[1]):
                        farm.add(unassigned.remove(int(command[1])))
                        moved = True
                        break
            if not moved:
                print "Robot not found."
        elif command[0] == 'factory':
            pass
        elif command[0] == 'none':
            pass
        elif command[0] == 'update':
            pDisplay(simName, unassigned, farm, factory)
        elif command[0] == 'run':
            break
        else:
            print "Invalid command. Please try again."