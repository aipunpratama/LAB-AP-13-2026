def konversi_suhu(suhu, asal, tujuan):
    asal = asal.upper()
    tujuan = tujuan.upper()
    skala_valid = {"C", "F", "K"}  

    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")  

 
    if asal == "C":
        temp_c = suhu
    elif asal == "F":
        temp_c = (suhu - 32) * 5 / 9
    elif asal == "K":
        temp_c = suhu - 273.15

    
    if tujuan == "C":
        return round(temp_c, 1)
    elif tujuan == "F":
        return round((temp_c * 9 / 5) + 32, 1)
    elif tujuan == "K":
        return round(temp_c + 273.15, 1)



print("=== Konversi Suhu ===")  

while True:
    input_suhu = (input("Masukkan suhu (atau 'selesai' untuk keluar): ").strip().lower())
    if input_suhu == "selesai":
        break 

    try:
        suhu = float(input_suhu) 
        skala_asal = input("Skala asal (C/F/K): ").strip() 
        skala_tujuan = input("Skala tujuan (C/F/K): ").strip()  

        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan) 
        print(f"Hasil: {suhu} {skala_asal.upper()} = {hasil} {skala_tujuan.upper()}")  
    except ValueError:
        print("Error: Input suhu harus berupa angka.")