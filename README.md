# Sistem Manajemen Toko

Sistem manajemen toko berbasis Python yang lengkap dengan antarmuka terpisah untuk operator dan pelanggan. Sistem ini menyediakan manajemen inventaris, fungsionalitas keranjang belanja, manajemen member, dan pelacakan penjualan.

## Fitur-Fitur

### Fitur Operator
- **Sistem Login Aman**: Otentikasi multi-pengguna dengan proteksi password
- **Manajemen Inventaris**: 
  - Lihat barang berdasarkan kategori, jenis produk, atau brand
  - Tambah kategori dan produk baru
  - Hapus item berdasarkan kategori, nama produk, atau ID
  - Update harga produk dan tingkat stok
- **Pelacakan Penjualan**: Pantau total pendapatan
- **Manajemen Member**: Lihat member pelanggan yang terdaftar

### Fitur Pelanggan
- **Jelajahi Produk**: Lihat produk dengan opsi filter
- **Keranjang Belanja**: Tambah/hapus item dengan manajemen kuantitas
- **Pendaftaran Member**: Daftar untuk mendapat diskon saat checkout
- **Sistem Checkout**: Selesaikan pembelian dengan aplikasi diskon otomatis

### Kemampuan Utama
- **Manajemen Stok Real-time**: Update stok otomatis selama transaksi
- **Penetapan Harga Dinamis**: Modifikasi harga yang mudah untuk operator
- **Sistem Diskon**: Generasi diskon acak untuk member baru (5-20%)
- **Persistensi Data**: Database dalam memori selama sesi
- **Validasi Input**: Penanganan error yang kuat dan validasi input pengguna

## Instalasi

### Prasyarat
- Python 3.6 atau lebih tinggi
- Package Python yang diperlukan:

```bash
pip install tabulate
```

### Setup
1. Clone atau download file `toko_main_gabung.py`
2. Pastikan Anda telah menginstall dependencies yang diperlukan
3. Jalankan aplikasi:

```bash
python toko_main_gabung.py
```

## Cara Penggunaan

### Memulai Aplikasi

Ketika Anda menjalankan program, Anda akan melihat menu utama:

```
=== MENU USER ===
1. operator
2. customer
3. Keluar
Pilihan:
```

### Akses Operator

#### Data Login
Sistem dilengkapi dengan akun operator yang sudah dikonfigurasi:

| ID Operator | Username | Password |
|-------------|----------|----------|
| 1101        | Axel     | abc123   |
| 1102        | Lukman   | bcd234   |
| 1103        | Almira   | cde345   |
| 1104        | Hashfi   | def456   |
| 1105        | Zulfan   | efg567   |
| 1106        | Krysna   | fgh678   |
| 1107        | Bayu     | ghi789   |

#### Opsi Menu Operator

1. **List Barang** - Lihat inventaris
   - Lihat semua item
   - Filter berdasarkan kategori (makanan, minuman, perlengkapan kerja)
   - Filter berdasarkan jenis produk
   - Filter berdasarkan brand

2. **Update Barang** - Kelola inventaris
   - Tambah kategori atau produk baru
   - Hapus kategori atau item individual
   - Update harga produk dan stok

3. **Cek Uang Masuk** - Lihat total pendapatan penjualan

4. **Lihat Daftar Member** - Lihat pelanggan yang terdaftar

### Akses Pelanggan

#### Opsi Menu Pelanggan

1. **Lihat Keranjang** - Lihat isi keranjang belanja
2. **Tambah Barang** - Jelajahi dan tambah produk ke keranjang
3. **Kurangi Barang** - Hapus item dari keranjang
4. **Checkout** - Selesaikan pembelian dengan opsi pendaftaran member
5. **Keluar** - Keluar dari mode pelanggan

## Data Sampel

### Produk yang Sudah Dimuat

Sistem dilengkapi dengan inventaris sampel:

**Kategori Makanan:**
- Susu: Nestle (Rp 10.000), Oatside (Rp 12.000)
- Roti: Nestle (Rp 14.000), ABC (Rp 13.000)

**Kategori Minuman:**
- Jus: ABC (Rp 20.000), Sunkist (Rp 22.000)

**Kategori Perlengkapan Kerja:**
- Buku Tulis: Kiki (Rp 35.000), Estudee (Rp 40.000)
- Pulpen: Pilot (Rp 8.000), Snowman (Rp 10.000)

### Member yang Sudah Terdaftar
- pimpi (ID: 1)
- fikri (ID: 2)  
- badu (ID: 3)

## Contoh Alur Kerja

### Menambah Produk Baru (Operator)
1. Login sebagai operator
2. Pilih "Update barang"
3. Pilih "Menambahkan" → "Barang"
4. Pilih kategori target
5. Masukkan nama produk, brand, harga, dan stok

### Melakukan Pembelian (Pelanggan)
1. Pilih "customer" dari menu utama
2. Pilih "Tambah Barang" untuk menjelajahi produk
3. Pilih item dan tambah ke keranjang menggunakan ID produk
4. Gunakan "Checkout" untuk menyelesaikan pembelian
5. Opsional: daftar sebagai member untuk mendapat diskon

### Melihat Laporan Penjualan (Operator)
1. Login sebagai operator
2. Pilih "Cek uang masuk"
3. Lihat total pendapatan dari semua transaksi

## Detail Teknis

### Struktur Data
- **Produk**: Struktur dictionary bersarang (kategori → produk → brand → detail)
- **Keranjang**: Struktur serupa dengan pelacakan kuantitas
- **Otentikasi**: Kredensial pengguna berbasis dictionary
- **Member**: Pemetaan nama-ke-ID sederhana

### Fungsi Utama
- `f_login()`: Menangani otentikasi operator
- `f_show_shop_items()`: Menampilkan inventaris dengan filter
- `f_add_to_cart()`: Mengelola operasi keranjang
- `f_id_adder()`: Menghasilkan ID produk unik

## Fitur Keamanan

- **Percobaan Login**: Dibatasi hingga 5 kali percobaan password
- **Validasi Input**: Pemeriksaan komprehensif untuk semua input pengguna
- **Konfirmasi**: Konfirmasi keamanan untuk operasi kritis

## Keterbatasan

- **Persistensi Data**: Data tidak disimpan antar sesi
- **Sesi Tunggal**: Hanya satu operator/pelanggan yang dapat menggunakan sistem pada satu waktu
- **Pool Diskon Tetap**: Persentase diskon sudah ditentukan sebelumnya

## Pengembangan Masa Depan

- Integrasi database untuk persistensi data
- Akses bersamaan multi-pengguna
- Fitur pelaporan lanjutan
- Dukungan gambar produk
- Integrasi pemindaian barcode
- Fungsionalitas cetak struk

## Cara Kontribusi

Untuk berkontribusi pada proyek ini:
1. Fork repository
2. Buat branch fitur
3. Lakukan perubahan Anda
4. Test secara menyeluruh
5. Kirim pull request

## Panduan Troubleshooting

### Masalah Umum

**Error: ModuleNotFoundError: No module named 'tabulate'**
- Solusi: Install package yang diperlukan dengan `pip install tabulate`

**Login Gagal**
- Pastikan ID operator berupa angka (1101-1107)
- Pastikan password sesuai dengan tabel di atas (case-sensitive)

**Input Tidak Valid**
- Sistem akan memberikan pesan error yang jelas
- Ikuti format input yang diminta (angka untuk ID, harga, stok)
