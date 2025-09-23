#cara copy list
a = [1,2,3,4,5]

#pakai copy()
b = a.copy()
print(b)

#pakai list()
c = list(a)
print(c)

#pakai slicing
d = a[:]
print(d)

#pakai extend()
e = []
e.extend(a)
print(e)

#pakai loop
f = []
for i in a:
    f.append(i)
print(f)

#pakai list comprehension
print([i for i in a])
