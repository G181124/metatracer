
import argparse
import sys
import os
import datetime
from nucleus_ops import (
    x1_imgmeta,
    x2_docmeta,
    x3_hashgen,
    x4_fileinfo,
    x5_geolocate,
    x6_cleanmeta
)

def get_export_path(module_name, original_path):
    basename = os.path.basename(original_path)
    name, _ = os.path.splitext(basename)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"output/{module_name}_{name}_{timestamp}.txt"
    return filename

def main():
    parser = argparse.ArgumentParser(
        description='MetaTraceRA - Metadata Analyzer CLI Tool'
    )

    parser.add_argument('--file', help='Analisis metadata dari file gambar')
    parser.add_argument('--doc', help='Analisis metadata dari dokumen Word/PDF')
    parser.add_argument('--hash', help='Hitung hash dari file (MD5, SHA1, SHA256)')
    parser.add_argument('--fileinfo', help='Info dasar dari file')
    parser.add_argument('--geolocate', help='Deteksi lokasi dari metadata foto')
    parser.add_argument('--clean', help='Hapus metadata dari file gambar')
    parser.add_argument('--export', action='store_true', help='Simpan hasil ke file di folder output')

    args = parser.parse_args()

    os.makedirs("output", exist_ok=True)

    if args.file:
        out = get_export_path("imgmeta", args.file) if args.export else None
        x1_imgmeta.run(args.file, out)
    elif args.doc:
        out = get_export_path("docmeta", args.doc) if args.export else None
        x2_docmeta.run(args.doc, out)
    elif args.hash:
        out = get_export_path("hash", args.hash) if args.export else None
        x3_hashgen.run(args.hash, out)
    elif args.fileinfo:
        out = get_export_path("fileinfo", args.fileinfo) if args.export else None
        x4_fileinfo.run(args.fileinfo, out)
    elif args.geolocate:
        out = get_export_path("geolocate", args.geolocate) if args.export else None
        x5_geolocate.run(args.geolocate, out)
    elif args.clean:
        out = get_export_path("clean", args.clean) if args.export else None
        x6_cleanmeta.run(args.clean, out)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
