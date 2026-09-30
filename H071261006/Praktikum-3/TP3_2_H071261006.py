print("----- Setup Denah Bioskop NontonYuk -----")

while True:
    try:
        N = int(input("masukkan jumlah baris: "))
        if N <=0:
            print("Jumlah baris harus  lebih dari 0")
            continue
        break
    except ValueError:
        print("Input baris harus berupa angka!")

while True:
    try:
        M = int(input("masukkan jumlah kursi perbaris: "))
        if M <=0:
            print("jumlah kursi harus lebih dari 0")
            continue
        break
    except ValueError:
        print("input kursi harus berupa angka!")

print("---Daftar kursi tersedia---")
for baris in range(1, N+1):
    for kursi in range(1, M+1):
        if kursi == 13:
            continue
        if baris == 1 and kursi % 2 == 0:
            continue
        print(f"Baris {baris} - Kursi {kursi}")