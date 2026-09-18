nilai_tes = float(input("Masukkan nilai tes: "))

if nilai_tes >= 80:
    print("Lolos ke tahap wawancara")
elif nilai_tes >= 65:
    pengalaman_kerja = int(input("Masukkan pengalaman kerja (dalam tahun): "))
    if pengalaman_kerja >= 2:
        print("Lolos ke tahap wawancara")
    else:
        print("Tidak lolos ke tahap wawancara")
else:
    print("Tidak lolos ke tahap wawancara")
