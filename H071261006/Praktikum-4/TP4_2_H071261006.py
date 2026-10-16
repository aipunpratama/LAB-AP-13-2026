def hitung_statistik(*nilai_list):
    if not nilai_list:
        return None
    
    rata_rata = sum(nilai_list) / len(nilai_list)
    tertinggi = int(max(nilai_list))
    terendah = int(min(nilai_list))
    
    return rata_rata, tertinggi, terendah

data_nilai = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ").strip()
    
    if input_nilai == "":
        break
        
    try:
        nilai = float(input_nilai)
        data_nilai.append(nilai)
    except ValueError:
        print("Input tidak valid! Harap masukkan angka yang benar.")

hasil = hitung_statistik(*data_nilai)

if hasil is None:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = hasil
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")