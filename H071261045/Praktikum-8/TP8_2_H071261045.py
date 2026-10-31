import re

print("=== Registrasi Username ===")
print("Ketik 'SELESAI' untuk mengakhiri.")

def validasi_username(username):
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,11}$'
    return re.match(pattern, username)

daftar_username = []

while True:
    username = input("Masukkan username: ")
    if username == "SELESAI".lower():
        break

    if validasi_username(username):
        print("Username tersedia.")
        daftar_username.append(username) 
    else:
        print("Username tidak valid!")

print("=== Rekapitulasi ===") 
print("\nUsername valid:")
for i, uname in enumerate(daftar_username):
    print(f"{i+1}. {uname}")
print(f"Jumlah username valid: {len(daftar_username)}")

