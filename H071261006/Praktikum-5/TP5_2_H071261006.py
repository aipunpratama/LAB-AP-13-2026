# --- SOAL 2: SENSOR KATA ---

# 1. Fungsi untuk mencari semua posisi indeks kata target
def cek_kata(teks, kata):
    indeks_list = []
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    
    start = 0
    while True:
        idx = teks_lower.find(kata_lower, start)
        if idx == -1:
            break
        indeks_list.append(idx)
        start = idx + 1 
        
    return indeks_list


# 2. Fungsi untuk memastikan kata yang ketemu adalah kata utuh (bukan bagian kata lain)
def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if i > 0:
        if teks[i - 1] in alfabet:
            return False
    idx_sesudah = i + panjang
    if idx_sesudah < len(teks):
        if teks[idx_sesudah] in alfabet:
            return False
    return True

 
# 3. Fungsi Utama Sensor Kata
def sensor_kata(teks, kata, simbol):
    indeks_semua = cek_kata(teks, kata)
    panjang_kata = len(kata)
    
    indeks_valid = []
    for idx in indeks_semua:
        if cek_batas_kata(teks, idx, panjang_kata):
            indeks_valid.append(idx)
            
    teks_tersensor = ""
    posisi_sekarang = 0
    
    for idx in indeks_valid:
        teks_tersensor += teks[posisi_sekarang:idx] + (simbol * panjang_kata)
        posisi_sekarang = idx + panjang_kata
    teks_tersensor += teks[posisi_sekarang:]
    return (teks_tersensor, len(indeks_valid), indeks_valid)


# --- Program Utama ---
masukkan_teks = input("Masukkan Teks: ")
kata_target = input("Masukkan kata target: ")
simbol_sensor = input("Masukkan simbol: ")

# Jalankan fungsi
hasil_teks, jumlah, list_indeks = sensor_kata(masukkan_teks, kata_target, simbol_sensor)

# Tampilkan hasil
print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah}  Indeks: {list_indeks}")