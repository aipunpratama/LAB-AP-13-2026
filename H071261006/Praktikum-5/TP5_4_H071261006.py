# --- SOAL 4: VALIDASI EMAIL ---

# 1. Fungsi Cek Aturan Anomali Email
def deteksi_anomali_email(email, daftar_terdaftar):
    anomali = []
    if email.count("@") != 1:
        anomali.append("Harus memiliki tepat satu karakter @.")
        return anomali  
    local, domain = email.split("@")
    
    if len(local) == 0 or len(domain) == 0:
        anomali.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    if " " in email:
        anomali.append("Tidak boleh mengandung spasi di posisi manapun.")
    if local.startswith(".") or local.endswith(".") or ".." in local:
        anomali.append("Bagian local tidak boleh diawali atau diakhiri titik (.), serta tidak boleh mengandung titik berurutan (..).")
    if "." not in domain:
        anomali.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        anomali.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
    if email in daftar_terdaftar:
        anomali.append("Email sudah terdaftar (Duplikat).")
    domain_resmi = (".com", ".id", ".ac.id")
    if not any(domain.endswith(ext) for ext in domain_resmi):
        anomali.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
    return anomali


# 2. Fungsi Cetak Bingkai Teks
def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return
    
    panjang_maks = max(len(email) for email in daftar_email_valid)
    lebar = panjang_maks + 4  
    garis_border = karakter_border * lebar
    
    print("\n+" + "-" * (lebar - 2) + "+")
    print("HASIL EMAIL VALID")
    print("+" + "-" * (lebar - 2) + "+")
    for email in daftar_email_valid:
        spasi = (lebar - len(email) - 3) * " "
        print(f"| {email}{spasi}|")
    print(garis_border)


# --- PROGRAM UTAMA SOAL 4 ---
print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.\n")

daftar_valid = []

while True:
    email_in = input("Masukkan email: ").strip()
    
    if email_in.lower() == "tutup":
        break
        
    errors = deteksi_anomali_email(email_in, daftar_valid)
    
    if len(errors) == 0:
        daftar_valid.append(email_in)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")
        for err in errors:
            print(f"   {err}")

cetak_daftar(daftar_valid, border)