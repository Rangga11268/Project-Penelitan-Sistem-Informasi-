import os
import subprocess

def generate_bab1_pdf():
    pdf_filename = "BAB_1_PENDAHULUAN_KELOMPOK_1_UBSI.pdf"
    output_pdf_path = os.path.abspath(os.path.join("docs", pdf_filename))
    temp_html_path = os.path.abspath(os.path.join("docs", "temp_bab1_pendahuluan.html"))
    
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>BAB 1 PENDAHULUAN - TUGAS PENELITIAN SISTEM INFORMASI</title>
<style>
  @page {
    size: A4;
    margin: 30mm 25mm 25mm 30mm;
    @bottom-right {
      content: counter(page);
      font-family: 'Times New Roman', Times, serif;
      font-size: 10pt;
      color: #333333;
    }
  }

  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #111111;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    text-align: justify;
  }

  /* Header Cover Section */
  .doc-header {
    text-align: center;
    border-bottom: 2px solid #000000;
    padding-bottom: 15px;
    margin-bottom: 25px;
  }

  .univ-name {
    font-size: 14pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .faculty-name {
    font-size: 11pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-top: 3px;
  }

  .course-name {
    font-size: 11pt;
    font-style: italic;
    margin-top: 5px;
    color: #333333;
  }

  .title-box {
    background-color: #f8f9fa;
    border-left: 4px solid #1a365d;
    padding: 12px 16px;
    margin: 20px 0;
    text-align: left;
  }

  .doc-title-label {
    font-size: 10pt;
    font-weight: bold;
    text-transform: uppercase;
    color: #1a365d;
    margin-bottom: 4px;
  }

  .doc-title-text {
    font-size: 12pt;
    font-weight: bold;
    line-height: 1.4;
    color: #000000;
  }

  .meta-table {
    width: 100%;
    margin-bottom: 25px;
    font-size: 10.5pt;
    border-collapse: collapse;
  }

  .meta-table td {
    padding: 3px 0;
    vertical-align: top;
  }

  .meta-label {
    width: 20%;
    font-weight: bold;
  }

  .meta-colon {
    width: 3%;
  }

  .meta-val {
    width: 77%;
  }

  /* Headings */
  h1 {
    font-size: 14pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin-top: 25px;
    margin-bottom: 20px;
    letter-spacing: 0.5px;
  }

  h2 {
    font-size: 12pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-top: 20px;
    margin-bottom: 10px;
    border-bottom: 1px solid #cccccc;
    padding-bottom: 4px;
    color: #0f172a;
  }

  h3 {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 14px;
    margin-bottom: 6px;
    color: #1e293b;
  }

  p {
    margin-top: 0;
    margin-bottom: 10px;
    text-indent: 30px;
  }

  p.no-indent {
    text-indent: 0;
  }

  ol, ul {
    margin-top: 0;
    margin-bottom: 10px;
    padding-left: 30px;
  }

  li {
    margin-bottom: 6px;
  }

  /* Tables */
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0 20px 0;
    font-size: 10pt;
  }

  table.data-table th, table.data-table td {
    border: 1px solid #333333;
    padding: 7px 9px;
    text-align: left;
    vertical-align: top;
  }

  table.data-table th {
    background-color: #f1f5f9;
    font-weight: bold;
    color: #0f172a;
  }

  .highlight-box {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    padding: 10px 14px;
    margin: 15px 0;
    font-size: 10.5pt;
  }

  .footer-note {
    margin-top: 30px;
    border-top: 1px solid #dddddd;
    padding-top: 10px;
    text-align: center;
    font-size: 9.5pt;
    color: #555555;
    font-style: italic;
  }
</style>
</head>
<body>

<div class="doc-header">
  <div class="univ-name">UNIVERSITAS BINA SARANA INFORMATIKA</div>
  <div class="faculty-name">FAKULTAS TEKNIK DAN INFORMATIKA — PROGRAM STUDI SISTEM INFORMASI</div>
  <div class="course-name">Tugas Mata Kuliah: Penelitian Sistem Informasi (Semester 5) — Dosen: Syifa Nur Rakhmah, M.Kom.</div>
</div>

<div class="title-box">
  <div class="doc-title-label">JUDUL TUGAS PENELITIAN SISTEM INFORMASI (KELOMPOK 1)</div>
  <div class="doc-title-text">"Penerapan Algoritma FP-Growth dalam Multi-Attribute Association Rule Mining untuk Analisis Pola Pembelian Sepeda Motor dan Preferensi Skema Pembiayaan Konsumen (Studi Kasus: PT. Sinar Surya Matahari)"</div>
</div>

<table class="meta-table">
  <tr>
    <td class="meta-label">Anggota Kelompok</td>
    <td class="meta-colon">:</td>
    <td class="meta-val">
      1. Darell Rangga Putra R. (NIM: 19241009)<br>
      2. Megi Refkiansyah (NIM: 19240488)<br>
      3. Wahyu Rizky (NIM: 19240493)
    </td>
  </tr>
  <tr>
    <td class="meta-label">Objek Riset</td>
    <td class="meta-colon">:</td>
    <td class="meta-val">PT. Sinar Surya Matahari (Dealer Resmi Sepeda Motor Yamaha)</td>
  </tr>
  <tr>
    <td class="meta-label">Dataset</td>
    <td class="meta-colon">:</td>
    <td class="meta-val">3.113 Data Transaksi Riil DMS (Periode Juni – Agustus 2026)</td>
  </tr>
  <tr>
    <td class="meta-label">Target Luaran</td>
    <td class="meta-colon">:</td>
    <td class="meta-val">Publikasi Artikel Jurnal Terakreditasi Nasional (SINTA 2 / SINTA 3 / SINTA 4)</td>
  </tr>
</table>

<h1>BAB I<br>PENDAHULUAN</h1>

<h2>1.1 LATAR BELAKANG (BACKGROUND)</h2>
<p>Industri otomotif roda dua di Indonesia merupakan salah satu sektor penggerak ekonomi retail terbesar dengan volume transaksi mencapai jutaan unit per tahun. Dalam proses bisnis jaringan dealer resmi (<em>authorized dealer</em>), transaksi sepeda motor tergolong sebagai transaksi barang tahan lama dengan keterlibatan keputusan tinggi (<em>high-involvement durable goods purchase</em>). Pada transaksi bernilai tinggi ini, keputusan konsumen tidak hanya dipengaruhi oleh preferensi karakteristik fisik kendaraan (seperti tipe model, kapasitas mesin, dan varian warna), melainkan sangat bergantung pada ketersediaan instrumen fasilitas pembiayaan konsumen (<em>consumer financing / multifinance leasing</em>). Data asosiasi industri mencatat bahwa lebih dari 75% transaksi pembelian sepeda motor baru di Indonesia dilakukan melalui skema kredit bertahap.</p>

<p>PT. Sinar Surya Matahari merupakan dealer resmi sepeda motor Yamaha yang melayani penjualan unit baru, suku cadang, dan jasa perawatan resmi. Dalam operasional hariannya, perusahaan mencatatkan ribuan transaksi penjualan yang melibatkan interaksi multi-pihak antara dealer, calon pembeli, serta berbagai mitra lembaga pembiayaan resmi (seperti Bussan Auto Finance / BAF, Adira Dinamika Multi Finance, dan OTO Multiartha). Namun, data riwayat transaksi penjualan yang tersimpan di dalam basis data <em>Dealer Management System</em> (DMS) selama ini hanya berfungsi sebagai arsip pencatatan administratif dan pelaporan akuntansi periodik. Data tersebut belum dimanfaatkan secara optimal sebagai aset strategis untuk mengekstraksi wawasan pengetahuan bisnis (<em>knowledge discovery</em>).</p>

<p>Ketiadaan analisis data berbasis pola transaksi historis menimbulkan sejumlah permasalahan nyata di tingkat operasional dan manajerial dealer. Pertama, fenomena <em>lost sales</em> akibat kegagalan negosiasi kredit (<em>price shock</em>), di mana calon pembeli membatalkan pesanan karena pramuniaga (<em>sales counter</em>) secara keliru menawarkan simulasi tenor cicilan atau lembaga pembiayaan yang tidak sesuai dengan daya bayar karakteristik segmen konsumen motor tersebut. Kedua, terjadinya <em>leasing mismatch</em>, yaitu ketidakcocokan antara profil pembeli tipe motor tertentu dengan karakteristik persetujuan kredit lembaga pembiayaan yang diajukan, sehingga memperpanjang siklus verifikasi dan meningkatkan rasio penolakan (<em>rejection rate</em>). Ketiga, terjadinya ketidakseimbangan persediaan (<em>inventory imbalance</em>) varian warna dan model motor antar-cabang wilayah karena alokasi unit masih dilakukan secara perkiraan manual tanpa mempertimbangkan preferensi lokal konsumen.</p>

<p>Oleh karena itu, diperlukan penerapan teknik <em>Data Mining</em>, khususnya <em>Association Rule Mining</em> (penambangan kaidah asosiasi), untuk membedah keterkaitan tersembunyi antara pilihan produk fisik kendaraan dengan preferensi skema pembiayaan konsumen. Dengan memanfaatkan algoritma <em>Frequent Pattern Growth</em> (FP-Growth), ribuan riwayat transaksi faktur dapat diproses secara efisien untuk menemukan pola kombinasi terkuat guna mendukung perumusan strategi penjualan cerdas (<em>smart sales script</em>), perencanaan promosi bersama lembaga pembiayaan, dan optimalisasi alokasi inventaris dealer.</p>

<h2>1.2 TINJAUAN PUSTAKA SINGKAT (LITERATURE REVIEW)</h2>
<p>Perkembangan penelitian <em>Association Rule Mining</em> (ARM) dalam disiplin ilmu Sistem Informasi dan <em>Knowledge Discovery in Databases</em> (KDD) selama rentang waktu 3 hingga 5 tahun terakhir (2021–2025) menunjukkan kemajuan pesat dalam pemanfaatan algoritma penambangan pola frekuensi transaksi.</p>

<p>Penelitian terdahulu yang dilakukan oleh Widodo et al. (2022) pada dealer resmi sepeda motor Yamaha (PT. Alfa Scorpii Medan) telah menerapkan teknik <em>data mining</em> untuk mengidentifikasi minat konsumen dalam memilih tipe sepeda motor, namun penelitian tersebut menggunakan algoritma klasifikasi pohon keputusan (C4.5) yang bersifat memprediksi kelas label tunggal, bukan menambang aturan kombinasi antar-variabel transaksi. Sementara itu, kajian penerapan algoritma asosiasi pada sektor otomotif di jurnal nasional terakreditasi SINTA sebagian besar masih terfokus pada ranah purna jual dan suku cadang (<em>aftersales & spare parts</em>). Sebagai contoh, Soleh et al. (2022) menerapkan algoritma FP-Growth untuk menganalisis keranjang belanja suku cadang pada toko onderdil, Subakti & Nataliani (2022) menggunakan algoritma Apriori untuk penempatan produk oli motor, dan Rahmatullah et al. (2022) memanfaatkan Apriori untuk memprediksi penjualan <em>sparepart</em> pada dealer PT. Lautan Teduh Interniaga Kotabumi. Penelitian-penelitian tersebut membuktikan keandalan kaidah asosiasi dalam penataan stok barang homogen bernilai rendah, namun belum menjangkau analisis transaksi unit kendaraan utuh.</p>

<p>Di sisi lain, penelitian mutakhir mengenai perbandingan efisiensi algoritma penambangan asosiasi secara konsisten menegaskan keunggulan algoritma FP-Growth dibandingkan algoritma Apriori klasik. Rahman & Riana (2025) serta Rachmawati et al. (2024) membuktikan bahwa FP-Growth memiliki efisiensi komputasi dan pemanfaatan memori yang jauh lebih unggul karena menggunakan struktur pohon kompak (<em>FP-Tree</em>) dan pembentukan basis pola kondisional (<em>Conditional Pattern Base</em>), sehingga mengeliminasi <em>bottleneck</em> pemindaian basis data berulang kali serta menghindari pembentukan kandidat itemset kombinatorik yang membebani memori (<em>candidate generation bottleneck</em>). Lebih lanjut, Saptadi et al. (2023) dan Muharam et al. (2025) menerapkan penambangan asosiasi pada data transaksi ritel harian (<em>Fast-Moving Consumer Goods</em> / FMCG) dan F&B, namun penelitian-penelitian tersebut masih menerapkan model transaksi satu dimensi (<em>single-attribute itemset</em>) yang hanya menghubungkan nama barang konsumsi instan.</p>

<p>Mengenai penambangan data multi-atribut, Ramadhan & Sensuse (2020) dalam publikasinya di <em>Jurnal Sistem Informasi Bisnis (JSINBIS)</em> memformulasikan konsep <em>Multi-Dimensional Association Rule Mining</em> pada bisnis ritel untuk menggabungkan atribut produk dengan dimensi waktu belanja. Landasan metodologis ini membuka peluang pengembangan lebih lanjut untuk mengintegrasikan variabel non-komoditas ke dalam struktur keranjang transaksi data mining.</p>

<h2>1.3 RUMUSAN MASALAH & CELAH PENELITIAN (RESEARCH GAP)</h2>
<p class="no-indent"><strong>A. Rumusan Masalah:</strong></p>
<ol>
  <li>Bagaimana mentransformasikan data transaksi penjualan faktur tunggal PT. Sinar Surya Matahari menjadi representasi keranjang transaksi multi-atribut (<em>multi-attribute predicate basket</em>) yang terstruktur tanpa menimbulkan aturan asosiasi semu (<em>spurious/trivial rules</em>)?</li>
  <li>Bagaimana menerapkan algoritma <em>Frequent Pattern Growth</em> (FP-Growth) untuk mengekstraksi kaidah asosiasi yang menghubungkan model motor, varian warna, lembaga pembiayaan (<em>leasing</em>), tenor angsuran, dan wilayah domisili konsumen?</li>
  <li>Bagaimana menguji validitas dan kekuatan kaidah asosiasi yang terbentuk menggunakan evaluasi tiga metrik (<em>Support</em>, <em>Confidence</em>, dan <em>Lift Ratio</em> &gt; 1.0)?</li>
  <li>Bagaimana merumuskan rekomendasi strategi bisnis terapan (<em>smart sales script</em>, program promo bersama leasing, dan manajemen stok wilayah) berdasarkan kaidah asosiasi yang valid?</li>
</ol>

<p class="no-indent"><strong>B. Celah Penelitian (Research Gap):</strong></p>
<ul>
  <li><strong>Kesenjangan Domain (Domain Gap):</strong> Riset aturan asosiasi di industri kendaraan bermotor selama ini hampir 90% terbatas pada keranjang belanja onderdil/suku cadang bernilai murah (<em>low-ticket spare parts</em>) atau jasa servis berkala. Belum ada penelitian yang menambang pola keterkaitan transaksi penjualan unit baru sepeda motor pada dealer resmi.</li>
  <li><strong>Kesenjangan Dimensi Finansial (Product-Finance Integration Gap):</strong> Dalam literatur data mining perbankan dan multifinance, variabel pembiayaan konsumen (kredit, leasing, tenor) hampir selalu diteliti menggunakan algoritma klasifikasi risiko gagal bayar (<em>credit scoring/risk modeling</em> seperti C4.5, Naive Bayes, atau Regresi Logistik). Belum ada penelitian di jurnal terakreditasi yang memodelkan skema leasing dan durasi tenor sebagai dimensi preferensi komersial yang berasosiasi langsung dengan atribut fisik unit kendaraan.</li>
  <li><strong>Kesenjangan Metodologis (Multi-Attribute Structure Gap):</strong> Mayoritas riset asosiasi masih bertumpu pada <em>single-attribute itemset</em> (Item A &rarr; Item B). Penelitian yang mengintegrasikan 5 dimensi atribut heterogen (Model Kendaraan, Warna, Lembaga Leasing, Tenor Cicilan, dan Domisili) ke dalam struktur pohon <em>FP-Tree</em> pada data skala <em>enterprise</em> masih sangat langka.</li>
</ul>

<h2>1.4 KEBARUAN (NOVELTY) & SOLUSI YANG DITAWARKAN</h2>
<p class="no-indent"><strong>A. Kebaruan Penelitian (Scientific Novelty):</strong></p>
<ol>
  <li><strong>Kebaruan Metodologis (Multi-Attribute Predicate Itemset Transformation):</strong> Mengembangkan kerangka kerja transformasi data faktur penjualan tunggal menjadi entitas <em>predicate transaction basket</em> multidimensi. Metode ini secara sistematis memetakan atribut kategorikal heterogen ke dalam format biner terindeks, sehingga algoritma FP-Growth dapat mengekstrak kaidah asosiasi lintas-dimensi tanpa menghasilkan aturan absurd seperti {Mio} &rarr; {NMAX} (karena satu faktur fisik hanya membeli 1 unit motor).</li>
  <li><strong>Kebaruan Integrasi Domain (Product-Finance Association Modeling):</strong> Menjadi penelitian pionir yang menjembatani karakteristik fisik produk bernilai tinggi (<em>high-involvement durable goods</em>) dengan preferensi instrumen pembiayaan konsumen (<em>multifinance structure</em>). Pendekatan ini memperlakukan skema kredit (BAF, Adira, OTO, Cash) dan rentang tenor (11, 23, 30, 35 bulan) sebagai bagian integral dari pola perilaku keputusan pembelian konsumen.</li>
  <li><strong>Kebaruan Preskriptif-Manajerial (Actionable Business Intelligence):</strong> Menghasilkan kaidah asosiasi yang ditransformasikan secara langsung menjadi solusi preskriptif manajerial tingkat operasional, meliputi:
    <ul>
      <li>Penyusunan panduan penjualan cerdas (<em>Smart Sales Script</em>) bagi tenaga penjual counter dealer.</li>
      <li>Perumusan program promosi bersama dealer dan lembaga pembiayaan (<em>Joint Multifinance Bundling Campaign</em>).</li>
      <li>Rekomendasi alokasi kuota unit dan varian warna per wilayah cabang pemasaran.</li>
    </ul>
  </li>
</ol>

<p class="no-indent"><strong>B. Solusi yang Ditawarkan:</strong></p>
<p>Solusi yang ditawarkan dalam penelitian ini adalah mengimplementasikan algoritma FP-Growth berbasis kerangka kerja standar <em>Cross-Industry Standard Process for Data Mining</em> (CRISP-DM) yang dievaluasi secara ketat menggunakan metrik <em>Support</em>, <em>Confidence</em>, dan <em>Lift Ratio</em> (Lift &gt; 1.0) untuk menjamin bahwa seluruh aturan yang dihasilkan merepresentasikan dependensi korelasi positif murni dan bukan kejadian acak (<em>co-occurrence by chance</em>).</p>

<h2>1.5 RUANG LINGKUP PENELITIAN (SCOPE & LIMITATIONS)</h2>
<p class="no-indent">Untuk menjaga fokus penelitian dan menjamin kedalaman analisis, ruang lingkup dan batasan penelitian ditetapkan sebagai berikut:</p>
<ol>
  <li><strong>Objek Penelitian:</strong> Penelitian dilakukan pada <strong>PT. Sinar Surya Matahari (SSM Motor)</strong>, dealer resmi sepeda motor Yamaha (Layanan 3S: <em>Sales, Service, Sparepart</em>).</li>
  <li><strong>Sumber dan Volume Data:</strong> Dataset yang digunakan adalah data transaksi riil penjualan unit sepeda motor baru bersumber dari basis data <em>Dealer Management System</em> (DMS) internal perusahaan sebanyak <strong>3.113 catatan transaksi empiris</strong>.</li>
  <li><strong>Periode Waktu Data:</strong> Data transaksi mencakup rentang waktu operasional aktif triwulan ketiga, yaitu <strong>bulan Juni hingga Agustus 2026</strong>.</li>
  <li><strong>Variabel dan Atribut Penelitian:</strong> Penelitian dibatasi pada 5 (lima) dimensi atribut transaksi utama, yaitu:
    <ul>
      <li><em>Model / Tipe Sepeda Motor:</em> Kategori Matic Premium (NMAX Series, Aerox Series, XMAX), Matic Classy (Fazzio Hybrid, Grand Filano Hybrid), Matic Standar/Entry (Mio M3, Gear 125), serta segmen Sport dan Moped.</li>
      <li><em>Varian Warna Kendaraan:</em> Karakteristik visual unit (Matte Black, Metallic Red, Cyan, Silver, White, dll.).</li>
      <li><em>Lembaga Pembiayaan (Financing Method):</em> Metode pembayaran Tunai (CASH) dan Lembaga Pembiayaan Kredit (BAF, ADIRA Finance, OTO Multiartha).</li>
      <li><em>Tenor Pembiayaan:</em> Durasi angsuran kredit konsumen (11 bulan, 23 bulan, 30 bulan, dan 35 bulan).</li>
      <li><em>Wilayah Domisili Konsumen:</em> Lokasi administratif pembeli pada cakupan wilayah pemasaran dealer (Jabodetabek: Jakarta Timur, Jakarta Selatan, Jakarta Barat, Bekasi Kota, Bekasi Kabupaten, Depok, Bogor, Tangerang).</li>
    </ul>
  </li>
  <li><strong>Batasan Algoritma & Pengujian:</strong> Algoritma yang digunakan adalah <strong>Frequent Pattern Growth (FP-Growth)</strong>. Evaluasi aturan asosiasi dibatasi pada aturan yang memenuhi nilai ambang batas minimum yang ditentukan (<em>Minimum Support & Confidence</em>) serta wajib memiliki nilai <strong>Lift Ratio &gt; 1.0</strong>.</li>
</ol>

<h2>1.6 TUJUAN PENELITIAN (RESEARCH OBJECTIVES)</h2>
<p class="no-indent">Tujuan yang ingin dicapai melalui pelaksanaan penelitian ini adalah:</p>
<ol>
  <li><strong>Tujuan Metodologis:</strong> Menerapkan dan menguji performa algoritma FP-Growth dalam mengekstraksi aturan asosiasi dari dataset transaksi penjualan multi-atribut (<em>Multi-Attribute Association Rule Mining</em>) pada data transaksional skala korporasi dealer sepeda motor.</li>
  <li><strong>Tujuan Eksploratif & Analitis:</strong> Mengidentifikasi pola kombinasi dan keterkaitan yang kuat antara tipe model sepeda motor, varian warna, lembaga pembiayaan (<em>multifinance</em>), durasi tenor kredit, dan wilayah domisili pembeli berdasarkan 3.113 transaksi riil PT. Sinar Surya Matahari.</li>
  <li><strong>Tujuan Evaluatif:</strong> Menganalisis dan memvalidasi kekuatan kaidah asosiasi yang terbentuk berdasarkan standar pengujian <em>Support</em>, <em>Confidence</em>, dan <em>Lift Ratio</em> (Lift &gt; 1.0) guna memastikan aturan yang diekstrak memiliki signifikansi statistik yang valid.</li>
  <li><strong>Tujuan Terapan & Manajerial:</strong> Menghasilkan rekomendasi strategis berbasis data (<em>data-driven strategic recommendations</em>) bagi manajemen PT. Sinar Surya Matahari berupa panduan skrip penjualan terarah (<em>Smart Sales Script</em>), formulasi paket promosi kredit gabungan, serta optimalisasi distribusi stok unit antar-wilayah guna meningkatkan efisiensi operasional dan meminimalkan tingkat kegagalan penjualan (<em>lost sales</em>).</li>
  <li><strong>Tujuan Luaran Ilmiah:</strong> Menghasilkan artikel ilmiah berkualitas standar publikasi pada <strong>Jurnal Nasional Terakreditasi SINTA (SINTA 2 / SINTA 3 / SINTA 4)</strong> atau Prosiding Seminar Nasional di bidang Sistem Informasi dan Ilmu Komputer.</li>
</ol>

<div class="footer-note">
  Dokumen Tugas Bab I Pendahuluan — Mata Kuliah Penelitian Sistem Informasi (UBSI Semester 5) — Kelompok 1
</div>

</body>
</html>
"""

    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Temporary HTML written to:", temp_html_path)
    
    browsers = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'
    ]
    
    browser_exe = None
    for b in browsers:
        if os.path.exists(b):
            browser_exe = b
            break
            
    if not browser_exe:
        print("Error: No browser found!")
        return False
        
    cmd = [
        browser_exe,
        '--headless=new',
        '--disable-gpu',
        f'--print-to-pdf={output_pdf_path}',
        '--no-pdf-header-footer',
        temp_html_path
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(output_pdf_path) and os.path.getsize(output_pdf_path) > 1000:
        print(f"[SUCCESS] Clean Academic PDF created: {output_pdf_path} ({os.path.getsize(output_pdf_path):,} bytes)")
        if os.path.exists(temp_html_path):
            os.remove(temp_html_path)
        return True
    else:
        print("Failed to generate PDF. Return code:", res.returncode)
        return False

if __name__ == '__main__':
    generate_bab1_pdf()
