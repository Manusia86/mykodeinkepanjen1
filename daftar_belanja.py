belanja = ["beras", "gula", "telur", "minyak", "kopi"] 

print(belanja)

while True:
    a = input('masukkan nama barang yang ingin ditambahkan(ketik "0" untuk mengakhiri): ')
    if a == '0':
        break
    belanja.append(a)

p = input('masukkan item yang ingin di hapus: ')
if p in belanja:
    belanja.remove(p)
    print('item berhasil dihapus')
else:
    print('item tidak ada di daftar belanja')

    

for i in range(len(belanja)):
    print('{}. {}'. format(i+1, belanja[i]))