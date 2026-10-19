def daftar_kandidat(kandidat_set, nama):
    nama_kandidat = nama.capitalize()
    if nama_kandidat in kandidat_set:
        print(f"Kandidat '{nama_kandidat}' sudah terdaftar!")
    else:
        kandidat_set.add(nama_kandidat)  
        print(f"'{nama_kandidat}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_key = nama_pemilih.lower() 
    kandidat_pilihan = pilihan.capitalize()
    if pemilih_key in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return
    if kandidat_pilihan not in kandidat_set:
        print(f"Pilihan '{pilihan}' tidak ada dalam daftar kandidat!")
        return
    
    rekap_suara[pemilih_key] = kandidat_pilihan
    print(f"Suara '{nama_pemilih}' untuk '{kandidat_pilihan}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
    for pilihan in rekap_suara.values():
        perolehan[pilihan] = perolehan[pilihan] + 1
        
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n==========================================")
    print("HASIL PEMILIHAN KETUA KELAS")
    print("==========================================")
    
    total_suara = 0
    for kandidat in perolehan:
        suara = perolehan[kandidat]
        print(f"{kandidat}: {suara} suara")
        total_suara = total_suara + suara
        
    print(f"Total suara masuk: {total_suara}")
    
    if total_suara == 0:
        print("Belum ada suara yang masuk.")
        return
    suara_tertinggi = 0
    for suara in perolehan.values():
        if suara > suara_tertinggi:
            suara_tertinggi = suara
            
    pemenang = []
    for kandidat in perolehan:
        if perolehan[kandidat] == suara_tertinggi:
            pemenang.append(kandidat)
    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {suara_tertinggi} suara!")
    print("==========================================")

def main_voteclass():
    kandidat_set = set()
    rekap_suara = {}
    
    print("==========================================")
    print("SISTEM PEMILIHAN KETUA KELAS")
    print("==========================================")
    print("FASE PENDAFTARAN KANDIDAT")

    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidat_set) < 2: 
                print("Minimal harus ada 2 kandidat!")
                continue
            else:
                break
        daftar_kandidat(kandidat_set, nama)
        
    print(f"\nKandidat terdaftar: {kandidat_set}")
    print("\nFASE PEMUNGUTAN SUARA")

    while True:
        pemilih = input("\nNama pemilih (kosongkan untuk selesai): ").strip()
        if pemilih == "":
            break
            
        print(f"Kandidat yang tersedia: {kandidat_set}")
        pilihan = input("Pilih kandidat: ").strip()
        berikan_suara(rekap_suara, kandidat_set, pemilih, pilihan)
        
    perolehan = hitung_suara(rekap_suara, kandidat_set)
    tampilkan_hasil(perolehan)

    main_voteclass()