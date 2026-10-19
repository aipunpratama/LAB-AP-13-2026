daftar_list_kandidat = set()
daftar_suara_kandidat = {}
daftar_suara_pemilihan = {}
rekapan_suara_yang_memilih = set()

def daftar_kandidat(nama):
    if nama in daftar_suara_kandidat:
        return False
    daftar_suara_kandidat[nama] = 0
    daftar_list_kandidat.add(nama)
    return True

def hitung_suara(kandidat):
    if kandidat not in daftar_suara_kandidat:
        return False
    daftar_suara_kandidat[kandidat] += 1
    return True

def berikan_suara(nama_pemilih, pilihan):
    if nama_pemilih in rekapan_suara_yang_memilih:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return
    if not hitung_suara(pilihan):
        print(f"Kandidat '{pilihan}' tidak terdaftar, suara tidak dicatat")
        return
    rekapan_suara_yang_memilih.add(nama_pemilih)
    daftar_suara_pemilihan[nama_pemilih] = pilihan
    print(f"Suara '{nama_pemilih}' untuk '{pilihan}' berhasil dicatat!")
    print()

def tampilkan_hasil():
    total_suara = len(daftar_suara_pemilihan)
    for nama, suara in daftar_suara_kandidat.items():
        print(f"   {nama}: {suara} suara")
    print()
    print(f"Total suara masuk: {total_suara}")

    if total_suara == 0:
        print("Belum ada suara yang masuk")
        return

    tertinggi = max(daftar_suara_kandidat.values())
    pemenang = [n for n, s in daftar_suara_kandidat.items() if s == tertinggi]

    if len(pemenang) > 1:
        print(f"Hasil seri antara {', '.join(pemenang)} dan perlu pemilihan ulang")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")

print("==================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("==================================")
while True:
    nama_kandidat = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip().title()
    if nama_kandidat == "":
        break
    if daftar_kandidat(nama_kandidat):
        print(f"'{nama_kandidat}' berhasil didaftarkan sebagai kandidat!")
    else:
        print(f"'{nama_kandidat}' sudah terdaftar")

if not daftar_list_kandidat:
    print("Belum ada kandidat terdaftar. Program selesai.")
    raise SystemExit

print()
print(f" Kandidat terdaftar: {daftar_list_kandidat}")
print()
print("--- FASE PEMUNGUTAN SUARA ---")
while True:
    print()
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip().title()
    if nama_pemilih == "":
        break
    print(f"Kandidat yang tersedia: {daftar_list_kandidat}")
    pilih_kandidat = input("Pilih kandidat: ").strip().title()
    if pilih_kandidat == "":
        print("Nama kandidat tidak boleh kosong")
        continue
    berikan_suara(nama_pemilih, pilih_kandidat)
print()
print("=================================")
print("   HASIL PEMILIHAN KETUA KELAS")
print("=================================")
tampilkan_hasil()