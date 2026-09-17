p = int(input("Masukkan persentase cabai: "))

if p >= 0 and p <= 10:
    print("Level Aman")
elif p >= 11 and p <= 40:
    print("Level Sedang")
elif p >= 41 and p <= 70:
    print("Level Pedas")
elif p > 70:
    print("Level Ekstrem")
else:
    print("Tidak Valid")