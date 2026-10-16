angka = int(input("Angka: "))

if angka % 2 == 0:
    print("Genap")
else:
    print("Ganjil")

if angka > 0:
    print("Positif")

elif angka < 0:
    print("Negativ")

else:
    print("Nol")

if angka >= 1 and angka <= 10:
    print("dalam rentang ✅")

else:
    print("di luar rentang ❌")
