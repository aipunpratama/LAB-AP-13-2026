while True:
    try:
        kuota = int(input("Masukkan maksimal kursi bus: "))
        if kuota <= 0:
            print("Jumlah kursi harus lebih dari 0!\n")
            continue
        break
    except:
        print("Input jumlah kursi harus berupa angka!\n")

print("\n--- Sistem Reservasi PO BUS Dimulai ---\n")

total_pendapatan = 0

while kuota > 0:
    print(f"Sisa kursi: {kuota}")
    try:
        umur = int(input("Masukkan umur penumpang: "))
        if umur < 0:
            print("Umur tidak valid!\n")
            continue
            
        if umur <= 5:
            harga = 0
            print("Kategori: Balita - Tiket Gratis (Rp 0)\n")
        elif umur <= 12:
            harga = 50000
            print("Kategori: Anak - Harga: Rp 50.000\n")
        else:
            harga = 100000
            print("Kategori: Dewasa - Harga: Rp 100.000\n")
            
        total_pendapatan = total_pendapatan + harga
        kuota = kuota - 1
    except:
        print("Input umur harus berupa angka!\n")
        continue

print("--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total_pendapatan)