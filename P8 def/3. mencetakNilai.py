# 3. buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang di masukan :
# ex : ganjil (100)

def ganjil(batas):
    for i in range(1, batas + 1, 2):
        print(i)
ganjil(100)