import re

print("=== Validasi Data Mahasiswa ===\n")

def validasi_data():
    nim = input("Masukkan NIM        : ")
    email = input("Masukkan Email      : ")
    no_telp = input("Masukkan No. Telp   : ")

    validasi_nim = re.match(r'^H071\d{6}$', nim)
    validasi_email = re.match(r'[\w\.-]+@[\w\.-]+\.\w{2,}$', email)
    validasi_nomor = re.match(r'^\d{10,13}$', no_telp)
    print("--- Hasil Validasi ---\n")

    print(f"NIM         : {'Valid' if validasi_nim else 'Tidak Valid'}")
    print(f"Email       : {'Valid' if validasi_email else 'Format email tidak valid!'}")
    print(f"No. Telepon : {'Valid' if validasi_nomor else 'Nomor telepon tidak valid!'}")

    if validasi_data == "Valid":
        print(f"Data mahasiswa berhasil diverifikasi!")
    else:
        print()    

validasi_data()