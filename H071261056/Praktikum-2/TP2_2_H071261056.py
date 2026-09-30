#2
jarak_pengiriman = int(input("masukan_jarak_pengiriman:"))
layanan_express =input("layanan_express(ya/tidak):")

if jarak_pengiriman < 5:
    tarif = 10000
elif jarak_pengiriman <= 20:
    tarif = 20000
else :
    tarif = 35000

biaya_tambahan= 15000 if layanan_express == "ya" else (0 if layanan_express == "tidak" else None)
total_tarif = tarif + biaya_tambahan
print ("Total tarif pengiriman : Rp", total_tarif)