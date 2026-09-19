#Soal Nomor 3
nilai = int(input("Masukkan Nilai Test Anda : "))
if nilai >= 80 :
    print ("Selamat, Anda Lulus Ke Tahap Wawancara")
elif  65 <= nilai <= 79  :
    pengalaman_kerja = int(input("Masukkan Pengalaman Kerja Anda (Tahun) : "))
    if pengalaman_kerja >= 2 :
        print ("Lulus Bersyarat")
    else :
        print ("Tidak Lulus")
else :
    print ("Tidak Lulus")