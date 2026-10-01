print ("--- Setup Denah Bioskop NontonYuk ---")
while True :
    try :
        baris = int(input ("Masukkan Jumlah Baris : "))
        if baris < 0 :
            print ("Jumlah Baris Harus Lebih Dari 0!")
        elif baris > 2 :
            print ("Jumlah Baris Hanya 2")
        elif 0 < baris <= 2 :
            kursi = int(input ("Masukkan Jumlah Kursi Per Baris : "))
            break
    except :
        print ("Input Harus Berupa Angka!")

print ("--- Daftar Kursi Tersedia ---")
for baris in range(1,3) :
    for kursi in range (1, 16, 1) :
         if kursi == 13 :
            continue
         if baris == 1 :
            if kursi % 2 != 0 :
             print(f"Baris {baris} - Kursi {kursi}")
         else :
            print(f"Baris {baris} - Kursi {kursi}")