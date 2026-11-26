# UTS Object Oriented Programming 1

- Nama : Ryandra Gunawan
- NIM : 25552011102

Soal yang dikerjakan: **Soal 2 - Sistem Pengelolaan Kendaraan** (angka terakhir NIM = 2)

## Penjelasan Singkat

Program ini dibuat untuk mengelola kendaraan yang disewakan oleh perusahaan rental. Ada dua class:

- `Kendaraan` (parent class), punya atribut merek, nomor polisi, dan tarif sewa. Tarif sewa dibuat private (`__tarif_sewa`), jadi untuk membaca dan mengubahnya pakai method `get_tarif_sewa()` dan `set_tarif_sewa()`.
- `Mobil` (child class), turunan dari `Kendaraan` dengan tambahan atribut jumlah kursi. Constructor-nya memanggil `super().__init__()`.

Method `hitung_biaya_sewa(hari)` dipakai untuk menghitung biaya sewa (tarif per hari x jumlah hari). Method `tampilkan_info()` di-override di class `Mobil` supaya bisa menampilkan jumlah kursi juga.

Objek yang dibuat ada dua, yaitu `motor` (objek dari class Kendaraan) dan `mobil` (objek dari class Mobil).

## Cara Menjalankan

```
python sistem_kendaraan.py
```

## Hasil Program

```
--- Data Kendaraan ---
Merek        : Honda Beat
Nomor Polisi : B 1234 XYZ
Tarif/hari   : Rp 75000

--- Data Mobil ---
Merek        : Toyota Avanza
Nomor Polisi : D 5678 ABC
Tarif/hari   : Rp 350000
Jumlah Kursi : 7

--- Biaya Sewa ---
Sewa Honda Beat 3 hari = Rp 225000
Sewa Toyota Avanza 3 hari = Rp 1050000

--- Ubah Tarif Mobil ---
Tarif baru Toyota Avanza : Rp 400000
Sewa Toyota Avanza 3 hari = Rp 1200000
Tarif harus lebih dari 0, tarif tidak diubah

--- Cek Data Tiap Objek ---
Tarif motor : 75000
Tarif mobil : 400000
```

Dari hasil di atas bisa dilihat kalau tarif mobil diubah jadi 400000, tarif motor tetap 75000. Jadi setiap objek punya datanya masing-masing. Waktu tarif diisi -50000, tarifnya tidak berubah karena ada pengecekan di method `set_tarif_sewa()`.
