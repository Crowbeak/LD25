#TODO: Make Workplace instance name (farm, etc.) an attribute of the instance
#      so it can be called without having to reference a constant.
#      This would allow for two farms, etc, without having to build in silly
#      lines of code.

import time

PHASES = ['ROBOT PLACEMENT', 'SIMULATION RESULTS']
WORKS = ['FARM', 'FACTORY', 'UNASSIGNED']


def disp(stringList):
    """
    Prints strings in list word with a 0.2 second time step between each string.
    """
    for i in stringList:
        print i
        time.sleep(0.1)


#TODO: Make this take a simulation object instead of a name.
def keyAndTitle(num, simName='Simulation'):
    """
    Prints key and title for the display output.
    
    num: The index of the appropriate subtitle in PHASES (a non-negative int).
    simName: Simulation name (a string).
    """
    print "\nSIMULATION: {} \n".format(simName)
    time.sleep(0.2)
    print "{}".format(PHASES[num])
    time.sleep(0.2)
    
    key1 = ["KEY",
            "----------",
            "ID:   Robot's ID number",
            "AGE:  Years robot has been in service",
            "CARR: Tens of pounds robot can carry",
            "BATT: Battery life of robot",
            "UTIL: Rating of robot's ability to complete varied tasks",
            "COST: Weekly costs of maintaining robot",
            "BRKS: Number of times robot has broken down"]
    disp(key1)
    
    if num == 1:
        print "T.OUT: Robot's total output over simulated timeframe."
        time.sleep(0.2)
        print "A.OUT: Robot's average output per week over simulated timeframe."
        time.sleep(0.2)


def pWork(work, num):
    """
    Displays 
    num: index in WORKS
    #TODO: proper description
    """
    print "\n{} ROBOTS".format(WORKS[num])
    time.sleep(0.2)
    if work.getMax() == None:
        print "NO MAXIMUM"
        time.sleep(0.2)
    else:
        print "MAX NUMBER OF ROBOTS:", work.getMax()
        time.sleep(0.2)
    print "  ID  AGE CARR BATT UTIL COST BRKS"
    time.sleep(0.2)
    print "----------------------------------"
    
    for robot in work.robots():
        id, age, str, batt, util, cost, brks, out = robot.stats()
        print repr(id).rjust(4), repr(age).rjust(4), repr(str).rjust(4),
        print repr(batt).rjust(4), repr(util).rjust(4), repr(cost).rjust(4),
        print repr(brks).rjust(4)
    

#TODO: Make pDisplay take a list of Wrokplace objects instead of specific ones.
def pDisplay(unassigned, farm, factory, simName='Simulation'):
    """
    Prints console information during the robot placement phase of simulation.
    
    unassigned
    """
    keyAndTitle(0, simName)
    
    pWork(farm, 0)
    pWork(factory, 1)
    pWork(unassigned, 2)


#TODO: Make this take a simulation object so it can print lines based on
#      available work sites.
def pCommand():
    """
    Displays console commands during the robot placement phase of simulation.
    """
    word = ["\nCOMMANDS",
            "----------",
            "FARM [ID]    - Move robot with ID number [ID] to the farm",
            "FACTORY [ID] - Move robot with ID number [ID] to the factory",
            "NONE [ID]    - Return robot to unassigned robot pool",
            "UPDATE       - Reprint robot lists",
            "RUN          - Run simulation"]
    disp(word)
    

def sStatus(i, duration):
    #TODO: description.
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
    elif i == (weeks-1):
        print "SIMULATION COMPLETE.\n"
        time.sleep(0.2)


def rWork(work, num, weeks, simName='Simulation'):
    """
    Takes a Workplace instance as an argument and displays results of simulation.
    #TODO: finish description.
    """
    print "\n{} ROBOTS".format(WORKS[num])
    time.sleep(0.2)
    print "INDIVIDUAL OUTPUTS"
    time.sleep(0.2)
    print "  ID  AGE CARR BATT UTIL COST BRKS |    T.OUT  A.OUT"
    time.sleep(0.2)
    print "-----------------------------------|----------------"
    
    for robot in work.robots():
        id, age, str, batt, util, cost, brks, out = robot.stats()
        print repr(id).rjust(4), repr(age).rjust(4), repr(str).rjust(4),
        print repr(batt).rjust(4), repr(util).rjust(4), repr(cost).rjust(4),
        print repr(brks).rjust(4), '|',  repr(out).rjust(8),
        print repr(out/weeks).rjust(6)
    
    print "\nTOTAL {} OUTPUT:".format(WORKS[num]), work.totalOut()
    time.sleep(0.2)
    print "\nAVERAGE WEEKLY OUTPUT PER ROBOT:", work.avgOut(weeks)
    time.sleep(0.2)


def rEnd():
    """
    Displays options to end or restart simulation after robot placement is
    complete.
    """
    word = ["\nCOMMANDS",
            "----------",
            "RESTART  - Restart simulation.",
            "DECOM - Choose robots to decommission.\n"]
    disp(word)