import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re

doc_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1.docx'
doc = docx.Document(doc_path)

# Data for Darell's section
# Format: list of items: (text, type, indent_level, has_image)
# types: 'heading1_num', 'heading2_num', 'heading3_num', 'body', 'list_a', 'list_1', 'list_sub_a', 'image_caption'

items = [
    ("1.\tPendekatan dan Desain Penelitian", "h1"),
    ("Penelitian ini dirancang sebagai penelitian terapan (applied research) yang memadukan tiga pilar metodologis utama guna menjamin ketelitian ilmiah dan kegunaan praktis:", "body"),
    ("a. Pendekatan Kuantitatif Komputasional (Computational Data-Driven Research): Seluruh proses analisis berpijak pada data empiris faktual berskala besar yang diukur secara matematis melalui metrik frekuensi kemunculan bersama (co-occurrence) dan korelasi statistik antaratribut keputusan pembelian (Sugiyono, 2019; Tan et al., 2018; Sekaran & Bougie, 2016). Melalui pendekatan kuantitatif berbasis komputasi ini, pola keterkaitan perilaku konsumen yang laten dan tidak kasat mata pada rekaman operasional harian dapat diidentifikasi secara objektif, terukur, dan terbebas dari bias subjektivitas pengamat.", "list_a"),
    ("b. Paradigma Association Rule Mining (ARM) Induktif-Eksploratif: Berbeda dengan penelitian kuantitatif konvensional yang bertumpu pada pengujian hipotesis deduktif dengan asumsi variabel terikat tunggal, desain penelitian ini mengadopsi paradigma aturan asosiasi yang bersifat induktif-eksploratif (Han et al., 2022). Paradigma ini bertujuan menemukan keteraturan pola kombinasi atribut yang sering muncul secara simultan (frequent itemsets) di dalam keranjang transaksi tanpa memerlukan penetapan variabel dependen dan independen di awal. Karakteristik ini sangat relevan untuk membedah kompleksitas transaksi dealer sepeda motor yang melibatkan lima dimensi keputusan sekaligus: model kendaraan, varian warna estetika, skema metode pembayaran, durasi tenor kredit, dan wilayah domisili konsumen.", "list_a"),
    ("c. Kerangka Kerja Berkelanjutan CRISP-DM (Iterative Lifecycle): Guna memandu seluruh rangkaian aktivitas penelitian agar terstruktur dan memiliki ketelitian metodologis yang tinggi, penelitian ini mengimplementasikan kerangka kerja standar industri Cross-Industry Standard Process for Data Mining (CRISP-DM) (Sharda et al., 2020; Turban et al., 2018). Kerangka kerja ini mencakup enam fase terintegrasi: Pemahaman Bisnis (Business Understanding), Pemahaman Data (Data Understanding), Persiapan Data (Data Preparation), Pemodelan (Modeling), Evaluasi (Evaluation), dan Penyebaran (Deployment). Keunggulan fundamental CRISP-DM terletak pada sifatnya yang berdaur ulang dan iteratif (iterative feedback loop), yang memungkinkan penyempurnaan parameter pemodelan komputasi algoritma FP-Growth secara berulang hingga menghasilkan kaidah asosiasi yang selaras dengan kebutuhan strategis dealer PT. Sinar Surya Matahari (SSM Motor). Penerapan kerangka ini memastikan penelitian memiliki dasar saintifik yang kokoh, transparan, serta memenuhi kaidah keterulangan (replicability) dalam domain penambangan data otomotif.", "list_a"),
    ("2.\tBagan Alir Tahapan Penelitian", "h1"),
    ("Guna memberikan visualisasi yang terstruktur mengenai alur operasional penelitian dari tahap awal identifikasi masalah hingga perumusan rekomendasi bisnis, dirancang bagan alir penelitian kuantitatif berbasis komputasi data mining. Alur tahapan penelitian secara komprehensif disajikan pada Gambar 3.1.", "body"),
    ("__IMAGE__", "image"),
    ("Gambar 3.1 Bagan Alir Tahapan Penelitian Multi-Attribute Association Rule Mining", "caption"),
    ("Bagan alir pada Gambar 3.1 menggambarkan keterkaitan sistematis alur operasional penelitian yang dirancang mengikuti metodologi CRISP-DM melalui enam tahapan proses berurutan:", "body"),
    ("a. Tahap Identifikasi Masalah Bisnis: Menganalisis kendala operasional pada PT. Sinar Surya Matahari terkait ketidakseimbangan alokasi persediaan varian warna unit dan ketiadaan panduan promosi pembiayaan berbasis data, kemudian menerjemahkannya ke dalam sasaran analitis penambangan data yang terukur.", "list_a"),
    ("b. Tahap Ekstraksi dan Pemahaman Data: Mengekstraksi rekaman faktur transaksi penjualan resmi periode 1 Juni hingga 31 Agustus 2026 dari sistem basis data Yamaha Dealer Management System (Y-DMS) sebanyak 3.113 transaksi, serta memetakan karakteristik lima atribut analisis utama.", "list_a"),
    ("c. Tahap Persiapan dan Transformasi Data: Menjalankan pembersihan data dari nilai kosong dan transaksi anomali, melakukan anonimisasi data pribadi konsumen, serta merekayasa representasi data ke dalam format keranjang predikat multi-atribut biner (multi-attribute predicate basket) guna mencegah munculnya kaidah asosiasi semu.", "list_a"),
    ("d. Tahap Pemodelan Algoritma FP-Growth: Memproses matriks transaksi biner melalui pemindaian data untuk membentuk Header Table, menyusun struktur pohon frekuensi pola (FP-Tree) di memori kerja sistem, serta menambang kombinasi pola frekuensi tinggi secara rekursif berbasis Conditional Pattern Base tanpa pembangkitan kandidat.", "list_a"),
    ("e. Tahap Evaluasi dan Validasi Aturan: Menguji seluruh kaidah asosiasi yang terbentuk menggunakan Standar Validasi Tiga Metrik, yaitu nilai ambang batas Minimum Support, Minimum Confidence, serta memastikan nilai Lift Ratio lebih besar dari satu (Lift > 1,0) guna menyaring korelasi positif murni.", "list_a"),
    ("f. Tahap Hilirisasi Rekomendasi Preskriptif: Mentransformasikan kaidah asosiasi yang terbukti valid menjadi rekomendasi keputusan manajerial terapan bagi operasional dealer, meliputi perancangan panduan penjualan cerdas bagi pramuniaga (Smart Sales Script), pedoman distribusi alokasi stok varian warna antarcabang, dan program promosi pembiayaan bersama lembaga leasing.", "list_a"),
    ("3.\tPembahasan Rinci Tahapan Penelitian", "h1"),
    ("Pelaksanaan penelitian diuraikan secara mendalam berdasarkan enam tahapan siklus hidup CRISP-DM:", "body"),
    ("a. Tahap 1: Pemahaman Bisnis (Business Understanding)", "h2"),
    ("Tahap pemahaman bisnis merupakan fase awal yang krusial untuk menyelaraskan antara kebutuhan operasional bisnis otomotif dengan tujuan teknis penambangan data. Pelaksanaan tahap ini difokuskan pada dua aspek utama:", "body"),
    ("1) Identifikasi Permasalahan Operasional Bisnis: PT. Sinar Surya Matahari (SSM Motor) sebagai dealer resmi sepeda motor Yamaha menghadapi tantangan dalam merencanakan alokasi unit persediaan dan merancang skema promosi penjualan yang tepat sasaran. Selama ini, analisis penjualan kerap dilakukan secara parsial per atribut (misalnya hanya melihat total unit per model), sehingga keterkaitan preferensi konsumen yang melibatkan kombinasi warna unit, preferensi lembaga pembiayaan, tenor kredit, dan wilayah domisili belum terpetakan secara utuh. Akibatnya, dealer kerap menghadapi ketidaksesuaian persediaan (mismatch inventory), seperti penumpukan unit warna tertentu di gudang atau keterlambatan pemenuhan unit bagi konsumen kredit di wilayah tertentu.", "list_1"),
    ("2) Perumusan Sasaran Analitis Penambangan Data: Kendala operasional bisnis tersebut diterjemahkan menjadi sasaran teknis penambangan data, yaitu mengekstraksi kaidah asosiasi multi-atribut yang mampu mengungkap pola kombinasi keputusan pembelian konsumen dari data riil transaksi faktur penjualan. Temuan pola asosiasi tersebut ditargetkan untuk memberikan landasan empiris bagi manajemen dealer dalam merumuskan strategi pengadaan unit persediaan terintegrasi, penawaran paket pembiayaan (leasing bundling), dan penetrasi pemasaran kewilayahan yang lebih efektif dan efisien.", "list_1"),
    ("b. Tahap 2: Pemahaman Data (Data Understanding)", "h2"),
    ("Tahap pemahaman data bertujuan untuk mengidentifikasi karakteristik, format, sebaran, dan kualitas data yang akan diolah. Pelaksanaan tahap ini mencakup tiga prosedur operasional:", "body"),
    ("1) Sumber Data dan Periode Pengamatan: Sumber data primer penelitian ini diperoleh langsung dari basis data operasional Yamaha Dealer Management System (Y-DMS) PT. Sinar Surya Matahari. Data yang diekstraksi mencakup seluruh catatan transaksi faktur penjualan sepeda motor baru selama periode kuartal ketiga (Q3), terhitung sejak 1 Juni 2026 hingga 31 Agustus 2026.", "list_1"),
    ("2) Kriteria Seleksi Sampel Transaksi: Penarikan sampel dilakukan menggunakan teknik purposive sampling berbasis kriteria inklusi dan eksklusi (Sekaran & Bougie, 2016):", "list_1"),
    ("a) Kriteria Inklusi: Mencakup seluruh transaksi faktur penjualan fisik unit sepeda motor baru yang berstatus sah, selesai (closed), dan telah disetujui pembiayaannya atau lunas dalam rentang waktu pengamatan, dengan kelengkapan data yang sempurna pada lima atribut utama. Melalui kriteria ini, diperoleh 3.113 transaksi faktur valid yang diteliti secara sensus.", "list_sub_a"),
    ("b) Kriteria Eksklusi: Mengeliminasi transaksi pemesanan yang dibatalkan oleh pembeli (canceled), transaksi penolakan kredit oleh pihak leasing, faktur retur (return) unit, transaksi servis perawatan berkala bengkel, penjualan suku cadang murni, serta data faktur yang memiliki nilai kosong (missing values).", "list_sub_a"),
    ("3) Dimensi Atribut Keputusan Pembelian Konsumen: Sebanyak 3.113 rekaman faktur transaksi yang lolos seleksi memetakan lima dimensi atribut keputusan pembelian:", "list_1"),
    ("a) Model Sepeda Motor: Merangkum 44 varian produk Yamaha yang terbagi ke dalam segmen Maxi Series (NMAX, Aerox, XMAX), Classy (Grand Filano, Fazzio), Matic 125 (Mio M3, Gear 125, FreeGo), Sport (R15, MT-15, XSR 155), dan Bebek/Moped (MX King, Vega Force, Jupiter Z1).", "list_sub_a"),
    ("b) Varian Warna Kendaraan: Merangkum 22 opsi warna estetika pabrikan (antara lain Matte Black, Metallic Red, Prestige Silver, Dull Blue, Cyan, White).", "list_sub_a"),
    ("c) Lembaga Pembiayaan atau Metode Pembayaran: Mencakup transaksi pembelian tunai (Cash) serta fasilitas pembiayaan kredit melalui perusahaan leasing rekanan resmi (BAF, Adira Finance, OTO Finance, Mandiri Utama Finance/MUF, dan Indomobil Finance).", "list_sub_a"),
    ("d) Durasi Tenor Angsuran Kredit: Mencakup rentang jangka waktu cicilan pembiayaan yang dipilih konsumen, yaitu 11 bulan, 23 bulan, 30 bulan, 35 bulan, serta kategori Non-Kredit untuk pembelian tunai.", "list_sub_a"),
    ("e) Wilayah Domisili Konsumen: Meliputi 10 wilayah administratif domisili tempat tinggal pembeli di kawasan operasional dealer (Kota Serang, Kabupaten Serang, Kota Cilegon, Kabupaten Pandeglang, Kabupaten Lebak, Tangerang, dan sekitarnya).", "list_sub_a"),
]

# Foreign terms to italicize automatically
foreign_terms = [
    r'\bapplied research\b', r'\bcomputational data-driven research\b', r'\bdata mining\b',
    r'\bco-occurrence\b', r'\bAssociation Rule Mining\b', r'\bfrequent itemsets\b',
    r'\bCross-Industry Standard Process for Data Mining\b', r'\bBusiness Understanding\b',
    r'\bData Understanding\b', r'\bData Preparation\b', r'\bModeling\b', r'\bEvaluation\b',
    r'\bDeployment\b', r'\biterative feedback loop\b', r'\bFP-Growth\b', r'\breplicability\b',
    r'\bMulti-Attribute Association Rule Mining\b', r'\bYamaha Dealer Management System\b',
    r'\bmulti-attribute predicate basket\b', r'\bHeader Table\b', r'\bFP-Tree\b',
    r'\bFrequent Pattern Tree\b', r'\bConditional Pattern Base\b', r'\bMinimum Support\b',
    r'\bMinimum Confidence\b', r'\bLift Ratio\b', r'\bSmart Sales Script\b', r'\bleasing\b',
    r'\bmismatch inventory\b', r'\bleasing bundling\b', r'\bpurposive sampling\b',
    r'\bclosed\b', r'\bcanceled\b', r'\breturn\b', r'\bmissing values\b',
    r'\bMaxi Series\b', r'\bClassy\b', r'\bMatic 125\b', r'\bSport\b', r'\bBebek/Moped\b',
    r'\bMatte Black\b', r'\bMetallic Red\b', r'\bPrestige Silver\b', r'\bDull Blue\b',
    r'\bCyan\b', r'\bWhite\b', r'\bCash\b', r'\bNon-Kredit\b', r'\bOne-Hot Encoding\b'
]
combined_regex = re.compile(r'(' + '|'.join(foreign_terms) + r')', re.IGNORECASE)

# First delete existing paragraphs 168 to 189
p_start = doc.paragraphs[168]
p_target_after = doc.paragraphs[190] # Tahap 3

# Delete paragraphs from 168 to 189
for _ in range(190 - 168):
    p = doc.paragraphs[168]
    p._element.getparent().remove(p._element)

# Now insert new paragraphs before p_target_after
img_path = r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Gambar_3_1_Bagan_Alir_Penelitian.png'

for text, p_type in items:
    new_p = p_target_after.insert_paragraph_before()
    new_p.paragraph_format.line_spacing = 1.5
    new_p.paragraph_format.space_after = Pt(4)
    
    if p_type == "image":
        new_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = new_p.add_run()
        run.add_picture(img_path, width=Inches(5.6))
        continue
    
    if p_type == "caption":
        new_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = new_p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
        run.font.italic = True
        continue
    
    new_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # Check bold title prefixes like 'a. ...: ' or '1) ...: '
    prefix = ""
    rest = text
    
    if p_type == "h1":
        run = new_p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        new_p.paragraph_format.space_before = Pt(8)
        continue
    elif p_type == "h2":
        run = new_p.add_run(text)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
        run.font.bold = True
        new_p.paragraph_format.space_before = Pt(6)
        continue
    
    # Handle list prefixes with bold
    colon_idx = -1
    if p_type in ['list_a', 'list_1', 'list_sub_a']:
        # e.g., "a. Pendekatan Kuantitatif Komputasional (Computational Data-Driven Research): "
        colon_idx = text.find(': ')
        if colon_idx != -1:
            prefix = text[:colon_idx+2]
            rest = text[colon_idx+2:]
            
            # Format prefix (bold, with proper italics inside if needed)
            parts = combined_regex.split(prefix)
            for part in parts:
                if not part: continue
                r = new_p.add_run(part)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)
                r.font.bold = True
                if combined_regex.fullmatch(part):
                    r.font.italic = True
    
    # Now format rest of the paragraph with regex for italics
    parts = combined_regex.split(rest)
    for part in parts:
        if not part: continue
        r = new_p.add_run(part)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        if combined_regex.fullmatch(part):
            r.font.italic = True

doc.save(doc_path)
print("Penelitian SI - Kelompok 1.docx successfully updated with new BAB III Darell section!")
