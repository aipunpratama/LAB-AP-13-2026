#soal 1. Tentukan subtotal untuk Kopi Susu, Matcha Latte, dan Americano berdasarkan data harga dan jumlah yang terjual. Simpan hasilnya dalam sub_kopi, sub_matcha, dan sub_americano.
#soal 2. Masukkan ketiga subtotal tersebut ke dalam list bernama subtotal_pendapatan
#soal 3. Hitung total_seluruh. Gunakan BIAYA_OPERASIONAL = 15000, kemudian hitung pendapatan_bersih.
#soal 4. Hitung jumlah semua barang yang terjual. Buat target_tercapai dengan kondisi total pendapatan > Rp200.000 dan jumlah barang > 10.


menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

#Soal 1
subtotal_Kopi_Susu = harga[0]*jumlah[0]
subtotal_Matcha_Latte = harga[1]*jumlah[1]
subtotal_Americano = harga[2]*jumlah[2]

#Soal 2
subtotal_pendapatan = [subtotal_Kopi_Susu, subtotal_Matcha_Latte, subtotal_Americano]
print(subtotal_pendapatan)

#Soal 3
BIAYA_OPERASIONAL = 15000
total_seluruh = (subtotal_Kopi_Susu + subtotal_Matcha_Latte +subtotal_Americano)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL
print("Total Seluruh:", total_seluruh)
print("Pendapatan Bersih:", pendapatan_bersih)

#Soal 4
jumlah_semua_barang = (jumlah[0] + jumlah[1] + jumlah[2])
target_tercapai = (total_seluruh > 200000) and (jumlah_semua_barang > 10)
print("Jumlah barang terjual:", jumlah_semua_barang)
print("Target tercapai?:", target_tercapai)