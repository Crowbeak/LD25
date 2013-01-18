import random
import string
import time
from LD25class import *
from LD25display import *

BREAKDOWN_CHANCE = [0, 0, 1, 1, 2, 3]
WEEKS_NUM = 104

errorCMD = ["\nERROR: Robot does not exist or command was mistyped.",
            "Please try again."]
errorMaxRobots = ["\nERROR: Maximum robot capacity exceeded.",
                  "Please remove one or more robots from destination before adding more."]

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
def placementPhase(workplaces, simName):
    pDisplay(workplaces, simName)
    
    command = [False]
    
    while command[0] != 'run':
        pCommandMenu()
        input = raw_input("\nPlease choose an option from above:")
        command = input.lower().split()
        command.append(' ')
        
        if command[0] == 'update':
            pDisplay(workplaces, simName)
        elif command[0] == 'run':
            break
        else:
            for workplace in workplaces:
                if command[0] == workplace.cmd:
                    id = int(command[1])
                    oldHome = workplace
                
                    found = False
                    while not found:
                        for other in workplaces:
                            if other is workplace:
                                continue
                            else:
                                for robot in other.robots:
                                    if robot.id == id:
                                        oldHome = other
                                        found = True
                                        break
                        #Robot not found anywhere; break loop w/o changing oldHome.
                        break
                    
                    if oldHome == workplace:
                        printText(errorCMD)
                    else:
                        move = oldHome.removeRobot(id)
                        try:
                            workplace.addRobot(move)
                        except TooManyRobots:
                            oldHome.addRobot(move)
                            printText(errorMaxRobots)


#TODO: Make this take a SimState instance. (Maybe?)
def calculationPhase(workplaces):
    for i in range(WEEKS_NUM):
        for workplace in workplaces:
            workplace.update()
        cStatus(i, WEEKS_NUM)
        

#TODO: Make this take a SimState instance.
#TODO: Make this take newRobotsNum from SimState
def resultsPhase(workplaces, simName, newRobotsNum):
    printKeyAndTitle(1, simName)
    for workplace in workplaces:
        rDisplayWorkplaceResults(workplace, WEEKS_NUM, simName)

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
            for workplace in workplaces:
                for robot in workplace.robots:
                    idNums.append(robot.id)
                
            for i in range(newRobotsNum):
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


def runSim(oldRobotsNum, newRobotsNum, simName="Simulation"):
    oldRobotL = initRobots(oldRobotsNum, True)
    newRobotL = initRobots(newRobotsNum, False)
    farmAvgDowntime = random.randint(1, 7)
    factAvgDowntime = random.randint(1, 7)
    farmRobotsNum = oldRobotsNum/random.randint(2, 4)
    factoryRobotsNum = oldRobotsNum - farmRobotsNum
    
    simRunning = True
    while simRunning:
        unassigned = Unassigned(newRobotL[:])
        farm = Farm(farmRobotsNum, farmAvgDowntime, oldRobotL[:farmRobotsNum])
        factory = Factory(factoryRobotsNum, factAvgDowntime, oldRobotL[farmRobotsNum:])
        workplaces = [farm, factory, unassigned]
        #simulation = SimState(workplaces, simName)
        
        placementPhase(workplaces, simName)
        calculationPhase(workplaces)
        simRunning = resultsPhase(workplaces, simName, newRobotsNum)

if __name__ == '__main__':
    runSim(10, 2)
