jarak = int(input("Masukkan jarak pengiriman (km): "))
layanan_express = input("Layanan express (ya/tidak): ").lower()

if jarak < 5:
    tarif_dasar = 10000
elif 5<=jarak <= 20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000

biaya_tambahan = 15000 if layanan_express == "ya" else (0 if layanan_express == "tidak" else None)

total_tarif = tarif_dasar + biaya_tambahan

print(f"Total tarif pengiriman: Rp{total_tarif}")