def rekap_nilai(*args):
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata_rata, tertinggi, terendah

daftar_nilai = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if input_nilai == "":
        break
    daftar_nilai.append(float(input_nilai))

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, max_nilai, min_nilai = rekap_nilai(*daftar_nilai)
    
    if max_nilai.is_integer():
        max_nilai = int(max_nilai)
    if min_nilai.is_integer():
        min_nilai = int(min_nilai)
        
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {max_nilai}")
    print(f"Nilai terendah: {min_nilai}")