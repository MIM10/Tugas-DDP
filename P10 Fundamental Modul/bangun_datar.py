def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("\nLuas Persegi:", luas)
    print("Keliling Persegi:", keliling, "\n")

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("\nLuas Persegi Panjang:", luas)
    print("Keliling Persegi Panjang:", keliling, "\n")

def lingkaran(jariJari):
    phi = 3.14
    luas = phi * jariJari * jariJari
    keliling = 2 * phi * jariJari
    print("\nLuas Lingkaran:", luas)
    print("Keliling Lingkaran:", keliling, "\n")

def segitiga_sama_sisi(alas, tinggi):
    luas = 0.5 * alas * tinggi
    keliling = alas * 3
    print("\nLuas Segitiga Sama Sisi:", luas)
    print("Keliling Segitiga Sama Sisi:", keliling, "\n")

def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("\nLuas Belah Ketupat:", luas)
    print("Keliling Belah Ketupat:", keliling, "\n")

def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2 * alas + sisi_miring 
    print("\nLuas Jajar Genjang:", luas)
    print("Keliling Jajar Genjang:", keliling, "\n")

def layang_layang(diagonal1,diagonal2,sisi_atas,sisi_bawah):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 2 * (sisi_atas + sisi_bawah)
    print("\nLuas Layang-Layang:", luas)
    print("Keliling Layang-Layang:", keliling, "\n")