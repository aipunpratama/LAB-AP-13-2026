n = int(input("Masukkan nilai tes: "))

if n >= 80:
    print("Lolos ke Tahap Wawancara")
else:
    p = int(input("Masukkan  pengalaman kerja (tahun): "))
    if n >= 65 and p >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")