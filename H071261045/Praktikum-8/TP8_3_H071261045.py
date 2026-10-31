import re

def bersihkan_dan_validasi_telepon(nomor_mentah):
    nomor_bersih = re.sub(r'[\s-]', '', nomor_mentah)
    pattern = r'^\d{10,13}$'
    is_valid = bool(re.match(pattern, nomor_bersih))
    return nomor_bersih, is_valid

print("=== Pembersihan Data Nomor Telepon ===")
jumlah_data = int(input("Masukkan jumlah data: "))

list_mentah = []
list_bersih = []
list_status = []
jumlah_valid = 0

for i in range(jumlah_data):
    nomor = input(f"Nomor ke-{i+1}: ")
    list_mentah.append(nomor)
    
    bersih, valid = bersihkan_dan_validasi_telepon(nomor)
    list_bersih.append(bersih)
    
    if valid:
        list_status.append("Valid")
        jumlah_valid += 1
    else:
        list_status.append("Tidak valid")
        
print("\n--- Hasil Pembersihan ---")
for i in range(jumlah_data):
    print(f"Data {i+1}:")
    print(f"Sebelum: {list_mentah[i]}")
    print(f"Sesudah: {list_bersih[i]}")
    print(f"Status : {list_status[i]}\n")
    
print(f"Jumlah nomor valid: {jumlah_valid}")