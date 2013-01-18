#TODO: Make Workplace instance name (farm, etc.) an attribute of the instance
#      so it can be called without having to reference a constant.
#      This would allow for two farms, etc, without having to build in silly
#      lines of code.
#TODO: Display the number of weeks during calculation phase results.

import time

PHASES = ['ROBOT PLACEMENT', 'SIMULATION RESULTS']


def printText(stringList):
    """
    Prints strings in list word with a 0.2 second time step between each string.
    """
    for i in stringList:
        print i
        time.sleep(0.1)


#TODO: Make this work. Currently unused.
def initErrors():
    errors = {}
    errors[id] = ["ERROR: Invalid robot ID number.",
                  "Please try again."]
    errors[farmMax] = ["ERROR: Farm already contains max number of robots.",
                       "Please remove one or more robots from farm before adding more."]
    errors[factoryMax] = ["ERROR: Factory already contains max number of robots.",
                          "Please remove one or more robots from factory before adding more."]
    errors[commands] = ['Invalid command. Please try again.']
    return errors


###############################################################################
# Simulation - General Display Functions
###############################################################################
#TODO: Make this take a simulation object instead of a name and number.
def printKeyAndTitle(num, simName='Simulation'):
    """
    num: The index of the appropriate subtitle in PHASES (a non-negative int).
    simName: Simulation name (a string).
    """
    key1 = ["\nSIMULATION: {} \n".format(simName),
            "{}\n".format(PHASES[num]),
            "KEY",
            "----------",
            "ID:   Robot's ID number",
            "AGE:  Years robot has been in service",
            "CARR: Tens of pounds robot can carry",
            "BATT: Battery life of robot",
            "UTIL: Rating of robot's ability to complete varied tasks",
            "COST: Weekly costs of maintaining robot",
            "BRKS: Number of times robot has broken down"]
    printText(key1)
    
    if num == 1:
        key2 = ["T.OUT: Robot's total output over simulated timeframe",
                "A.OUT: Robot's average output per week over simulated timeframe"]
        printText(key2)


###############################################################################
# Simulation - Placement Phase Display Functions
###############################################################################
def pDisplayWorkplace(work):
    """
    Displays the robots in a workplace and their stats in table form.
    
    work: a Workplace instance.
    """
    print "\n{} ROBOTS".format(work.type)
    time.sleep(0.2)
    
    if work.maxRobots == None:
        print "NO MAXIMUM"
        time.sleep(0.2)
    else:
        print "MAX NUMBER OF ROBOTS:", work.maxRobots
        time.sleep(0.2)
        
    head = ["  ID  AGE CARR BATT UTIL COST BRKS",
            "----------------------------------"]
    printText(head)
    
    for robot in work.robots:
        print repr(robot.id).rjust(4), repr(robot.age).rjust(4),
        print repr(robot.strength).rjust(4), repr(robot.battery).rjust(4),
        print repr(robot.utility).rjust(4), repr(robot.cost).rjust(4),
        print repr(robot.breakdowns).rjust(4)
    

#TODO: Make this take a list of Wrokplace objects instead of specific ones.
def pDisplay(unassigned, farm, factory, simName='Simulation'):
    """
    Prints console information during the robot placement phase of simulation.
    
    unassigned: an Unassigned instance.
    farm: a Farm instance.
    factory: a Factory instance.
    simName: the simulation name (a string).
    """
    printKeyAndTitle(0, simName)
    
    pDisplayWorkplace(farm)
    pDisplayWorkplace(factory)
    pDisplayWorkplace(unassigned)


#TODO: Make this take a simulation object so it can print lines based on
#      available work sites.
def pCommandMenu():
    """
    Displays console commands during the robot placement phase of simulation.
    """
    commands = ["\nCOMMANDS",
                "----------",
                "FARM [ID]    - Move robot with ID number [ID] to the farm",
                "FACTORY [ID] - Move robot with ID number [ID] to the factory",
                "NONE [ID]    - Return robot to unassigned robot pool",
                "UPDATE       - Reprint robot lists",
                "RUN          - Run simulation"]
    printText(commands)
    

###############################################################################
# Simulation - Calculation Phase Display Functions
###############################################################################
def cStatus(i, duration):
    """
    Calls to time.sleep() inserted because calculation takes almost no time.
    """
    tenths = duration/10
    
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
    elif i == (duration-1):
        print "SIMULATION COMPLETE.\n"
        time.sleep(0.2)


###############################################################################
# Simulation - Results Phase Display Functions
###############################################################################
def rDisplayWorkplaceResults(work, weeks, simName='Simulation'):
    """
    Displays results of the calculation phase of simulation for the Workplace
    instance given.
    
    work: a Workplace instance (any type).
    weeks: number of weeks over which the results were calculated.
    simName: the name of the simulation (a string).
    """
    head = ["\n{} ROBOTS".format(work.type),
            "INDIVIDUAL OUTPUTS",
            "  ID  AGE CARR BATT UTIL COST BRKS |    T.OUT  A.OUT",
            "-----------------------------------|----------------"]
    printText(head)
    
    for robot in work.robots:
        print repr(robot.id).rjust(4), repr(robot.age).rjust(4),
        print repr(robot.strength).rjust(4), repr(robot.battery).rjust(4),
        print repr(robot.utility).rjust(4), repr(robot.cost).rjust(4),
        print repr(robot.breakdowns).rjust(4), '|',
        print repr(robot.output).rjust(8), repr(robot.output/weeks).rjust(6)
    
    #TODO: Try to make this a nice list. Parentheses?
    print "\nTOTAL {} OUTPUT:".format(work.type), work.getTotalOutput()
    time.sleep(0.2)
    print "\nAVERAGE WEEKLY OUTPUT PER ROBOT:", work.getAvgOutput(weeks)
    time.sleep(0.2)


def rEnd():
    """
    Displays console commands after the calculation phase of simulation
    is complete.
    """
    commands = ["\nCOMMANDS",
                "----------",
                "RESTART  - Restart simulation.",
                "DECOM - Choose robots to decommission.\n"]
    printText(commands)