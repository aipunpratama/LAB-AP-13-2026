tingkat_kepedasan = int(input("Masukkan tingkat kepedasan: "))

if tingkat_kepedasan >= 0 and tingkat_kepedasan <= 10:
    print("Level Aman.")
elif tingkat_kepedasan >= 11 and tingkat_kepedasan <= 40:
    print("Level Sedang.")
elif tingkat_kepedasan >= 41 and tingkat_kepedasan <= 70:
    print("Level Pedas.")
elif tingkat_kepedasan > 70:
    print("Level Ekstrem.")
else:
    print("Input tidak valid.")