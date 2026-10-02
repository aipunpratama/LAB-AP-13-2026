def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *= 0.9  # harga utuh 100% - Diskon 10% = 90% = 0.9
    return int(subtotal)


def member():
    print("Selamat datang di Kasir Minimarket!")
    status_member = (input("Apakah Anda member? (y/n): ").lower())


    total_belanja = 0

    while True:
        nama_barang = str(input("Masukkan nama barang (kosongkan untuk selesai): "))
        if nama_barang == "":
            break  

        harga = int(input("Harga barang: ")) 
        jumlah = int(input("Jumlah barang: "))

        subtotal = hitung_subtotal(harga, jumlah, status_member == 'y')
        print(f"Subtotal {nama_barang}: Rp{subtotal}")

        total_belanja += subtotal

    print(f"Total belanja: Rp{total_belanja}")

member()
