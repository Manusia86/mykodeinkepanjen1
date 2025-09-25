a = ['paprika', 'bayam', 'kangkung', 'selada']
b = []

#pakai list comprehension
#Ini cara panjang. Kamu loop semua isi list a, lalu kalau ada huruf 'a', masukin ke b.
for i in a:
    if 'a' in i:
        b.append(i)
print(b)
#ini sintaks list comprehension
#newlist = [expression for item in iterable if condition == True]
list_baru = [i for i in a if 'a' in i]
print(list_baru)

#tanpa if statemen
ini_baru = [i for i in a]
print(ini_baru)

#pakai range
inirange = [i for i in range(10)]
print(inirange)

#menerima angka kurang dari 5
kuranglima = [i for i in range(10)  if i < 5]

#Tetapkan nilai dalam daftar baru ke huruf besar:
inibesar = [i.upper() for i in a]
print(inibesar)
#Tetapkan semua nilai dalam daftar baru ke 'halo':
inihalo = ['halo' for i in a]
print(inihalo)

#Kembalikan "orange" bukannya "banana":
gantibuat = [i if i != 'bayam' else 'orange' for i in a]
