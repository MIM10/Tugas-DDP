class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

class Badak(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, berat, jumlah_cula):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.berat = berat
        self.jumlah_cula = jumlah_cula

    def info_badak(self):
        print(f"Badak {self.name} hidup di {self.hidup}. Makanannya adalah {self.makanan}.")
        print(f"Badak ini memiliki berat {self.berat} kg dan jumlah cula sebanyak {self.jumlah_cula}.")

class Ikan(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna

    def info_ikan(self):
        print(f"Ikan {self.name} hidup di {self.hidup}. Makanannya adalah {self.makanan}.")
        print(f"Ikan ini adalah {self.jenis} dan berwarna {self.warna}.")

class Ular(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, panjang, berbisa):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.panjang = panjang
        self.berbisa = berbisa

    def info_ular(self):
        print(f"Ular {self.name} hidup di {self.hidup}. Makanannya adalah {self.makanan}.")
        print(f"Ular ini memiliki panjang {self.panjang} meter dan {'berbisa' if self.berbisa else 'tidak berbisa'}.")

# Contoh penggunaan
badak1 = Badak("Badak Jawa", "Rumput", "Darat", "Vivipar", 1500, 2)
badak1.info_badak()

ikan1 = Ikan("Nemo", "Plankton", "Air", "Ovipar", "Clownfish", "Orange")
ikan1.info_ikan()

ular1 = Ular("Cobra", "Hewan Kecil", "Darat", "Ovipar", 2.5, True)
ular1.info_ular()
