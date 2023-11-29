def duplikasi(data):
    dataDuplikasi = []
    for buah in data:
        dataDuplikasi.append(buah)
        dataDuplikasi.append(buah)
    return dataDuplikasi

buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

print("Ini versi asli:\n", buah,"\n")
print("Ini versi duplikasi:\n", duplikasi(buah))