from pulp import *
import numpy as np
import pprint
m = LpProblem(sense=LpMinimize)#モデルの作成
i = LpVariable("i",lowBound=1,upBound=6)
j = LpVariable("j",lowBound=1,upBound=9)

I = ["コショウ","塩","さとう","醬油","みりん","酒"]
print("調味料の集合 I = {:}".format(I))

C = [4,4,0,2,1,0]

J =["1","2","3","4","5","6","7","8","9"]
print("調味料設置個所　J ={:}".format(J))

D =[1,2,3,3,4,5,4,5,6]


cc = np.zeros((len(I),len(J)))
for ci,cii in enumerate(I):
	for cj,cji in enumerate(J):
		cc[ci][cj] =C[ci]*D[cj]


c={}
for ci in I:
	for cj in J:
		c[ci,cj] = cc[I.index(ci)][J.index(cj)]

x={}
for ii in I:
	for jj in J:
		x[ii,jj] = LpVariable("x({:},{:})".format(ii,jj),0,1,LpBinary)


#目的関数
m += lpSum(c[i,j] * x[i,j] for i in I for j in J)

#制約条件
for i in I:
	m += sum(x[i,j] for j in J) ==1

for j in J:
	m += sum(x[i,j] for i in I) <=1
		
solver = m.solve()


print("解 x[i,j]")


CH =np.zeros((len(I),len(J)))
list =[["","",""],["","",""],["","",""]]
for i in I:
	for j in J:
		print("{:} ={:}, ".format(x[i,j].name,x[i,j].value()),end ="")
		if x[i,j].value() == 1:
			CH[I.index(i)][J.index(j)] = j
			j = int(j) -1
			if j < 3:
				list[0][j] = i
			elif 3 <= j and j <6:
				list[1][j-3] = i
			elif 6<= j and j <9:
				list[2][j-6] = i
	print("")
print("*******************")

pprint.pprint(list)