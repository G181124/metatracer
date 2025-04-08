# MetaTraceRA

MetaTraceRA adalah alat CLI ringan untuk analisis metadata file secara lokal dan real-time.

## Fitur
- Metadata gambar (EXIF)
- Metadata PDF & DOCX
- Hashing (MD5, SHA1, SHA256)
- Info teknis file
- Deteksi lokasi GPS
- Pembersihan metadata gambar

## Instalasi
```bash
git clone https://github.com/G181124/metatracer.git
cd metatracer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Penggunaan
```bash
python metatracera.py --file foto.jpg --export
```

Lihat semua opsi dengan:
```bash
python metatracera.py --help
```
