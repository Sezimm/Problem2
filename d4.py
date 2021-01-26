#1
lang1 = 'Rast'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for i in range(6):
    if languages[i] == lang1:
    	print("Yes")

#2
i = 0
while languages[i] != "php":
	print(languages[i])
	i+=1

#3
c = 7
for j in range(5):
	c = c * 7
	print("\n",c,"\n")

#4
for k in range(6):
	print(k, languages[k])

#5

	
print()
#6
names = ['Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан']
i = 2
while i <= 12:
	print(names[i])
	i += 2

print()
#7
i = 1
while i <= 12:
	print(names[i])
	i += 2

#8
d = int(input("chislo: "))
##1
if (d >= 100) & (d < 1000):
	print("Yes, trehznachnoe")
else:
	print("No, ne trehznachnoe")
##2
if (d > 0) & (d%2==0):
	print("Yes, polojitelnoe i chetnoe")
else:
	print("No, ne polojitelnoe ili(i) ne chetnoe")
##3
if d%31==0:
	print("Yes")
else:
	print("No")
##4
if ((d > 100) & (d%17==0)) | ((d > 150) & (d==13**2)):
	print(d)

print()
#9
t = -100
p = t
j = 0
k = 0
while t <= 100:
	if (t%13==0) & (t%2==0):
		print(t,t**2)
		k += 1
	t += 1
print(k)
print()
while p <= 100:
	if p%2==1:
		j += 1
		print(p)
	p += 7
print(j)	
			


	

