from pathlib import PureWindowsPath
#penjummlahan matrix 2D

x = int(input('masukkan jumlah baris: '))
y = int(input('masukkan jumlah kolom: '))
a = []
b = []
result = []
#buat list a
print('\nmatrix a')
for i in range(x):
  row = []
  for j in range(y):
    d = int(input(f'masukkan elemen matrix ke-[{i+1}[{j+1}]]: '))
    row.append(d)
  a.append(row)

#buat list b
print('\nmatrix b')
for i in range(x):
  row = []
  for j in range(y):
    d = int(input(f'masukan elemen matrix ke [{i+1}][{j+1}]: '))
    row.append(d)
  b.append(row)

#ini penjumlahan 
for i in range(x):
  row = []
  for j in range(y):
    total = a[i][j] + b[i][j]
    row.append(total)
  result.append(row)
#menampilkan matrix a
print('\nmatrix a dan b')
for A,B in zip(a, b):
  print(A, B)
  
print('''menu penjumlahan matrix
1.penjumlahan
2. pengurangan
3. perkalian''')
while True:
  n = input('masukkan angka pilihan(ketik "n" untuk berhenti):')
  if n == '1':
    print('penjumlahan')
    result = []
    for i in range(x):
      row = []
      for j in range(y):
        total = a[i][j] + b[i][j]
        row.append(total)
      result.append(row)

    for v in result:
      print(v)
    
  elif n == '2':
    print('pengurangan')
    result = []
    for i in range(x):
      row = []
      for j in range(y):
        total = a[i][j] - b[i][j]
        row.append(total)
      result.append(row)

    for v in result:
      print(v)
  elif n == '3':
    print('perkalian')
    result = []
    for i in range(x):
      row = []
      for j in range(y);
      
  elif n == 'n':
    break
  else:
    print('masukkan angka yang benar')
