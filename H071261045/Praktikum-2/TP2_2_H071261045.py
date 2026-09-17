jarak_pengiriman = int(input("Masukkan jarak pengiriman: "))
layanan_express = input("Layanan Express (ya/tidak): ")
if jarak_pengiriman < 5:
    tarif_pengiriman = 10000
elif jarak_pengiriman <= 20:
    tarif_pengiriman = 20000
else:
    tarif_pengiriman = 35000

layanan = 15000 if layanan_express == "ya" else (0 if layanan_express == "tidak" else None)
tarif = tarif_pengiriman + layanan
print("Total tarif pengiriman: Rp", tarif)


