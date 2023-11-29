def balikan(daftar_buah):
    return daftar_buah[::-1]

buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

print("Ini versi Asli:\n", buah, "\n")
print("Ini versi Terbalik:\n", balikan(buah))