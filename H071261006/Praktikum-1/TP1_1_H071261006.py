#1
menu = ["kopi susu", "matcha latte", "americano"]
harga = [18000, 22000, 15000]
jumlah = [4,3,5]

sub_kopi_susu = harga[0] * jumlah[0]
sub_matcha_latte = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

#2
subtotal_pendapatan = sub_kopi_susu + sub_matcha_latte+ sub_americano

#3
total_seluruh = subtotal_pendapatan
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

#4
jumlah_barang = (jumlah[0] + jumlah[1] + jumlah[2])
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

#5
print("target tercapai: ", target_tercapai)
print("sub pendapatan kopi susu: ", sub_kopi_susu)
print("sub pendapatan matcha: ", sub_matcha_latte)
print("sub pendapatan americano: ", sub_americano)
print("pendapatan bersih: ", pendapatan_bersih)
print(f"Total pendapatan: {total_seluruh} yeyyy")