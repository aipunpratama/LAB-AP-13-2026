judul_nya = []
artis_nya = []
durasi_nya = []
genre_nya = set()
lagu_dan_genre = {}
genre_dan_total = {}
genre = ["Pop", "Rock", "Jazz", "RnB", "Dangdut"]
genre_valid = {g.lower(): g for g in genre}


def format_durasi(detik):
    return f"{detik // 60}:{detik % 60:02d}"


def tambah_lagu(playlist, judul, artis, genre_lagu, durasi):
    playlist[judul] = genre_lagu
    judul_nya.append(judul)
    artis_nya.append(artis)
    durasi_nya.append(durasi)
    genre_nya.add(genre_lagu)
    genre_dan_total[genre_lagu] = genre_dan_total.get(genre_lagu, 0) + 1


def tampilkan_playlist(playlist):
    if not judul_nya:
        print("Playlist masih kosong")
        return

    teks_durasi = [format_durasi(d) for d in durasi_nya]
    lebar_judul = max(len("Judul"), max(len(j) for j in judul_nya))
    lebar_artis = max(len("Artis"), max(len(a) for a in artis_nya))
    lebar_genre = max(len("Genre"), max(len(playlist[j]) for j in judul_nya))
    lebar_durasi = max(len("Durasi"), max(len(t) for t in teks_durasi))

    header = (f" {'No':<3} {'Judul':<{lebar_judul}}  {'Artis':<{lebar_artis}}  "
              f"{'Genre':<{lebar_genre}}  {'Durasi':>{lebar_durasi}}")
    garis = "=" * len(header)

    print(garis)
    print(header)
    print(garis)
    for nomor, (judul, artis, teks) in enumerate(zip(judul_nya, artis_nya, teks_durasi), start=1):
        print(f" {nomor:<3} {judul:<{lebar_judul}}  {artis:<{lebar_artis}}  "
              f"{playlist[judul]:<{lebar_genre}}  {teks:>{lebar_durasi}}")
    print(garis)

    total = sum(durasi_nya)
    print(f"Total durasi playlist: {total // 60} menit {total % 60} detik")
    print()


def filter_genre(playlist, genre_target):
    print(f"Lagu bergenre '{genre_target}':")
    urutan = 0
    for i, judul in enumerate(judul_nya):
        if playlist[judul] == genre_target:
            urutan += 1
            print(f"  {urutan}. {judul} - {artis_nya[i]} ({format_durasi(durasi_nya[i])})")
    if urutan == 0:
        print("  Tidak ada lagu dengan genre tersebut")


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(judul_nya):
        print("Tidak ada lagu pada nomor tersebut/tidak valid")
        return

    judul = judul_nya.pop(nomor - 1)
    artis_nya.pop(nomor - 1)
    durasi_nya.pop(nomor - 1)
    genre_lagu = playlist.pop(judul)

    genre_dan_total[genre_lagu] -= 1
    if genre_dan_total[genre_lagu] == 0:
        del genre_dan_total[genre_lagu]
        genre_nya.discard(genre_lagu)

    print(f"Lagu nomor {nomor} telah berhasil dihapus")
    print()
    tampilkan_playlist(playlist)


def statistik_playlist(playlist, genre_dan_total):
    if not judul_nya:
        print("Playlist masih kosong")
        return

    terpanjang = durasi_nya.index(max(durasi_nya))
    terpendek = durasi_nya.index(min(durasi_nya))

    print("===============================================")
    print("       STATISTIK PLAYLIST PLAYTUNE")
    print("===============================================")
    print(f"Total lagu        : {len(judul_nya)}")
    print(f"Jumlah genre      : {len(genre_nya)}")
    print(f"Daftar genre      : {', '.join(sorted(genre_nya))}")
    print()
    print("Distribusi genre:")
    for nama_genre, jumlah in sorted(genre_dan_total.items()):
        print(f"  {nama_genre:<8}: {'#' * jumlah} ({jumlah})")
    print()
    print(f"Lagu terpanjang : {judul_nya[terpanjang]} ({format_durasi(durasi_nya[terpanjang])})")
    print(f"Lagu terpendek  : {judul_nya[terpendek]} ({format_durasi(durasi_nya[terpendek])})")
    print("===============================================")


print("===============================")
print("   PLAYLIST MUSIK - PLAYTUNE")
print("===============================")

while True:
    print()
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    try:
        menu = int(input("Pilih menu (1-6): "))

        if menu == 1:
            judul_lagu = input("Judul lagu: ").strip().title()
            if judul_lagu == "":
                print("Judul tidak boleh kosong")
                continue
            if judul_lagu in lagu_dan_genre:
                print(f"Lagu '{judul_lagu}' sudah ada di playlist")
                continue
            artis_lagu = input("Artis: ").strip().title()
            genre_lagu = genre_valid.get(input("(Pop/Rock/Jazz/RnB/Dangdut): ").strip().lower())
            if genre_lagu is None:
                print("Genre yang anda masukkan tidak valid")
                continue
            durasi_lagu = int(input("Durasi (dalam detik): "))
            if durasi_lagu <= 0:
                print("Durasi harus lebih dari 0 detik")
                continue
            tambah_lagu(lagu_dan_genre, judul_lagu, artis_lagu, genre_lagu, durasi_lagu)
            print(f"Lagu '{judul_lagu}' oleh {artis_lagu} berhasil ditambahkan!")

        elif menu == 2:
            print()
            tampilkan_playlist(lagu_dan_genre)

        elif menu == 3:
            print(f"Genre tersedia: {', '.join(sorted(genre_nya))}")
            genre_target = genre_valid.get(input("Masukkan genre yang ingin difilter: ").strip().lower())
            if genre_target is None:
                print("Genre yang anda masukkan tidak valid")
                continue
            filter_genre(lagu_dan_genre, genre_target)

        elif menu == 4:
            if not judul_nya:
                print("Playlist masih kosong")
                continue
            tampilkan_playlist(lagu_dan_genre)
            nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
            hapus_lagu(lagu_dan_genre, nomor)

        elif menu == 5:
            statistik_playlist(lagu_dan_genre, genre_dan_total)

        elif menu == 6:
            print("Terima kasih telah menggunakan PlayTune!")
            break

        else:
            print("Input yang anda masukkan tidak valid")

    except ValueError:
        print("Input yang anda masukkan tidak valid")