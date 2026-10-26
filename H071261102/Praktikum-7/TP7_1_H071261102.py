import os
import random
from datetime import datetime

FOLDER_INVOICES = "invoices"
os.makedirs(FOLDER_INVOICES, exist_ok=True)


def buat_id_transaksi(nama_kasir, waktu):
    inisial = "".join(kata[0] for kata in nama_kasir.split()).upper()
    tahun = waktu.strftime("%y")
    bulan = waktu.strftime("%m")
    tanggal = waktu.strftime("%d")
    jam_menit = waktu.strftime("%H%M")
    angka_acak = str(random.randint(100, 999))
    return f"{inisial}{tahun}{bulan}{tanggal}{jam_menit}{angka_acak}"


def buat_invoice():
    print("\n=== BUAT TRANSAKSI BARU ===")
    nama_kasir = input("Nama kasir: ").strip()

    if not nama_kasir:
        print("Nama kasir tidak boleh kosong.")
        return

    produk = []

    while True:
        print("\nMasukkan data produk")
        nama_produk = input("Nama produk (kosongkan jika selesai): ").strip()

        if not nama_produk:
            if not produk:
                print("Minimal harus ada satu produk.")
                continue
            break

        try:
            harga = int(input("Harga produk (Rp): "))
            jumlah = int(input("Jumlah produk: "))

            if harga < 0 or jumlah <= 0:
                print("Harga tidak boleh negatif dan jumlah harus lebih dari 0.")
                continue

        except ValueError:
            print("Harga dan jumlah harus berupa angka.")
            continue

        produk.append({
            "nama": nama_produk,
            "harga": harga,
            "jumlah": jumlah,
            "subtotal": harga * jumlah
        })

    waktu = datetime.now()
    id_transaksi = buat_id_transaksi(nama_kasir, waktu)
    total = sum(item["subtotal"] for item in produk)
    jalur_invoice = os.path.join(
        FOLDER_INVOICES,
        f"{id_transaksi}.txt"
    )

    with open(jalur_invoice, "w", encoding="utf-8") as file:
        file.write("=" * 48 + "\n")
        file.write("                 INVOICE BELANJA\n")
        file.write("=" * 48 + "\n")
        file.write(f"Waktu       : {waktu.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"ID Transaksi: {id_transaksi}\n")
        file.write(f"Nama Kasir  : {nama_kasir}\n")
        file.write("-" * 48 + "\n")
        file.write(
            f"{'Produk':20} {'Harga':>9} {'Jumlah':>6} {'Subtotal':>10}\n"
        )
        file.write("-" * 48 + "\n")

        for item in produk:
            file.write(
                f"{item['nama'][:20]:20} "
                f"{item['harga']:>9} "
                f"{item['jumlah']:>6} "
                f"{item['subtotal']:>10}\n"
            )

        file.write("-" * 48 + "\n")
        file.write(f"TOTAL TRANSAKSI: Rp. {total}\n")
        file.write("=" * 48 + "\n")

    file_baru = not os.path.exists("trx_history.txt")

    with open("trx_history.txt", "a", encoding="utf-8") as file:
        if file_baru:
            file.write("=" * 76 + "\n")
            file.write(
                f"| {'Waktu':19} | {'ID Transaksi':16} "
                f"| {'Nominal Transaksi':22} |\n"
            )
            file.write("=" * 76 + "\n")

        file.write(
            f"| {waktu.strftime('%Y-%m-%d %H:%M:%S')} | "
            f"{id_transaksi:16} | Rp. {total:<18} |\n"
        )
        file.write("=" * 76 + "\n")

    print("\nTransaksi berhasil!")
    print(f"ID Transaksi : {id_transaksi}")
    print(f"Total        : Rp. {total}")
    print(f"Invoice disimpan di: {jalur_invoice}")
    print("Riwayat transaksi telah diperbarui.")


def cari_invoice():
    print("\n=== CARI INVOICE ===")
    id_transaksi = input("Masukkan ID transaksi: ").strip()
    jalur_invoice = os.path.join(
        FOLDER_INVOICES,
        f"{id_transaksi}.txt"
    )

    if os.path.isfile(jalur_invoice):
        with open(jalur_invoice, "r", encoding="utf-8") as file:
            print("\n" + file.read())
    else:
        print("Invoice tidak ditemukan.")


def tampilkan_menu():
    while True:
        print("\n========== APLIKASI KASIR ==========")
        print("1. Buat invoice / transaksi baru")
        print("2. Cari dan tampilkan invoice")
        print("3. Lihat riwayat transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            buat_invoice()

        elif pilihan == "2":
            cari_invoice()

        elif pilihan == "3":
            try:
                with open("trx_history.txt", "r", encoding="utf-8") as file:
                    print("\n=== RIWAYAT TRANSAKSI ===")
                    print(file.read())
            except FileNotFoundError:
                print("Belum ada riwayat transaksi.")

        elif pilihan == "4":
            print("Program kasir selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1 sampai 4.")


if __name__ == "__main__":
    tampilkan_menu()