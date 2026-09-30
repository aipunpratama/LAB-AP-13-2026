#Tugas 1
print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.\n")

while True:
    try:
        user_input = input("Masukkan jumlah item: ")
        jumlah_item = int(user_input)
        
        if jumlah_item == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break
        elif jumlah_item < 0:
            print("Jumlah tidak boleh negatif")
            continue
        elif jumlah_item > 100:
            print("Maksimal 100 item per transaksi!")
            continue
        else:
            print(f"Transaksi {jumlah_item} item berhasil!\n")
            
    except :
        print("Input harus berupa angka!")