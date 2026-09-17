nilai_tes = int(input("masukkan nilai tes: "))
if nilai_tes >=80:
    print("lolos ke tahap wawancara")
elif 65<= nilai_tes <80:
    pengalaman_kerja = int(input("masukkan pengalaman kerja (tahun): "))
    if pengalaman_kerja >=2:
        print("lolos bersyarat")
    else:
        print("tidak lolos")
else:
    print("tidak lolos")