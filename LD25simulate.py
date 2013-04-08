import random
import string
import time
import copy
from LD25class import *
from LD25display import *

#TODO: Make breakdown chance an attribute of a workplaceToBe instance.
BREAKDOWN_CHANCE = [0, 0, 1, 1, 2, 3]

errorCMD = ["\nERROR: Robot does not exist or command was mistyped.",
            "Please try again."]
errorMaxRobots = ["\nERROR: Maximum robot capacity exceeded.",
                  "Please remove one or more robots from destination before adding more."]


def initRobots(workplaceToBe):
    robots = []
    if workplaceToBe.robotsAreOld:
        id = random.randint(337, 742)
        for i in range(workplaceToBe.numberOfRobots):
            age = random.randint(5, 20)
            strength = (random.randint(50, 150)/10) - age/5.0
            battery = (random.randint(90, 150)/10) - age/5.0
            utility = random.randint(1, 10)
            cost = random.randint(35, 150)
            breakdowns = random.choice(BREAKDOWN_CHANCE)

            robots.append(LaborRobot(id, age, strength, battery, utility, cost,
                                     breakdowns))
            id += random.randint(4, 10)
    else:
        id = random.randint(925, 986)
        for i in range(workplaceToBe.numberOfRobots):
            age = 0
            strength = random.randint(70, 190)/10
            battery = random.randint(100, 160)/10
            utility = random.randint(1, 10)
            cost = random.randint(55, 180)

            robots.append(LaborRobot(id, age, strength, battery, utility,
                                     cost))
            id += 1
    
    return robots


def buildPossibleCMD(workplaces):
    possibleCMD = ['UPDATE', 'RUN']
    for workplace in workplaces:
        possibleCMD.append(workplace.cmd)
    return possibleCMD


def placementPhase(simState):
    pDisplay(simState)
    possibleCMD = buildPossibleCMD(simState.workplaces)
    
    command = [False]
    while command[0] != 'RUN':
        pCommandMenu(simState.workplaces)
        input = raw_input("\nPlease choose an option from above:")
        command = input.upper().split()
        command.append(' ')
        
        if command[0] not in possibleCMD:
            printText(errorCMD)
        elif command[0] == 'UPDATE':
            pDisplay(simState)
        elif command[0] == 'RUN':
            break
        else:
            for workplace in simState.workplaces:
                if command[0] == workplace.cmd:
                    id = int(command[1])
                    oldHome = workplace
                
                    found = False
                    while not found:
                        for other in simState.workplaces:
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
                            print "\nSUCCESS. Robot #{} moved from {} to {}.".format(id,
                                                                                     oldHome.name,
                                                                                     workplace.name)
                        except TooManyRobots:
                            oldHome.addRobot(move)
                            printText(errorMaxRobots)


def calculationPhase(simState):
    simState.phase = 'CALCULATION'
    for i in range(simState.weeks):
        for workplace in simState.workplaces:
            workplace.update()
        cStatus(i, simState.weeks)
        

def resultsPhase(simState):
    simState.phase = 'SIMULATION RESULTS'
    printKeyAndTitle(simState)
    for workplace in simState.workplaces:
        rDisplayWorkplaceResults(workplace, simState.weeks)

    restart = True
    doneYet = False
    while not doneYet:
        rEnd()
        input = raw_input("\nPlease choose an option from above:")
        command = input.upper().split()
        command.append(' ')
        
        if command[0] == 'RESTART':
            doneYet = True
        elif command[0] == 'DECOM':
            idNums = []
            for workplace in simState.workplaces:
                for robot in workplace.robots:
                    idNums.append(robot.id)
                
            for i in range(simState.robotsToDiscardNum):
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


def runSim(workplacesToBe, robotsToDiscardNum, simName="SIMULATION"):
    workplaces = []
    for i in workplacesToBe:
        robots = initRobots(i)
        workplaces.append(i.constructor(i.numberOfRobots, copy.deepcopy(robots),
                                        i.name, i.cmd))
    
    simRunning = True
    while simRunning:
        simState = SimState(robotsToDiscardNum, copy.deepcopy(workplaces),
                            simName)
        
        placementPhase(simState)
        calculationPhase(simState)
        simRunning = resultsPhase(simState)

if __name__ == '__main__':
    workplacesToBe = []
    workplacesToBe.append(WorkplaceToBe(7, True, Farm, "FARM", "FARM"))
    workplacesToBe.append(WorkplaceToBe(5, True, Factory, "FACTORY", "FACT"))
    workplacesToBe.append(WorkplaceToBe(2, False, Unassigned, "UNASSIGNED",
                                        "NONE"))
    runSim(workplacesToBe, 2, "TEST #1")
