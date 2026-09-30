#2
#Denah Kursi Bioskop Sebuah studio bioskop memiliki N baris dan M kursi di setiap barisnya. 
# Buatlah program Python menggunakan nested loop untuk mencetak daftar kursi yang siap dipesan oleh penonton, dengan aturan berikut:
#  ● Aturan Mitos: Kursi nomor 13 di baris mana pun tidak pernah dijual. Jika program bertemu kursi nomor 13, wajib dilewati. 
# ● Aturan Baris VVIP: Khusus Baris 1 (paling depan), jarak kursinya dibuat renggang, sehingga hanya kursi bernomor ganjil (1, 3, 5, dst.) yang bisa dipesan. 
# ● Aturan Baris Reguler: Untuk Baris 2 dan seterusnya, semua kursi bisa dipesan secara normal (1, 2, 3, 4, dst.). 
print ("=== Setup Denah Bioskop NontonYuk ===")
print ()


while True :
    try:
        Baris = int(input("jumlah Baris :"))
        if Baris <=0:
            print ("jumlah Baris tidak boleh kurang dari 0!")
            continue
        else :
            break
    except ValueError :
        print ("Input harus berupa angka!")

while True :
    try:
        Kursi = int(input("jumlah Kursi per baris :"))
        if Kursi <=0:
            print ("jumlah tidak boleh kurang dari 0!")
            continue
        else :
            break
    except ValueError :
        print ("Input harus berupa angka!")
print()
print ("=== Daftar Kursi Tersedia ===")
print ()
for Baris in range (1,Baris + 1):
    for Kursi in range (1, Kursi + 1):
        if Kursi == 13 :
            continue
        if Baris == 1 and Kursi % 2 == 0 :
            continue
        print (f"Baris {Baris} - Kursi {Kursi}")