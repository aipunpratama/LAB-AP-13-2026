level_pedas = int(input("Masukkan level pedas: "))
if level_pedas <0:
    print("level tidak valid")
elif 0 <= level_pedas <=10:
    print("level aman")
elif 11<= level_pedas <=40:
    print("level sedang")
elif 41<= level_pedas <=70:
    print("level pedas")
else:
    print("level ekstrem")
