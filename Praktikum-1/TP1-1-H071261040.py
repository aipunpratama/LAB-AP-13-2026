menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

#Nomor 1
sub_kopi = harga [0] * jumlah [0]
sub_matcha = harga [1] * jumlah [1] 
sub_americano = harga [2] * jumlah [2]  

#Nomor 2
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano] 

#Nomor 3
biaya_operasional = 15000
total_seluruh = sub_kopi + sub_matcha + sub_americano
pendapatan_bersih = total_seluruh - biaya_operasional

#Nomor 4
print ("--PENDAPATAN--")
print ("Total Pendapatan :", "Rp", total_seluruh)
print ("Pendapatan Bersih :", "Rp", pendapatan_bersih) 
if total_seluruh > 200000 and sum (jumlah) > 10 :
 print ("Target Tercapai") 
else :
 print ("Target Tidak Tercapai")