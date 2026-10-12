
def cek_kata(teks, kata):
    indeks_kemunculan = []
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    mulai = 0

    if kata == "":
        return indeks_kemunculan

    while True:
        indeks = teks_kecil.find(kata_kecil, mulai)

        if indeks == -1:
            break

        indeks_kemunculan.append(indeks)
        mulai = indeks + 1

    return indeks_kemunculan


def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    if i > 0 and teks[i - 1].lower() in alfabet:
        return False

    akhir = i + panjang

    if akhir < len(teks) and teks[akhir].lower() in alfabet:
        return False

    return True


def sensor_kata(teks, kata, simbol):
    indeks_kemunculan = cek_kata(teks, kata)
    indeks_valid = []

    for i in indeks_kemunculan:
        if cek_batas_kata(teks, i, len(kata)):
            indeks_valid.append(i)

    teks_tersensor = ""
    posisi_sebelumnya = 0
    jumlah_tersensor = 0

    for i in indeks_valid:
        if i >= posisi_sebelumnya:
            teks_tersensor = (
                teks_tersensor
                + teks[posisi_sebelumnya:i]
                + simbol * len(kata)
            )

            posisi_sebelumnya = i + len(kata)
            jumlah_tersensor += 1

    teks_tersensor = teks_tersensor + teks[posisi_sebelumnya:]

    return teks_tersensor, jumlah_tersensor, indeks_valid


teks = input("Masukkan teks: ")
kata = input("Masukkan kata yang ingin disensor: ")
simbol = input("Masukkan simbol sensor: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Teks tersensor:", hasil)
print("Jumlah kata tersensor:", jumlah)
print("Indeks awal:", indeks)
