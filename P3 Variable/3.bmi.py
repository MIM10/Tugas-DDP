tinggiBadan = int(input("Masukkan tinggi badan Anda : "))

beratL = (tinggiBadan - 100) - ((tinggiBadan - 100) * 0.1)
beratP = (tinggiBadan - 100) - ((tinggiBadan - 100) * 0.15)

print("Berat badan ideal untuk Pria adalah : ", beratL, "kg")
print("Berat badan ideal untuk Wanita adalah : ", beratP, "kg")

