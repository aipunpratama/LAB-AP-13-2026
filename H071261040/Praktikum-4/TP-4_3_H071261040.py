import time

def hitung_mundur(n):
    print(n)
    time.sleep(1)
    if n == 0:
        print("Luncurkan!")
        return
    hitung_mundur(n - 1)

while True:
    try:
        angka = int(input("Masukkan angka awal hitung mundur: "))
    except ValueError:
        print("Input tidak valid, masukkan angka bulat.")
        continue
    if angka < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
    else:
        break
hitung_mundur(angka)