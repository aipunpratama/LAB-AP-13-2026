jarak_pengiriman = int(input("Masukkan jarak pengiriman: "))
layanan_express = input("layanan express (ya/tidak):").lower()

if jarak_pengiriman <5:
    tarif_dasar = 10000
elif 5<= jarak_pengiriman <=20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000
 
BIAYA_TAMBAHAN = 15000 if layanan_express == "ya" else "tidak"
total_tarif = BIAYA_TAMBAHAN + tarif_dasar
print(f"total tarif: Rp {total_tarif}")