def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 0.9  # diskon 10%
    return int(round(subtotal))


print("Selamat datang di Kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ").strip().lower()
member = status == "y"

total = 0
while True:
    nama = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, member)
    print(f"Subtotal {nama}: Rp{subtotal}")
    total += subtotal

print(f"Total belanja: Rp{total}")