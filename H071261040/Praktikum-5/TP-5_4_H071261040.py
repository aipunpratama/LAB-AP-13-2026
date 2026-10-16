def deteksi_anomali_email(email):
    masalah = []

    if email.count("@") != 1:
        return ["Harus memiliki tepat satu karakter @."]

    local, domain = email.split("@")

    if local == "" or domain == "":
        masalah.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        masalah.append("Email tidak boleh mengandung spasi.")

    if local.startswith(".") or local.endswith(".") or ".." in local:
        masalah.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan.")

    if "." not in domain:
        masalah.append("Bagian domain wajib memiliki minimal satu titik.")
    elif ".." in domain or domain.endswith("."):
        masalah.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    akhir = email.lower()
    if not (akhir.endswith(".com") or akhir.endswith(".id") or akhir.endswith(".ac.id")):
        masalah.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return masalah

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return "(tidak ada email valid)"
    border = karakter_border[0] if karakter_border else "="
    terpanjang = 0
    for e in daftar_email_valid:
        if len(e) > terpanjang:
            terpanjang = len(e)
    lebar = terpanjang + 2  
    garis = "+" + border * lebar + "+"
    baris = [garis]
    for e in daftar_email_valid:
        baris.append("| " + e + " " * (terpanjang - len(e)) + " |")
    baris.append(garis)
    return "\n".join(baris)

print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print()
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

valid = []
while True:
        email = input("Masukkan email: ")
        if email.strip().lower() == "tutup":
            break

        masalah = deteksi_anomali_email(email)
        if email in valid:
            masalah.append("Email sudah terdaftar (Duplikat).")

        if masalah:
            print(">> Email DITOLAK karena:")
            for m in masalah:
                print("   -", m)
        else:
            print(">> Email VALID!")
            valid.append(email)

print()
print("--- HASIL EMAIL VALID ---")
print(cetak_daftar(valid, border))