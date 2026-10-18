def daftar_kandidat(kandidat_set, nama):
    kandidat_bersih = nama.strip().capitalize()
    if kandidat_bersih:
        if kandidat_bersih in kandidat_set:
            print(f"Kandidat '{kandidat_bersih}' sudah terdaftar!")
        else:
            kandidat_set.add(kandidat_bersih)
            print(f"'{kandidat_bersih}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_lower = nama_pemilih.strip().lower()
    pilihan_capitalize = pilihan.strip().capitalize()

    if pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return False

    if pilihan_capitalize not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak terdaftar.")
        return False

    rekap_suara[pemilih_lower] = pilihan_capitalize
    print(f"Suara '{nama_pemilih}' untuk '{pilihan_capitalize}' berhasil dicatat!")
    return True

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set} #dictionary
    for pilihan in rekap_suara.values():
        if pilihan in perolehan:
            perolehan[pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n=== HASIL PEMILIHAN KETUA KELAS ===")
    total_suara = sum(perolehan.values())

    for kandidat, jumlah in perolehan.items():
        print(f"{kandidat}: {jumlah} suara")

    print(f"Total suara masuk: {total_suara}")

    if not perolehan or total_suara == 0:
        print("Tidak ada suara yang masuk.")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == suara_tertinggi]

    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")

def program_utama():
    kandidat_set = set()
    rekap_suara = {} #dictionary

    print("=== FASE PENDAFTARAN KANDIDAT ===")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
        if not nama.strip():
            break
        daftar_kandidat(kandidat_set, nama)

    if len(kandidat_set) < 2:
        print("\nJumlah kandidat kurang dari 2. Pendaftaran dibatalkan.")
        return

    print(f"\nKandidat terdaftar: {kandidat_set}")
    print("\n=== FASE PEMUNGUTAN SUARA ===")

    while True:
        nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ")
        if not nama_pemilih.strip():
            break

        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ")
        berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

if __name__ == "__main__":
    program_utama()