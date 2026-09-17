tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu kunjungan (Pagi/Malam): ")
pengunjung = input("Masukkan tipe pengunjung (Anak/Dewasa):")

match tujuan:
    case "Pantai":
        if waktu == "Pagi" and pengunjung == "Anak" or pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket A")
        elif waktu == "Malam" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Paket Rekomendasi: Tidak ada paket yang cocok")

    case "Pegunungan":
        if waktu == "Pagi" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        elif waktu == "Malam" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Paket Rekomendasi: Tidak ada paket yang cocok")

    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Paket Rekomendasi: Tidak ada paket yang cocok")

    case _:
        print("Paket Rekomendasi: Tidak ada paket yang cocok")
