print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist,nilai_objetive):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objetive = nilai_objetive

    def hitung_skor_akhir(self):
        skor_akhir = (self.nilai_kill * 0.3) + (self.nilai_assist * 0.3) + (self.nilai_objetive * 0.4)
        return skor_akhir

    def status_performa(self):
        skor_akhir = self.hitung_skor_akhir()
        if 60 <= skor_akhir < 100:
            return "Unggul"
        elif skor_akhir <= 60:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        skor_akhir = self.hitung_skor_akhir()
        status = self.status_performa()
        print(f"| {no:<3} | {self.nama:<10} | {self.id_pemain:<11} | {self.role:<10} | {skor_akhir:<10.2f} | {status:<15}|")

while True:
        try:
            jumlah_pemain = int(input("Masukkan jumlah pemain: "))
        except ValueError:
            print("Input harus berupa angka.")
            jumlah_pemain = 0

        daftar_pemain = []
        for i in range(jumlah_pemain):
            print(f"\n-- Data Pemain ke-{i+1} --")
            nama = input("Nama: ")
            id_pemain = input("ID Pemain: ")
            role = input("Role: ")
        
            try:
                nilai_kill = float(input("Nilai Kill: "))
                nilai_assist = float(input("Nilai Assist: "))
                nilai_objetive = float(input("Nilai Objective: "))
                
            except ValueError:
                print("Nilai harus berupa angka. Silakan ulangi input untuk pemain ini")

            pemain = Pemain(nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objetive)
            daftar_pemain.append(pemain)

        if len(daftar_pemain) > 0:
            print("=== REKAPITULASI PERFORMA PEMAIN ===")
            print("\n" + "="*77)
            print(f"| {'No':<3} | {'Nama':<10} | {'ID Pemain':<11} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<15}|")
            print("="*77)
        

            for i, pemain in enumerate(daftar_pemain, start=1):
                pemain.tampilkan_data(i)

            print("="*77)