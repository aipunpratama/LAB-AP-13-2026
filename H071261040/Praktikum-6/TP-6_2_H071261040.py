def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()
    if nama in kandidat_set:
        return f"'{nama}' sudah terdaftar sebagai kandidat!"
    kandidat_set.add(nama)
    return f"'{nama}' berhasil didaftarkan sebagai kandidat!"

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    kunci = nama_pemilih.strip().lower()
    pilihan = pilihan.strip().capitalize()

    if kunci in rekap_suara:
        return f"'{nama_pemilih.strip()}' sudah memberikan suara sebelumnya!"
    if pilihan not in kandidat_set:
        return f"Error: Kandidat '{pilihan}' tidak ada! Suara tidak dicatat."

    rekap_suara[kunci] = pilihan
    return f"Suara '{nama_pemilih.strip()}' untuk '{pilihan}' berhasil dicatat!"


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in sorted(kandidat_set)}
    for kandidat in rekap_suara.values():
        perolehan[kandidat] += 1
    return perolehan


def tampilkan_hasil(perolehan):
   
    print("=============================")
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=============================")
    for kandidat, jumlah in perolehan.items():
        print(f" {kandidat}: {jumlah} suara")

    total = sum(perolehan.values())
    print(f"Total suara masuk: {total}")

    if total == 0:
        print("Belum ada suara yang masuk, tidak ada pemenang.")
    else:
        tertinggi = max(perolehan.values())
        pemenang = [k for k, v in perolehan.items() if v == tertinggi]
        if len(pemenang) > 1:
            print(f"Hasil SERI antara: {', '.join(pemenang)}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")
    print("=============================")


print("=============================")
print(" SISTEM PEMILIHAN KETUA KELAS")
print("=============================")

print("--- FASE PENDAFTARAN KANDIDAT ---")
kandidat_set = set()
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat sebelum melanjutkan!")
            continue
        break
    print(daftar_kandidat(kandidat_set, nama))
print(f"Kandidat terdaftar: {kandidat_set}")

print("--- FASE PEMUNGUTAN SUARA ---")
rekap_suara = {}
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ")
    print(berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan))

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)