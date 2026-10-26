
from datetime import datetime
import random
from pathlib import Path


# Folder untuk menyimpan semua invoice
INVOICE_DIR = Path(__file__).parent / "invoices"
INVOICE_DIR.mkdir(exist_ok=True)

# File untuk menyimpan riwayat transaksi
HISTORY_FILE = Path(__file__).parent / "trx_history.txt"


def buat_id_transaksi(nama_kasir, waktu):
    # Membuat inisial nama kasir
    inisial = "".join(
        bagian[0] for bagian in nama_kasir.strip().split() if bagian
    ).upper()

    if not inisial:
        inisial = "K"

    # Membuat ID transaksi
    id_transaksi = (
        f"{inisial}"
        f"{waktu.strftime('%y%m%d%H%M')}"
        f"{random.randint(100, 999)}"
    )

    return id_transaksi


def format_rupiah(nominal):
    return f"Rp. {nominal:,.0f}".replace(",", ".")


def simpan_riwayat(waktu, id_transaksi, total):
    # Membuat file riwayat jika belum ada
    if not HISTORY_FILE.exists():
        with HISTORY_FILE.open("w", encoding="utf-8") as file:
            file.write("=" * 78 + "\n")
            file.write(
                f"| {'Waktu':19} | {'ID Transaksi':18} | "
                f"{'Nominal Transaksi':22} |\n"
            )
            file.write("=" * 78 + "\n")

    # Menambahkan transaksi ke riwayat
    with HISTORY_FILE.open("a", encoding="utf-8") as file:
        file.write(
            f"| {waktu.strftime('%Y-%m-%d %H:%M:%S'):19} | "
            f"{id_transaksi:18} | "
            f"{format_rupiah(total):22} |\n"
        )
        file.write("=" * 78 + "\n")


def buat_invoice():
    print("\n=== BUAT INVOICE ===")

    nama_kasir = input("Nama kasir: ").strip()

    while not nama_kasir:
        print("Nama kasir tidak boleh kosong.")
        nama_kasir = input("Nama kasir: ").strip()

    produk = []

    # Input beberapa produk dalam satu transaksi
    while True:
        print(f"\nProduk ke-{len(produk) + 1}")

        nama_produk = input(
            "Nama produk (kosong untuk selesai): "
        ).strip()

        if not nama_produk:
            if produk:
                break

            print("Masukkan setidaknya satu produk.")
            continue

        try:
            harga = int(input("Harga produk (angka rupiah): "))
            jumlah = int(input("Jumlah produk: "))

            if harga < 0 or jumlah <= 0:
                print(
                    "Harga tidak boleh negatif dan jumlah "
                    "harus lebih dari 0."
                )
                continue

        except ValueError:
            print("Harga dan jumlah harus berupa angka bulat.")
            continue

        subtotal = harga * jumlah

        produk.append({
            "nama": nama_produk,
            "harga": harga,
            "jumlah": jumlah,
            "subtotal": subtotal
        })

    # Menentukan waktu, ID transaksi, dan total belanja
    waktu = datetime.now()
    id_transaksi = buat_id_transaksi(nama_kasir, waktu)

    total = sum(item["subtotal"] for item in produk)

    # Menentukan lokasi file invoice
    path_invoice = INVOICE_DIR / f"{id_transaksi}.txt"

    # Menulis invoice ke file TXT
    with path_invoice.open("w", encoding="utf-8") as file:
        file.write("========== INVOICE ==========\n")
        file.write(f"ID Transaksi : {id_transaksi}\n")
        file.write(
            f"Waktu        : {waktu.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write(f"Nama Kasir   : {nama_kasir}\n")
        file.write("-" * 60 + "\n")

        file.write(
            f"{'Produk':20} {'Harga':>12} "
            f"{'Jumlah':>7} {'Subtotal':>14}\n"
        )
        file.write("-" * 60 + "\n")

        for item in produk:
            file.write(
                f"{item['nama'][:20]:20} "
                f"{format_rupiah(item['harga']):>12} "
                f"{item['jumlah']:>7} "
                f"{format_rupiah(item['subtotal']):>14}\n"
            )

        file.write("-" * 60 + "\n")
        file.write(f"TOTAL: {format_rupiah(total)}\n")
        file.write("=" * 60 + "\n")

    # Mencatat transaksi ke riwayat
    simpan_riwayat(waktu, id_transaksi, total)

    print("\nTransaksi berhasil!")
    print(f"ID transaksi : {id_transaksi}")
    print(f"Total        : {format_rupiah(total)}")
    print(f"Invoice disimpan di: {path_invoice}")


def cari_invoice():
    print("\n=== CARI INVOICE ===")

    id_transaksi = input("Masukkan ID transaksi: ").strip()

    # Mencari file berdasarkan ID transaksi
    path_invoice = INVOICE_DIR / f"{id_transaksi}.txt"

    if path_invoice.is_file():
        with path_invoice.open("r", encoding="utf-8") as file:
            isi_invoice = file.read()

        print("\n" + isi_invoice)

    else:
        print("Invoice tidak ditemukan.")


def tampilkan_riwayat():
    print("\n=== RIWAYAT TRANSAKSI ===")

    if HISTORY_FILE.is_file():
        with HISTORY_FILE.open("r", encoding="utf-8") as file:
            print(file.read())

    else:
        print("Belum ada riwayat transaksi.")


def main():
    while True:
        print("\n===== APLIKASI KASIR =====")
        print("1. Buat invoice")
        print("2. Cari invoice")
        print("3. Tampilkan riwayat transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            buat_invoice()

        elif pilihan == "2":
            cari_invoice()

        elif pilihan == "3":
            tampilkan_riwayat()

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Masukkan angka 1-4.")


if __name__ == "__main__":
    main()