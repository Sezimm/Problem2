#23
name = input("Kak vas zovut?: " )
age = input("Skoklko vam let?: ")
film = input("Vash lubimayi film?: ")

print("Privet ", name)
print(film, " eto horoshii film!\n ")

#31
a = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
print(len(a.split()))
print()

#25
b = "У вас есть строка 'Запуск Ethereum 2.0 состоится 1 декабря. На депозитный контракт внесено более 524 288 ETH'"
y = b.split()
for d in y:
	print(d, type(d))
print()

#11
v = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
d = v.split()
c = []
w = ""
for s in d:
	c.append(s.title())
for t in range(len(c)):
	w = w + c[t]+" "
print(w)
print()

#2
s = input("Vedite simvol: ")
x = 'GitHub'
print(s.join(x))
print()

#5
z = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
print(z.replace("е","3"))
print()

#0
e = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric jlhkjgkhjgk hlkjkjhlk uhllllkhk hgfytftrdfty ihgiougoiugiou iuhiuogoiygiogiog'
d = e.split()
r = len(d)
for g in range(r // 2):
	print(d[g].lower(), end = " ")
s = r-r//2
while s < r:
	print(d[s].upper(), end = " ")
	s += 1
print()


#1
y = 5 > 2
t=str(y)
print(t)
print(type(t))





