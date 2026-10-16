ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(karakter, k):
    idx = ALFABET.find(karakter.lower())
    if idx == -1:  
        return karakter
    baru = ALFABET[(idx + k) % 26]
    if karakter == karakter.upper():
        return baru.upper()
    return baru.lower()

def mesin_enkripsi(teks, k):
    hasil = ""
    for karakter in teks:
        hasil += cek_sandi(karakter, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if pesan.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan))
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kunci = input("Masukkan kata kunci target: ")
print()
print("Output Deskripsi:", retas_sandi(sandi, kunci))