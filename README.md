# MetaTraceRA

MetaTraceRA adalah alat forensik metadata berbasis CLI yang cepat, ringan, dan dirancang khusus untuk sistem seperti Kali Linux. Tools ini bekerja **real-time** tanpa database lokal dan mendukung berbagai tipe file seperti gambar, dokumen, serta memiliki fitur penghapusan metadata.

---

## 🔧 Fitur Utama

- Analisis metadata gambar (EXIF)
- Metadata dokumen PDF dan DOCX
- Hashing file (MD5, SHA1, SHA256)
- Informasi teknis file (ukuran, tipe MIME, timestamp)
- Deteksi lokasi dari metadata GPS (EXIF)
- Pembersihan metadata gambar
- Dukungan ekspor hasil
- Mode analisis gabungan `--analyze`

---

## ⚙️ Instalasi

### 1. Clone Repository
```
git clone https://github.com/G181124/metatracera.git
cd metatracera
```

### 2. Buat Virtual Environment (Direkomendasikan)
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

---

## 🚀 Cara Penggunaan

### 📸 Analisis metadata gambar (EXIF)
```
python metatracera.py --file foto.jpg
```

### 📝 Metadata dokumen PDF atau DOCX
```
python metatracera.py --doc file.pdf
python metatracera.py --doc file.docx
```

### 🔐 Hashing file
```
python metatracera.py --hash file.zip
```

### 📂 Informasi dasar file
```
python metatracera.py --fileinfo file.png
```

### 🌍 Lokasi dari metadata GPS (jika ada)
```
python metatracera.py --geolocate gambar.jpg
```

### ✂️ Hapus metadata dari gambar
```
python metatracera.py --clean gambar.jpg
```

### 🧠 Analisis metadata + lokasi sekaligus
```
python metatracera.py --analyze gambar.jpg
```

### 📤 Ekspor hasil ke folder `output/`
Tambahkan `--export` ke perintah apa pun:
```
python metatracera.py --file gambar.jpg --export
```

---

## 📁 Output
Semua hasil ekspor akan disimpan otomatis ke folder `output/` dengan nama unik berdasarkan timestamp dan nama file.

---

## 🧪 Catatan
- `--geolocate` hanya bekerja jika metadata GPS tersedia
- `--clean` hanya untuk file gambar (format JPEG)
- Tool ini tidak menyimpan data apa pun secara permanen

Gunakan MetaTraceRA dengan bijak.
