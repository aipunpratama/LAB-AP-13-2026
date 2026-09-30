#1
#Kamu sedang mengembangkan program kasir otomatis untuk Dins Store, 
# sebuah toko virtual yang menjual berbagai item Roblox Fish It. 
# Program ini bertugas merekap jumlah item yang terjual dalam setiap transaksi harian.
#  Program harus terus berjalan dan meminta input dari kasir secara berulang sampai sesi toko diputuskan untuk ditutup.
#  Buatlah program Python dengan aturan kelayakan sistem sebagai berikut:
# ● Program akan terus menampilkan prompt "Masukkan jumlah item: " berulang kali.
# ● Jika kasir salah mengetik dengan memasukkan huruf atau simbol (bukan angka bulat), program tidak boleh error atau terhenti. 
# Gunakan struktur try-except untuk menangkap kegagalan tersebut dan tampilkan pesan peringatan: "Input harus berupa angka!".
# ● Jika angka yang dimasukkan kurang dari 0 (negatif), tampilkan pesan: "Jumlah tidak boleh negatif" dan langsung lompat meminta input transaksi berikutnya.
# ● Jika angka yang dimasukkan lebih dari 100 (melebihi batas stok sekali beli), tampilkan pesan: "Maksimal 100 item per transaksi!" dan lewati transaksi tersebut. 
# ● Tampilkan pesan "Transaksi [X] item berhasil!" hanya jika input berupa angka yang valid dan lolos dari kedua aturan pembatasan di atas.
# ● Jika kasir memasukkan angka 0, itu menandakan toko ditutup. Tampilkan pesan "Toko ditutup. Sesi rekap selesai." lalu hentikan program sepenuhnya. 
print ("=== Rekapitulasi Transaksi Dins Store ===")
print (" Ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True :
    try :
        jumlah_item = int(input("masukan jumlah item :"))
        if jumlah_item == 0:
            print ("Toko ditutup. Sesi rekap selesai")
            break
        elif jumlah_item <0:
            print ("angka tidak boleh negatif!")
        elif jumlah_item >100:
            print ("Maksimal 100 per item transaksi!")
        else :
            print (f"Transaksi {jumlah_item} item berhasil!")
    except ValueError:
        print ("Input harus berupa angka!")
