def tambah_buku(inventaris, judul, penulis, harga, stok):
    inventaris.append({
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    })
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    return [b for b in inventaris if kata_kunci.lower() in b["judul"].lower()]

def update_stok(inventaris, judul, jumlah):
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            stok_baru = b["stok"] + jumlah
            if stok_baru < 0:
                print("Gagal: Stok tidak boleh negatif setelah perubahan.")
            else:
                b["stok"] = stok_baru
                status = "berkurang" if jumlah < 0 else "bertambah"
                print(f"Stok '{b['judul']}' {status} {abs(jumlah)}. Stok sekarang: {stok_baru}")
            return
    print("Error: Buku tidak ditemukan dalam inventaris.")

def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris masih kosong.")
        return
    
    total_stok = sum(b["stok"] for b in inventaris)
    total_aset = sum(b["harga"] * b["stok"] for b in inventaris)
    buku_termahal = max(inventaris, key=lambda x: x["harga"])
    
    print("\n=== RINGKASAN INVENTARIS BOOKNEST ===")
    print(f"Jumlah jenis buku: {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    print(f"Buku termahal   : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("=====================================")

def program_utama():
    inventaris = []
    
    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ").strip()
        
        if pilihan == '1':
            judul = input("Judul buku: ").strip()
            penulis = input("Penulis: ").strip()
            try:
                harga = float(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif!")
                    continue
                tambah_buku(inventaris, judul, penulis, harga, stok)
            except ValueError:
                print("Error: Harga harus berupa angka dan stok berupa bilangan bulat!")
                
        elif pilihan == '2':
            keyword = input("Masukkan kata kunci judul: ").strip()
            hasil = cari_buku(inventaris, keyword)
            print(f"Ditemukan {len(hasil)} buku:")
            for i, b in enumerate(hasil, 1):
                print(f"{i}. {b['judul']}")
                print(f"{b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")
                
        elif pilihan == '3':
            judul_update = input("Judul buku yang ingin diupdate: ").strip()
            try:
                jml = int(input("Jumlah perubahan (positif tambah, negatif=kurang): "))
                update_stok(inventaris, judul_update, jml)
            except ValueError:
                print("Error: Masukkan angka yang valid untuk perubahan stok.")
                
        elif pilihan == '4':
            ringkasan_inventaris(inventaris)
            
        elif pilihan == '5':
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-5.")

if __name__ == "__main__":
    program_utama()