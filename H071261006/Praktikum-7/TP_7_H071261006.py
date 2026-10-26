import os
import random
from datetime import datetime

# SOAL 1: PEMBUATAN INVOICE & ID TRANSAKSI UNIK
os.makedirs("invoices", exist_ok=True)
print("==================================================")
print("                 SELAMAT DATANG                   ")
print("==================================================")

nama_kasir = input("Masukkan nama kasir     : ").strip()
daftar_kata = nama_kasir.split()
inisial = ""
for kata in daftar_kata:    
    inisial += kata[0].upper()

while True:
    print("==================================================")
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print("==================================================")
    
    opsi = input("Masukkan opsi pilihan   : ").strip()
    print("==================================================")
    
    if opsi == "1":
        # --- PROSES SOAL 1: TRANSAKSI BARU ---
        sekarang = datetime.now()
        tahun   = sekarang.strftime('%y')
        bulan   = sekarang.strftime('%m')
        tanggal = sekarang.strftime('%d')
        jam     = sekarang.strftime('%H')
        menit   = sekarang.strftime('%M')
        
        angka_acak = random.randint(100, 999)
        trx_id = f"{inisial}{tahun}{bulan}{tanggal}{jam}{menit}{angka_acak}"
        
        daftar_barang = []
        total_bayar = 0
        
        while True:
            nama_produk = input("Masukkan nama produk    : ").strip()
            harga = int(input("Masukkan harga produk   : "))
            jumlah = int(input("Masukkan jumlah produk  : "))
            
            subtotal = harga * jumlah
            total_bayar += subtotal
            
            daftar_barang.append(f"{nama_produk} x{jumlah} - Rp {subtotal}\n")
            
            print("--------------------------------------------------")
            tambah = input("Tambah produk? (y/t)    : ").strip().lower()
            print("--------------------------------------------------")
            
            if tambah == 't':
                break
        
        # Susun Tampilan Struk Invoice
        waktu_str = sekarang.strftime('%Y-%m-%d %H:%M:%S')
        
        isi_invoice = f"ID Transaksi : {trx_id}\n"
        isi_invoice += f"Kasir        : {nama_kasir}\n"
        isi_invoice += f"Waktu        : {waktu_str}\n"
        isi_invoice += "-" * 50 + "\n"
        isi_invoice += "".join(daftar_barang)
        isi_invoice += "-" * 50 + "\n"
        isi_invoice += f"Total        : Rp {total_bayar}\n"
        
        # Simpan Invoice ke file .txt di folder invoices/
        nama_file_invoice = f"invoices/{trx_id}.txt"
        with open(nama_file_invoice, "w") as file:
            file.write(isi_invoice)


        # SOAL 3: PENCATATAN RIWAYAT TRANSAKSI (TRX_HISTORY)
        
        nama_file_riwayat = "trx_history.txt"
        
        # Cek jika file belum ada, buatkan header tabelnya dulu
        if not os.path.exists(nama_file_riwayat):
            with open(nama_file_riwayat, "w") as file:
                file.write("=" * 65 + "\n")
                file.write(f"| {'Waktu':^19} | {'ID Transaksi':^17} | {'Nominal Transaksi':^18} |\n")
                file.write("=" * 65 + "\n")
                
        # Tambahkan baris riwayat transaksi baru di paling bawah (mode "a")
        with open(nama_file_riwayat, "a") as file:
            file.write(f"| {waktu_str} | {trx_id:<17} | Rp. {total_bayar:<14} |\n")
            file.write("=" * 65 + "\n")
            
        print("               TRANSAKSI BERHASIL                 ")
        print("==================================================")


    elif opsi == "2":
        # SOAL 2: PENCARIAN INVOICE BERDASARKAN ID
        input_id = input("Masukkan ID Transaksi   : ").strip()
        file_cari = f"invoices/{input_id}.txt"
        
        print("==================================================")
        # Memeriksa keberadaan file dengan os.path.exists
        if os.path.exists(file_cari):
            print("=== ISI INVOICE ===")
            # Membaca isi file dengan mode "r"
            with open(file_cari, "r") as file:
                print(file.read())
        else:
            print("Invoice tidak ditemukan!")
        print("==================================================")

    elif opsi == "3":
        # --- KELUAR DARI PROGRAM ---
        print("Terima kasih!")
        break   
    else:
        print("Opsi tidak valid, silakan coba lagi.")
        