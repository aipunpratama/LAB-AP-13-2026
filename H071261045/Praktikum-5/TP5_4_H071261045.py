
def deteksi_anomali_email(email):
    error = []

    # Aturan 1: Harus memiliki tepat satu @
    if email.count("@") != 1:
        error.append("Email harus memiliki tepat satu karakter @")
        return error

    local, domain = email.split("@")

    if local == "" or domain == "":
        error.append("Bagian local dan domain tidak boleh kosong")

    if " " in email:
        error.append("Email tidak boleh mengandung spasi")

    if local.startswith(".") or local.endswith("."):
        error.append("Bagian local tidak boleh diawali atau diakhiri titik")

    if ".." in local:
        error.append("Bagian local tidak boleh mengandung titik berurutan")

    if "." not in domain:
        error.append("Domain harus memiliki minimal satu titik")

    if ".." in domain:
        error.append("Domain tidak boleh mengandung titik berurutan")

    if domain.endswith("."):
        error.append("Domain tidak boleh diakhiri titik")

    domain_resmi = (".com", ".id", ".ac.id")

    if not domain.lower().endswith(domain_resmi):
        error.append("Email harus berakhiran .com, .id, atau .ac.id")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        return "Belum ada email valid."

    email_terpanjang = max(len(email) for email in daftar_email_valid)
    lebar = email_terpanjang + 4
    border = karakter_border * lebar

    hasil = border + "\n"

    for email in daftar_email_valid:
        isi = "| " + email
        isi = isi + " " * (lebar - len(isi) - 1) + "|"
        hasil = hasil + isi + "\n"

    hasil = hasil + border
    return hasil


# Program utama
daftar_email_valid = []

while True:
    email = input("Masukkan email (ketik 'tutup' untuk selesai): ").strip()

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    # Memeriksa email duplikat
    duplikat = False

    for email_tersimpan in daftar_email_valid:
        if email.lower() == email_tersimpan.lower():
            duplikat = True
            break

    if duplikat:
        error.append("Email tidak boleh duplikat")

    if len(error) == 0:
        daftar_email_valid.append(email)
        print("Email valid!")
        print("Gulungan perkamen:")
        print(cetak_daftar(daftar_email_valid, "="))
    else:
        print("Email tidak valid. Rincian kesalahan:")

        for pesan in error:
            print("-", pesan)

print("Program selesai.")
print("Daftar seluruh email valid:")
print(cetak_daftar(daftar_email_valid, "="))
