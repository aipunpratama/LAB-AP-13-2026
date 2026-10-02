def hitung_mundur(n):
    print(n)
    if n == 0:
        print("Luncurkan!")
    else:
        hitung_mundur(n - 1)

def minta_input_valid():
    angka = int(input("Masukkan angka awal hitung mundur: "))
    if angka < 0 or angka == -0:
        print("Input tidak valid, angka tidak boleh negatif.")
        return minta_input_valid()
    return angka

angka_awal = minta_input_valid()
hitung_mundur(angka_awal)