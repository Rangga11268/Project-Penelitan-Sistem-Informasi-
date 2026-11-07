import pypdf

reader = pypdf.PdfReader(r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok BAB 3 .pdf')
print('Total pages:', len(reader.pages))

with open('pdf_bab3_extracted.txt', 'w', encoding='utf-8') as out:
    for i, p in enumerate(reader.pages):
        text = p.extract_text()
        out.write(f"\n\n=== HALAMAN {i+1} ===\n\n")
        out.write(text)

print("Saved extracted text to pdf_bab3_extracted.txt")
