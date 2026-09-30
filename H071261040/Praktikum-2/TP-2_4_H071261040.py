#Soal Nomor 4
tujuan = input ("Pilih Tujuan (Pantai/Pegunungan/Kota) : ")
waktu = input ("Masukkan Waktu (Pagi/Malam) : ")
tipe_pengunjung = input ("Tipe Pengunjung (Anak/Dewasa) : ")
match tujuan : 
    case "Pantai" :
        if waktu == "Pagi"  :
            print ("Rekomendasi Paket : Paket A")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa" :
            print ("Rekomendasi Paket : Paket C")
        else :
            print ("Tidak Ada Paket Yang cocok")
    case "Pegunungan" :
        if waktu == "Pagi" and tipe_pengunjung == "Dewasa" :
            print ("Rekomendasi Paket : Paket B")
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa" :
            print ("Rekomendasi Paket : Paket C")
        else :
            print ("Tidak Ada Paket Yang cocok")
    case "Kota" :
        if waktu == "Malam" :
            print ("Rekomendasi Paket : Paket C")
        else :
            print ("Tidak Ada Paket Yang Cocok")
    case _: 
        print ("Tidak Ada Paket Yang Cocok")