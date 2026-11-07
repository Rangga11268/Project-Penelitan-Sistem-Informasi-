import docx
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import re
import os

foreign_terms = [
    r'\bapplied research\b', r'\bcomputational data-driven research\b', r'\bdata mining\b',
    r'\bCross-Industry Standard Process for Data Mining\b', r'\bBusiness Understanding\b',
    r'\bData Understanding\b', r'\bData Preparation\b', r'\bModeling\b', r'\bEvaluation\b',
    r'\bDeployment\b', r'\bFP-Growth\b', r'\bFrequent Pattern Growth\b', r'\bFP-Tree\b',
    r'\bFrequent Pattern Tree\b', r'\bConditional Pattern Base\b', r'\bHeader Table\b',
    r'\bNode-Link\b', r'\bnode-links\b', r'\btwo-pass database scan\b', r'\bcandidate generation-free\b',
    r'\bdivide-and-conquer\b', r'\bfrequent itemsets\b', r'\bin-memory structure\b',
    r'\bYamaha Dealer Management System\b', r'\bbaseline behavior\b', r'\bpurposive sampling\b',
    r'\bclosed and final\b', r'\bcanceled\b', r'\brejected\b', r'\breturn\b', r'\bmissing values\b',
    r'\bMaxi Series\b', r'\bClassy\b', r'\bMatic 125\b', r'\bSport\b', r'\bMoped\b',
    r'\bMatte Black\b', r'\bCyan\b', r'\bMetallic Red\b', r'\bPrestige Silver\b', r'\bWhite\b',
    r'\bCash\b', r'\bNon-Kredit\b', r'\bmarket basket analysis\b', r'\bempty itemsets\b',
    r'\bdata cleaning\b', r'\bstring standardization\b', r'\bnoise\b', r'\bdata anonymization\b',
    r'\bchassis number\b', r'\bmulti-attribute predicate basket\b', r'\bspurious rules\b',
    r'\bone-hot encoding\b', r'\bbinary incidence matrix\b', r'\bTri-Metric Validation\b',
    r'\bSupport\b', r'\bConfidence\b', r'\bLift Ratio\b', r'\bSmart Sales Script\b',
    r'\bRegional Inventory Allocation\b', r'\bJoint Multifinance Bundling Program\b', r'\bleasing\b'
]
combined_regex = re.compile(r'(' + '|'.join(foreign_terms) + r')', re.IGNORECASE)

def add_formatted_text(p, text, font_name='Times New Roman', font_size_pt=10, bold_prefix=None):
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = font_name
        r_pre.font.size = Pt(font_size_pt)
        r_pre.font.bold = True
        
    parts = combined_regex.split(text)
    for part in parts:
        if not part: continue
        r = p.add_run(part)
        r.font.name = font_name
        r.font.size = Pt(font_size_pt)
        if combined_regex.fullmatch(part):
            r.font.italic = True

def create_academic_table(doc, headers, data, col_widths, font_size_pt=8.5, font_name='Times New Roman'):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:insideH w:val="none"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)
    
    def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>\n'
            f'  <w:top w:w="{top}" w:type="dxa"/>\n'
            f'  <w:bottom w:w="{bottom}" w:type="dxa"/>\n'
            f'  <w:left w:w="{left}" w:type="dxa"/>\n'
            f'  <w:right w:w="{right}" w:type="dxa"/>\n'
            f'</w:tcMar>'
        )
        tcPr.append(tcMar)
        
    header_row = table.rows[0]
    trPr = header_row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    
    for i, title in enumerate(headers):
        cell = header_row.cells[i]
        cell.width = Inches(col_widths[i])
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        tcPr = cell._tc.get_or_add_tcPr()
        tcPr.append(parse_xml(f'<w:tcBorders {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/></w:tcBorders>'))
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(title)
        r.font.name = font_name
        r.font.size = Pt(font_size_pt)
        r.font.bold = True

    for row_idx, row_data in enumerate(data):
        row = table.rows[row_idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            cell = row.cells[col_idx]
            cell.width = Inches(col_widths[col_idx])
            set_cell_margins(cell, top=60, bottom=60, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            if len(headers) == 4 and col_idx in [1, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif len(headers) == 3 and col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_text(p, cell_value, font_name=font_name, font_size_pt=font_size_pt)

    return table

headers1 = ['Atribut', 'Tipe Data', 'Jumlah Varian', 'Keterangan dan Contoh Nilai']
data1 = [
    ['Model Motor', 'Kategorikal', '44 Model', 'Lini produk Yamaha pada segmen Maxi Series, Classy, Matic 125, Sport, dan Moped (contoh: Aerox 155 Cyber City, NMAX Connected, Grand Filano, Fazzio Neo, Gear 125).'],
    ['Varian Warna', 'Kategorikal', '22 Warna', 'Pilihan estetika warna eksterior dari pabrikan (contoh: Matte Black, Metallic Red, Prestige Silver, Dull Blue, White, Cyan).'],
    ['Lembaga Pembiayaan', 'Kategorikal', '4 Kategori', 'Skema pembelian tunai (Cash) dan fasilitas pembiayaan kredit melalui mitra resmi (BAF, Adira Finance, OTO Multiartha).'],
    ['Tenor Angsuran', 'Diskret', '5 Opsi', 'Jangka waktu cicilan yang disepakati konsumen (11 Bulan, 23 Bulan, 30 Bulan, 35 Bulan, Non-Kredit).'],
    ['Wilayah Domisili', 'Kategorikal', '10 Area', 'Wilayah tempat tinggal konsumen di kawasan aglomerasi Jabodetabek (Kota Bekasi, Kab. Bekasi, Jakarta Timur, Jakarta Selatan, Depok, Bogor, Tangerang, dll.).']
]
col_widths1 = [1.3, 0.9, 0.9, 3.4]

headers2 = ['No. Faktur', 'Data Mentah Transaksi Y-DMS', 'Representasi Keranjang Predikat Multiatribut']
data2 = [
    ['TRX-0001', 'Aerox Cyber City, Cyan, BAF, 35 Bulan, Kota Bekasi', '{Model=Aerox Cyber City, Warna=Cyan, Leasing=BAF, Tenor=35 Bln, Wilayah=Kota Bekasi}'],
    ['TRX-0002', 'NMAX Connected, Matte Black, Adira, 35 Bulan, Jakarta Timur', '{Model=NMAX Connected, Warna=Matte Black, Leasing=Adira, Tenor=35 Bln, Wilayah=Jakarta Timur}'],
    ['TRX-0003', 'Grand Filano Lux, White, Cash, Non-Kredit, Jakarta Selatan', '{Model=Grand Filano Lux, Warna=White, Leasing=Cash, Tenor=Non-Kredit, Wilayah=Jakarta Selatan}'],
    ['TRX-0004', 'Fazzio Neo, Dull Blue, OTO Multiartha, 23 Bulan, Kab. Bekasi', '{Model=Fazzio Neo, Warna=Dull Blue, Leasing=OTO, Tenor=23 Bln, Wilayah=Kab. Bekasi}'],
    ['TRX-0005', 'Gear 125 Standard, Metallic Red, BAF, 35 Bulan, Depok', '{Model=Gear 125 Std, Warna=Metallic Red, Leasing=BAF, Tenor=35 Bln, Wilayah=Depok}']
]
col_widths2 = [1.0, 2.6, 2.9]

doc_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\02_Publikasi_Jurnal_JUTISI\Draf_Artikel_JUTISI_Kelompok_1.docx'
doc = docx.Document(doc_path)

# Clear trailing empty paragraphs after paragraph 39
while len(doc.paragraphs) > 40:
    p_last = doc.paragraphs[-1]
    p_last._element.getparent().remove(p_last._element)

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = True
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10)
    r.font.bold = True
    return p

def add_body(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    add_formatted_text(p, text, font_name='Times New Roman', font_size_pt=10)
    return p

def add_table_caption(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(8.5)
    r.font.bold = True
    return p

# --- BUILD SECTION II: METODE PENELITIAN ---
add_heading_1("II. METODE PENELITIAN")

# Sub A
add_heading_2("A. Rancangan dan Alur Prosedur Penelitian")
add_body(
    "Penelitian ini dirancang sebagai penelitian terapan (applied research) berbasis pendekatan kuantitatif komputasional "
    "(computational data-driven research) yang mengadopsi metodologi standar industri Cross-Industry Standard Process for Data Mining "
    "(CRISP-DM) [4]. Kerangka kerja ini mencakup enam fase terpadu yang bersifat iteratif: Pemahaman Bisnis (Business Understanding), "
    "Pemahaman Data (Data Understanding), Persiapan Data (Data Preparation), Pemodelan (Modeling), Evaluasi (Evaluation), dan "
    "Penyebaran (Deployment). Alur operasional penelitian dimulai dari inisiasi studi pendahuluan untuk memetakan kendala mismatch inventory "
    "dan skema pembiayaan pada PT. Sinar Surya Matahari, dilanjutkan dengan ekstraksi 3.113 data faktur penjualan resmi dari sistem basis data "
    "Yamaha Dealer Management System (Y-DMS), pembersihan dan rekayasa keranjang predikat multiatribut, pemodelan pohon frekuensi pola FP-Tree, "
    "pengujian validitas kaidah asosiasi dengan Standar Tiga Metrik (Support, Confidence, Lift Ratio > 1,0), hingga perumusan rekomendasi "
    "strategi bisnis preskriptif bagi manajemen dealer [4]."
)

# Image placement
img_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Penelitian SI\Gambar_3_1_Bagan_Alir_Penelitian.png'
if os.path.exists(img_path):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(2)
    run_img = p_img.add_run()
    run_img.add_picture(img_path, width=Inches(3.8))
    
    p_cap_img = doc.add_paragraph()
    p_cap_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap_img.paragraph_format.space_before = Pt(0)
    p_cap_img.paragraph_format.space_after = Pt(6)
    r_ci = p_cap_img.add_run("Gambar 1. Bagan Alir Tahapan Penelitian CRISP-DM dan FP-Growth")
    r_ci.font.name = 'Times New Roman'
    r_ci.font.size = Pt(8.5)
    r_ci.font.italic = True

# Sub B
add_heading_2("B. Sumber dan Karakteristik Data Penelitian")
add_body(
    "Data penelitian bersumber langsung dari basis data operasional Yamaha Dealer Management System (Y-DMS) PT. Sinar Surya Matahari "
    "pada Gudang Distribusi SSM Bekasi dan Showroom SSM Motor Jakarta Timur selama kuartal ketiga (1 Juni hingga 31 Agustus 2026) "
    "yang merefleksikan transaksi normal (baseline behavior). Penarikan sampel menerapkan teknik purposive sampling dengan kriteria inklusi "
    "berupa faktur penjualan fisik sepeda motor baru yang berstatus selesai (closed and final) serta memiliki kelengkapan atribut sempurna "
    "sehingga diperoleh 3.113 rekaman transaksi valid (diteliti secara sensus). Sebaliknya, kriteria eksklusi mengeliminasi pesanan yang dibatalkan "
    "(canceled), pengajuan kredit yang ditolak (rejected), faktur retur (return), layanan servis berkala bengkel, penjualan suku cadang murni, "
    "serta data dengan nilai kosong (missing values). Data transaksi mencakup lima dimensi keputusan pembelian: model kendaraan "
    "(44 varian produk pada segmen Maxi Series, Classy, Matic 125, Sport, dan Moped), varian warna bodi (22 pilihan warna eksterior pabrikan), "
    "skema lembaga pembiayaan (opsi tunai/Cash dan 3 mitra kredit resmi: BAF, Adira Finance, OTO Multiartha), durasi tenor angsuran kredit "
    "(5 opsi cicilan: 11, 23, 30, 35 bulan, dan Non-Kredit), serta wilayah domisili konsumen (10 area administratif aglomerasi Jabodetabek). "
    "Rincian karakteristik dimensi data transaksi disajikan pada Tabel I."
)
add_table_caption("TABEL I\nSTRUKTUR DIMENSI DAN KARAKTERISTIK ATRIBUT DATA TRANSAKSI PENJUALAN")
t1 = create_academic_table(doc, headers1, data1, col_widths1)

# Sub C
add_heading_2("C. Rekayasa Predicate Basket Multiatribut dan Algoritma FP-Growth")
add_body(
    "Tahap persiapan data (data preparation) merupakan fase rekayasa data mentah menjadi format representasi tabular terstruktur yang siap "
    "diproses oleh algoritma komputasi FP-Growth. Fase ini diawali dengan prosedur pembersihan dan standardisasi data (data cleaning) untuk menangani "
    "nilai kosong (missing values), menyeragamkan format penulisan string (string standardization), memverifikasi keunikan nomor faktur, serta menyingkirkan "
    "derau (noise). Selanjutnya, dilakukan anonimisasi data privasi konsumen (data anonymization) dengan mengeliminasi atribut identitas personal seperti NIK, "
    "nama pembeli, nomor telepon, dan nomor rangka (chassis number) demi mematuhi etika penelitian. Mengingat faktur penjualan fisik dealer motor hanya "
    "mencatat satu unit motor per transaksi, analisis keranjang belanja (market basket analysis) konvensional tidak dapat diterapkan langsung karena "
    "akan menghasilkan kombinasi kosong (empty itemsets). Oleh karena itu, data transaksi ditransformasikan ke dalam representasi keranjang predikat "
    "multiatribut (multi-attribute predicate basket transformation) berformat pasangan logika Atribut=Nilai (seperti Model=Aerox Cyber City, Warna=Cyan, "
    "Leasing=BAF, Tenor=35 Bulan, Wilayah=Kota Bekasi), sehingga algoritma FP-Growth dapat menemukan keterkaitan lintas-dimensi tanpa menimbulkan kaidah "
    "asosiasi semu (spurious rules) [2], [11]. Seluruh predikat kategorikal kemudian dikodekan ke dalam matriks biner kuantitatif (binary incidence matrix) "
    "berdimensi 3.113 baris melalui one-hot encoding sebagai berkas input terstandarisasi. Cuplikan sampel transformasi data transaksi mentah Y-DMS disajikan pada Tabel II."
)
add_table_caption("TABEL II\nCUPLIKAN TRANSFORMASI DATA TRANSAKSI MENJADI KERANJANG PREDIKAT MULTIATRIBUT")
t2 = create_academic_table(doc, headers2, data2, col_widths2)

add_body(
    "Proses penambangan pola frekuensi tinggi dijalankan menggunakan algoritma Frequent Pattern Growth (FP-Growth) [1], [3]. Algoritma ini "
    "memadatkan basis data transaksi ke dalam struktur pohon frekuensi pola (FP-Tree) di memori kerja sistem melalui dua tahap pemindaian "
    "(two-pass database scan). Pemindaian pertama membentuk Header Table yang memuat daftar item berfrekuensi tinggi terurut menurun berdasarkan "
    "ambang batas Minimum Support. Pemindaian kedua membaca kembali seluruh transaksi dan memetakannya ke dalam cabang simpul FP-Tree dengan tautan "
    "pointer (node-links). Selanjutnya, ekstraksi frequent itemsets dilakukan secara rekursif menggunakan pendekatan divide-and-conquer berbasis "
    "Conditional Pattern Base (CPB) dari simpul terbawah (bottom-up) tanpa melalui pembangkitan kandidat kombinasi (candidate generation-free) [1]."
)

# Sub D
add_heading_2("D. Validasi Tiga Metrik dan Perumusan Rekomendasi Preskriptif")
add_body(
    "Kaidah asosiasi yang terbentuk dievaluasi secara kuantitatif menggunakan Standar Validasi Tiga Metrik (Tri-Metric Validation) [2]. "
    "Tingkat dukungan (Support) mengukur persentase probabilitas kemunculan bersama anteseden (X) dan konsekuen (Y) terhadap total populasi transaksi "
    "(Support = P(X ∩ Y)). Tingkat kepastian bersyarat (Confidence) mengukur derajat keandalan munculnya konsekuen Y apabila anteseden X telah terjadi "
    "(Confidence = P(Y | X) = Support(X ∪ Y) / Support(X)). Sedangkan Lift Ratio mengukur kekuatan korelasi dependensi relatif terhadap ekspektasi "
    "kemunculan acak (Lift = Confidence(X => Y) / Support(Y)). Kriteria penyaringan kelayakan ilmiah menetapkan bahwa hanya aturan dengan nilai Lift > 1,0 "
    "yang dipertahankan sebagai korelasi positif murni yang valid untuk strategi bisnis, sedangkan aturan dengan Lift <= 1,0 dieliminasi karena bersifat "
    "independen atau substitutif [2]. Seluruh kaidah asosiasi yang lolos validasi kemudian dihilirkan menjadi tiga rekomendasi manajerial preskriptif: "
    "perancangan panduan penawaran penjualan cerdas bagi pramuniaga (Smart Sales Script), pedoman alokasi distribusi persediaan varian warna antarcabang "
    "(Regional Inventory Allocation), serta perumusan program promosi pembiayaan bersama lembaga leasing rekanan (Joint Multifinance Bundling Program) [4]."
)

target_out = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\02_Publikasi_Jurnal_JUTISI\Draf_Artikel_JUTISI_Kelompok_1_Updated.docx'
doc.save(target_out)
print('Successfully saved to:', target_out)
try:
    doc.save(doc_path)
    print('Successfully updated main file:', doc_path)
except Exception as e:
    print('Note: Main file is currently open in Word. Saved to Updated.docx:', e)
print("Draf_Artikel_JUTISI_Kelompok_1.docx successfully updated with Section II (METODE PENELITIAN)!")
