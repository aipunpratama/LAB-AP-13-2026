daftar_buku = {}
daftar_penulis = {}
daftar_harga = {}
daftar_stok = {}
 
 
def tambah_buku(judul, penulis, harga, stok):
    daftar_buku[judul] = judul
    daftar_penulis[judul] = penulis
    daftar_harga[judul] = harga
    daftar_stok[judul] = stok
 
def cari_judul(kata_kunci):
    kata_kunci = kata_kunci.lower()
    return [judul for judul in daftar_buku if kata_kunci in judul.lower()]
 
def mencari_buku(kata_kunci):
    hasil = cari_judul(kata_kunci)
    if not hasil:
        print("Tidak ada buku yang ditemukan")
        return
    print(f"Ditemukan {len(hasil)} buku:")
    for urutan, judul in enumerate(hasil, start=1):
        penulis = daftar_penulis[judul]
        harga = daftar_harga[judul]
        stok = daftar_stok[judul]
        print(f"  {urutan}. {judul} - {penulis} | Rp{harga} | Stok: {stok}")

def update_stok(judul, perubahan):
    if judul not in daftar_stok:
        print(f"Buku '{judul}' tidak ditemukan")
        return
    if daftar_stok[judul] + perubahan < 0:
        print(f"Gagal membuat perubahan. Stok '{judul}' hanya {daftar_stok[judul]}")
        return
    daftar_stok[judul] += perubahan
    if perubahan >= 0:
        print(f"Stok '{judul}' bertambah {perubahan}. Stok sekarang: {daftar_stok[judul]}")
    else:
        print(f"Stok '{judul}' berkurang {-perubahan}. Stok sekarang: {daftar_stok[judul]}")
 
def termahal():
    if not daftar_harga:
        print("Buku termahal     : -")
        return
    judul = max(daftar_harga, key=daftar_harga.get)
    print(f"Buku termahal     : {judul} (Rp{daftar_harga[judul]})")
 
def ringkasan():
    total_jenis = len(daftar_buku)
    total_stok = sum(daftar_stok.values())
    total_aset = sum(daftar_harga[j] * daftar_stok[j] for j in daftar_harga)
    print("===================================")
    print("  RINGKASAN INVENTARIS BOOKNEST")
    print("===================================")
    print(f"Jumlah jenis buku : {total_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    termahal()

 
print()
print("=======================================")
print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=======================================")
 
while True:
    print()
    print("Menu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
 
    try:
        menu = int(input("Pilih menu (1-5): "))
 
        if menu == 1:
            judul_buku = input("Judul buku: ").strip().title()
            if judul_buku == "":
                print("Judul tidak boleh kosong")
                continue
            penulis = input("Penulis: ").strip().title()
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif")
                continue
            if judul_buku in daftar_buku:
                print(f"Buku '{judul_buku}' sudah ada, datanya akan diperbarui")
            tambah_buku(judul_buku, penulis, harga, stok)
            print()
            print(f"Buku '{judul_buku}' berhasil ditambahkan!")
 
        elif menu == 2:
            kata_kunci = input("Masukkan kata kunci judul: ").strip()
            mencari_buku(kata_kunci)
 
        elif menu == 3:
            judul_buku = input("Judul buku yang ingin diupdate: ").strip().title()
            perubahan = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(judul_buku, perubahan)
 
        elif menu == 4:
            ringkasan()
 
        elif menu == 5:
            print("Terima kasih telah menggunakan BookNest!")
            break
 
        else:
            print("Input yang anda masukkan tidak valid")

    except ValueError:
        print("Input yang anda masukkan tidak valid")