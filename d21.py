#0
t = {7,5,8,4,6,9,7,8,2,1,4,7}
t.remove(7)
print(t)
print()

#1
a = {3,24,47}
r = {24,14,77}
t ={9,7,8}
h = set.union(a,r,t)
print(h)
print()

#2
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2.difference(farm_1))
print()

#3
j = { 3, 45, 47, 895, 14}
j.add(66)
j.pop()
print(j)
print()


#000
menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
menu['besh_barmak'] = 130
menu['lagman'] = 135
del menu['borsh']
print(menu)
print()

#10
menu['drinks']=['Coca-Cola', 'Sprite', 'Fanta']
print(menu)
print()

#020
set1 = {'add', 'remove', 'clear', 'update', 'difference', 'discard', 'intersection', 'pop'}
set2 = {'clear', 'keys', 'items', 'get', 'values', 'update'}
print(set1.intersection(set2))
print()

#31
p = {}
for t in range(3):
	name = input("Vedite imya: ")
	password = input("Vedite parol: ")
	p[name]=password
print(p)
print()

#27
y = {'Adel': 'programmer', 
	'Jannet': 'Teacher', 
	'Liza': 'Dancer', 
	'Keyt': 'Singer', 
	'Masha': 'Actress'}
for name, job in y.items():
	print(f"Zdravstvuyte,{name} prekrasnaya professiya {job}")
print()

#22
'''
q = set()
for h in range(11):
	g = int(input("vvedite chislo: "))
	q.add(g)
print(tuple(q))
print()
'''

#11
south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
t = set(south_american_countries)
print(list(t))
print()

#101
suitcase = []
for t in range(5):
	j = input("Vesh: ")
	suitcase.append(j)
print(suitcase)
suitcase.pop()
print(suitcase)
print()

#001
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
print(farm_2.intersection(farm_1))
print(farm_1.difference(farm_2))
print()

#100
print(farm_2.difference(farm_1))