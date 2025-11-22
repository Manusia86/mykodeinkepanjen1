data_siswa = {
   'siswa 1': {
        'nama': 'Andi',
        'umur' : 15,
        'kelas': '10A',
        'nilai' : [100, 90, 95]
   },
   'siswa 2' : {
       'nama' : 'Budi',
       'umur' : 16,
       'kelas' : '10B',
       'nilai' : [85, 80, 88]       
   },
   'siswa 3' : {
       'nama' : 'Joko',
       'umur' : 15,
       'kelas' : '10A',
       'nilai' : [70, 75, 78]
   }
}

for i, a in data_siswa.items():
    print(f"{i}: {a['nama']}, umur {a['umur']}, kelas {a['kelas']}, nilai {a['nilai']}")



merubah = input('ingin merubah data siswa? (y/n): ')
if merubah.lower() == 'y':
    while True:
        print('''=== apa yang ingin diubah? ===
        1. nama
        2. umur
        3. kelas
        4. nilai
        5. menambah data siswa
        6. berhenti''')
        change = int(input('masukkan pilihan anda (1-4): '))
        if change == 1:
            print('merubah nama sisawa')
            siswa = input('masukkan nama siswa yang ingin di ubah:').lower()
            if siswa in [a['nama'].lower() for a in data_siswa.values()]:
                    nama_baru = input('masukkan nama baru: ').lower()
                    a['nama'] = nama_baru
                    print('data berhasil diubah')
            else:
                    print('data tidak ditemukan')
            lanjut = input('ingin mengubah data lagi? (y/n): ')
            if lanjut.lower() != 'y':
                break
        elif change == 2:
             print('merubah umur siswa')
             siswa= input('masukkan nama siswa yang ingin di ubah:').lower()
             if siswa in [a['nama'].lower() for a in data_siswa.values()]:
                  umur_baru = int(input('masukkan umur baru: '))
                  a['umur'] = umur_baru        
                  print('data berhasil diubah')
                  lanjut = input('ingin mengubah data lagi? (y/n): ')
                  if lanjut.lower() != 'y':
                      break
             else:
                  print('data tidak ditemukan')
                  lanjut = input('ingin mengubah data lagi? (y/n): ')
                  if lanjut.lower() != 'y':
                      break
        elif change == 3:
             print('merubah kelas siswa')
             siswa = input('masukkan nama siswa yang ingin di ubah: ').lower()
             if siswa in [a['nama'].lower() for a in data_siswa.values()]:
                  kelas_baru = input('masukkan kelas baru: ')
                  a['kelas'] = kelas_baru
                  print('data berhasil diubah')
                  lanjut = input('ingin mengubah data lagi? (y/n): ')
                  if lanjut.lower() != 'y':
                      break
             else:
                  print('data tidak ditemukan')
                  lanjut = input('ingin mengubah data lagi? (y/n): ')
                  if lanjut.lower() != 'y':
                      break
        elif change == 4:
             print('merubah nilai siswa')
             siswa = input('masukkan nama siswa yang ingin di ubah: ').lower()
             if siswa in [a['nama'].lower() for a in data_siswa.values()]:
                  for value in range(len(a['nilai'])):
                       nilai_baru = int(input(f'masukkan nilai ke-{value + 1} baru: '))
                       a['nilai'][value] = nilai_baru
                  print('data berhasil diubah')
                  lanjut = input('ingin mengubah data lagi? (y/n): ')
                  if lanjut.lower() != 'y':
                      break
             else:   
                  print('data tidak ditemukan')   
                  lanjut = input('ingin mengubah data lagi? (y/n): ')
                  if lanjut.lower() != 'y':
                    break
        elif change == 5:
             print('menambah data siswa baru')
             berapa = int(input('berapa data siswa yang ingin ditambahkan? '))
             for n in range(berapa):
                  nama_data = input('masukkan kode data siswa (contoh: siswa 4): ')
                  nama_baru = input('masukkan nama siswa: ')
                  umur_baru = int(input('masukkan umur siswa: '))
                  kelas_baru = input('masukkan kelas siswa: ')
                  nilai_baru = []
                  for m in range(len(a['nilai'])):
                       nilai = int(input(f'masukkan nilai ke-{m + 1}: '))
                       nilai_baru.append(nilai)
                  data_siswa[nama_data] = {
                       'nama' : nama_baru,
                       'umur' : umur_baru,
                       'kelas' : kelas_baru,
                       'nilai' : nilai_baru
                  }
             print('data siswa berhasil ditambahkan')
             lanjut = input('ingin mengubah data lagi? (y/n): ')
             if lanjut.lower() != 'y':
                break
        elif change == 6:
            print('berhenti mengubah data siswa')
            break
            
                    
                  
                  
print('=== data siswa terbaru ===')
for i, a in data_siswa.items():
    print(f"{i}: {a['nama']}, umur {a['umur']}, kelas {a['kelas']}, nilai {a['nilai']}")
