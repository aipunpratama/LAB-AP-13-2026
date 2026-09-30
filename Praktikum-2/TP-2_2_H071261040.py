#Soal Nomor 2
jarak = int(input("Masukkan Jarak Pengiriman (KM) : "))
layanan = input("Layanan Express (Ya/Tidak) : ")
biaya_tambahan = 15000 if layanan == "Ya" else (0 if layanan == "Tidak" else None)
if jarak < 5 :
    jarak = 10000
elif jarak <= 20 :
    jarak = 20000
else :
    jarak = 35000
tarif = jarak + biaya_tambahan
print ("Total tarif pengiriman : Rp ", tarif)