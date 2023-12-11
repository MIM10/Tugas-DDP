# 1
def tambah(bil1, bil2):
    print("\n-----     Penjumlahan      -----")
    print("Hasil pertambahan dari", bil1, "+", bil2, "adalah:", bil1 + bil2)

# 2
def kurang(bil1, bil2):
    print("\n-----     Pengurangan      -----")
    print("Hasil pengurangan dari", bil1, "-", bil2, "adalah:", bil1 - bil2)

# 3
def kali(bil1, bil2):
    print("\n-----      Perkalian       -----")
    print("Hasil perkalian dari", bil1, "x", bil2, "adalah:", bil1 * bil2)

# 4
def bagi(bil1, bil2):
    print("\n-----      Pembagian       -----")
    print("Hasil pembagian dari", bil1, "/", bil2, "adalah:", bil1 / bil2)

# 5
def pangkat(bil1, bil2):
    print("\n-----     Perpangkatan     -----")
    print("Hasil pemangkatan dari", bil1, "^", bil2, "adalah:", bil1 ** bil2)

# 6
def modulus(bil1, bil2):
    print("\n-----       Modulus        -----")
    print("Hasil modulus dari", bil1, "%", bil2, "adalah:", bil1 % bil2)

# 7
def akar(bil):
    print("\n-----     Akar Kuadrat     -----")
    print("Akar kuadrat dari", bil, "adalah:", bil ** 0.5)

# 8
def pembulatan(bil):
    print("\n-----      Pembulatan      -----")
    print("Hasil pembulatan dari", bil, "adalah:", round(bil))

# 9
def pembagi_bulat(bil1, bil2):
    print("\n-----      Pembagi Bulat   -----")
    print("Hasil pembagian bulat dari", bil1, "//", bil2, "adalah:", bil1 // bil2)

# 10
def faktorial_alternatif(bil):
    print("\n----- Faktorial Alternatif -----")
    if bil < 0:
        print("Faktorial tidak terdefinisi untuk angka negatif.")
    elif bil == 0 or bil == 1:
        print("Faktorial dari", bil, "adalah 1")
    else:
        hasil = 1
        for i in range(2, bil + 1):
            hasil *= i
        print("Faktorial dari", bil, "adalah:", hasil)

tambah(5, 5)
kurang(5, 5)
kali(5, 5)
bagi(5, 5)
pangkat(5, 5)
modulus(5, 5)
akar(5)
pembulatan(5)
pembagi_bulat(5, 5)
faktorial_alternatif(5)