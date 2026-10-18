def detik_ke_menit(detik):
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

    print("\n==== PLAYLIST MUSIK PLAYTUNE ====")
    print(f"{'No':<4} {'Judul':<20} {'Artis':<15} {'Genre':<10} {'Durasi':<8}")
    print("-" * 60)
    
    total_durasi = 0
    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu
        total_durasi += durasi
        durasi_str = detik_ke_menit(durasi)
        print(f"{i:<4} {judul:<20} {artis:<15} {genre:<10} {durasi_str:<8}")
    
    print("-" * 60)
    total_menit = detik_ke_menit(total_durasi)
    print(f"Total durasi playlist: {total_menit.split(':')[0]} menit {total_menit.split(':')[1]} detik")

def filter_genre(playlist, genre_target):
    # Menggunakan list comprehension sesuai aturan soal
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]

def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus dari playlist.")
    else:
        print("Error: Nomor lagu tidak valid.")

def statistik_playlist(playlist, genre_set):
    if not playlist:
        print("Playlist masih kosong, belum ada statistik.")
        return

    total_lagu = len(playlist)
    
    distribusi = {} #dictionary
    for lagu in playlist:
        genre = lagu[2]
        distribusi[genre] = distribusi.get(genre, 0) + 1

    # Mencari lagu terpanjang dan terpendek berdasarkan durasi (indeks ke-3)
    lagu_terpanjang = max(playlist, key=lambda x: x[3])
    lagu_terpendek = min(playlist, key=lambda x: x[3])

    print("\n== STATISTIK PLAYLIST PLAYTUNE ==")
    print(f"Total lagu          : {total_lagu}")
    print(f"Jumlah genre unik   : {len(genre_set)}")
    print(f"Daftar genre        : {genre_set}")
    print("Distribusi genre:")
    for genre, jumlah in distribusi.items():
        bar = "#" * jumlah
        print(f"  {genre:<10} : {bar} ({jumlah})")
    
    print(f"Lagu terpanjang     : {lagu_terpanjang[0]} ({detik_ke_menit(lagu_terpanjang[3])})")
    print(f"Lagu terpendek      : {lagu_terpendek[0]} ({detik_ke_menit(lagu_terpendek[3])})")

def program_utama():
    playlist = []
    genre_set = set()

    while True:
        print("\nMenu PlayTune:")
        print("1. Tambah Lagu")
        print("2. Tampilkan Playlist")
        print("3. Filter berdasarkan Genre")
        print("4. Hapus Lagu")
        print("5. Statistik Playlist")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == '1':
            judul = input("Judul lagu: ").strip()
            artis = input("Artis: ").strip()
            genre = input("Genre: ").strip()
            try:
                durasi = int(input("Durasi (dalam detik): "))
                if durasi <= 0:
                    print("Durasi harus berupa angka positif!")
                    continue
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
            except ValueError:
                print("Error: Durasi harus berupa angka bulat positif!")

        elif pilihan == '2':
            tampilkan_playlist(playlist)

        elif pilihan == '3':
            if not genre_set:
                print("Belum ada genre yang tersedia.")
                continue
            print(f"Genre tersedia: {genre_set}")
            target = input("Masukkan genre yang ingin difilter: ").strip()
            hasil_filter = filter_genre(playlist, target)
            if not hasil_filter:
                print(f"Tidak ada lagu dengan genre '{target}'.")
            else:
                print(f"Lagu bergenre '{target}':")
                for i, l in enumerate(hasil_filter, 1):
                    print(f"{i}. {l[0]} - {l[1]} ({detik_ke_menit(l[3])})")

        elif pilihan == '4':
            tampilkan_playlist(playlist)
            if playlist:
                try:
                    nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                    hapus_lagu(playlist, nomor)
                except ValueError:
                    print("Error: Masukkan nomor yang valid.")

        elif pilihan == '5':
            statistik_playlist(playlist, genre_set)

        elif pilihan == '6':
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 6.")

if __name__ == "__main__":
    program_utama()