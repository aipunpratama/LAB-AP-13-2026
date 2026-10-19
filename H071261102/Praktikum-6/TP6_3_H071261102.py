def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    playlist.append((judul, artis, genre, durasi))
    genre_set.add(genre)

def tampilkan_playlist(playlist):
    print(f"{'No':<4}{'Judul':<20}{'Artis':<20}{'Genre':<12}{'Durasi':<10}")
    print("-" * 66)
    
    total_detik = 0
    for idx, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        total_detik += durasi
        menit = durasi // 60
        detik = durasi % 60
        durasi_str = f"{menit}:{detik:02d}"
        print(f"{idx:<4}{judul:<20}{artis:<20}{genre:<12}{durasi_str:<10}")
        
    print("=" * 66)
    total_menit = total_detik // 60
    sisa_detik = total_detik % 60
    print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik")

def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]

def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        return playlist.pop(nomor - 1)
    return None

def statistik_playlist(playlist, genre_set):
    print("=== STATISTIK PLAYLIST ===")
    print(f"Total Lagu          : {len(playlist)}")
    print(f"Jumlah Genre Unik   : {len(genre_set)}")
    
    distribusi = {}
    for lagu in playlist:
        g = lagu[2]
        distribusi[g] = distribusi.get(g, 0) + 1
        
    print("Distribusi Lagu per Genre:")
    if distribusi:
        for g, count in distribusi.items():
            print(f"  - {g}: {count} lagu")
    else:
        print("  - Tidak ada lagu")
        
    if playlist:
        terpanjang = max(playlist, key=lambda x: x[3])
        terpendek = min(playlist, key=lambda x: x[3])
        
        m_long, s_long = terpanjang[3] // 60, terpanjang[3] % 60
        m_short, s_short = terpendek[3] // 60, terpendek[3] % 60
        
        print(f"Lagu Terpanjang     : {terpanjang[0]} - {terpanjang[1]} ({m_long}:{s_long:02d})")
        print(f"Lagu Terpendek      : {terpendek[0]} - {terpendek[1]} ({m_short}:{s_short:02d})")
    else:
        print("Lagu Terpanjang     : -")
        print("Lagu Terpendek      : -")

playlist = []
genre_set = set()

print("=" * 40)
print("PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter Berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
    
    pilihan = input("\nPilih menu (1-6): ")
    
    if pilihan == '1':
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        
        while True:
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi > 0:
                    break
                else:
                    print("Durasi harus angka positif!")
            except ValueError:
                print("Input tidak valid! Durasi harus berupa angka.")
        
        tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")
        
    elif pilihan == '2':
        print()
        if not playlist:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)
            
    elif pilihan == '3':
        print(f"Genre tersedia: {genre_set}")
        genre_target = input("Masukkan genre yang ingin difilter: ")
        hasil_filter = filter_genre(playlist, genre_target)
        
        print(f"\nLagu bergenre '{genre_target}':")
        if hasil_filter:
            for idx, lagu in enumerate(hasil_filter, 1):
                judul, artis, genre, durasi = lagu
                menit = durasi // 60
                detik = durasi % 60
                print(f"{idx}. {judul} - {artis} ({menit}:{detik:02d})")
        else:
            print("Tidak ada lagu dengan genre tersebut.")
            
    elif pilihan == '4':
        print()
        if not playlist:
            print("Playlist kosong, tidak ada lagu yang bisa dihapus.")
        else:
            tampilkan_playlist(playlist)
            try:
                nomor = int(input("\nMasukkan nomor lagu yang ingin dihapus: "))
                lagu_dihapus = hapus_lagu(playlist, nomor)
                if lagu_dihapus:
                    print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus!")
                    genre_set.clear()
                    for l in playlist:
                        genre_set.add(l[2])
                else:
                    print("Nomor lagu tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
                
    elif pilihan == '5':
        print()
        statistik_playlist(playlist, genre_set)
        
    elif pilihan == '6':
        print("Keluar dari program. Terima kasih!")
        break
    else:
        print("Pilihan menu tidak valid. Silakan pilih 1-6.")