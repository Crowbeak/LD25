#TODO: Create three functions -- placement, calculate, and resutls -- to make
#      runSim more readable.
#TODO: Create special 

import random
import string
import time
from LD25class import *
from LD25display import *

BREAKDOWN_CHANCE = [0, 0, 1, 1, 2, 3]
WEEKS_NUM = 104

errorID = ["\nERROR: Invalid robot ID number.",
           "Please try again."]
errorFarmMax = ["\nERROR: Farm already contains max number of robots.",
                "Please remove one or more robots from farm before adding more."]
errorFactoryMax = ["\nERROR: Factory already contains max number of robots.",
                   "Please remove one or more robots from factory before adding more."]
errorCMD = ['\nInvalid command. Please try again.']

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


#TODO: Make this take a SimState instance.
#TODO: Create moveRobotTo(works, command) function for readability.
def placementPhase(workplaces, simName):
    pDisplay(workplaces, simName)
    
    command = [False]
    
    while command[0] != 'run':
        pCommandMenu()
        input = raw_input("\nPlease choose an option from above:")
        command = input.lower().split()
        command.append(' ')
    
        if command[0] == workplaces[0].name.lower():
            id = int(command[1])
            oldHome = workplaces[0]
            
            for robot in workplaces[1].robots:
                if robot.id == id:
                    oldHome = workplaces[1]
                    break
                    
            if oldHome == workplaces[0]:
                for robot in workplaces[2].robots:
                    if robot.id == id:
                        oldHome = workplaces[2]
                        break
                
            if oldHome == workplaces[0]:
                printText(errorID)
            else:
                move = oldHome.removeRobot(id)
                try:
                    workplaces[0].addRobot(move)
                except TooManyRobots:
                    oldHome.addRobot(move)
                    printText(errorFarmMax)
        elif command[0] == workplaces[1].name.lower():
            id = int(command[1])
            oldHome = workplaces[1]
            
            for robot in workplaces[0].robots:
                if robot.id == id:
                    oldHome = workplaces[0]
                    break
            
            if oldHome == workplaces[1]:
                for robot in workplaces[2].robots:
                    if robot.id == id:
                        oldHome = workplaces[2]
                        break
                            
            if oldHome == workplaces[1]:
                printText(errorID)
            else:
                move = oldHome.removeRobot(id)
                try:
                    workplaces[1].addRobot(move)
                except TooManyRobots:
                    oldHome.addRobot(move)
                    printText(errorFactoryMax)
        elif command[0] == 'none':
            id = int(command[1])
            oldHome = workplaces[2]
            
            for robot in workplaces[0].robots:
                if robot.id == id:
                    oldHome = workplaces[0]
                    break
            if oldHome == workplaces[2]:
                for robot in workplaces[1].robots:
                    if robot.id == id:
                        oldHome = workplaces[1]
                        break
                
            if oldHome == workplaces[2]:
                printText(errorID)
            else:
                move = oldHome.removeRobot(id)
                workplaces[2].addRobot(move)
        elif command[0] == 'update':
            pDisplay(workplaces, simName)
        elif command[0] == 'run':
            break
        else:
            printText(errorCMD)


#TODO: Make this take a SimState instance.
def calculationPhase(farm, factory):
    for i in range(WEEKS_NUM):
        factory.update()
        farm.update()
        cStatus(i, WEEKS_NUM)
        

#TODO: Make this take a SimState instance.
def resultsPhase(farm, factory, simName):
    printKeyAndTitle(1, simName)
    rDisplayWorkplaceResults(farm, WEEKS_NUM, simName)
    rDisplayWorkplaceResults(factory, WEEKS_NUM, simName)

    restart = True
    doneYet = False
    while not doneYet:
        rEnd()
        input = raw_input("\nPlease choose an option from above:")
        command = input.lower().split()
        command.append(' ')
        
        if command[0] == 'restart':
            doneYet = True
        elif command[0] == 'decom':
            idNums = []
            for robot in farm.robots:
                idNums.append(robot.id)
            for robot in factory.robots:
                idNums.append(robot.id)
            for robot in unassigned.robots:
                idNums.append(robot.id)
                
            for i in range(newRobots):
                extant = False
                while not extant:
                    input = raw_input("Enter ID of robot #{} to be decommissioned:".format(i+1))
                    try:
                        if int(input) in idNums:
                            extant = True
                        else:
                            printText(errorID)
                    except ValueError:
                        input = ' '
                        printText(errorID)
            print '\nSIMULATION COMPLETE\n'
            restart = False
            doneYet = True
        else:
            printText(errorCMD)
    
    return restart


def runSim(oldRobots, newRobots, simName="Simulation"):
    """
    oldRobots: Number of robots in operation at the site (a non-negative int).
    newRobots: Number of incoming new robots to fit in (a positive int).
    simName: Name of current simulation.
    """
    oldRobotL = initRobots(oldRobots, True)
    newRobotL = initRobots(newRobots, False)
    farmAvgDowntime = random.randint(1, 7)
    factAvgDowntime = random.randint(1, 7)
    farmRobotsNum = oldRobots/random.randint(2, 4)
    factoryRobotsNum = oldRobots - farmRobotsNum
    
    simRunning = True
    while simRunning:
        unassigned = Unassigned(newRobotL[:])
        farm = Farm(farmRobotsNum, farmAvgDowntime, oldRobotL[:farmRobotsNum])
        factory = Factory(factoryRobotsNum, factAvgDowntime, oldRobotL[farmRobotsNum:])
        workplaces = [farm, factory, unassigned]
        #simulation = SimState(workplaces, simName)
        
        placementPhase(workplaces, simName)
        calculationPhase(farm, factory)
        simRunning = resultsPhase(farm, factory, simName)

if __name__ == '__main__':
    runSim(10, 2)
