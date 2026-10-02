def rekap_nilai(*args):
    if not args:
        return None
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    return rata_rata, tertinggi, terendah

daftar_nilai = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if input_nilai == "":
        break

    nilai = (float(input_nilai) if "." in input_nilai else int(input_nilai)
    )
    daftar_nilai += [nilai]

if not daftar_nilai:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai) 
    print(f"Rata-rata kelas: {rata}") 
    print(f"Nilai tertinggi: {tertinggi}")  
    print(f"Nilai terendah: {terendah}")  