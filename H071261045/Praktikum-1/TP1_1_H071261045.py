menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# 1. Menentukan subtotal Kopi Susu, Matcha Latte, dan Americano
subtotal_kopi_susu = harga[0] * jumlah[0]
subtotal_matcha_latte = harga[1] * jumlah[1]
subtotal_americano = harga[2] * jumlah[2]

# 2. Masukkan subtotal ke dalam list
subtotal_pendapatan = [subtotal_kopi_susu + subtotal_matcha_latte + subtotal_americano]

# 3. Menghitung ketiga subtotal
total_pendapatan = (subtotal_kopi_susu + subtotal_matcha_latte + subtotal_americano)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_pendapatan - BIAYA_OPERASIONAL

# 4. Menentukan apakah target tercapai
total_barang_terjual = jumlah[0] + jumlah[1] + jumlah[2]
target_tercapai = total_pendapatan > 200000 and total_barang_terjual > 10

# Menampilkan hasil perhitungan
print("Pendapatan dari Kopi Susu: Rp", subtotal_kopi_susu)
print("Pendapatan dari Matcha Latte: Rp", subtotal_matcha_latte)
print("Pendapatan dari Americano: Rp", subtotal_americano)
print("Total Pendapatan: Rp", total_pendapatan)
print("Pendapatan Bersih: Rp", pendapatan_bersih)
print("Target Tercapai:", target_tercapai)
