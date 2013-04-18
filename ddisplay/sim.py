import time

import ddisplay

###############################################################################
# Simulation - General Display Functions
###############################################################################
def print_key(sim_state):
    ddisplay.print_text(["\nSIMULATION: {} \n".format(sim_state.name),
                        "{}\n".format(sim_state.phase),
                        "\nKEY",
                        "----------",
                        "ID:   Robot's ID number",
                        "AGE:  Years robot has been in service",
                        "CARR: Tens of pounds robot can carry",
                        "BATT: Battery life of robot",
                        "UTIL: Rating of robot's ability to complete varied tasks",
                        "COST: Weekly costs of maintaining robot",
                        "BRKS: Number of times robot has broken down"])
    
    if sim_state.phase == 'SIMULATION RESULTS':
        ddisplay.print_text(["T.OUT: Robot's total output over simulated timeframe",
                            "A.OUT: Robot's average output per week over simulated timeframe"])


###############################################################################
# Simulation - Placement Phase Display Functions
###############################################################################
def placement_display(sim_state):
    """
    Prints console information during the robot placement phase of simulation.
    """
    print_key(sim_state)
    
    for workplace in sim_state.workplaces:
        ddisplay.print_text(["\n{} ROBOTS".format(workplace.name)])
    
        if workplace.max_robots == None:
            ddisplay.print_text(["NO MAXIMUM"])
        else:
            ddisplay.print_text(["MAX NUMBER OF ROBOTS: {}".format(workplace.max_robots)])
        
        ddisplay.print_text(["  ID  AGE CARR BATT UTIL COST BRKS",
                            "----------------------------------"])
    
        for robot in workplace.robots:
            #TODO: Clean this shit up. Check tutorial pg 54 (PDF).
            print repr(robot.id).rjust(4), repr(robot.age).rjust(4),
            print repr(robot.strength).rjust(4), repr(robot.battery).rjust(4),
            print repr(robot.utility).rjust(4), repr(robot.cost).rjust(4),
            print repr(robot.breakdowns).rjust(4)


def placement_cmd(workplaces):
    """
    Displays console commands during the robot placement phase of simulation.
    """
    ddisplay.print_text(["\nCOMMAND   | EFFECT",
                         "----------|-----------------------------------------------"])
    for workplace in workplaces:
        if workplace.cmd == "NONE":
            print "NONE [ID] | Return robot to unassigned robot pool"
        else:
            print "{} [ID] | Move robot with ID number [ID] to {}".format(workplace.cmd,
                                                                          workplace.name)
    ddisplay.print_text(["UPDATE    | Reprint robot lists",
                         "RUN       | Run simulation"])
    

###############################################################################
# Simulation - Calculation Phase Display Functions
###############################################################################
def calc_status(i, cycles):
    """
    Calls to print_text() inserted because calculation takes almost no time.
    """
    tenths = cycles/10
    
    if i == 0:
        ddisplay.print_text(["\n\nSIMULATING. PLEASE WAIT..."])
    elif i == (cycles-1):
        ddisplay.print_text(["SIMULATION COMPLETE.\n"])
    else:
        for j in xrange(1, 10):
            if i == tenths*j:
                ddisplay.print_text(["...{}0% complete".format(j)])


###############################################################################
# Simulation - Results Phase Display Functions
###############################################################################
def results(workplace, weeks):
    """
    Displays results of the calculation phase of simulation in table format for
    the Workplace instance given.
    """
    ddisplay.print_text(["\n{} ROBOTS".format(workplace.name),
                        "INDIVIDUAL OUTPUTS",
                        "  ID  AGE CARR BATT UTIL COST BRKS |    T.OUT  A.OUT",
                        "-----------------------------------|----------------"])
    for robot in workplace.robots:
        print repr(robot.id).rjust(4), repr(robot.age).rjust(4),
        print repr(robot.strength).rjust(4), repr(robot.battery).rjust(4),
        print repr(robot.utility).rjust(4), repr(robot.cost).rjust(4),
        print repr(robot.breakdowns).rjust(4), '|',
        print repr(robot.total_output).rjust(8),
        print repr(robot.total_output/weeks).rjust(6)
    
    ddisplay.print_text(["\nTOTAL {} OUTPUT: {}".format(workplace.name,
                                                       workplace.total_output()),
                        "\nAVERAGE WEEKLY OUTPUT PER ROBOT: {}".format(workplace.avg_output(weeks))])


def end_menu():
    """
    Displays console commands after the calculation phase of simulation
    is complete.
    """
    ddisplay.print_text(["\nCOMMAND   | EFFECT",
                        "----------|----------------------------------------------",
                        "RESTART   | Restart simulation.",
                        "DECOM     | Choose robots to decommission.\n"])