## ✅ **README.md untuk MetaTraceRA**

```markdown
# MetaTraceRA

MetaTraceRA adalah alat CLI ringan untuk analisis metadata file secara lokal dan real-time.  
Dirancang untuk keperluan forensik digital, investigasi ringan, serta perlindungan privasi pengguna.

---

## 🚀 Fitur Utama

- Ekstraksi metadata dari gambar (EXIF)
- Metadata dari dokumen Word (.docx) dan PDF
- Hashing file (MD5, SHA1, SHA256)
- Informasi teknis file (ukuran, MIME, timestamp)
- Deteksi lokasi dari metadata GPS
- Penghapusan metadata dari gambar
- Ekspor hasil ke file `.txt` otomatis (opsional)

---

## 📥 Instalasi

```bash
# Clone repository
git clone https://github.com/username/metatracera.git
cd metatracera

# Install dependensi
pip install -r requirements.txt
```

> Disarankan menggunakan Python 3.8 atau lebih tinggi.  
> Ideal digunakan di Kali Linux atau sistem Linux lain berbasis CLI.

---

## 🧪 Cara Penggunaan

```bash
# Metadata gambar
python metatracera.py --file foto.jpg

# Metadata dokumen
python metatracera.py --doc laporan.docx
python metatracera.py --doc laporan.pdf

# Hash file
python metatracera.py --hash target.zip

# Informasi file
python metatracera.py --fileinfo secret.docx

# Deteksi lokasi dari EXIF
python metatracera.py --geolocate selfie.jpg

# Hapus metadata dari gambar
python metatracera.py --clean selfie.jpg
```

Tambahkan `--export` untuk menyimpan hasil analisis ke folder `output/`, misalnya:

```bash
python metatracera.py --file selfie.jpg --export
```

---

## 📂 Output

- Semua file yang diekspor disimpan di folder `output/`
- Nama file disesuaikan secara otomatis dengan timestamp agar tidak tertimpa

Contoh:
```
output/imgmeta_selfie_20250408_123455.txt
output/cleaned_selfie.jpg
```

---

## 💡 Catatan

- Tidak menyimpan data sensitif
- Tidak menggunakan database lokal
- Semua proses berjalan di sistem lokal dan real-time

---

## 🛡️ Cocok Untuk

- Investigator OSINT
- Forensik digital ringan
- Jurnalis dan aktivis
- Masyarakat umum yang ingin melindungi metadata pribadinya

---

## 📧 Kontak & Kontribusi

Silakan fork, pull request, atau laporkan issue melalui halaman GitHub project.

---

© 2025 MetaTraceRA — Dibuat dengan semangat perlindungan digital 👣
```
