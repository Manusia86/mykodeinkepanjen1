daftar_nilai = []
siswa_lulus = []
siswa_tidak_lulus = []
for i in range(10):
  nilai = int(input('masukkan nilai nya: '))
  daftar_nilai.append(nilai)
print(f'daftar nilai: {daftar_nilai}')
for nilai in daftar_nilai:
  if nilai >= 75:
    siswa_lulus.append(nilai)
  elif nilai < 75:
    siswa_tidak_lulus.append(nilai)
print(f'jumlah siswa lulus: {len(siswa_lulus)}')
print(f'jumlah siswa tidak lulus: {len(siswa_tidak_lulus)}')
persen = len(siswa_lulus) / len(daftar_nilai) * 100
print(f'presentase kelulusan: {persen}%')
