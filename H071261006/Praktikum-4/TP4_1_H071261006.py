def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal - (subtotal * 0.10)
    return subtotal

print("Selamat Datang di Kasir Minimarket\n")

status_member = input("apakah anda member? (y/n): ")
is_member = (status_member == "y")

total_belanja = 0

while True:
    barang = input("masukkan nama barang: ")
    
    if barang == "":
        break
    harga = int(input("masukkan harga barang: "))
    jumlah = int(input("masukkan jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, is_member)
    total_belanja = total_belanja + subtotal

    print(f"subtotal {barang}: Rp{int(subtotal)}")

print(f"total belanja: Rp{int(total_belanja)}")