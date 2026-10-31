import re

def bersihkan_nomor(telp):
    return re.sub(r"[ -]", "", telp)
def validasi_nomor(telp_bersih):
    return re.fullmatch(r"\d{10,13}", telp_bersih)

print("=== Pembersihan Data Nomor ===")
try:
    jumlah = int(input("masukkan jumlah data: "))
    data_sebelum = []
    data_sesudah = []
    status_list = []
    list_valid = []

    for i in range(1, jumlah + 1):
        nomor = input(f"Nomor ke-{i}: ")
        data_sebelum.append(nomor)
        no_bersih = bersihkan_nomor(nomor)
        data_sesudah.append(no_bersih)
    
        if validasi_nomor(no_bersih):
            status_list.append("Valid")
            list_valid.append(no_bersih)
        else:
            status_list.append("Tidak valid")

    print("\n--- Hasil Pembersihan ---")
    for i in range(jumlah):
        print(f"Data {i+1}:")
        print(f"Sebelum: {data_sebelum[i]}")
        print(f"Sesudah: {data_sesudah[i]}")
        print(f"Status : {status_list[i]}\n")

    print("Jumlah nomor valid:", len(list_valid))

except:
    print("Error: Jumlah data harus berupa angka bulat!")