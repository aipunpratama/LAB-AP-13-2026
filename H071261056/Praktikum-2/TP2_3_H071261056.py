#3
nilai = int(input("masukan_nilai:"))

if nilai >= 80:
    print ("Lolos ke Tahap Wawancara")
elif 65<= nilai <80:
    pengalaman_kerja = int(input("masukan pengalaman kerja (tahun):"))
    if pengalaman_kerja >=2:
        print ("Lolos Bersyarat")
    else :
        print("tidak lolos")
else :
    ("Tidak lolos")
