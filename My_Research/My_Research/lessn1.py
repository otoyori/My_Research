from pulp import *

m = LpProblem(sense=LpMaximize)#モデルの作成
x = LpVariable("x",lowBound=0,upBound=5)
y = LpVariable("y",lowBound=0,upBound=10)
m += x+y

m += 2*x +y -10 == 0
m.solve()

print(value(x),value(y),value(m.objective))