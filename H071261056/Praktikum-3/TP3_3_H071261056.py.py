#3
#Sistem Reservasi "PO BUS" Kamu sedang membangun sistem pemesanan tiket otomatis untuk armada PO BUS.
#  Sebuah bus memiliki kuota maksimal sebanyak N kursi.
#  Sistem akan terus memproses penumpang satu per satu hingga seluruh kursi di dalam bus tersebut terisi penuh.
#  ● Program meminta input jumlah kursi bus (N) di awal. 
# ● Gunakan perulangan while yang akan terus meminta input umur penumpang selama kuota kursi masih tersedia.
#  ● Jika umur yang dimasukkan kurang dari 0, tampilkan pesan "Umur tidak valid!" dan gunakan continue untuk mengabaikan input tersebut agar kuota kursi tidak berkurang.
#  ● Gunakan Logika Bertingkat (if-elif-else) untuk menentukan harga tiket berdasarkan umur: 
# ○ Umur 0 - 5 tahun: Gratis (Rp 0).
#  ○ Umur 6 - 12 tahun: Tiket Anak (Rp 50000).
#  ○ Umur di atas 12 tahun: Tiket Dewasa (Rp 100000). 
# ● Setiap kali tiket berhasil diproses, kurangi sisa kursi dan tambahkan harga tiket ke dalam total pendapatan bus. 
# ● Tugas: Buatlah program berdasarkan aturan di atas. Setelah perulangan selesai (seluruh kursi habis), cetak total pendapatan yang terkumpul dari perjalanan bus tersebut. 

sisa_kursi = int(input("masukkan jumlah kursi bus :"))
Total_pendapatan = 0

while sisa_kursi > 0 :
    print (f"sisa kursi {sisa_kursi}")
    try:
        umur = int(input("masukan umur penumpang :"))
    except ValueError:
        print ("Input umur harus berupa angka!")
        continue
    
    if umur <0:
        print ("umur tidak valid!")
        continue
    elif umur <= 5:
        Kategori = "Balita"
        Harga = 0
    elif umur <= 12:
        Kategori = "Anak"
        Harga = 50000
    else :
        Kategori = "Dewasa"
        Harga = 100000

    print (f"Kategori {Kategori} - Harga {Harga}")


    Total_pendapatan += Harga
    sisa_kursi -= 1
print ("=== Semua Kursi Terisi ===")
print (f"Total pendapatan perjalanan PO BUS kali ini : {Total_pendapatan}")