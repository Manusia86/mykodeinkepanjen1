data_siswa = {
    'andi': {'mtk': 70, 'informatika': 88, 'bing': 99},
    'budi': {'mtk': 85, 'informatika': 92, 'bing': 80},
    'citra': {'mtk': 78, 'informatika': 75, 'bing': 85}
}

rata_rata_siswa = {}  # ini namanya harus sama dengan yang kamu pakai di print nanti
for nama, nilai_mapel in data_siswa.items():
    mean = sum(nilai_mapel.values()) / len(nilai_mapel)
    rata_rata_siswa[nama] = mean

siswa_tertinggi = max(rata_rata_siswa, key=rata_rata_siswa.get)
nilai_tertinggi = rata_rata_siswa[siswa_tertinggi]

print('---data siswa---')
for nama, nilai_mapel in data_siswa.items():
    nilai_str = ', '.join([f"'{mapel}': {nilai}" for mapel, nilai in nilai_mapel.items()])
    print(f"{nama} -> {{{nilai_str}}} | Rata-rata: {rata_rata_siswa[nama]:.2f}")

print()
print(f"Siswa dengan rata-rata tertinggi: {siswa_tertinggi} ({nilai_tertinggi:.2f})")
