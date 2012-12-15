from LD25class import *

r1 = LaborRobot(1, 0, 1.0, 12.0, 5, 100)
r2 = LaborRobot(2, 10, 5.0, 16.0, 10, 200, 1, 10)

print "Testing r1 farmOutput. Should be 8.75:", str(r1.farmOutput())
print "Testing r1 factoryOutput. Should be 52.5:", str(r1.factoryOutput())
print "Testing r1 breakdown. Should be 0.01:", str(r1.breakdown())
print "Testing r2 breakdown. Should be 0.10:", str(r2.breakdown())
print "Testing r1 stats.", str(r1.stats())

robots = [r1]

w1 = Farm(2, 10, 3, robots[:])
w2 = Factory(1, 10, 7, robots[:])

print "w1 is a Farm?", isinstance(w1, Farm)
print "w1 is a Factory?", isinstance(w1, Factory)
print "w1 is a Workplace?", isinstance(w1, Workplace)

print "Adding r2 to w1."
w1.add(r2)

print "Robots in w1:", w1.robots()

print "Total w1 output:", w1.totalOut()
print "Total w1 cost:", w1.totalCost()
print "Average w1 output:", w1.avgOut()
print "Average w1 cost:", w1.avgCost()

print "Removing r1 from w1."
w1.remove(r1)

print "Robots in w1:", w1.robots()