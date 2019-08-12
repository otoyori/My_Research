"修士研究プログラム 練習"

from pulp import *
m = LpProblem(sense=LpMaximize) # 数理モデル
x = LpVariable('x', lowBound=0, cat=LpInteger) # 変数
y = LpVariable('y', lowBound=0, cat=LpInteger) # 変数
z = LpVariable('z', lowBound=0, cat=LpInteger) # 変数
m += 70 * x + 100 * y + 120 * z # 目的関数
m += 3 * x + 5 * z <= 74 # 材料Aの上限の制約条件
m += 2 * y + 8 * z <= 62 # 材料Bの上限の制約条件
m += 8 * x + 12 * y <= 99 # 材料Cの上限の制約条件
m += 5 * x + 10 * z <= 80 # 材料Dの上限の制約条件
m.solve() # ソルバーの実行
print(value(x), value(y), value(z), value(m.objective))