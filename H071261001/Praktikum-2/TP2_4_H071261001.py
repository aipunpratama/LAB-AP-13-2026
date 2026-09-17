tujuan = input("Masukkan tujuan (pantai/pegunungan/kota): ").lower()
waktu = input("Masukkan waktu (pagi/malam): ").lower()
pengunjung = input("Masukkan tipe pengunjung (anak/dewasa): ").lower()


match tujuan:
    case "pantai":
        if waktu == "pagi" and pengunjung == "anak":
            print("Paket A")
        elif waktu == "pagi" and pengunjung == "dewasa":
            print("Paket A")
        elif waktu == "malam" and pengunjung == "dewasa":
            print("Paket C")
    case "pegunungan":
        if waktu == "siang" and pengunjung == "dewasa":
            print("Paket B")
        elif waktu == "malam" and pengunjung == "dewasa":
            print("Paket C")
    case "kota":
        if waktu == "malam":
            print("Paket C")
        elif waktu == "malam" and pengunjung == "dewasa":
            print("Paket C")
    case _:
        print("Tidak ada paket yang cocok")