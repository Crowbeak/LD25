PHASES = ['ROBOT PLACEMENT', 'SIMULATION RESULTS']
WORKS = ['FARM', 'FACTORY', 'UNASSIGNED']


def keyAndTitle(num, simName='Simulation'):
    """
    Prints key and title for the display output.
    
    num: The index of the appropriate subtitle in PHASES (a non-negative int).
    simName: Simulation name (a string).
    """
    print "\nSIMULATION: {} \n".format(simName)
    print "{}".format(PHASES[num])
    
    print "KEY"
    print "----------"
    print "ID:   Robot's ID number"
    print "AGE:  Years robot has been in service"
    print "STR:  Tens of pounds robot can carry"
    print "BATT: Battery life of robot"
    print "UTIL: Rating of robot's ability to complete varied tasks"
    print "COST: Weekly costs of maintaining robot"
    print "BRKS: Number of times robot has broken down"
    
    if num == 1:
        print "T.OUT: Robot's total output over simulated timeframe."
        print "A.OUT: Robot's average output per week over simulated timeframe."


def pWork(work, num):
    """
    num: index in WORKS
    #TODO: proper description
    """
    print "\n{} ROBOTS".format(WORKS[num])
    if work.getMax() == None:
        print "NO MAXIMUM"
    else:
        print "MAX NUMBER OF ROBOTS:", work.getMax()
    print "  ID  AGE  STR BATT UTIL COST BRKS"
    print "----------------------------------"
    
    for robot in work.robots():
        id, age, str, batt, util, cost, brks, out = robot.stats()
        print repr(id).rjust(4), repr(age).rjust(4), repr(str).rjust(4),
        print repr(batt).rjust(4), repr(util).rjust(4), repr(cost).rjust(4),
        print repr(brks).rjust(4)
    

def pDisplay(unassigned, farm, factory, simName='Simulation'):
    """
    Prints console information during the robot placement phase of simulation.
    
    #TODO: finish description.
    """
    keyAndTitle(0, simName)
    
    pWork(unassigned, 2)
    pWork(farm, 0)
    pWork(factory, 1)

        
def pCommand():
    #TODO: description.
    print "\nCOMMANDS"
    print "----------"
    print "FARM [ID]    - Move robot with ID number [ID] to the farm"
    print "FACTORY [ID] - Move robot with ID number [ID] to the factory"
    print "NONE [ID]    - Return robot to unassigned robot pool"
    print "UPDATE       - Reprint robot lists"
    print "RUN          - Run simulation"
    
    
def sStatus(i, weeks):
    #TODO: description.
    tenths = weeks/10
    
    if i == 0:
        print "\n\nSIMULATING. PLEASE WAIT..."
    elif i == tenths:
        print "...10% complete"
    elif i == tenths*2:
        print "...20% complete"
    elif i == tenths*3:
        print "...30% complete"
    elif i == tenths*4:
        print "...40% complete"
    elif i == tenths*5:
        print "...50% complete"
    elif i == tenths*6:
        print "...60% complete"
    elif i == tenths*7:
        print "...70% complete"
    elif i == tenths*8:
        print "...80% complete"
    elif i == tenths*9:
        print "...90% complete"
    elif i == (weeks-1):
        print "SIMULATION COMPLETE.\n"

def rWork(work, num, weeks, simName='Simulation'):
    """
    Takes a Workplace instance as an argument and displays results of simulation.
    #TODO: finish description.
    """
    print "\n{} ROBOTS".format(WORKS[num])
    print "INDIVIDUAL OUTPUTS"
    print "  ID  AGE  STR BATT UTIL COST BRKS |    T.OUT  A.OUT"
    print "-----------------------------------|----------------"
    
    for robot in work.robots():
        id, age, str, batt, util, cost, brks, out = robot.stats()
        print repr(id).rjust(4), repr(age).rjust(4), repr(str).rjust(4),
        print repr(batt).rjust(4), repr(util).rjust(4), repr(cost).rjust(4),
        print repr(brks).rjust(4), '|',  repr(out).rjust(8),
        print repr(out/weeks).rjust(6)