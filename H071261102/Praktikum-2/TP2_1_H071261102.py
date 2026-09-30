level_pedas = int(input("Masukkan persentase cabai :"))

if 0<= level_pedas <=10:
    print("Level Aman")
elif 11<= level_pedas <=40:
    print("Level Sedang")
elif 41<= level_pedas <=70:
    print("Level Pedas")
elif level_pedas >70:
    print("Level Ekstrem")
else:
    print("Persentase cabai tidak valid")
