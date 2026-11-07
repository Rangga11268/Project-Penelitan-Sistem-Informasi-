import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1.docx'
doc = docx.Document(doc_path)

# Let's find index of 'BAB III'
bab3_idx = None
for i, p in enumerate(doc.paragraphs):
    if 'BAB III' in p.text and 'METODOLOGI' in p.text:
        bab3_idx = i
        break

print(f"BAB III found at index {bab3_idx}")

# Also find Tahap 3 (Persiapan Data) which starts Wahyu's section
tahap3_idx = None
for i, p in enumerate(doc.paragraphs):
    if i > bab3_idx and any(term in p.text for term in ['Tahap 3: Persiapan Data', '3. Tahap 3: Persiapan Data', '3.3.3']):
        tahap3_idx = i
        break

print(f"Tahap 3 found at index {tahap3_idx}")
