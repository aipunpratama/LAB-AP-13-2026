#1
presentase_cabai = int(input("masukan presntase cabai (angka):"))

if 0 <= presentase_cabai <= 10:
    print("level aman")
elif 11 <= presentase_cabai <= 40:
    print("level sedang")
elif 41 <= presentase_cabai <= 70:
    print("level pedas")
elif presentase_cabai > 70:
    print("level ekstrim")
else :
    print("invalid")

