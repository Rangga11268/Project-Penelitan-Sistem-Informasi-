import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re
import os

foreign_terms = [
    r'\bdata preparation\b', r'\bFP-Growth\b', r'\bdata cleaning\b', r'\bmissing values\b',
    r'\bstring standardization\b', r'\bnoise\b', r'\bdata anonymization\b', r'\bchassis number\b',
    r'\bmulti-attribute predicate basket transformation\b', r'\bspurious rules\b',
    r'\bone-hot encoding\b', r'\bbinary incidence matrix\b', r'\binput\b',
    r'\bmarket basket analysis\b', r'\bempty itemsets\b', r'\bmulti-attribute predicate basket\b',
    r'\bAerox Cyber City\b', r'\bCyan\b', r'\bBAF\b', r'\bKota Bekasi\b'
]
combined_regex = re.compile(r'(' + '|'.join(foreign_terms) + r')', re.IGNORECASE)

def add_formatted_text(p, text, font_name='Times New Roman', font_size_pt=12, bold_prefix=None):
    if bold_prefix:
        prefix_run = p.add_run(bold_prefix)
        prefix_run.font.name = font_name
        prefix_run.font.size = Pt(font_size_pt)
        prefix_run.font.bold = True
        
    parts = combined_regex.split(text)
    for part in parts:
        if not part: continue
        r = p.add_run(part)
        r.font.name = font_name
        r.font.size = Pt(font_size_pt)
        if combined_regex.fullmatch(part):
            r.font.italic = True

wahyu_proposal_text = (
    "Tahap persiapan data (data preparation) merupakan fase rekayasa data mentah menjadi bentuk representasi tabular "
    "terstruktur yang siap diproses oleh algoritma komputasi FP-Growth. Fase ini diawali dengan prosedur pembersihan dan "
    "standardisasi data (data cleaning) untuk menangani nilai kosong (missing values), menyeragamkan format penulisan teks "
    "(string standardization), memverifikasi keunikan nomor faktur, dan menyingkirkan derau (noise). Selanjutnya, dilakukan "
    "anonimisasi data privasi konsumen (data anonymization) dengan mengeliminasi penuh atribut identitas personal langsung "
    "seperti Nomor Induk Kependudukan (NIK), nama pembeli, nomor telepon, dan nomor rangka (chassis number) demi menjaga etika penelitian. "
    "Langkah berikutnya adalah transformasi keranjang predikat multiatribut (multi-attribute predicate basket transformation) "
    "untuk mengonversi data faktur penjualan motor tunggal menjadi pasangan predikat unik berformat Atribut=Nilai "
    "(seperti Model=Aerox Cyber City, Warna=Cyan, Leasing=BAF, Tenor=35 Bulan, Wilayah=Kota Bekasi), sehingga algoritma FP-Growth "
    "dapat menemukan keterkaitan lintas-dimensi tanpa menghasilkan kaidah semu (spurious rules). Rangkaian persiapan data diakhiri dengan "
    "pengodean matriks biner (one-hot encoding) yang mengubah seluruh pasangan predikat kategorikal ke dalam representasi matriks biner "
    "kuantitatif (binary incidence matrix) berdimensi 3.113 baris sebagai berkas input terstandarisasi yang siap diolah pada tahap pemodelan komputasi. "
    "Cuplikan sampel transformasi data transaksi mentah Y-DMS menjadi keranjang predikat multiatribut disajikan pada Tabel 3.2."
)

wahyu_journal_text = (
    "Tahap persiapan data (data preparation) merupakan fase rekayasa data mentah menjadi bentuk representasi tabular "
    "terstruktur yang siap diproses oleh algoritma komputasi FP-Growth. Fase ini diawali dengan prosedur pembersihan dan "
    "standardisasi data (data cleaning) untuk menangani nilai kosong (missing values), menyeragamkan format string "
    "(string standardization), memverifikasi keunikan nomor faktur, serta menyingkirkan derau (noise). Selanjutnya, dilakukan "
    "anonimisasi data privasi konsumen (data anonymization) dengan mengeliminasi penuh atribut identitas personal seperti NIK, "
    "nama pembeli, nomor telepon, dan nomor rangka (chassis number). Mengingat transaksi riil dealer sepeda motor hanya mencatat satu unit motor per lembar faktur, "
    "analisis keranjang belanja (market basket analysis) konvensional tidak dapat diterapkan langsung karena akan memicu kombinasi kosong (empty itemsets). "
    "Oleh karena itu, data ditransformasikan ke dalam representasi keranjang predikat multiatribut (multi-attribute predicate basket transformation) "
    "berformat pasangan Atribut=Nilai (seperti Model=Aerox Cyber City, Warna=Cyan, Leasing=BAF, Tenor=35 Bulan, Wilayah=Kota Bekasi), sehingga "
    "algoritma FP-Growth dapat menemukan keterkaitan lintas-dimensi tanpa menghasilkan kaidah semu (spurious rules). Rangkaian persiapan data diakhiri "
    "dengan pengodean matriks biner (one-hot encoding) ke dalam representasi matriks biner kuantitatif (binary incidence matrix) berdimensi 3.113 baris "
    "sebagai berkas input terstandarisasi. Cuplikan sampel transformasi data transaksi mentah Y-DMS disajikan pada Tabel II."
)

def fix_and_update(doc_path):
    print(f"Fixing and updating: {doc_path}")
    doc = docx.Document(doc_path)
    
    # 1. Restore paragraph 103 in Bab 2
    if len(doc.paragraphs) > 103 and "Tahap 3 (CRISP-DM): Persiapan Data" in doc.paragraphs[103].text:
        doc.paragraphs[103].text = "c. Tahap Persiapan Data (Data Preparation)"
        doc.paragraphs[103].runs[0].font.name = "Times New Roman"
        doc.paragraphs[103].runs[0].font.size = Pt(12)
        doc.paragraphs[103].runs[0].font.bold = True
        print("Restored Bab 2 paragraph 103 header.")
        
    # 2. Find target in Bab 3 (i > 180)
    for i in range(180, len(doc.paragraphs)):
        p = doc.paragraphs[i]
        if "persiapan data (data preparation)" in p.text.lower() or "tahap persiapan data" in p.text.lower():
            p.text = ""
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(6)
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            add_formatted_text(p, wahyu_proposal_text, font_name='Times New Roman', font_size_pt=12, bold_prefix="Tahap 3 (CRISP-DM): Persiapan Data (Data Preparation): ")
            print(f"Updated Bab 3 paragraph {i} with bold prefix and Wahyu's text.")
            break
            
    doc.save(doc_path)

p1 = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1.docx'
p3 = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1 - Final_Revisi.docx'

fix_and_update(p1)
if os.path.exists(p3):
    fix_and_update(p3)
print("Fix completed!")
