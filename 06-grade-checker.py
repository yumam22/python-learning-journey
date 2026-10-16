angka = int(input("Masukkan angka: "))

if angka < 0 or angka > 100:
    print("Angka tidak valid")

elif angka >= 90 and angka <= 100:
    print("A - Sangat baik")

elif angka >= 80 and angka < 90:
    print("B - Baik")

elif angka >= 70 and angka < 80:
    print("C - Cukup")

else:
    print("D - Perlu belajar")
