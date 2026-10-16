def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = [b for b in inventaris if kata_kunci.lower() in b["judul"].lower()]
    print(f"Ditemukan {len(hasil)} buku:")
    i = 1
    for b in hasil:
        print(f"{i}. {b['judul']}")
        print(f"   {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")
        i += 1

def update_stok(inventaris, judul, jumlah):
    ditemukan = False
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            ditemukan = True
            stok_baru = b["stok"] + jumlah
            if stok_baru < 0:
                print(f"Gagal! Stok '{b['judul']}' tidak boleh menjadi negatif.")
            else:
                b["stok"] = stok_baru
                aksi = "berkurang" if jumlah < 0 else "bertambah"
                print(f"Stok '{b['judul']}' {aksi} {abs(jumlah)}. Stok sekarang: {b['stok']}")
            break
    if not ditemukan:
        print(f"Error: Buku dengan judul '{judul}' tidak ditemukan.")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong.")
        return
    
    jumlah_jenis = len(inventaris)
    total_stok = sum(b["stok"] for b in inventaris)
    total_aset = sum(b["harga"] * b["stok"] for b in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x["harga"])
    
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print(f"Jumlah jenis buku: {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print("========================================")
    print(f"Total nilai aset : Rp{total_aset}")
    print(f"Buku termahal    : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("========================================")

inventaris = []
while True:
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
                continue
            tambah_buku(inventaris, judul, penulis, harga, stok)
        except ValueError:
            print("Error: Harga harus berupa angka dan stok harus berupa bilangan bulat!")
            
    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)
        
    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Error: Jumlah perubahan harus berupa angka!")
            
    elif pilihan == "4":
        ringkasan_inventaris(inventaris)
        
    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-5.")