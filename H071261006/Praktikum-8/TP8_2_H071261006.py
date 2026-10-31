import re

def validasi_username(uname):
    return re.fullmatch(r"[a-zA-Z]\w{4,11}", uname)
print("--- Registrasi Username ---")
print("Ketik 'SELESAI' untuk mengakhiri")

list_valid = []
while True:
    uname = input("Masukkan username: ")
    if uname.upper() == "SELESAI":
        break
    if validasi_username(uname):
        print("Username tersedia. ")
        list_valid.append(uname)
    else:
        print("Username tidak valid!")

print("\n=== Rekapitulasi ===")
print("Username valid: ")
for i, u in enumerate(list_valid, 1):
    print(f"{i}. {u}")
print()
print("Jumlah username valid:", len(list_valid))