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
```bash
git clone https://github.com/G181124/metatracera.git
cd metatracera
```

### 2. Buat Virtual Environment (Direkomendasikan)
```bash
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
```bash
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

---

## 📜 Lisensi

```
MIT License

Copyright (c) 2025 MetaTraceRA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

Gunakan MetaTraceRA dengan bijak.
