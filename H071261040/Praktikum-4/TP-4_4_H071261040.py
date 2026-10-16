def konversi_suhu(suhu, asal, tujuan):
    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    elif asal == "K":
        celsius = suhu - 273.15
    else:
        raise ValueError("Skala suhu tidak dikenali")

    if tujuan == "C":
        hasil = celsius
    elif tujuan == "F":
        hasil = celsius * 9 / 5 + 32
    elif tujuan == "K":
        hasil = celsius + 273.15
    else:
        raise ValueError("Skala suhu tidak dikenali")

    return round(hasil, 2)

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

    asal = input("Skala asal (C/F/K): ").strip().upper()
    tujuan = input("Skala tujuan (C/F/K): ").strip().upper()

    try:
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali.")