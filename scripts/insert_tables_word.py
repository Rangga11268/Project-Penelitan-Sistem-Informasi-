import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import re
import os

# Foreign terms for italicization
foreign_terms = [
    r'\bapplied research\b', r'\bcomputational data-driven research\b', r'\bdata mining\b',
    r'\bco-occurrence\b', r'\bAssociation Rule Mining\b', r'\bfrequent itemsets\b',
    r'\bCross-Industry Standard Process for Data Mining\b', r'\bBusiness Understanding\b',
    r'\bData Understanding\b', r'\bData Preparation\b', r'\bModeling\b', r'\bEvaluation\b',
    r'\bDeployment\b', r'\biterative feedback loop\b', r'\bFP-Growth\b', r'\breplicability\b',
    r'\bMulti-Attribute Association Rule Mining\b', r'\bYamaha Dealer Management System\b',
    r'\bmulti-attribute predicate basket\b', r'\bmulti-attribute association rules\b',
    r'\bmulti-attribute predicate basket transformation\b',
    r'\bHeader Table\b', r'\bFP-Tree\b', r'\bFrequent Pattern Tree\b', r'\bConditional Pattern Base\b',
    r'\bMinimum Support\b', r'\bMinimum Confidence\b', r'\bLift Ratio\b', r'\bSmart Sales Script\b',
    r'\bleasing\b', r'\bmismatch inventory\b', r'\bleasing bundling\b', r'\bpurposive sampling\b',
    r'\bclosed\b', r'\bcanceled\b', r'\breturn\b', r'\bmissing values\b', r'\btrivial rules\b',
    r'\bdata cleaning\b', r'\bdata anonymization\b', r'\bmarket basket analysis\b', r'\bempty itemsets\b',
    r'\bMaxi Series\b', r'\bClassy\b', r'\bMatic 125\b', r'\bSport\b', r'\bMoped\b', r'\bBebek/Moped\b',
    r'\bMatte Black\b', r'\bMetallic Red\b', r'\bPrestige Silver\b', r'\bDull Blue\b',
    r'\bCyan\b', r'\bWhite\b', r'\bCash\b', r'\bNon-Kredit\b', r'\bOne-Hot Encoding\b', r'\bone-hot encoding\b'
]
combined_regex = re.compile(r'(' + '|'.join(foreign_terms) + r')', re.IGNORECASE)

def add_formatted_text(p, text, font_name='Times New Roman', font_size_pt=12, bold_prefix=None):
    if bold_prefix and text.startswith(bold_prefix):
        prefix_run = p.add_run(bold_prefix)
        prefix_run.font.name = font_name
        prefix_run.font.size = Pt(font_size_pt)
        prefix_run.font.bold = True
        text = text[len(bold_prefix):]
        
    parts = combined_regex.split(text)
    for part in parts:
        if not part: continue
        r = p.add_run(part)
        r.font.name = font_name
        r.font.size = Pt(font_size_pt)
        if combined_regex.fullmatch(part):
            r.font.italic = True

def create_academic_table(doc, headers, data, col_widths, font_size_pt=9, font_name='Times New Roman'):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Table borders (Open Academic 3-horizontal borders: Top, Header bottom, Table bottom)
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
    
    def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
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
        
    # Header row
    header_row = table.rows[0]
    trPr = header_row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    
    for i, title in enumerate(headers):
        cell = header_row.cells[i]
        cell.width = Inches(col_widths[i])
        set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
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

    # Data rows
    for row_idx, row_data in enumerate(data):
        row = table.rows[row_idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            cell = row.cells[col_idx]
            cell.width = Inches(col_widths[col_idx])
            set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            
            # Alignments: Center for codes and counts, Left for names and descriptions
            if len(headers) == 4 and col_idx in [1, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif len(headers) == 3 and col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                
            add_formatted_text(p, cell_value, font_name=font_name, font_size_pt=font_size_pt)

    return table

# Table 1 Data
headers1 = ['Atribut', 'Tipe Data', 'Jumlah Varian', 'Keterangan dan Contoh Nilai']
data1 = [
    ['Model Motor', 'Kategorikal', '44 Model', 'Lini produk Yamaha pada segmen Maxi Series, Classy, Matic 125, Sport, dan Moped (contoh: Aerox 155 Cyber City, NMAX Connected, Grand Filano, Fazzio Neo, Gear 125).'],
    ['Varian Warna', 'Kategorikal', '22 Warna', 'Pilihan estetika warna eksterior dari pabrikan (contoh: Matte Black, Metallic Red, Prestige Silver, Dull Blue, White).'],
    ['Lembaga Pembiayaan', 'Kategorikal', '4 Kategori', 'Skema pembelian tunai (Cash) dan fasilitas pembiayaan kredit melalui mitra resmi (BAF, Adira Finance, OTO Multiartha).'],
    ['Tenor Angsuran', 'Diskret', '5 Opsi', 'Jangka waktu cicilan yang disepakati konsumen (11 Bulan, 23 Bulan, 30 Bulan, 35 Bulan, Non-Kredit).'],
    ['Wilayah Domisili', 'Kategorikal', '10 Area', 'Wilayah tempat tinggal konsumen di kawasan aglomerasi Jabodetabek (Kota Bekasi, Kab. Bekasi, Jakarta Timur, Jakarta Selatan, Depok, Bogor, Tangerang, dll.).']
]
col_widths1_proposal = [1.3, 1.0, 1.0, 3.0]
col_widths1_journal = [1.3, 0.9, 0.9, 3.4]

# Table 2 Data
headers2 = ['No. Faktur', 'Data Mentah Transaksi Y-DMS', 'Representasi Keranjang Predikat Multiatribut']
data2 = [
    ['TRX-0001', 'Aerox Cyber City, Cyan, BAF, 35 Bulan, Kota Bekasi', '{Model=Aerox Cyber City, Warna=Cyan, Leasing=BAF, Tenor=35 Bln, Wilayah=Kota Bekasi}'],
    ['TRX-0002', 'NMAX Connected, Matte Black, Adira, 35 Bulan, Jakarta Timur', '{Model=NMAX Connected, Warna=Matte Black, Leasing=Adira, Tenor=35 Bln, Wilayah=Jakarta Timur}'],
    ['TRX-0003', 'Grand Filano Lux, White, Cash, Non-Kredit, Jakarta Selatan', '{Model=Grand Filano Lux, Warna=White, Leasing=Cash, Tenor=Non-Kredit, Wilayah=Jakarta Selatan}'],
    ['TRX-0004', 'Fazzio Neo, Dull Blue, OTO Multiartha, 23 Bulan, Kab. Bekasi', '{Model=Fazzio Neo, Warna=Dull Blue, Leasing=OTO, Tenor=23 Bln, Wilayah=Kab. Bekasi}'],
    ['TRX-0005', 'Gear 125 Standard, Metallic Red, BAF, 35 Bulan, Depok', '{Model=Gear 125 Std, Warna=Metallic Red, Leasing=BAF, Tenor=35 Bln, Wilayah=Depok}']
]
col_widths2_proposal = [1.0, 2.5, 2.8]
col_widths2_journal = [1.0, 2.6, 2.9]

# --- 1. UPDATE PROPOSAL: Penelitian SI - Kelompok 1.docx ---
def update_proposal_docx(file_path):
    print(f"\nProcessing proposal document: {file_path}")
    doc = docx.Document(file_path)
    
    # Locate insertion boundary:
    # Target starts at paragraph mentioning "Tahap Inisiasi" or index 193
    # Target ends before "Tahap 4 (CRISP-DM): Pemodelan"
    start_idx = None
    end_idx = None
    
    for i, p in enumerate(doc.paragraphs):
        if "Tahap Inisiasi" in p.text and start_idx is None:
            start_idx = i
        if ("Tahap 4 (CRISP-DM)" in p.text or "Pemodelan Algoritma FP-Growth" in p.text) and start_idx is not None and i > start_idx:
            end_idx = i
            break
            
    if start_idx is None or end_idx is None:
        print(f"Error: Could not locate section bounds in {file_path}! start={start_idx}, end={end_idx}")
        return False
        
    print(f"Found replacement bounds: start_idx={start_idx}, end_idx={end_idx}")
    target_after = doc.paragraphs[end_idx]
    
    # Paragraph contents to insert:
    p1_text = "Rangkaian tahapan penelitian diawali dengan inisiasi studi pendahuluan melalui pengamatan langsung terhadap alur operasional dan pencatatan transaksi pada dealer PT. Sinar Surya Matahari (SSM Motor). Inisiasi ini bertujuan untuk membedah tantangan faktual yang dihadapi pihak manajemen dalam tata kelola persediaan unit serta merumuskan integrasi antara kendala bisnis dengan kebutuhan analisis penambangan data (data mining). Berdasarkan telaah awal, dealer menghadapi kendala ketidakseimbangan penyerapan persediaan varian warna tertentu dan minimnya pemetaan pola perilaku konsumen terkait kombinasi tipe kendaraan dengan preferensi pembiayaan, tenor angsuran, serta sebaran wilayah tempat tinggal. Kendala operasional tersebut kemudian dikonversikan menjadi masalah penelitian kuantitatif komputasional berbasis Multi-Attribute Association Rule Mining."
    
    p2_text = "Pada tahap pemahaman bisnis (Business Understanding), fokus utama diarahkan untuk menyelaraskan kebutuhan bisnis operasional dealer dengan sasaran analitis teknis penambangan data. Evaluasi mendalam terhadap praktik manajemen persediaan memperlihatkan bahwa analisis penjualan yang selama ini bertumpu pada agregasi parsial per model kendaraan belum sanggup mengungkap keterkaitan multivariabel yang saling mempengaruhi. Hal tersebut berpotensi menimbulkan mismatch inventory, seperti penumpukan stok untuk varian warna tertentu di gudang serta keterlambatan distribusi unit bagi konsumen kredit di wilayah tertentu. Berangkat dari kondisi tersebut, sasaran analitis penelitian ditetapkan secara eksplisit untuk mengekstraksi kaidah asosiasi yang menghubungkan kelima atribut keputusan pembelian. Temuan pola asosiasi ini ditargetkan menjadi dasar empiris yang aplikatif bagi manajemen dealer dalam merancang panduan penjualan terpadu (Smart Sales Script), penataan alokasi pengadaan persediaan antarcabang, dan program penawaran paket pembiayaan (leasing bundling) yang terarah."
    
    p3_text = "Tahap pemahaman data (Data Understanding) bertujuan untuk mengidentifikasi karakteristik, format, sebaran, dan kualitas data yang bersumber langsung dari basis data operasional Yamaha Dealer Management System (Y-DMS) PT. Sinar Surya Matahari selama periode kuartal ketiga (1 Juni hingga 31 Agustus 2026). Penarikan sampel data menerapkan teknik purposive sampling berlandaskan kriteria inklusi dan eksklusi yang ketat. Kriteria inklusi mencakup seluruh rekaman transaksi faktur resmi penjualan fisik sepeda motor baru yang berstatus sah, selesai (closed), serta lunas atau telah disetujui pembiayaannya oleh pihak rekanan dengan kelengkapan data sempurna pada lima dimensi atribut utama. Sebaliknya, kriteria eksklusi menyingkirkan rekaman transaksi yang dibatalkan (canceled), penolakan kredit oleh pihak leasing, retur barang, layanan servis bengkel berkala, penjualan suku cadang murni, dan data transaksi dengan nilai kosong (missing values). Berdasarkan penyaringan sensus tersebut, diperoleh 3.113 rekaman transaksi faktur valid yang memetakan lima dimensi keputusan pembelian: model sepeda motor (44 varian lintas 5 segmen), varian warna bodi kendaraan (22 pilihan warna estetika pabrikan), lembaga pembiayaan atau metode pembayaran (opsi tunai dan 3 perusahaan kredit resmi), durasi tenor angsuran kredit (5 opsi jangka waktu cicilan), dan wilayah domisili konsumen (10 area kabupaten/kota aglomerasi). Struktur dimensi dan karakteristik atribut data transaksi tersebut disajikan pada Tabel 3.1."
    
    cap1_text = "Tabel 3.1 Struktur Dimensi dan Karakteristik Atribut Data Transaksi Penjualan PT. SSM Motor"
    
    p4_text = "Tahap persiapan data (Data Preparation) merupakan fase rekayasa data mentah menjadi bentuk representasi tabular terstruktur yang siap diproses oleh algoritma FP-Growth. Prosedur pembersihan data (data cleaning) dijalankan untuk memastikan standarisasi penamaan nilai data dan penanganan anomali format rekaman. Guna mematuhi etika penelitian dan perlindungan privasi konsumen, dilakukan anonimisasi data (data anonymization) melalui penghilangan atribut identitas personal seperti nomor kartu tanda penduduk, nomor rangka, nomor mesin, serta penyamaran kode faktur. Mengingat transaksi riil dealer sepeda motor hanya mencatat satu unit fisik per lembar faktur, penelitian ini mengimplementasikan transformasi keranjang predikat multiatribut (multi-attribute predicate basket transformation). Setiap transaksi direkayasa menjadi kumpulan item logika berpasangan Atribut=Nilai, sehingga seluruh dimensi keputusan dapat dianalisis secara simultan dalam satu transaksi tanpa menimbulkan kaidah asosiasi semu (trivial rules). Selanjutnya, representasi predikat tersebut dikonversi ke dalam format matriks biner (one-hot encoding) sebagai masukan utama algoritma penambangan data. Ilustrasi transformasi data transaksi mentah Y-DMS menjadi keranjang predikat multiatribut disajikan pada Tabel 3.2."
    
    cap2_text = "Tabel 3.2 Cuplikan Sampel Transformasi Data Transaksi Menjadi Keranjang Predikat Multiatribut"

    # Delete existing paragraphs between start_idx and end_idx
    num_to_delete = end_idx - start_idx
    for _ in range(num_to_delete):
        p_del = doc.paragraphs[start_idx]
        p_del._element.getparent().remove(p_del._element)
        
    # Helper to insert paragraph before target_after
    def insert_para(text, bold_prefix=None, space_after=6, space_before=0, line_spacing=1.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
        new_p = target_after.insert_paragraph_before()
        new_p.alignment = align
        new_p.paragraph_format.line_spacing = line_spacing
        new_p.paragraph_format.space_before = Pt(space_before)
        new_p.paragraph_format.space_after = Pt(space_after)
        add_formatted_text(new_p, text, font_name='Times New Roman', font_size_pt=12, bold_prefix=bold_prefix)
        return new_p

    def insert_caption(cap_text):
        new_p = target_after.insert_paragraph_before()
        new_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        new_p.paragraph_format.line_spacing = 1.0
        new_p.paragraph_format.space_before = Pt(8)
        new_p.paragraph_format.space_after = Pt(4)
        r = new_p.add_run(cap_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        r.font.bold = True
        return new_p

    # Insert Paragraph 1
    insert_para(p1_text, bold_prefix="Tahap Inisiasi dan Identifikasi Masalah Awal (Mulai): ", space_before=4)
    
    # Insert Paragraph 2
    insert_para(p2_text, bold_prefix="Tahap 1 (CRISP-DM): Pemahaman Bisnis (Business Understanding): ", space_before=4)
    
    # Insert Paragraph 3
    insert_para(p3_text, bold_prefix="Tahap 2 (CRISP-DM): Pemahaman Data (Data Understanding): ", space_before=4)
    
    # Insert Caption 1
    insert_caption(cap1_text)
    
    # Insert Table 1
    t1 = create_academic_table(doc, headers1, data1, col_widths1_proposal, font_size_pt=9.5)
    target_after._element.addprevious(t1._element)
    
    # Space paragraph after Table 1
    sp1 = target_after.insert_paragraph_before()
    sp1.paragraph_format.space_after = Pt(4)
    sp1.paragraph_format.space_before = Pt(0)
    
    # Insert Paragraph 4
    insert_para(p4_text, bold_prefix="Tahap 3 (CRISP-DM): Persiapan Data (Data Preparation): ", space_before=4)
    
    # Insert Caption 2
    insert_caption(cap2_text)
    
    # Insert Table 2
    t2 = create_academic_table(doc, headers2, data2, col_widths2_proposal, font_size_pt=9)
    target_after._element.addprevious(t2._element)
    
    # Space paragraph after Table 2
    sp2 = target_after.insert_paragraph_before()
    sp2.paragraph_format.space_after = Pt(4)
    sp2.paragraph_format.space_before = Pt(0)
    
    doc.save(file_path)
    print(f"Successfully updated {file_path} with flowing paragraphs and academic tables!")
    return True

# --- 2. UPDATE JOURNAL: Draf_Artikel_JUTISI_2026_Kelompok_1.docx ---
def update_journal_docx(file_path):
    print(f"\nProcessing journal document: {file_path}")
    doc = docx.Document(file_path)
    
    # 1. Remove leftover template Table 0 if present (the dummy font styles table)
    for tbl in list(doc.tables):
        if len(tbl.rows) > 0 and 'Biasa (Regular)' in [c.text for c in tbl.rows[min(1, len(tbl.rows)-1)].cells]:
            print("Removing leftover template dummy table from journal...")
            tbl._tbl.getparent().remove(tbl._tbl)
            
    # Locate Section II and subsections
    p_sec2 = None
    p_subA = None
    p_subB = None
    p_subC = None
    
    for i, p in enumerate(doc.paragraphs):
        if "II. METODE PENELITIAN" in p.text:
            p_sec2 = i
        if "A. Objek dan Pengumpulan Data" in p.text:
            p_subA = i
        if "B. Transformasi Predicate Basket" in p.text:
            p_subB = i
        if "C. Algoritma FP-Growth" in p.text:
            p_subC = i
            
    print(f"Journal indices: sec2={p_sec2}, subA={p_subA}, subB={p_subB}, subC={p_subC}")
    
    # Text for Subsection A:
    subA_text = "Data penelitian bersumber dari rekaman data operasional Yamaha Dealer Management System (Y-DMS) pada dealer resmi PT. Sinar Surya Matahari (SSM Motor) selama periode kuartal ketiga (1 Juni hingga 31 Agustus 2026). Pengambilan sampel dilakukan menggunakan teknik purposive sampling dengan kriteria inklusi berupa transaksi faktur penjualan fisik sepeda motor baru yang berstatus sah, selesai (closed), disetujui pembiayaannya atau lunas, serta memiliki data lengkap pada seluruh atribut. Kriteria eksklusi mengeleminasi data transaksi batal (canceled), penolakan kredit oleh pihak leasing, retur unit, transaksi bengkel, penjualan suku cadang terpisah, serta data dengan nilai kosong (missing values). Berdasarkan kriteria seleksi tersebut, diperoleh populasi sensus sebanyak 3.113 transaksi faktur valid. Karakteristik atribut data transaksi mencakup lima dimensi keputusan pembelian: model kendaraan, varian warna estetika, skema lembaga pembiayaan, durasi tenor kredit, dan wilayah domisili konsumen. Rincian struktur dimensi data transaksi disajikan pada Tabel I."
    
    capI_text = "TABEL I\nSTRUKTUR DIMENSI DAN KARAKTERISTIK ATRIBUT DATA TRANSAKSI PENJUALAN"
    
    # Text for Subsection B:
    subB_text = "Mengingat transaksi dealer fisik hanya mencatat satu unit motor per faktur transaksi, pengolahan data konvensional market basket analysis tidak dapat diterapkan secara langsung karena akan menghasilkan kombinasi kosong (empty itemsets). Oleh karena itu, data transaksi ditransformasikan ke dalam representasi keranjang predikat multiatribut (multi-attribute predicate basket). Setiap dimensi keputusan direkayasa menjadi pasangan logika predikat Atribut=Nilai, sehingga kelima dimensi atribut diperlakukan setara sebagai item diskret dalam satu transaksi. Setelah melalui pembersihan (data cleaning) dan penyamaran privasi (data anonymization), data dikodekan ke dalam matriks biner (one-hot encoding) bernilai 1 jika predikat muncul dan 0 jika tidak. Cuplikan sampel transformasi data transaksi mentah Y-DMS menjadi keranjang predikat multiatribut disajikan pada Tabel II."
    
    capII_text = "TABEL II\nCUPLIKAN TRANSFORMASI DATA TRANSAKSI MENJADI KERANJANG PREDIKAT MULTIATRIBUT"
    
    # Update paragraph under subA
    p_body_A = doc.paragraphs[p_subA + 1]
    p_body_A.text = ""
    p_body_A.paragraph_format.line_spacing = 1.0
    p_body_A.paragraph_format.space_after = Pt(4)
    p_body_A.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_formatted_text(p_body_A, subA_text, font_name='Times New Roman', font_size_pt=10)
    
    # Caption I
    cap_I = doc.paragraphs[p_subB].insert_paragraph_before()
    cap_I.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_I.paragraph_format.line_spacing = 1.0
    cap_I.paragraph_format.space_before = Pt(6)
    cap_I.paragraph_format.space_after = Pt(2)
    r_cap_I = cap_I.add_run(capI_text)
    r_cap_I.font.name = 'Times New Roman'
    r_cap_I.font.size = Pt(8.5)
    r_cap_I.font.bold = True
    
    # Table I
    t_I = create_academic_table(doc, headers1, data1, col_widths1_journal, font_size_pt=8.5)
    doc.paragraphs[p_subB]._element.addprevious(t_I._element)
    
    # Update paragraph under subB
    # Re-find p_subB index since we inserted paragraphs
    for i, p in enumerate(doc.paragraphs):
        if "B. Transformasi Predicate Basket" in p.text:
            p_subB_new = i
        if "C. Algoritma FP-Growth" in p.text:
            p_subC_new = i
            break
            
    p_body_B = doc.paragraphs[p_subB_new + 1]
    p_body_B.text = ""
    p_body_B.paragraph_format.line_spacing = 1.0
    p_body_B.paragraph_format.space_after = Pt(4)
    p_body_B.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_formatted_text(p_body_B, subB_text, font_name='Times New Roman', font_size_pt=10)
    
    # Caption II
    cap_II = doc.paragraphs[p_subC_new].insert_paragraph_before()
    cap_II.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap_II.paragraph_format.line_spacing = 1.0
    cap_II.paragraph_format.space_before = Pt(6)
    cap_II.paragraph_format.space_after = Pt(2)
    r_cap_II = cap_II.add_run(capII_text)
    r_cap_II.font.name = 'Times New Roman'
    r_cap_II.font.size = Pt(8.5)
    r_cap_II.font.bold = True
    
    # Table II
    t_II = create_academic_table(doc, headers2, data2, col_widths2_journal, font_size_pt=8)
    doc.paragraphs[p_subC_new]._element.addprevious(t_II._element)
    
    doc.save(file_path)
    print(f"Successfully updated journal {file_path} with JuTISI tables and refined paragraphs!")
    return True

if __name__ == '__main__':
    p1 = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1.docx'
    p3 = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1 - Final_Revisi.docx'
    p2 = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\02_Publikasi_Jurnal_JUTISI\Draf_Artikel_JUTISI_2026_Kelompok_1.docx'
    
    update_proposal_docx(p1)
    if os.path.exists(p3):
        update_proposal_docx(p3)
    update_journal_docx(p2)
    print("\nALL DOCUMENTS UPDATED SUCCESSFULLY!")
