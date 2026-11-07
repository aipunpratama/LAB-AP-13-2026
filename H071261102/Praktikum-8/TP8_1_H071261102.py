import re

cek_nim = r'^H071\d{6}$'
cek_email = r'^\w+@\w+(\.\w+)*\.[a-zA-Z]{2,3}$'
cek_telpon = r'^\d{10,13}$'

def validasi_nim(nim, cek_nim):
    return re.fullmatch(cek_nim, nim) is not None

def validasi_email(email, cek_email):
    return re.fullmatch(cek_email, email) is not None

def validasi_telpon(telpon, cek_telpon):
    return re.fullmatch(cek_telpon, telpon) is not None

NIM = input("Masukkan NIM".ljust(20) + ": ")
jalan = validasi_nim(NIM, cek_nim)
akhir_nim = "Valid" if jalan else "Format NIM Tidak Valid!"

email = input("Masukkan Email".ljust(20) + ": ")
jalan2 = validasi_email(email, cek_email)
akhir_email = "Valid" if jalan2 else "Format Email Tidak Valid!"

telpon = input("Masukkan No. Telp".ljust(20) + ": ")
jalan3 = validasi_telpon(telpon, cek_telpon)
akhir_telpon = "Valid" if jalan3 else "Nomor Telepon Tidak Valid!"

print("\n--- Hasil Validasi ---")
print("NIM".ljust(13) + ": " + akhir_nim)
print("Email".ljust(13) + ": " + akhir_email)
print("No.Telepon".ljust(13) + ": " + akhir_telpon)

if jalan and jalan2 and jalan3:
    print("\nData mahasiswa berhasil diverifikasi!")
else:
    print("\nData mahasiswa gagal untuk diverifikasi")