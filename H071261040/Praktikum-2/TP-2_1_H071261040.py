#Soal Nomor 1
persentase_cabai = float(input("Masukkan persentase cabai : "))
if persentase_cabai < 0 or persentase_cabai > 100 :
    print ("Invalid")
elif persentase_cabai <= 10 :
    print ("Level Aman")
elif persentase_cabai <= 40 :
    print ("Level Sedang")
elif persentase_cabai <= 70 :
    print ("Level Pedas")
else :
    print ("Level Ekstrem")