# --- SOAL 3: BRUTE FORCE CAESAR CIPHER ---

ALFABET = "abcdefghijklmnopqrstuvwxyz"

# 1. Fungsi Menggeser Satu Karakter
def cek_sandi(ch, k):
    ch_lower = ch.lower()
    idx = ALFABET.find(ch_lower)
    if idx == -1:
        return ch
    idx_baru = (idx + k) % 26
    char_baru = ALFABET[idx_baru]
    
    return char_baru.upper() if ch.isupper() else char_baru

# 2. Fungsi Enkripsi & Dekripsi
def mesin_enkripsi(teks, k):
    hasil = ""
    for char in teks:
        hasil += cek_sandi(char, k)
    return hasil
def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

# 3. Fungsi Peretas (Brute Force 0-25)
def retas_sandi(sandi, kata_kunci):
    hasil_retas = []
    kata_kunci_lower = kata_kunci.lower()
    for k in range(26):
        teks_dekripsi = mesin_dekripsi(sandi, k)
        if kata_kunci_lower in teks_dekripsi.lower():
            hasil_retas.append((k, teks_dekripsi))
            
    return hasil_retas

# --- Program Utama Soal 3 ---
sandi_masuk = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci_target = input("Masukkan kata kunci target: ")

hasil = retas_sandi(sandi_masuk, kata_kunci_target)
print(f"Output Deskripsi: {hasil}")