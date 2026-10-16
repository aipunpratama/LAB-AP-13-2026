while True :
    try :
        kursi = int(input("Masukkan maksimal kursi bus: "))
        if kursi <= 0 :
            print("Jumlah kursi harus lebih dari 0!")
        else :
            break
    except :
        print("Input jumlah kursi harus berupa angka!")

print("--- Sistem Reservasi PO BUS Dimulai ---")

sisa_kursi = kursi
total_pendapatan = 0

while sisa_kursi > 0 :
    print(f"Sisa kursi: {sisa_kursi}")
    try :
        umur = int(input("Masukkan umur penumpang: "))
        if umur < 0 or umur == -0 :
            print("Umur tidak valid!")
        elif umur <= 5 :
            harga = 0
            print("Kategori: Balita - Tiket Gratis (Rp 0)")
        elif umur <= 12 :
            harga = 50000
            print(f"Kategori: Anak - Harga: Rp {harga}")
        else :
            harga = 100000
            print(f"Kategori: Dewasa - Harga: Rp {harga}")
        
        total_pendapatan += harga
        sisa_kursi -= 1
    except :
        print("Input umur harus berupa angka!")

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")