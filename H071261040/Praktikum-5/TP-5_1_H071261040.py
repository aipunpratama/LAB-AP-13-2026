ALFABET = "abcdefghijklmnopqrstuvwxyz"

def bersihkan_teks(teks):
    hasil = ""
    for karakter in teks:
        if karakter in ALFABET or karakter in ALFABET.upper():
            hasil += karakter
    return hasil.lower()

def cek_palinrome(teks):
    terbalik = "".join(reversed(teks))
    if teks == terbalik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != terbalik[i]:
            return (False, i)

def inti_palinrome(teks):
    bersih = bersihkan_teks(teks)
    terpanjang = {"teks": "", "panjang": 0, "indeks_awal": 0}
    n = len(bersih)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = bersih[i:j]
            if len(sub) > terpanjang["panjang"] and cek_palinrome(sub)[0]:
                terpanjang = {"teks": sub, "panjang": len(sub), "indeks_awal": i}
    return terpanjang


teks = input("Masukkan teks prasasti: ")
print()
print("Teks Bersih:", bersihkan_teks(teks))
print("Output Terharap:", inti_palinrome(teks))