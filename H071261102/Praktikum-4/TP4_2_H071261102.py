def rekap_nilai(*nilai):
    rata_rata = sum(nilai) / len(nilai)
    tertinggi = max(nilai)
    terendah = min(nilai)
    return rata_rata, tertinggi, terendah


def ubah_angka(teks):
    # int jika bilangan bulat, float jika ada desimal
    try:
        return int(teks)
    except ValueError:
        return float(teks)


daftar_nilai = []
while True:
    masukan = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if masukan == "":
        break
    daftar_nilai.append(ubah_angka(masukan))

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tinggi, rendah = rekap_nilai(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tinggi}")
    print(f"Nilai terendah: {rendah}")