import random

while True:
    # Input tinggi segitiga (untuk opsi segitiga)
    n = int(input('Masukkan tinggi segitiga: '))

    print('=== Pilih jenis looping ===')
    print('1. Permainan tebak angka')
    print('2. Segitiga rata kanan')
    print('3. Segitiga rata kiri')
    print('4. Segitiga simetris')
    print('5. Segitiga terbalik atau piramida terbalik')

    c = int(input('Masukkan pilihanmu (hanya angka 1-5): '))

    if c == 1:
        print("""=== Selamat datang di permainan tebak angka ===
=== Kamu akan menebak angka antara 1 sampai 100 ===
=== Kamu memiliki 7 kesempatan untuk menebak ===""")

        r = random.randint(1, 100)
        k = 7

        for i in range(k):
            t = int(input('Masukkan tebakanmu: '))

            if t > r:
                print('Tebakanmu terlalu besar!')
            elif t < r:
                print('Tebakanmu terlalu kecil!')
            else:
                print('🎉 Selamat! Tebakanmu benar 🎉')
                break

            print('Kesempatan tersisa: ' + str(k - (i + 1)))
            l = input('Masih ingin menebak? (y/n): ')
            if l.lower() == 'n':
                print(f'Jawaban yang benar adalah {r}')
                break

            if i == k - 1:
                print(f'😢 Kesempatanmu habis, jawaban yang benar adalah {r}')

    elif c == 2:
        print('=== Segitiga rata kanan ===')
        for i in range(1, n + 1):
            print(' ' * (n - i) + "*" * i)

    elif c == 3:
        print('=== Segitiga rata kiri ===')
        for i in range(1, n + 1):
            print('*' * i)

    elif c == 4:
        print('=== Segitiga simetris ===')
        for i in range(1, n + 1):
            print(' ' * (n - i) + '*' * (2 * i - 1))

    elif c == 5:
        print('=== Segitiga terbalik atau piramida terbalik ===')
        for i in range(n, 0, -1):
            print(' ' * (n - i) + '*' * (2 * i - 1))

    j = input('Ingin mengulang? (y/n): ')
    if j.lower() == 'y':
        continue
    else:
        print('Terima kasih sudah menggunakan program ini!')
        break
