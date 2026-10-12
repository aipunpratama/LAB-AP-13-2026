
def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for karakter in teks:
        karakter = karakter.lower()
        if karakter in alfabet:
            hasil = hasil + karakter
    return hasil


def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks))

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return False, i

    return True, -1


def inti_palinrome(teks):
    teks = bersihkan_teks(teks)
    palindrom_terpanjang = ""
    indeks_awal = 0

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            substring = teks[i:j]
            hasil_cek, indeks_beda = cek_palinrome(substring)

            if hasil_cek and len(substring) > len(palindrom_terpanjang):
                palindrom_terpanjang = substring
                indeks_awal = i

    return {
        "teks": palindrom_terpanjang,
        "panjang": len(palindrom_terpanjang),
        "indeks_awal": indeks_awal
    }


teks = input("Masukkan teks prasasti: ")
teks_bersih = bersihkan_teks(teks)
hasil_akhir = inti_palinrome(teks)
print(hasil_akhir)
print(f"Teks bersih: {teks_bersih}")
print(f"Output terharap: {hasil_akhir}")

