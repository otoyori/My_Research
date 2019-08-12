from pulp import *

m = LpProblem(sense=LpMaximize)
x = LpVariable("x",lowBound=0)
y = LpVariable("y",lowBound=0)
m += x+y

m += x*x -y ==0
m += 0.5 * x -y +1 ==0
m += y == 1
m.solve()

print(value(x),value(y),value(m.objective))