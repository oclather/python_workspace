#conding=utf-8

a = [1,2,3,5,180,182,444,55,22]
b = []
c = []
x = []

for i in a:
	for x in a:
		if i + x == 183:
			b.append(i)
			b.append(x)
			c.append(b)
		else:
			pass

print c