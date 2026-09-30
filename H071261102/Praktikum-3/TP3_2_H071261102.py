print("---- Setup Denah Bioskop NontonYuk ----")

while True:
    try:
        input_baris = input("Masukkan jumlah baris: ")
        baris = int(input_baris)
        if baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input baris harus berupa angka!")

while True:
    try:
        input_kursi = input("Masukkan kursi per baris: ")
        kursi = int(input_kursi)
        if kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input kursi harus berupa angka!")
        print()

print("---- Daftar Kursi Tersedia ----")

for b in range(1, baris + 1):
    for k in range(1, kursi + 1):
        if k == 13:
            continue
        
        if b == 1 and k % 2 == 0:
            continue
            
        print(f"Baris {b} - Kursi {k}")