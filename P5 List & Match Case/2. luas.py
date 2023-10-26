# 2. Buat program python dengan match case untuk menghitung luas bangun datar:

# jka pilih 1, maka menghitung luas persegi
# jka pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga
# selain pilihan di atas, maka keterangan: salah pilih angka

while True:
    print("""
[1] Menghitung luas persegi
[2] Menghitung luas lingkaran
[3] Menghitung luas segitiga\n
""")

    luasBangun = int(input("Masukkan pilihan (1/2/3): "))

    match luasBangun:
        case 1:
            sisi = int(input("Masukkan panjang sisi persegi: "))
            print("================================")
            print("Luas persegi adalah: ", sisi * sisi, "\n")
            break
        case 2:
            jariJari = int(input("Masukkan jari-jari lingkaran: "))
            print("================================")
            print("Luas lingkaran adalah: ", 3.14 * jariJari * jariJari, "\n")
            break
        case 3:
            alas = int(input("Masukkan panjang alas segitiga: "))
            tinggi = int(input("Masukkan tinggi segitiga: "))
            print("================================")
            print("Luas segitiga adalah: ", 0.5 * alas * tinggi, "\n")
            break
        case _:
            print("Pilihan tidak valid. Silahkan pilih 1, 2, atau 3.\n")
            print("================================")


