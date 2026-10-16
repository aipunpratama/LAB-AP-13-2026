print ("--- Rekapitulasi Transaksi Dins Store ---")
print ("Ketik '0' untuk menutup toko dan mengakhiri sesi.")
while True :
    try :
        jumlah_item = int(input ("Masukkan Jumlah Item : "))
        if jumlah_item == 0 :
            print ("Toko Ditutup. Transaksi Selesai")
            break
        elif jumlah_item > 100 :
         print ("Maksimal 100 Item Per Transaksi")
        elif jumlah_item < 0 :
         print ("Jumlah Tidak Boleh Negatif")
        else :
           print(f"Transaksi {jumlah_item} item berhasil!")
    except :
        print ("Input Harus Berupa Angka!")