import os
import subprocess

def generate_clean_academic_pdf():
    pdf_filename = "DOKUMEN_PROPOSAL_LENGKAP_PENELITIAN_SI_PLAN_A_DAN_PLAN_B.pdf"
    output_pdf_path = os.path.abspath(os.path.join("docs", pdf_filename))
    temp_html_path = os.path.abspath(os.path.join("docs", "temp_academic_proposal.html"))
    
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Dokumen Usulan Tugas Penelitian Sistem Informasi - Kelompok 1</title>
<style>
  @page {
    size: A4;
    margin: 25mm 20mm 25mm 25mm;
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
  }

  /* Cover Page */
  .cover-page {
    text-align: center;
    padding-top: 20px;
    height: 92vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
  }

  .cover-univ {
    font-size: 14pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #000000;
  }

  .cover-faculty {
    font-size: 11.5pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-top: 5px;
    color: #222222;
  }

  .cover-title-box {
    border-top: 2px solid #000000;
    border-bottom: 2px solid #000000;
    padding: 20px 10px;
    margin: 30px 0;
  }

  .cover-main-title {
    font-size: 14pt;
    font-weight: bold;
    line-height: 1.4;
    text-transform: uppercase;
    color: #000000;
    margin-bottom: 10px;
  }

  .cover-subtitle {
    font-size: 11.5pt;
    font-style: italic;
    color: #333333;
  }

  .cover-meta-box {
    margin: 25px auto;
    width: 85%;
    font-size: 11pt;
    text-align: left;
  }

  .cover-meta-table {
    width: 100%;
    border-collapse: collapse;
    border: none;
    margin: 0;
  }

  .cover-meta-table td {
    border: none;
    padding: 4px 6px;
    vertical-align: top;
  }

  .cover-year {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 30px;
    letter-spacing: 1px;
    color: #000000;
  }

  /* Headings */
  h1 {
    font-size: 13.5pt;
    font-weight: bold;
    text-transform: uppercase;
    border-bottom: 1.5px solid #111111;
    padding-bottom: 5px;
    margin-top: 25px;
    margin-bottom: 12px;
    color: #000000;
    page-break-after: avoid;
  }

  h2 {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 18px;
    margin-bottom: 8px;
    color: #111111;
    page-break-after: avoid;
  }

  h3 {
    font-size: 11.5pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 14px;
    margin-bottom: 6px;
    color: #222222;
    page-break-after: avoid;
  }

  p {
    text-align: justify;
    text-justify: inter-word;
    margin-top: 0;
    margin-bottom: 10px;
    text-indent: 30px;
  }

  .no-indent {
    text-indent: 0;
  }

  /* Callout Formal Box */
  .quote-box {
    background-color: #f9f9f9;
    border-left: 3.5px solid #222222;
    padding: 12px 15px;
    margin: 12px 0 16px 0;
    font-size: 11pt;
    line-height: 1.45;
  }

  .quote-box p {
    text-indent: 0;
    margin-bottom: 5px;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0 18px 0;
    font-size: 10.5pt;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #333333;
    padding: 6px 8px;
    vertical-align: top;
    line-height: 1.35;
  }

  th {
    background-color: #f0f0f0;
    font-weight: bold;
    color: #000000;
    text-align: center;
  }

  td.center {
    text-align: center;
  }

  td.right {
    text-align: right;
  }

  /* Lists */
  ol, ul {
    margin-top: 4px;
    margin-bottom: 10px;
    padding-left: 28px;
  }

  li {
    margin-bottom: 4px;
    text-align: justify;
  }

  .page-break {
    page-break-before: always;
  }

  .divider {
    height: 1px;
    background-color: #cccccc;
    margin: 20px 0;
  }
</style>
</head>
<body>

<!-- ================= COVER PAGE ================= -->
<div class="cover-page">
  <div>
    <div class="cover-univ">UNIVERSITAS BINA SARANA INFORMATIKA</div>
    <div class="cover-faculty">FAKULTAS TEKNIK DAN INFORMATIKA — PROGRAM STUDI SISTEM INFORMASI</div>
    
    <div class="cover-title-box">
      <div class="cover-main-title">DOKUMEN PROPOSAL PENGAJUAN PENELITIAN<br>MATA KULIAH PENELITIAN SISTEM INFORMASI</div>
      <div class="cover-subtitle">Penerapan Algoritma Association Rule Mining (FP-Growth) Berbasis Multi-Atribut dan Validasi Lift Ratio untuk Target Luaran Publikasi Jurnal Nasional SINTA</div>
    </div>
  </div>

  <div class="cover-meta-box">
    <p class="no-indent" style="text-align: center; font-weight: bold; margin-bottom: 12px;">Disusun untuk Memenuhi Tugas Mata Kuliah Penelitian Sistem Informasi (Semester 5)</p>
    
    <table class="cover-meta-table">
      <tr>
        <td style="width: 32%;"><strong>Dosen Pengampu</strong></td>
        <td style="width: 3%;">:</td>
        <td><strong>Syifa Nur Rakhmah, M.Kom.</strong></td>
      </tr>
      <tr>
        <td><strong>Kelompok / Kelas</strong></td>
        <td>:</td>
        <td>Kelompok 1 / Semester 5</td>
      </tr>
      <tr>
        <td><strong>Anggota Peneliti</strong></td>
        <td>:</td>
        <td>
          1. <strong>Darell Rangga Putra R.</strong> (NIM: 19241009)<br>
          2. <strong>Megi Refkiansyah</strong> (NIM: 19240488)<br>
          3. <strong>Wahyu Rizky</strong> (NIM: 19240493)
        </td>
      </tr>
      <tr>
        <td><strong>Target Luaran Tugas</strong></td>
        <td>:</td>
        <td>Publikasi Jurnal Nasional Terakreditasi SINTA (SINTA 2–4) / Prosiding Seminar Nasional</td>
      </tr>
      <tr>
        <td><strong>Pilihan Opsi Riset</strong></td>
        <td>:</td>
        <td><strong>Plan A (Dealer Otomotif SSM Motor)</strong> &amp; <strong>Plan B (Data Transaksi Farmasi)</strong></td>
      </tr>
    </table>
  </div>

  <div class="cover-year">
    JAKARTA<br>2026
  </div>
</div>

<!-- ================= RINGKASAN EKSEKUTIF ================= -->
<div class="page-break"></div>

<h1>RINGKASAN EKSEKUTIF: DUA OPSI RANCANGAN TUGAS RISET (PLAN A &amp; PLAN B)</h1>

<p>Sesuai dengan kontrak perkuliahan mata kuliah <em>Penelitian Sistem Informasi</em> Semester 5 di Universitas Bina Sarana Informatika (UBSI), setiap kelompok mahasiswa diarahkan untuk merancang proposal penelitian terapan di bidang sistem informasi dan data mining yang memenuhi standar luaran publikasi ilmiah berkala nasional (SINTA 1–4) atau prosiding seminar nasional.</p>

<p>Untuk mengantisipasi masukan dan arahan Dosen Pengampu (Ibu Syifa Nur Rakhmah, M.Kom.) saat proses bimbingan, Kelompok 1 telah menyusun dua opsi rancangan riset yang keduanya telah dilengkapi dengan dataset empiris yang bersih, telaah kesenjangan riset (<em>research gap</em>), bukti kebaruan (<em>novelty</em>), serta formulasi judul ilmiah yang baku.</p>

<table>
  <thead>
    <tr>
      <th style="width: 22%;">Parameter Evaluasi</th>
      <th style="width: 39%;">PLAN A: DEALER SSM MOTOR (PILIHAN UTAMA)</th>
      <th style="width: 39%;">PLAN B: APOTEK FARMASI (PILIHAN CADANGAN)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sektor / Domain</strong></td>
      <td>Industri Otomotif &amp; Lembaga Pembiayaan Konsumen (<em>Multifinance</em>)</td>
      <td>Sektor Pelayanan Kesehatan &amp; Instalasi Farmasi / Apotek</td>
    </tr>
    <tr>
      <td><strong>Sifat &amp; Sumber Data</strong></td>
      <td><strong>Data Primer Riil &amp; Eksklusif</strong> (Dealer Resmi Yamaha SSM Motor Indonesia)</td>
      <td><strong>Data Sekunder Ilmiah Bereputasi</strong> (Mendeley Data Repository DOI: 10.17632/2ym7v78wtd.1)</td>
    </tr>
    <tr>
      <td><strong>Volume Data</strong></td>
      <td><strong>3.113 baris transaksi riil</strong> (Periode Juni – Agustus 2026)</td>
      <td><strong>124.450 resep multi-item</strong> (514.620 baris data obat riil)</td>
    </tr>
    <tr>
      <td><strong>Dimensi Multi-Atribut</strong></td>
      <td>Tipe Motor + Varian Warna + Lembaga Pembiayaan (BAF/Adira/Oto/Cash) + Tenor Cicilan + Uang Muka (DP) + Domisili</td>
      <td>Nomor Resep + Nama Obat + Bentuk Sediaan + Jenis Layanan (Rawat Jalan / Rawat Inap) + Status Resep Racikan</td>
    </tr>
    <tr>
      <td><strong>Nilai Kebaruan (Novelty)</strong></td>
      <td><strong>Kebaruan Unik (100%):</strong> Belum pernah ada di Google Scholar riset yang menghubungkan tipe motor fisik dengan preferensi lembaga leasing dan tenor via FP-Growth.</td>
      <td><strong>Skala Data Sangat Besar (Big Data):</strong> Mematahkan kelemahan paper SINTA terdahulu yang mayoritas hanya mengolah 300–800 transaksi apotek mini.</td>
    </tr>
    <tr>
      <td><strong>Manfaat Manajerial Nyata</strong></td>
      <td>Panduan pramuniaga cerdas (<em>smart sales script</em>) untuk mencegah kegagalan closing (<em>price shock</em>) dan optimasi alokasi stok motor antar-cabang.</td>
      <td>Perancangan tata letak rak obat (<em>planogram layout</em>) untuk memangkas waktu pelayanan resep dan sinkronisasi pengadaan obat komplementer.</td>
    </tr>
    <tr>
      <td><strong>Status Kesiapan</strong></td>
      <td><strong>Pilihan Rekomendasi Nomor 1 (Siap Diajukan)</strong></td>
      <td><strong>Pilihan Cadangan Sempurna / Plan B (Siap Diajukan)</strong></td>
    </tr>
  </tbody>
</table>

<!-- ================= BAGIAN I: PLAN A ================= -->
<div class="page-break"></div>

<h1>BAGIAN I: USULAN PENELITIAN UTAMA (PLAN A) — STUDI KASUS DEALER SSM MOTOR</h1>

<h2>1.1 Formulasi Judul Penelitian (Standar Jurnal SINTA)</h2>
<div class="quote-box">
  <p><strong>Judul Bahasa Indonesia:</strong><br>
  <em>"Penerapan Algoritma FP-Growth pada Multi-Attribute Association Rule Mining untuk Analisis Pola Pemilihan Produk Sepeda Motor dan Skema Pembiayaan Konsumen (Studi Kasus: SSM Motor)"</em></p>
  <p style="margin-top: 8px;"><strong>Judul Bahasa Inggris:</strong><br>
  <em>"Implementation of FP-Growth Algorithm in Multi-Attribute Association Rule Mining for Analyzing Motorcycle Product Selection and Consumer Financing Schemes (Case Study: SSM Motor)"</em></p>
</div>

<h2>1.2 Latar Belakang &amp; Masalah Bisnis Nyata</h2>
<p>Industri penjualan sepeda motor di Indonesia memiliki karakteristik yang khas di mana lebih dari 75% hingga 85% transaksi pembelian kendaraan roda dua dilakukan melalui fasilitas pembiayaan konsumen (<em>multifinance / leasing</em>). Dalam proses operasional harian di dealer resmi seperti SSM Motor, pihak manajemen kerap menghadapi sejumlah kendala bisnis:</p>
<ol>
  <li><strong>Tingginya Kegagalan Konversi Penjualan (<em>Price Shock &amp; Financing Mismatch</em>):</strong> Banyak calon konsumen yang berminat pada model motor tertentu (misalnya seri Maxi seperti NMAX atau Aerox) membatalkan pesanan karena penawaran skema cicilan awal atau pilihan tenor yang disodorkan oleh pramuniaga (<em>sales counter</em>) tidak sesuai dengan kemampuan finansial debitur.</li>
  <li><strong>Ketidakseimbangan Alokasi Persediaan (<em>Inventory Holding Cost</em>):</strong> Dealer kerap menumpuk kombinasi varian warna dan tipe motor tertentu di gudang cabang yang kurang diminati oleh karakteristik wilayah domisili tersebut, sementara varian yang paling diminati justru mengalami kekosongan stok (<em>stockout</em>).</li>
  <li><strong>Promosi Bersama Multifinance yang Belum Terarah:</strong> Kerjasama promo subsidi uang muka (DP) atau potongan angsuran antara pihak dealer dengan perusahaan leasing (seperti BAF, Adira, dan OTO) selama ini masih bersifat coba-coba tanpa berbasis pola data transaksi historis.</li>
</ol>

<h2>1.3 Karakteristik Dataset Primer SSM Motor</h2>
<p>Penelitian Plan A menggunakan dataset transaksi primer riil yang diperoleh secara langsung dari dealer resmi Yamaha SSM Motor periode Juni hingga Agustus 2026 yang telah melalui tahap pra-pemrosesan data (<em>preprocessing</em>):</p>
<ul>
  <li><strong>Volume Data:</strong> 3.113 baris transaksi penjualan kendaraan bersih.</li>
  <li><strong>Atribut Transaksi:</strong> Nomor Faktur Penjualan, Tanggal/Bulan Transaksi, Cabang Dealer, Model/Tipe Motor (Matic, Maxi Series, Sport, Moped), Varian Warna Kendaraan, Metode Pembayaran (CASH vs KREDIT), Lembaga Pembiayaan / Multifinance (BAF, ADIRA, OTO), Tenor Cicilan (11, 23, 30, 35 Bulan), Nilai Uang Muka (DP), dan Wilayah Domisili Konsumen (Jabodetabek).</li>
</ul>

<h2>1.4 Kesenjangan Riset (Research Gap) &amp; Bukti Kebaruan (Novelty)</h2>
<p>Berdasarkan penelusuran literatur pada Google Scholar dan SINTA, penelitian data mining penjualan motor di Indonesia selama ini memiliki keterbatasan yang diselesaikan oleh penelitian ini:</p>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Parameter</th>
      <th style="width: 37%;">Penelitian Terdahulu di Jurnal SINTA</th>
      <th style="width: 38%;">Kebaruan Penelitian yang Diajukan (Plan A)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Fokus Analisis</strong></td>
      <td>Mayoritas hanya meneliti transaksi suku cadang (<em>sparepart</em>) bengkel atau peramalan total unit motor secara global.</td>
      <td><strong>Multi-Attribute Mining Terintegrasi:</strong> Mengintegrasikan tipe motor + varian warna + lembaga leasing + tenor + domisili ke dalam satu keranjang analisis.</td>
    </tr>
    <tr>
      <td><strong>Sifat Data</strong></td>
      <td>Banyak menggunakan data sekunder publik atau data simulasi buatan.</td>
      <td><strong>Data Primer Eksklusif (3.113 Transaksi):</strong> Data asli transaksi dealer resmi Yamaha yang belum pernah dipublikasikan oleh peneliti manapun.</td>
    </tr>
    <tr>
      <td><strong>Metrik Validasi</strong></td>
      <td>Hanya menggunakan nilai Support dan Confidence standar.</td>
      <td><strong>Validasi Tri-Metrik Wajib:</strong> Mewajibkan nilai <strong>Lift Ratio &gt; 1.0</strong> untuk membuktikan korelasi positif nyata.</td>
    </tr>
  </tbody>
</table>

<!-- ================= BAGIAN II: PLAN B ================= -->
<div class="page-break"></div>

<h1>BAGIAN II: USULAN PENELITIAN CADANGAN (PLAN B) — STUDI KASUS TRANSAKSI FARMASI</h1>

<h2>2.1 Formulasi Judul Penelitian (Standar Jurnal SINTA)</h2>
<div class="quote-box">
  <p><strong>Judul Bahasa Indonesia:</strong><br>
  <em>"Optimasi Tata Letak Rak dan Manajemen Persediaan Obat Apotek Menggunakan Algoritma FP-Growth Berbasis Kaidah Asosiasi Multiatribut"</em></p>
  <p style="margin-top: 8px;"><strong>Judul Bahasa Inggris:</strong><br>
  <em>"Optimizing Pharmacy Shelf Layout and Drug Inventory Management Using Multi-Attribute Association Rule Mining via FP-Growth Algorithm"</em></p>
</div>

<h2>2.2 Latar Belakang &amp; Masalah Operasional Instalasi Farmasi</h2>
<p>Instalasi farmasi dan apotek rumah sakit bertanggung jawab atas peracikan dan penyerahan ribuan item obat setiap harinya. Masalah utama yang dihadapi oleh pihak apotek meliputi:</p>
<ol>
  <li><strong>Tingginya Waktu Tunggu Pelayanan Resep (<em>Dispensing Lead Time</em>):</strong> Penumpukan antrean pasien sering terjadi akibat tata letak rak penyimpanan obat yang tidak terorganisasi berdasarkan pola kebersamaan peresepan dokter. Petugas apotek harus bolak-balik melintasi lorong rak yang berjauhan untuk mengambil obat-obat yang selalu diresepkan bersamaan.</li>
  <li><strong>Risiko Kekosongan Stok Obat Komplementer (<em>Stockout Risk</em>):</strong> Sering terjadi situasi di mana sediaan obat utama (misal: antibiotik serbuk injeksi) tersedia, namun cairan pelarut atau obat pendampingnya habis, mengakibatkan resep tidak dapat diproses (<em>lost sales / delayed therapy</em>).</li>
</ol>

<h2>2.3 Dataset Empiris &amp; Bukti Legalitas Ilmiah</h2>
<p>Penelitian Plan B didukung oleh dataset ilmiah terbuka berlisensi resmi <em>Creative Commons Attribution 4.0 International (CC BY 4.0)</em> yang dipublikasikan oleh Dr. Rendra Gustriansyah pada repositori ilmiah bereputasi Mendeley Data:</p>
<ul>
  <li><strong>Repositori &amp; DOI Resmi:</strong> Mendeley Data (DOI: 10.17632/2ym7v78wtd.1).</li>
  <li><strong>Volume Data:</strong> 514.620 baris rincian transaksi penjualan obat, 157.668 nomor faktur resep, dan 124.450 keranjang resep multi-item (&ge; 2 obat).</li>
  <li><strong>Varian Produk:</strong> 6.878 varian obat aktif (SKU) yang mencakup layanan Rawat Jalan (RJ), Rawat Inap (RI), dan Penjualan Bebas.</li>
</ul>

<h2>2.4 Telaah 10 Paper SINTA Eksisting &amp; Bukti Keunggulan Riset</h2>
<p>Berdasarkan penelusuran terhadap 10 paper publikasi data mining apotek di jurnal SINTA rentang 2017–2025 (seperti pada JITET SINTA 3, KomtekInfo SINTA 4, JNKTI SINTA 4, dan Pseudocode SINTA 4), ditemukan bahwa 90% paper terdahulu hanya mengolah <strong>300 hingga 1.500 transaksi</strong> dan memperlakukan data secara <em>flat</em> tanpa pemisahan jenis layanan medis. Penelitian Plan B ini memiliki kebaruan mutlak dengan mengolah lebih dari <strong>100.000 transaksi resep terstratifikasi</strong> disertai validasi farmakoterapi medis:</p>

<table>
  <thead>
    <tr>
      <th style="width: 30%;">Aturan Asosiasi Terverifikasi (Rules)</th>
      <th style="width: 35%;">Rasional Medis &amp; Farmakoterapi</th>
      <th style="width: 35%;">Implikasi Operasional &amp; Tata Letak Rak</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>{Glucobay 50 mg} &rarr; {Glucodex 80 mg}</strong><br><small>Confidence: 69.38% | Lift: 46.25</small></td>
      <td>Terapi kombinasi Diabetes Melitus Tipe 2 (Acarbose + Gliklazid) untuk mengendalikan lonjakan gula darah postprandial dan basal.</td>
      <td><strong>Penataan Berdekatan:</strong> Diletakkan berdampingan pada rak obat Endokrin / Metabolik.</td>
    </tr>
    <tr>
      <td><strong>{Spironolacton 25 mg} &rarr; {Furosemide 40 mg}</strong><br><small>Confidence: 32.28% | Lift: 17.76</small></td>
      <td>Terapi <em>Dual Diuretic</em> pada pasien gagal jantung (Furosemide membuang cairan, Spironolacton mencegah hipokalemia).</td>
      <td><strong>Zona Kardiovaskular:</strong> Penempatan bersamaan pada rak jantung guna mempercepat waktu peracikan resep poli spesialis.</td>
    </tr>
    <tr>
      <td><strong>{Methylprednisolone, Osteocal} &rarr; {Allopurinol}</strong><br><small>Confidence: 79.55% | Lift: 25.28</small></td>
      <td>Rejimen terapi asam urat akut: Allopurinol (penurun asam urat) + Steroid anti-radang + Suplemen kalsium pelindung tulang.</td>
      <td><strong>Bundling Persediaan:</strong> Penataan terintegrasi pada zona Anti-inflamasi dan Suplemen Tulang.</td>
    </tr>
    <tr>
      <td><strong>{Ceftriaxone 1000 mg} &rarr; {Dextrose 5% 100ml}</strong><br><small>Confidence: 35.97% | Lift: 15.68</small></td>
      <td>Sediaan antibiotik serbuk injeksi Ceftriaxone wajib dilarutkan menggunakan cairan infus D5W sebelum diinjeksikan.</td>
      <td><strong>Sinkronisasi Stok Inap:</strong> Pengadaan sistem <em>tied replenishment</em> rasio 1:1 antara serbuk vial dan pelarut infus.</td>
    </tr>
  </tbody>
</table>

<!-- ================= BAGIAN III: PANDUAN BIMBINGAN ================= -->
<div class="page-break"></div>

<h1>BAGIAN III: PANDUAN BIMBINGAN DOSEN &amp; SKRIP TANYA JAWAB TUGAS KULIAH</h1>

<p>Berikut adalah panduan praktis dan skrip jawaban akademik untuk merespons pertanyaan kritis Dosen Pengampu (Ibu Syifa Nur Rakhmah, M.Kom.) saat sesi bimbingan proposal atau presentasi tugas kelompok:</p>

<h2>3.1 Pertanyaan: "Apa itu Aturan Asosiasi menurut metodologi Data Mining?"</h2>
<div class="quote-box">
  <p><strong>Jawaban Rekomendasi:</strong><br>
  <em>"Aturan Asosiasi (Association Rule Mining) adalah salah satu dari 5 peran utama data mining yang bersifat <strong>Unsupervised Learning</strong>, bertujuan untuk menemukan pola keterkaitan atau kebersamaan kemunculan (co-occurrence) antar-atribut dalam basis data transaksional berukuran besar. Pola ini dinyatakan dalam bentuk implikasi logika: IF Antecedent &rarr; THEN Consequent, dan dievaluasi menggunakan tiga metrik baku: <strong>Support</strong> (frekuensi kemunculan), <strong>Confidence</strong> (derajat kepastian), dan <strong>Lift Ratio</strong> (validasi korelasi positif murni)."</em></p>
</div>

<h2>3.2 Pertanyaan: "Mengapa memilih algoritma FP-Growth dibandingkan Apriori?"</h2>
<div class="quote-box">
  <p><strong>Jawaban Rekomendasi:</strong><br>
  <em>"Algoritma FP-Growth dipilih karena jauh lebih efisien dalam hal waktu komputasi dan konsumsi memori RAM. Algoritma Apriori klasik mengalami hambatan komputasi karena harus membaca basis data berulang kali dan membangkitkan kombinasi kandidat yang meledak secara kombinatorial. Sebaliknya, FP-Growth hanya melakukan dua kali pemindaian data (two-pass scan) dan memadatkan seluruh transaksi ke dalam struktur pohon <strong>FP-Tree (Frequent Pattern Tree)</strong>, sehingga penambangan pola sering dapat dilakukan secara langsung tanpa membangkitkan kandidat secara berulang."</em></p>
</div>

<h2>3.3 Pertanyaan: "Apa manfaat nyata dan kontribusi praktis dari penelitian tugas ini?"</h2>
<div class="quote-box">
  <p><strong>Jawaban Rekomendasi:</strong><br>
  <em>"Manfaat penelitian tugas kelompok kami terbagi menjadi dua aspek:
  <br>1. <strong>Secara Praktis:</strong> Mengubah tumpukan data transaksi mentah menjadi <strong>kebijakan manajerial strategis</strong>, seperti penyusunan panduan rekomendasi penjualan (smart sales script) pada dealer motor atau pembuatan desain tata letak rak obat (planogram) pada apotek guna memangkas waktu pelayanan dan mencegah kekosongan stok.
  <br>2. <strong>Secara Akademis:</strong> Memenuhi standar luaran kontrak perkuliahan dengan menyajikan model data mining multi-atribut yang terbukti valid secara statistik (Lift Ratio &gt; 1.0) dan siap dipublikasikan pada jurnal nasional terakreditasi SINTA."</em></p>
</div>

<h2>3.4 Pertanyaan: "Mengapa nilai Lift Ratio sangat krusial dalam evaluasi kaidah?"</h2>
<div class="quote-box">
  <p><strong>Jawaban Rekomendasi:</strong><br>
  <em>"Nilai Support dan Confidence yang tinggi belum tentu mencerminkan hubungan sebab-akibat yang benar. Jika suatu barang memang berstatus sangat laris (top seller), barang tersebut akan sering muncul bersama barang lain semata-mata karena faktor kebetulan (spurious correlation). Metrik <strong>Lift Ratio</strong> mengukur rasio antara frekuensi kemunculan bersama dibandingkan jika kedua barang tersebut muncul secara independen. Nilai <strong>Lift Ratio &gt; 1.0</strong> adalah bukti mutlak bahwa kemunculan barang A secara nyata meningkatkan probabilitas terjadinya barang B."</em></p>
</div>

<div class="divider"></div>
<p style="text-align: center; font-size: 10pt; color: #555555; text-indent: 0;"><em>— Dokumen Usulan Tugas Mata Kuliah Penelitian Sistem Informasi UBSI Semester 5 —</em></p>

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
    generate_clean_academic_pdf()
