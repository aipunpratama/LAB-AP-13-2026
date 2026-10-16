print("="*33)
print("  SISTEM PEMILIHAN KETUA KELAS")
print("="*33)
def daftar_kandidat(kandidat_set, nama):
    nama_format = nama.capitalize()
    if nama_format in kandidat_set:
        print(f"Kandidat '{nama_format}' sudah terdaftar.")
    else:
        kandidat_set.add(nama_format)
        print(f"'{nama_format}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_key = nama_pemilih.lower()
    pilihan_format = pilihan.capitalize()
    
    if pemilih_key in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return
    
    if pilihan_format not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak terdaftar dalam pilihan.")
        return
        
    rekap_suara[pemilih_key] = pilihan_format
    print(f"Suara '{nama_pemilih}' untuk '{pilihan_format}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {kandidat: 0 for kandidat in kandidat_set}
    for pemilih, pilihan in rekap_suara.items():
        if pilihan in perolehan:
            perolehan[pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    total_suara = sum(perolehan.values())
    print("\n========================================")
    print("HASIL PEMILIHAN KETUA KELAS")
    print("========================================")
    for kandidat, suara in perolehan.items():
        print(f"{kandidat}: {suara} suara")
    print(f"Total suara masuk: {total_suara}")
    
    if total_suara == 0:
        print("Belum ada suara yang masuk.")
        return

    suara_tertinggi = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == suara_tertinggi]
    
    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
    print("========================================")

kandidat_set = set()
rekap_suara = {}

print("--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if not nama:
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat sebelum bisa lanjut!")
            continue
        break
    daftar_kandidat(kandidat_set, nama)
    
print(f"Kandidat terdaftar: {kandidat_set}")
print("--- FASE PEMUNGUTAN SUARA ---")
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
    if not nama_pemilih:
        break
    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ").strip()
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)
    
perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)