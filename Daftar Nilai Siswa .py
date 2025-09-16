nilai = []

while True:
    n = int(input('masukkan nilai:'))
    nilai.append(n)
    if len(nilai) == 5:
        break
mean = sum(nilai) / len(nilai)
ttg = max(nilai)
trd = min(nilai)

print('rata-rata nilai siswa: {}'. format(mean))
print(f'nilai tertinggi: {ttg}')
print(f'nilai terendah: {trd}')

n = int(input('masukkan nilai tambahan: '))
nilai.append(n)

print('daftar nilai siswa: {}'. format(nilai))