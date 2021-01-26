#problem2
print("Prolem2:")
a = 2**3
b = 3**2
if a > b:
	print("a bolshe")
else:
	print("b bolshe\n")

#problem22
print("Problem22:")
k = 10
l = 8
m = 12
if (k > l) & (k >m):
	print("k samoe bolhoe")
elif (l > k) & (l > m):
	print("l samoe bolshoe")
else:
	print("m samoe bolshoe")
if (k < l) & (k < m):
	print("k samoe malenkoe")
elif (l < k) & (l < m):
	print("l samoe malenkoe")
else:
	print("m samoe malenkoe")

#problem15
print("\nProblem15:")
q = 17391%17
w = 546%17
e = 934%17
if (q < w) & (q < e):
	print("ostatok '17391 % 17' menshe: ",q)
elif (w < q) & (w < e):
	print("ostatok '546 % 17' menshe: ",w)
else:
	print("ostatok '934 % 17' menshe: ",e)

#problem39
print("\nProblem39:")
x = 13**2
if x <= 172:
	x=x**2
	print("x**3: ",x)
else:
	x=x**2
	print("x**2: ", x)

#problem5
print("\nProblem5:")
r = int(input("vedite chislo: "))
if (r%2) == 0:
	print("Chetnoe")
else:
	print("Nechetnoe")
if (r%3) == 0:
	print("Da, delitsya na 3, bez ostatka")
else:
	print("Net, ne delitsya")
if (r**2) > 1000:
	print("Da, r bolshe 1000")
elif (r**2) < 1000:
	print("Net, menshe 1000")
else:
	print("r ravno 1000")

#problem3
print("\nProblem3:")
y = int(input("chislo: "))
if (y > 0 & y < 21) or (y > 57 & y < 100):
	print(" ne razreshennoe")
elif (y > 21) & (y < 57):
	print("razreshennoe chislo")



#problem7
print("\nProblem7:")
if 1 > 0:
	print("hey")

#problem9
print("\nProblem9:")
if 1 < 2:
	if 3 > 2:
		if 9 > 2:
			print("Llalalalala")

#problem 45:
print("\nProblem45:")
a = 10//5
b = 10/5
if a == b:
	print(a+b)
else:
	print("Ne ravny")

#problem33
print("\nProblem33:")
u = int(input("Chislo: "))
if u > 0:
	print(u * (-1))
else:
	print(u)

#problem11
print("\nProblem11: ")
a = 10
b = 5
if (a > 0) & (b > 0):
	print("Da, yavlyautsya")
else:
	print("Net")

#problem0
if a > b:
	print(a+2)
else:
	print(b+2)






