# Demographic Data Scraper

Skrip ini digunakan untuk mengunduh data demografi Indonesia dari Wikipedia dan menyimpannya dalam format CSV.

## Deskripsi

Skrip ini mengambil tabel demografi dari halaman Wikipedia mengenai Demografi Indonesia dan menyimpannya sebagai file CSV. Tabel yang diambil berisi informasi terkait dengan populasi dan karakteristik demografis lainnya.

## Instalasi

Pastikan Anda memiliki Python terinstal di sistem Anda. Skrip ini memerlukan pustaka `pandas`. Anda dapat menginstalnya dengan menggunakan pip:

```bash
pip install pandas
```

## Penggunaan
1. Clone repositori ini atau salin skrip ke dalam file Python (misalnya `demographics_scraper.py`).
2. Jalankan skrip dengan perintah berikut:
```bash
python demographics_scraper.py
```
### Hasil Eksekusi
Setelah skrip dijalankan, file `capital.csv` akan dibuat di direktori kerja Anda. File ini berisi data demografi yang diambil dari Wikipedia.

### Catatan
* Pastikan koneksi internet Anda aktif karena skrip ini membutuhkan akses ke URL halaman Wikipedia.
* Tabel yang diambil adalah yang kedua pada halaman tersebut. Jika halaman diperbarui atau strukturnya berubah, Anda mungkin perlu memodifikasi indeks tabel.
