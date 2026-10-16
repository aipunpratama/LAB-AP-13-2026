def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 0.9  
    return int(subtotal)

print("Selamat datang di Kasir Minimarket!")
member = input("Apakah Anda member? (y/n): ").strip().lower() == "y"

total = 0
while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    subtotal = hitung_subtotal(harga, jumlah, member)
    print(f"Subtotal {nama_barang}: Rp {subtotal}")
    total += subtotal

print(f"Total belanja: Rp {total}")