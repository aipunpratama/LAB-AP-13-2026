def rekap_nilai(*nilai):
    rata = sum(nilai) / len(nilai)
    return rata, max(nilai), min(nilai)

def konversi_ke_angka(teks):
    try:
        return int(teks)
    except ValueError:
        return float(teks)

daftar_nilai = []
while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
        break
    try:
        daftar_nilai.append(konversi_ke_angka(masukan))
    except ValueError:
        print("Input tidak valid, masukkan angka.")

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")