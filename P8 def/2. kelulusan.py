# 2. buatlah fungsi untuk mencari kelulusan nilai dari berikut : 
# jika nilai < 60 maka gagal 
# jika nilai = 61 - 70 maka baik 
# jika nilai = 71 - 80 maka sangat baik 
# jika nilai = 81 - 100 maka istimewa 

# ex:
# nilai (60)

def kelulusan(nilai):
    if nilai <= 0:
        return "Nilai tidak valid"
    elif nilai <= 60:
        return "Gagal"
    elif nilai <= 70:
        return "Baik"
    elif nilai <= 80:
        return "Sangat Baik"
    elif nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

print(kelulusan(int(input("Masukkan Nilai: "))))