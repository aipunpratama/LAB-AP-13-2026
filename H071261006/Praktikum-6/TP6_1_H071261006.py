def tambah_buku(inventaris, judul, penulis, harga, stok):
    inventaris.append({
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    })
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = [b for b in inventaris if kata_kunci.lower() in b["judul"].lower()]
    if not hasil:
        print("Buku tidak ditemukan.")
        return
    
    print(f"Ditemukan {len(hasil)} buku:")
    for i, buku in enumerate(hasil, 1):
        print(f"{i}. {buku['judul']} | {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print("Gagal: Stok tidak boleh menjadi negatif!")
                return
            buku["stok"] = stok_baru
            status = "bertambah" if jumlah >= 0 else "berkurang"
            print(f"Stok '{buku['judul']}' {status} {abs(jumlah)}. Stok sekarang: {buku['stok']}")
            return
    print("Error: Buku tidak ditemukan!")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong.")
        return
    
    total_jenis = len(inventaris)
    total_stok = sum(buku["stok"] for buku in inventaris)
    total_aset = sum(buku["harga"] * buku["stok"] for buku in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x["harga"])
    
    print("==========================================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("==========================================")
    print(f"Jumlah jenis buku : {total_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    print(f"Buku termahal     : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("==========================================")

def main_booknest():
    inventaris = []
    while True:
        print("==========================================")
        print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
        print("==========================================")
        print("Menu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == "1":
            judul = input("Judul buku: ").strip()
            penulis = input("Penulis: ").strip()
            try:
                harga = int(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif!")
                    continue
                tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Input harga dan stok harus berupa angka integer!")
        
        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ").strip()
            cari_buku(inventaris, kata_kunci)
            
        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ").strip()
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                update_stok(inventaris, judul, jumlah)
            except ValueError:
                print("Input jumlah perubahan harus berupa angka integer!")
                
        elif pilihan == "4":
            ringkasan_inventaris(inventaris)
            
        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan menu tidak valid.")
main_booknest()