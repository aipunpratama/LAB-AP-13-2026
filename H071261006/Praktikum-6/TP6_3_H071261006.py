def format_durasi(detik):
    menit = detik // 60
    sisa_detik = detik % 60
    return f"{menit}:{sisa_detik:02d}"

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return
        
    print("\n==========================================")
    print(f"{'No':<3} {'Judul':<20} {'Artis':<15} {'Genre':<10} {'Durasi':<6}")
    print("==========================================")
    
    total_detik = 0
    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        print(f"{i:<3} {judul:<20} {artis:<15} {genre:<10} {format_durasi(durasi):<6}")
        total_detik = total_detik + durasi
        
    print("==========================================")
    print(f"Total durasi playlist: {total_detik // 60} menit {total_detik % 60} detik")

def filter_genre(playlist, genre_target):
    hasil = []
    for lagu in playlist:
        genre_lagu = lagu[2] 
        if genre_lagu.lower() == genre_target.lower():
            hasil.append(lagu)
    return hasil

def hapus_lagu(playlist, nomor):
    indeks = nomor - 1
    if 0 <= indeks < len(playlist):
        lagu_dihapus = playlist.pop(indeks)  
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus!")
    else:
        print("Nomor lagu tidak valid!")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist kosong, tidak ada statistik.")
        return
        
    print("\n==========================================")
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("==========================================")
    print(f"Total lagu    : {len(playlist)}")
    print(f"Jumlah genre  : {len(genre_set)}")
    print(f"Daftar genre  : {genre_set}")
    
    distribusi = {}
    for lagu in playlist:
        genre = lagu[2]
        if genre in distribusi:
            distribusi[genre] = distribusi[genre] + 1
        else:
            distribusi[genre] = 1
            
    print("\nDistribusi genre:")
    for genre in distribusi:
        jumlah = distribusi[genre]
        print(f"{genre:<10}: {'#' * jumlah} ({jumlah})")
        
    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])
    
    print(f"\nLagu terpanjang: {lagu_terpanjang[0]} ({format_durasi(lagu_terpanjang[3])})")
    print(f"Lagu terpendek : {lagu_terpendek[0]} ({format_durasi(lagu_terpendek[3])})")
    print("==========================================")

def main_playtune():
    playlist = []    
    genre_set = set() 

    while True:
        print("\n==========================================")
        print("PLAYLIST MUSIK PLAYTUNE")
        print("==========================================")
        print("Menu:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == "1":
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().capitalize()
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Durasi harus angka positif!")
                    continue
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Input durasi harus angka integer!")
                
        elif pilihan == "2":
            tampilkan_playlist(playlist)
            
        elif pilihan == "3":
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ").strip()
            hasil = filter_genre(playlist, target)
            if hasil:
                print(f"\nLagu bergenre '{target}':")
                for i, lagu in enumerate(hasil, 1):
                    print(f"{i}. {lagu[0]} - {lagu[1]} ({format_durasi(lagu[3])})")
            else:
                print(f"Tidak ada lagu bergenre '{target}'.")
                
        elif pilihan == "4":
            tampilkan_playlist(playlist)
            if playlist:
                try:
                    nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, nomor)
                    genre_set.clear()
                    for lagu in playlist:
                        genre_set.add(lagu[2])
                except ValueError:
                    print("Input nomor harus berupa angka!")
                    
        elif pilihan == "5":
            statistik_playlist(playlist, genre_set)
            
        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan menu tidak valid.")

if __name__ == "__main__":
    main_playtune()