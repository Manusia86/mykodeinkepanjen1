a = ["apple", "banana", "cherry"]

#pakai for loop
print("pakai for loop")
for b in range(len(a)):
    print(a[b])

#pakai for each
print("pakai for each")
for x in a:
    print(x)

#pakai enumerate
print('pakai enumerate')
for aku,nilai in enumerate(a):
    print(aku,nilai) 

#pakai while loop
print('pakai while loop')
i = 0
while i < len(a):
    print(a[i])
    i += 1

#pakai list comprehension
print('pakai list comprehension')
[print(x) for x in a]

#pakai map
print('pakai map')
list(map(print, a))
