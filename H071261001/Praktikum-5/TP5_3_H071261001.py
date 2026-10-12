alfabet = 'abcdefghijklmnopqrstuvwxyz'

def cek_sandi(ch, k):
    if ch.lower() not in alfabet:
        return ch
    
    indeks_awal = alfabet.find(ch.lower())
    indeks_baru = (indeks_awal + k) % 26
    karakter_baru = alfabet[indeks_baru]
    
    if ch.isupper():
        return karakter_baru.upper()
    return karakter_baru

def proses_sandi(teks, k, is_enkripsi=True):
    if not is_enkripsi:
        k = -k
        
    teks_hasil = ""
    for ch in teks:
        teks_hasil += cek_sandi(ch, k)
        
    return teks_hasil

def brute_force_sandi(teks, kata_kunci):
    hasil_dekripsi = []
    kata_kunci_lower = kata_kunci.lower()
    
    for k in range(26):
        pesan_mencoba = proses_sandi(teks, k, is_enkripsi=False)
        if kata_kunci_lower in pesan_mencoba.lower():
            hasil_dekripsi.append((k, pesan_mencoba))
            
    return hasil_dekripsi

# Program Utama
pesan_terenkripsi = input("Masukkan pesan terenkripsi: ")
kata_kunci = input("Masukkan kata kunci target: ")

hasil = brute_force_sandi(pesan_terenkripsi, kata_kunci)

for kunci, pesan in hasil:
    print(f"Output Deskripsi: [{kunci}, '{pesan}']")