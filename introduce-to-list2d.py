print('soal ke 1')
print()
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print('baris ke 0 kolom ke 2: {}'. format(matrix[0][2]))
print('baris ke 1 kolom ke 0: {}'. format(matrix[1][0])) 
print('baris ke 3 kolom ke 1: {}'. format(matrix[2][0]))
print('seluruh baris ke 1: ')
print(matrix[0])
print('seluruh kolom ke 0: ')
for i in range(3):
  print(matrix[i][0])


  # soal ke 2
print()
print()

print('soal ke 2')
nilai = [
  [80, 75, 90], # nilai siswa 1 (matematika, ipa, bind)
  [85, 70, 95], # nilai siswa 2
  [78, 88, 84] # nilai siswa 3
]
print('menampilkan nilai siswa ke 1:') # 1
print(nilai[0])
print('menampilkan nilai bahasa siswa ke-3:') # 2
print(nilai[2][2])
a = sum(nilai[0])
print(f'total nilai siswa ke 1: {a}') # 3
print('seluruh nilai ipa: ') # 4
for i in range(3):
  print(nilai[i][1])

print('rata rata nilai bahasa semua siswa: ')
total = 0
for i in range(len(nilai)):
  total += nilai[i][2]
  mean = total / len(nilai)
print(f'rata rata nilai {mean:.2f}')

