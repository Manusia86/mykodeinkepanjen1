siswa = []

while True:
    nama = input('masukkan nama siswa: ')
    siswa.append(nama)
    if len(siswa) == 5:
        break

s = input('ingin mencari siapa: ')
if s in siswa:
    print('{} ada'. format(s))
else:
    print('{} tidak ada'. format(s))

for i in range(len(siswa)):
    print('{}. {}'. format(i+1, siswa[i]))

c = input('masukkan nama siswa yang akan di ganti: ')
v = input('masukkan nama pengganti: ')

if c in siswa:
    siswa[siswa.index(c)] = v
    print('nama siswa berhasil di ganti')
else:
    print('nama siswa tidak ada di daftar')

print('menampilkan tiga siswa pertama:')
print(siswa[0:3])
print('total siswa: {}'. format(len(siswa)))




