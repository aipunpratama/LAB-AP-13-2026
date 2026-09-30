while True:
    try:
        N = int(input("masukkan jumlah kursi bus: "))
        if N <= 0:
            print("jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input kursi harus berupa angka!")

print("--- Sistem Reservasi PO BUS Dimulai---")
total_pendapatan = 0
while N > 0:
    try:
        print(f"sisa kursi: {N}") 
        umur = int(input("masukkan umur penumpang: "))
        if umur < 0:
            print("Umur tidak valid!")
            continue
        if 0<= umur <=5:
            biaya = 0
            print("Kategori: Balita - Tiket Gratis (Rp 0)")
        elif 6<= umur <=12:
            biaya = 50000
            print("Kategori: Anak - biaya: Rp 50000")
        else:
            biaya = 100000
            print("Kategori: Dewasa - biaya: Rp 100000")
        total_pendapatan += biaya
        N -= 1
    except ValueError:
        print("Input umur harus berupa angka!")

print("--- Semua Kursi Terisi---")
print(f"Total pendapatan: {total_pendapatan}")