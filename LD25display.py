#TODO: Display the number of weeks during calculation phase results.

import time


def printText(stringList):
    """
    Prints strings in list word with a 0.2 second time step between each string.
    """
    for i in stringList:
        print i
        time.sleep(0.1)


###############################################################################
# Simulation - General Display Functions
###############################################################################
def printKeyAndTitle(simState):
    key1 = ["\nSIMULATION: {} \n".format(simState.name),
            "{}\n".format(simState.phase),
            "\nKEY",
            "----------",
            "ID:   Robot's ID number",
            "AGE:  Years robot has been in service",
            "CARR: Tens of pounds robot can carry",
            "BATT: Battery life of robot",
            "UTIL: Rating of robot's ability to complete varied tasks",
            "COST: Weekly costs of maintaining robot",
            "BRKS: Number of times robot has broken down"]
    printText(key1)
    
    if simState.phase == 'SIMULATION RESULTS':
        key2 = ["T.OUT: Robot's total output over simulated timeframe",
                "A.OUT: Robot's average output per week over simulated timeframe"]
        printText(key2)


###############################################################################
# Simulation - Placement Phase Display Functions
###############################################################################
def pDisplayWorkplace(workplace):
    """
    Displays the robots in a workplace and their stats in table form.
    """
    print "\n{} ROBOTS".format(workplace.name)
    time.sleep(0.2)
    
    if workplace.maxRobots == None:
        print "NO MAXIMUM"
        time.sleep(0.2)
    else:
        print "MAX NUMBER OF ROBOTS:", workplace.maxRobots
        time.sleep(0.2)
        
    head = ["  ID  AGE CARR BATT UTIL COST BRKS",
            "----------------------------------"]
    printText(head)
    
    for robot in workplace.robots:
        print repr(robot.id).rjust(4), repr(robot.age).rjust(4),
        print repr(robot.strength).rjust(4), repr(robot.battery).rjust(4),
        print repr(robot.utility).rjust(4), repr(robot.cost).rjust(4),
        print repr(robot.breakdowns).rjust(4)
    

def pDisplay(simState):
    """
    Prints console information during the robot placement phase of simulation.
    """
    printKeyAndTitle(simState)
    
    for workplace in simState.workplaces:
        pDisplayWorkplace(workplace)


def pCommandMenu(workplaces):
    """
    Displays console commands during the robot placement phase of simulation.
    """
    cmd1 = ["\nCOMMAND   | EFFECT",
            "----------|----------------------------------------------"]
    printText(cmd1)
    for workplace in workplaces:
        if workplace.cmd == "NONE":
            print "NONE [ID] | Return robot to unassigned robot pool"
        else:
            print "{} [ID] | Move robot with ID number [ID] to {}".format(workplace.cmd,
                                                                          workplace.name)
    cmd2 = ["UPDATE    | Reprint robot lists",
            "RUN       | Run simulation"]
    printText(cmd2)
    

###############################################################################
# Simulation - Calculation Phase Display Functions
###############################################################################
def cStatus(i, cycles):
    """
    Calls to time.sleep() inserted because calculation takes almost no time.
    """
    tenths = cycles/10
    
    if i == 0:
        print "\n\nSIMULATING. PLEASE WAIT..."
        time.sleep(0.2)
    elif i == tenths:
        print "...10% complete"
        time.sleep(0.2)
    elif i == tenths*2:
        print "...20% complete"
        time.sleep(0.2)
    elif i == tenths*3:
        print "...30% complete"
        time.sleep(0.2)
    elif i == tenths*4:
        print "...40% complete"
        time.sleep(0.2)
    elif i == tenths*5:
        print "...50% complete"
        time.sleep(0.2)
    elif i == tenths*6:
        print "...60% complete"
        time.sleep(0.2)
    elif i == tenths*7:
        print "...70% complete"
        time.sleep(0.2)
    elif i == tenths*8:
        print "...80% complete"
        time.sleep(0.2)
    elif i == tenths*9:
        print "...90% complete"
        time.sleep(0.2)
    elif i == (cycles-1):
        print "SIMULATION COMPLETE.\n"
        time.sleep(0.2)


###############################################################################
# Simulation - Results Phase Display Functions
###############################################################################
def rDisplayWorkplaceResults(workplace, weeks):
    """
    Displays results of the calculation phase of simulation in table format for
    the Workplace instance given.
    """
    head = ["\n{} ROBOTS".format(workplace.name),
            "INDIVIDUAL OUTPUTS",
            "  ID  AGE CARR BATT UTIL COST BRKS |    T.OUT  A.OUT",
            "-----------------------------------|----------------"]
    printText(head)
    for robot in workplace.robots:
        print repr(robot.id).rjust(4), repr(robot.age).rjust(4),
        print repr(robot.strength).rjust(4), repr(robot.battery).rjust(4),
        print repr(robot.utility).rjust(4), repr(robot.cost).rjust(4),
        print repr(robot.breakdowns).rjust(4), '|',
        print repr(robot.output).rjust(8), repr(robot.output/weeks).rjust(6)
    
    summ = ["\nTOTAL {} OUTPUT: {}".format(workplace.name,
                                           workplace.getTotalOutput()),
            "\nAVERAGE WEEKLY OUTPUT PER ROBOT: {}".format(workplace.getAvgOutput(weeks))]
    printText(summ)


def rEnd():
    """
    Displays console commands after the calculation phase of simulation
    is complete.
    """
    cmds = ["\nCOMMAND   | EFFECT",
            "----------|----------------------------------------------",
            "RESTART   | Restart simulation.",
            "DECOM     | Choose robots to decommission.\n"]
    printText(cmds)