# UTS Object Oriented Programming 1
# Nama : Ryandra Gunawan
# NIM  : 25552011102
# Soal 2 - Sistem Pengelolaan Kendaraan


class Kendaraan:
    def __init__(self, merek, nomor_polisi, tarif_sewa):
        self.merek = merek
        self.nomor_polisi = nomor_polisi
        self.__tarif_sewa = tarif_sewa  # private

    def get_tarif_sewa(self):
        return self.__tarif_sewa

    def set_tarif_sewa(self, tarif):
        if tarif > 0:
            self.__tarif_sewa = tarif
        else:
            print("Tarif harus lebih dari 0, tarif tidak diubah")

    def hitung_biaya_sewa(self, hari):
        return self.__tarif_sewa * hari

    def tampilkan_info(self):
        print("Merek        :", self.merek)
        print("Nomor Polisi :", self.nomor_polisi)
        print("Tarif/hari   : Rp", self.__tarif_sewa)


class Mobil(Kendaraan):
    def __init__(self, merek, nomor_polisi, tarif_sewa, jumlah_kursi):
        super().__init__(merek, nomor_polisi, tarif_sewa)
        self.jumlah_kursi = jumlah_kursi

    # override method dari class Kendaraan
    def tampilkan_info(self):
        print("Merek        :", self.merek)
        print("Nomor Polisi :", self.nomor_polisi)
        print("Tarif/hari   : Rp", self.get_tarif_sewa())
        print("Jumlah Kursi :", self.jumlah_kursi)


# buat objek
motor = Kendaraan("Honda Beat", "B 1234 XYZ", 75000)
mobil = Mobil("Toyota Avanza", "D 5678 ABC", 350000, 7)

print("--- Data Kendaraan ---")
motor.tampilkan_info()
print()
print("--- Data Mobil ---")
mobil.tampilkan_info()

print()
print("--- Biaya Sewa ---")
print("Sewa", motor.merek, "3 hari = Rp", motor.hitung_biaya_sewa(3))
print("Sewa", mobil.merek, "3 hari = Rp", mobil.hitung_biaya_sewa(3))

print()
print("--- Ubah Tarif Mobil ---")
mobil.set_tarif_sewa(400000)
print("Tarif baru", mobil.merek, ": Rp", mobil.get_tarif_sewa())
print("Sewa", mobil.merek, "3 hari = Rp", mobil.hitung_biaya_sewa(3))
mobil.set_tarif_sewa(-50000)

print()
print("--- Cek Data Tiap Objek ---")
print("Tarif motor :", motor.get_tarif_sewa())
print("Tarif mobil :", mobil.get_tarif_sewa())
