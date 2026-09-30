print("--- Rekapitulasi Transaksi Dins Store ---")
print("ketik '0' untuk menutup toko dan mengakhiri sesi.")
print()

while True:
    try: 
        item = int(input("masukkan jumlah item: "))
        if item == 0:
            print("Toko ditutup. Sesi rekap selesai.")
            break
        elif item < 0:
            print("Jumlah tidak boleh negatif")
            continue
        elif item > 100:
            print("Maksimal 100 item per transaksi")
            continue
        print(f"Transaksi {item} berhasil")
    except ValueError:
        print("Input harus berupa angka!")