import re

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim)
def validasi_email(email):
    return re.fullmatch(r"[\w.]+@[\w.]+\.[\w.]+", email)
def validasi_telp(telp):
    return re.fullmatch(r"\d{10,13}", telp)
print("=== Validasi Data Mahasiswa ===")
nim = input("Masukkan NIM: ")
email = input("Masukkan Email: ")
telp = input("Masukkan No. Telp: ")

v_nim = validasi_nim(nim)
v_email = validasi_email(email)
v_telp = validasi_telp(telp)

print("\n--- Hasil Validasi ---")
print("NIM: ", "Valid" if v_nim else "Format NIM tidak valid!")
print("Email: ", "Valid" if v_email else "Format Email tidak valid")
print("No.Telp: ", "Valid" if v_telp else "Nomor telepon tidak valid")

if v_nim and v_email and v_telp:
    print("\nData mahasiswa berhasil diverifikasi!")