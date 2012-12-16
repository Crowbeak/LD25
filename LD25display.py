def pDisplay(simName, unassigned, farm, factory):
    """
    Prints console information during the robot placement phase of simulation.
    """
    print "\nSimulation: {} \n".format(simName)
    
    print "KEY"
    print "----------"
    print "ID:   Robot's ID number"
    print "AGE:  Years robot has been in service"
    print "STR:  Tens of pounds robot can carry"
    print "BATT: Battery life of robot"
    print "UTIL: Rating of robot's ability to complete varied tasks"
    print "COST: Weekly costs of maintaining robot"
    print "BRKS: Number of times robot has broken down"
    
    print "\nUNASSIGNED ROBOTS"
    print "NO MAXIMUM"
    print "  ID  AGE  STR BATT UTIL COST BRKS"
    print "----------------------------------"
    
    for robot in unassigned.robots():
        id, age, str, batt, util, cost, brks, out = robot.stats()
        print repr(id).rjust(4), repr(age).rjust(4), repr(str).rjust(4),
        print repr(batt).rjust(4), repr(util).rjust(4), repr(cost).rjust(4),
        print repr(brks).rjust(4)
    
    print "\nFARM ROBOTS"
    print "MAX NUMBER OF ROBOTS:", farm.getMax()
    print "  ID  AGE  STR BATT UTIL COST BRKS"
    print "----------------------------------"
    
    for robot in farm.robots():
        id, age, str, batt, util, cost, brks, out = robot.stats()
        print repr(id).rjust(4), repr(age).rjust(4), repr(str).rjust(4),
        print repr(batt).rjust(4), repr(util).rjust(4), repr(cost).rjust(4),
        print repr(brks).rjust(4)

    print "\nFACTORY ROBOTS"
    print "MAX NUMBER OF ROBOTS:", factory.getMax()
    print "  ID  AGE  STR BATT UTIL COST BRKS"
    print "----------------------------------"
    
    for robot in factory.robots():
        id, age, str, batt, util, cost, brks, out = robot.stats()
        print repr(id).rjust(4), repr(age).rjust(4), repr(str).rjust(4),
        print repr(batt).rjust(4), repr(util).rjust(4), repr(cost).rjust(4),
        print repr(brks).rjust(4)
    
    
def pCommand():
    print "\nCOMMANDS"
    print "----------"
    print "FARM [ID]    - Move robot with ID number [ID] to the farm"
    print "FACTORY [ID] - Move robot with ID number [ID] to the factory"
    print "NONE [ID]    - Return robot to unassigned robot pool"
    print "UPDATE       - Reprint robot lists"
    print "RUN          - Run simulation"