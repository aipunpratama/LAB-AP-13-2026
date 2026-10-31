print("========================================")
print("  PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def format_durasi(detik):
    menit = detik // 60
    sisa_detik = detik % 60
    return f"{menit}:{sisa_detik:02d}"

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return
        
    print("==================================================")
    print(f"{'No':<3} | {'Judul':<20} | {'Artis':<15} | {'Genre':<8} | {'Durasi':<6}")
    print("--------------------------------------------------")
    total_detik = 0
    i = 1
    for judul, artis, genre, durasi in playlist:
        total_detik += durasi
        print(f"{i:<3} | {judul:<20} | {artis:<15} | {genre:<8} | {format_durasi(durasi):<6}")
        i += 1
    print("==================================================")
    m_total = total_detik // 60
    d_total = total_detik % 60
    print(f"Total durasi playlist: {m_total} menit {d_total} detik")

def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]

def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus dari playlist.")
    else:
        print("Nomor lagu tidak valid.")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist kosong, tidak ada statistik.")
        return
        
    total_lagu = len(playlist)
    jumlah_genre = len(genre_set)
    
    distribusi = {genre: 0 for genre in genre_set}
    for _, _, genre, _ in playlist:
        if genre in distribusi:
            distribusi[genre] += 1
            
    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])
    
    print("========================================")
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")
    print(f"Total lagu          : {total_lagu}")
    print(f"Jumlah genre        : {jumlah_genre}")
    print(f"Daftar genre        : {genre_set}")
    print("Distribusi genre:")
    for g, count in distribusi.items():
        print(f"  {g:<10} : {'#' * count} ({count})")
    print(f"Lagu terpanjang     : {lagu_terpanjang[0]} ({format_durasi(lagu_terpanjang[3])})")
    print(f"Lagu terpendek      : {lagu_terpendek[0]} ({format_durasi(lagu_terpendek[3])})")
    print("========================================")

playlist = []
genre_set = set()

while True:
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre: ")
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Durasi harus berupa angka positif!")
                continue
            tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Error: Durasi harus berupa angka bulat (detik)!")
            
    elif pilihan == "2":
        tampilkan_playlist(playlist)
        
    elif pilihan == "3":
        if not genre_set:
            print("Belum ada genre di playlist.")
            continue
        print(f"Genre tersedia: {genre_set}")
        genre_target = input("Masukkan genre yang ingin difilter: ")
        hasil_filter = filter_genre(playlist, genre_target)
        print(f"Lagu bergenre '{genre_target}':")
        i = 1
        for j, a, g, d in hasil_filter:
            print(f"{i}. {j} - {a} ({format_durasi(d)})")
            i += 1
            
    elif pilihan == "4":
        tampilkan_playlist(playlist)
        try:
            nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
            hapus_lagu(playlist, nomor)
        except ValueError:
            print("Error: Nomor lagu harus berupa angka!")
            
    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)
        
    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih angka 1-6.")