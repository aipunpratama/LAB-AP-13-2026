#Buatlah program untuk membantu pengguna menghitung luas dan keliling aebuah persegi panjang.
#kemudian  program menghitung:
# Luas = Panjang x Lebar
#keliling = 2 x (panjang + lebar)
#ketentuan: Gunakan input(), konversikan panjang dan lebar menjadi float
#gunkanan operator aritmatika, tampilkan hasil menggunakan f-string
#perhatikan identasi dan penamaan variabel
#program meminta pengguna memassukkan panjang, lebar

#Input
panjang = int((input("Masukkan panjang: ")))
lebar = int((input("Masukkan lebar: ")))

#Luas
Luas = float((panjang*lebar))
print("Luas: ", Luas)

#Keliling
Keliling = float((2*(panjang + lebar)))
print("Keliling: ", Keliling)