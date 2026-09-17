jarak = int(input("Masukkan jarak pengiriman: "))
express = input("Layanan express (ya/tidak): ").lower()

if jarak < 5:
    tarif_awal = 10000
elif jarak >= 5 and jarak <=20:
    tarif_awal = 20000
else:
    tarif_awal = 35000

biaya_tambahan = 15000 if express == "ya" else "tidak"
total_tarif = tarif_awal + biaya_tambahan
print("Total tarif pengiriman: Rp", total_tarif)