jmlhBaris = int(input("Masukkan Jumlah: "))

for baris in range(1, jmlhBaris + 1):
    for kolom in range(baris):
        print("*", end="")
    print()  # Pindah ke baris berikutnya