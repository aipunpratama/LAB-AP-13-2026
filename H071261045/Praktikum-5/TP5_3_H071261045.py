ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    if ch.lower() not in ALFABET:
        return ch

    indeks = ALFABET.find(ch.lower())
    indeks_baru = (indeks + k) % 26
    huruf_baru = ALFABET[indeks_baru]

    if ch.isupper():
        return huruf_baru.upper()

    return huruf_baru


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil = hasil + cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil = []

    for k in range(26):
        pesan_asli = mesin_dekripsi(sandi, k)

        if pesan_asli.lower().find(kata_kunci.lower()) != -1:
            hasil.append((k, pesan_asli))

    return hasil


sandi = input("Masukkan pesan tersita: ")
kata_kunci = input("Masukkan kata kunci target: ")

hasil = retas_sandi(sandi, kata_kunci)

print("Hasil dekripsi:", hasil)
