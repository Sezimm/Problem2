x = input()
y = len(x)
print(y)

b = 0
s = 0
for i in x:
	if ("a" <= i <= "z") or ("а" <= i <= "я"):
		s += 1
	if ("A" <= i <= "Z") or ("А" <= i <= "Я"):
		b += 1

print(s)
print(b)
print(s/y*100,"%")
print(b/y*100,"%")