def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_valid = ("C", "F", "K")
    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    # Ubah dulu ke Celsius
    if skala_asal == "C":
        celsius = suhu
    elif skala_asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:  # K
        celsius = suhu - 273.15

    # Ubah dari Celsius ke skala tujuan
    if skala_tujuan == "C":
        return celsius
    elif skala_tujuan == "F":
        return celsius * 9 / 5 + 32
    else:  # K
        return celsius + 273.15


print("=== Konversi Suhu ===")
while True:
    masukan = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if masukan.strip().lower() == "selesai":
        break

    try:
        suhu = float(masukan)
    except ValueError:
        print("Error: Suhu harus berupa angka.")
        continue

    skala_asal = input("Skala asal (C/F/K): ").strip().upper()
    skala_tujuan = input("Skala tujuan (C/F/K): ").strip().upper()

    try:
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu} {skala_asal} = {round(hasil, 2)} {skala_tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali.")