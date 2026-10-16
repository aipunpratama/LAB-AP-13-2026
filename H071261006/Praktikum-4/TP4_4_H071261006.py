def konversi_suhu(suhu, asal, tujuan):
    asal = asal.upper()
    tujuan = tujuan.upper()
    
    # 1. Konversi dari skala asal ke Celsius
    if asal == "C":
        suhu_c = suhu
    elif asal == "F":
        suhu_c = (suhu - 32) * 5 / 9
    elif asal == "K":
        suhu_c = suhu - 273.15
    else:
        raise ValueError("Skala asal tidak valid! (Gunakan C, F, atau K)")

    # 2. Konversi dari Celsius ke skala tujuan
    if tujuan == "C":
        return suhu_c
    elif tujuan == "F":
        return (suhu_c * 9 / 5) + 32
    elif tujuan == "K":
        return suhu_c + 273.15
    else:
        raise ValueError("Skala tujuan tidak valid! (Gunakan C, F, atau K)")


print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if input_suhu.lower() == 'selesai':
        break
    
    try:
        suhu = float(input_suhu)
    except ValueError:
        print("Error: Masukkan angka suhu yang valid!")
        continue

    asal = input("Skala asal (C/F/K): ")
    tujuan = input("Skala tujuan (C/F/K): ")

    try:
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal.upper()} = {hasil} {tujuan.upper()}")
    except ValueError as e:
        print(f"Error: {e}")