#12
a=(1, 1)
b=(3, 7)
c=(2, 3)
d=(9, 4)
e=(6, 4)
t = [a, b, c, d, e]
print(t)
print()

#32
u = ("la", "li", "ka")
print(u[0], u[1], u[2])
print()

#11
l = [7, "llll", 3.25, True, 3j]
print(l)
print()

#0
m = ["Altynai", "Aliya", "Asel", "Elya", "Mira"]
k = " "
print(k.join(m))
print()

#12
i = (2, 3, 5, 5, 8, 9, 74, 55, 13, 14, 147, 4, 14, 1, 88)
print(i[0:3])
print(i[3:6])
print(i[6:9])
print(i[9:12])
print(i[12:15])
print()

#17
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
k = 0
for i in range(21):
	if names[i] == "Jack":
		k += 1
print(k)

#17.2
print(names.count("Jack"))
print()


#72
names.pop(2)
names.pop(4)
names.pop(6)
names.pop(8)
print(names)
print()

#1
k = []
k.append("Sezim")
k.append("2000")
k.append("Python")
print(k)








