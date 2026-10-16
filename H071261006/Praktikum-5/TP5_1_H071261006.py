# --- SOAL 1 ---

# 1. Fungsi Pembersihan Teks
def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""

    for char in teks:
        char_lower = char.lower()
        if char_lower in alfabet:
            teks_bersih += char_lower
            
    return teks_bersih


# 2. Fungsi Cek Palindrom
def cek_palinrome(teks):
    teks_terbalik = "".join(reversed(teks))
    if teks == teks_terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != teks_terbalik[i]:
            return (False, i)


# 3. Fungsi Utama Pencari Palindrom Terpanjang
def inti_palinrome(teks):
    n = len(teks)
    palindrom_terpanjang = ""
    panjang_maks = 0
    indeks_awal = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            potongan = teks[i:j]
            is_palindrom, _ = cek_palinrome(potongan)

            if is_palindrom:
                if len(potongan) > panjang_maks:
                    panjang_maks = len(potongan)
                    palindrom_terpanjang = potongan
                    indeks_awal = i
    return {
        "teks": palindrom_terpanjang,
        "panjang": panjang_maks,
        "indeks_awal": indeks_awal
    }


# --- Program Utama ---
masukan_teks = input("Masukkan teks prasasti: ")

# Jalankan fungsi
teks_hasil_bersih = bersihkan_teks(masukan_teks)
hasil_akhir = inti_palinrome(teks_hasil_bersih)

# Tampilkan hasil
print(f"Teks Bersih: {teks_hasil_bersih}")
print(f"Output Terharap: {hasil_akhir}")