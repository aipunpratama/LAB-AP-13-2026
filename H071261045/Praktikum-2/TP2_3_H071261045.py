nilai = int(input("Masukkan nilai tes: "))

if nilai >= 80:
    print("Lolos ke Tahap Wawancara")
elif nilai >= 65:
    pengalaman_kerja = int(input("Masukkan pengalaman kerja (dalam tahun): "))
    if pengalaman_kerja >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")
else:
    print("Tidak Lolos")