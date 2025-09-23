karyawan = ['Abdul', 'Haris', 'Rizal', 'Dani']
absensi_karyawan = []

while True:
    nama = input('Masukkan nama karyawan (ketik "selesai" untuk berhenti): ')
    if nama.lower() == 'selesai':
        break
    if nama in karyawan:
        absensi_karyawan.append(nama)
    else:
        print(f'{nama} tidak ada di daftar karyawan.')

t = [k for k in karyawan if k not in absensi_karyawan]
if not t:
    print('semua karyawan hadir')
else:
    for i in t:
        print(f'{i} tidak hadir')
