ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_kata(teks, kata):
    teks_kecil = teks.lower()
    kata_kecil = kata.lower()
    hasil = []
    start = 0
    while True:
        idx = teks_kecil.find(kata_kecil, start)
        if idx == -1:
            break
        hasil.append(idx)
        start = idx + 1
    return hasil

def _huruf(karakter):
    return karakter.lower() in ALFABET and karakter != ""

def cek_batas_kata(teks, i, panjang):
    if i > 0 and _huruf(teks[i - 1]):
        return False
    if i + panjang < len(teks) and _huruf(teks[i + panjang]):
        return False
    return True

def sensor_kata(teks, kata, simbol):
    panjang = len(kata)
    hasil = ""
    indeks_sensor = []
    pos = 0
    if panjang == 0:
        return (teks, 0, [])
    for i in cek_kata(teks, kata):
        if i < pos: 
            continue
        if cek_batas_kata(teks, i, panjang):
            hasil = hasil + teks[pos:i] + simbol[0] * panjang
            pos = i + panjang
            indeks_sensor.append(i)
    hasil = hasil + teks[pos:]
    return (hasil, len(indeks_sensor), indeks_sensor)

teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")
hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)