class Pemain:
    def __init__(self, nama, id_pemain, role, kill, assist, objective):
        self.nama= nama
        self.id_pemain= id_pemain
        self.role= role
        self.kill= kill
        self.assist= assist
        self.objective= objective
    def hitung_skor_akhir(self):
        skor = (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
        return skor
    def status_performa(self):
        if self.hitung_skor_akhir() >=60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"
    def tampilkan_data(self, no):
        skor = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no:<4} | {self.nama:<10} | {self.id_pemain:<13} | {self.role:<10} | {skor:<12.2f} | {status:<17} |")

print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
jumlah = int(input("masukkan jumlah pemain: "))
daftar_pemain = []

for i in range(jumlah):
    print(f"\nData Pemain ke{i + 1}")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    kill = float(input("Nilai kill: "))
    assist = float(input("Nilai assist: "))
    objective = float(input("Nilai objective: "))

    p = Pemain(nama, id_pemain, role, kill, assist, objective)
    daftar_pemain.append(p)

print("\n=== REKAPITULASI PERFORMA PEMAIN ===")
print("=" * 75)
print(f"| {'No':<4} | {'Nama':<10} | {'ID pemain':<13} | {'Role':<10} | {'Skor':<12} | {'Status':<17} |")
print("=" * 75)

for index, p in enumerate(daftar_pemain, start=1):
    p.tampilkan_data(index)
print("=" * 85)