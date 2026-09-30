import os
import subprocess

def generate_pdf():
    pdf_filename = "DOKUMEN_PROPOSAL_LENGKAP_PENELITIAN_SI_PLAN_A_DAN_PLAN_B.pdf"
    output_pdf_path = os.path.abspath(os.path.join("docs", pdf_filename))
    temp_html_path = os.path.abspath(os.path.join("docs", "temp_academic_proposal.html"))
    
    html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Proposal Penelitian Sistem Informasi - Plan A & Plan B</title>
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
    line-height: 1.45;
    color: #111111;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
  }

  /* Cover Page Styling */
  .cover-page {
    text-align: center;
    padding-top: 40px;
    height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
  }

  .cover-univ {
    font-size: 14pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
    color: #000000;
  }

  .cover-faculty {
    font-size: 12pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 35px;
    color: #222222;
  }

  .cover-title-box {
    border-top: 2px solid #000000;
    border-bottom: 2px solid #000000;
    padding: 22px 10px;
    margin: 25px 0;
  }

  .cover-main-title {
    font-size: 15pt;
    font-weight: bold;
    line-height: 1.35;
    text-transform: uppercase;
    color: #000000;
    margin-bottom: 10px;
  }

  .cover-subtitle {
    font-size: 12pt;
    font-style: italic;
    color: #333333;
  }

  .cover-meta {
    margin-top: 40px;
    font-size: 11pt;
    line-height: 1.6;
    color: #111111;
  }

  .cover-meta strong {
    color: #000000;
  }

  .cover-year {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 50px;
    letter-spacing: 1px;
    color: #000000;
  }

  /* Headings */
  h1 {
    font-size: 14pt;
    font-weight: bold;
    text-transform: uppercase;
    border-bottom: 1.5px solid #111111;
    padding-bottom: 5px;
    margin-top: 30px;
    margin-bottom: 15px;
    color: #000000;
    page-break-after: avoid;
  }

  h2 {
    font-size: 12.5pt;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #111111;
    page-break-after: avoid;
  }

  h3 {
    font-size: 12pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 15px;
    margin-bottom: 8px;
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

  /* Callout / Quote Box (Monochrome Formal) */
  .quote-box {
    background-color: #f9f9f9;
    border-left: 3.5px solid #222222;
    padding: 12px 15px;
    margin: 15px 0;
    font-size: 11pt;
    line-height: 1.4;
  }

  .quote-box p {
    text-indent: 0;
    margin-bottom: 5px;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0 20px 0;
    font-size: 10.5pt;
    page-break-inside: avoid;
  }

  th, td {
    border: 1px solid #333333;
    padding: 7px 9px;
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
    margin-top: 5px;
    margin-bottom: 12px;
    padding-left: 30px;
  }

  li {
    margin-bottom: 5px;
    text-align: justify;
  }

  /* Page Break Utilities */
  .page-break {
    page-break-before: always;
  }

  .divider {
    height: 1px;
    background-color: #cccccc;
    margin: 25px 0;
  }

  .badge {
    font-weight: bold;
    display: inline-block;
    padding: 2px 6px;
    background-color: #e5e7eb;
    border: 1px solid #9ca3af;
    border-radius: 3px;
    font-size: 9pt;
  }
</style>
</head>
<body>

<!-- ================= COVER PAGE ================= -->
<div class="cover-page">
  <div>
    <div class="cover-univ">UNIVERSITAS BINA SARANA INFORMATIKA</div>
    <div class="cover-faculty">PROGRAM STUDI SISTEM INFORMASI — FAKULTAS TEKNIK & INFORMATIKA</div>
    
    <div class="cover-title-box">
      <div class="cover-main-title">DOKUMEN USULAN PENELITIAN & BUKTI NOVELTI RISET DATA MINING SISTEM INFORMASI</div>
      <div class="cover-subtitle">Penerapan Algoritma Association Rule Mining (FP-Growth) Berbasis Multi-Atribut dan Validasi Lift Ratio</div>
    </div>
  </div>

  <div class="cover-meta">
    <p class="no-indent" style="text-align: center;"><strong>Disusun sebagai Dokumen Rujukan Tugas Mata Kuliah Penelitian Sistem Informasi (Semester 5)</strong></p>
    <br>
    <table style="width: 75%; margin: 0 auto; border: none; font-size: 11pt;">
      <tr style="border: none;"><td style="border: none; width: 45%;"><strong>Mata Kuliah</strong></td><td style="border: none;">: Penelitian Sistem Informasi</td></tr>
      <tr style="border: none;"><td style="border: none;"><strong>Dosen Pengampu</strong></td><td style="border: none;">: Syifa Nur Rakhmah, M.Kom.</td></tr>
      <tr style="border: none;"><td style="border: none;"><strong>Fokus Target</strong></td><td style="border: none;">: Publikasi Jurnal Nasional Terakreditasi SINTA (SINTA 2–4)</td></tr>
      <tr style="border: none;"><td style="border: none;"><strong>Pilihan Studi Kasus</strong></td><td style="border: none;">: <strong>Plan A (SSM Motor)</strong> & <strong>Plan B (Farmasi Indonesia)</strong></td></tr>
    </table>
  </div>

  <div class="cover-year">
    JAKARTA<br>2026
  </div>
</div>

<!-- ================= RINGKASAN EKSEKUTIF ================= -->
<div class="page-break"></div>

<h1>RINGKASAN EKSEKUTIF: DUA OPSI RANCANGAN RISET (PLAN A & PLAN B)</h1>

<p>Dokumen ini disusun untuk memberikan fondasi akademis yang komprehensif, terstruktur, dan berdaya saing tinggi dalam rangka pengajuan proposal penelitian mata kuliah <em>Penelitian Sistem Informasi</em> di Universitas Bina Sarana Informatika. Untuk memastikan kelancaran proses bimbingan bersama Dosen Pengampu (Ibu Syifa Nur Rakhmah, M.Kom.), disiapkan dua opsi rencana penelitian (*Plan A* dan *Plan B*) yang keduanya telah dilengkapi dengan dataset empiris bersih, telaah kesenjangan riset (*research gap*), bukti kebaruan (*novelty*), serta formulasi judul baku berstandar SINTA.</p>

<table style="margin-top: 15px;">
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
      <td>Industri Otomotif & Lembaga Pembiayaan (*Multifinance*)</td>
      <td>Sektor Pelayanan Kesehatan & Instalasi Farmasi Apotek</td>
    </tr>
    <tr>
      <td><strong>Sifat & Sumber Data</strong></td>
      <td><strong>Data Primer Riil & Eksklusif</strong> (Dealer Resmi Yamaha SSM Motor Indonesia)</td>
      <td><strong>Data Sekunder Ilmiah Bereputasi</strong> (Mendeley Data Repository DOI: 10.17632/2ym7v78wtd.1)</td>
    </tr>
    <tr>
      <td><strong>Volume & Granularitas Data</strong></td>
      <td><strong>3.113 baris transaksi riil</strong> (Periode Juni – Agustus 2026)</td>
      <td><strong>124.450 resep multi-item</strong> (514.620 baris rincian obat riil)</td>
    </tr>
    <tr>
      <td><strong>Dimensi Multi-Atribut</strong></td>
      <td>Model/Tipe Motor + Varian Warna + Lembaga Pembiayaan (BAF/Adira/Oto/Cash) + Tenor Cicilan + Uang Muka (DP) + Wilayah Domisili</td>
      <td>Nomor Resep + Nama Obat + Bentuk Sediaan + Jenis Layanan (Rawat Jalan / Rawat Inap) + Status Resep Racikan</td>
    </tr>
    <tr>
      <td><strong>Keunggulan Utama & Novelty</strong></td>
      <td><strong>Kebaruan Sangat Unik (100%):</strong> Belum pernah ada di Google Scholar penelitian yang menghubungkan preferensi motor fisik dengan skema kredit pembiayaan via FP-Growth.</td>
      <td><strong>Skala Data Sangat Besar (Big Data):</strong> Mematahkan kelemahan paper SINTA terdahulu yang mayoritas hanya mengolah 300–800 transaksi apotek mini.</td>
    </tr>
    <tr>
      <td><strong>Actionable Business Output</strong></td>
      <td><em>Smart Sales Script</em> untuk mencegah <em>price shock</em> calon debitur dan optimasi alokasi stok unit per cabang.</td>
      <td><em>Planogram Layout</em> rak obat apotek untuk memangkas waktu racik (*dispensing lead time*) dan sinkronisasi stok obat.</td>
    </tr>
    <tr>
      <td><strong>Status Kesiapan</strong></td>
      <td><strong>Pilihan Rekomendasi #1 (Siap Diajukan)</strong></td>
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

<h2>1.2 Latar Belakang & Masalah Bisnis Nyata</h2>
<p>Industri penjualan sepeda motor di Indonesia memiliki karakteristik yang sangat unik di mana lebih dari 75% hingga 85% transaksi pembelian kendaraan roda dua dilakukan melalui skema pembiayaan konsumen (*consumer credit / leasing*). Dalam proses operasional di dealer resmi seperti SSM Motor, manajemen kerap menghadapi permasalahan strategis, antara lain:</p>
<ol>
  <li><strong>Tingginya Kegagalan Konversi Penjualan (*Price Shock / Financing Mismatch*):</strong> Banyak calon konsumen yang berminat pada model motor tertentu (misal: Maxi Series seperti NMAX atau Aerox) membatalkan transaksi karena penawaran skema angsuran atau pilihan tenor cicilan yang disodorkan oleh pramuniaga (*salesman*) tidak sesuai dengan profil daya bayar dan preferensi finansial mereka.</li>
  <li><strong>Ketidakseimbangan Alokasi Stok Unit (*Inventory Holding Cost*):</strong> Dealer seringkali menumpuk kombinasi varian warna dan tipe motor tertentu di gudang cabang yang kurang diminati oleh karakteristik demografis wilayah tersebut, sementara varian yang paling dicari justru mengalami kekosongan (*stockout*).</li>
  <li><strong>Promosi Finansial yang Belum Terarah:</strong> Kerjasama promosi antara pihak dealer dengan lembaga multifinance (seperti BAF, Adira Finance, dan OTO Multiartha) masih bersifat seragam (*one-size-fits-all*), tanpa segmentasi presisi berbasis pola transaksi historis.</li>
</ol>

<h2>1.3 Karakteristik Dataset Primer SSM Motor</h2>
<p>Penelitian ini menggunakan dataset transaksi penjualan primer yang diperoleh secara langsung dari basis data dealer resmi SSM Motor periode Juni hingga Agustus 2026. Data telah melalui tahap pembersihan (*preprocessing*) dan tersimpan rapi pada repositori proyek:</p>
<ul>
  <li><strong>Total Transaksi:</strong> 3.113 baris transaksi penjualan bersih.</li>
  <li><strong>Atribut Transaksi:</strong> Nomor Faktur Penjualan, Tanggal/Bulan Transaksi, Cabang Penjualan, Tipe/Model Motor (Matic, Maxi, Sport, Moped), Varian Warna Kendaraan, Metode Pembayaran (CASH vs KREDIT), Lembaga Pembiayaan / Multifinance (BAF, ADIRA, OTO), Tenor Angsuran (11, 23, 30, 35 Bulan), Nilai Uang Muka (DP), dan Wilayah Domisili Konsumen (Jakarta, Bogor, Depok, Tangerang, Bekasi).</li>
</ul>

<h2>1.4 Kesenjangan Riset (Research Gap) & Bukti Novelty</h2>
<p>Berdasarkan penelusuran literatur pada Google Scholar dan SINTA, riset data mining penjualan kendaraan bermotor di Indonesia selama ini memiliki kesenjangan riset (*research gap*) sebagai berikut:</p>
<table style="margin-top: 10px;">
  <thead>
    <tr>
      <th style="width: 25%;">Parameter</th>
      <th style="width: 37%;">Penelitian Terdahulu di Indonesia</th>
      <th style="width: 38%;">Kebaruan Penelitian yang Diajukan (Plan A)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Fokus Analisis</strong></td>
      <td>Hanya menganalisis transaksi suku cadang (*sparepart*) bengkel atau peramalan volume unit motor.</td>
      <td><strong>Multi-Attribute Mining Terintegrasi:</strong> Menghubungkan tipe motor + varian warna + lembaga leasing + tenor + domisili.</td>
    </tr>
    <tr>
      <td><strong>Sifat Data</strong></td>
      <td>Banyak menggunakan data sekunder publik atau data simulasi dummy.</td>
      <td><strong>Data Primer Riil (3.113 Transaksi):</strong> Data asli dealer resmi Yamaha yang belum pernah dipublikasikan.</td>
    </tr>
    <tr>
      <td><strong>Validasi Kaidah</strong></td>
      <td>Hanya menggunakan nilai Support dan Confidence standar.</td>
      <td><strong>Validasi Tri-Metrik:</strong> Wajib memenuhi nilai <strong>Lift Ratio &gt; 1.0</strong> guna menjamin korelasi positif nyata.</td>
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

<h2>2.2 Latar Belakang & Masalah Operasional Instalasi Farmasi</h2>
<p>Instalasi farmasi dan apotek rumah sakit bertanggung jawab atas peracikan dan penyerahan ribuan item obat setiap harinya. Permasalahan utama yang sering terjadi di unit farmasi meliputi:</p>
<ol>
  <li><strong>Tingginya Waktu Tunggu Pelayanan Resep (*Dispensing Lead Time*):</strong> Penumpukan antrean pasien sering terjadi akibat tata letak obat di rak penyimpanan yang tidak terorganisasi berdasarkan pola kebersamaan peresepan. Petugas apotek harus berpindah-pindah antar-lorong rak yang berjauhan untuk mengambil obat-obat yang sebenarnya selalu diresepkan bersamaan.</li>
  <li><strong>Risiko Kekosongan Obat Komplementer (*Stockout Risk*):</strong> Sering terjadi situasi di mana obat utama (misal: antibiotik serbuk injeksi) tersedia, namun cairan pelarut atau obat penyertanya habis, mengakibatkan resep tidak dapat diproses (*lost sales / delayed therapy*).</li>
</ol>

<h2>2.3 Dataset Empiris & Bukti Legalitas Ilmiah</h2>
<p>Penelitian Plan B didukung oleh dataset ilmiah terbuka berlisensi resmi <em>Creative Commons Attribution 4.0 International (CC BY 4.0)</em> yang dipublikasikan oleh peneliti Dr. Rendra Gustriansyah pada repositori bereputasi Mendeley Data:</p>
<ul>
  <li><strong>Repositori &amp; DOI:</strong> Mendeley Data ([DOI: 10.17632/2ym7v78wtd.1](https://doi.org/10.17632/2ym7v78wtd.1)).</li>
  <li><strong>Volume Data:</strong> 514.620 baris rincian transaksi penjualan, 157.668 nomor faktur resep, dan 124.450 keranjang resep multi-item (&ge; 2 obat).</li>
  <li><strong>Varian Produk:</strong> 6.878 varian obat aktif (*SKU*) mencakup layanan Rawat Jalan (RJ), Rawat Inap (RI), dan Penjualan Bebas.</li>
</ul>

<h2>2.4 Telaah 10 Paper SINTA Eksisting & Bukti Keunggulan Riset</h2>
<p>Berdasarkan penelusuran terhadap 10 paper publikasi data mining apotek/farmasi di jurnal SINTA rentang 2017–2025 (seperti pada JITET SINTA 3, KomtekInfo SINTA 4, JNKTI SINTA 4, dan Pseudocode SINTA 4), ditemukan bahwa 90% paper terdahulu hanya mengolah <strong>300 hingga 1.500 transaksi</strong> dan memperlakukan data secara <em>flat</em> tanpa pemisahan jenis layanan. Penelitian Plan B ini memiliki kebaruan mutlak dengan mengolah **>100.000 transaksi resep terstratifikasi** disertai validasi farmakoterapi medis nyata:</p>

<table style="margin-top: 10px;">
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
      <td>Terapi kombinasi Diabetes Melitus Tipe 2 (Acarbose + Gliklazid) guna mengendalikan lonjakan gula darah postprandial dan basal.</td>
      <td><strong>Penataan Berdekatan:</strong> Diletakkan berdampingan pada rak obat Endokrin/Metabolik.</td>
    </tr>
    <tr>
      <td><strong>{Spironolacton 25 mg} &rarr; {Furosemide 40 mg}</strong><br><small>Confidence: 32.28% | Lift: 17.76</small></td>
      <td><em>Dual Diuretic Therapy</em> pada pasien gagal jantung (Furosemide membuang cairan, Spironolacton mencegah hipokalemia).</td>
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

<h1>BAGIAN III: PANDUAN BIMBINGAN DOSEN & SKRIP TANYA JAWAB SIDANG</h1>

<p>Berikut adalah panduan praktis dan skrip jawaban akademik untuk merespons pertanyaan kritis Dosen Pengampu (Ibu Syifa Nur Rakhmah, M.Kom.) saat sesi bimbingan proposal atau seminar:</p>

<h2>3.1 Pertanyaan: "Apa itu Aturan Asosiasi menurut metodologi Data Mining?"</h2>
<div class="quote-box">
  <p><strong>Jawaban Rekomendasi:</strong><br>
  <em>"Aturan Asosiasi (*Association Rule Mining*) adalah salah satu dari 5 peran utama data mining yang bersifat **Unsupervised Learning**, bertujuan untuk menemukan pola keterkaitan atau kebersamaan kemunculan (*co-occurrence*) antar-atribut dalam basis data transaksional berukuran besar. Pola ini dinyatakan dalam bentuk implikasi logika: $\text{IF Antecedent } \rightarrow \text{ THEN Consequent}$, dan dievaluasi menggunakan tiga metrik baku: **Support** (frekuensi kemunculan), **Confidence** (derajat kepastian), dan **Lift Ratio** (validasi korelasi positif murni)."</em></p>
</div>

<h2>3.2 Pertanyaan: "Mengapa memilih algoritma FP-Growth dibandingkan Apriori?"</h2>
<div class="quote-box">
  <p><strong>Jawaban Rekomendasi:</strong><br>
  <em>"Algoritma FP-Growth dipilih karena jauh lebih efisien dalam hal waktu komputasi dan konsumsi memori. Algoritma Apriori klasik mengalami *bottleneck* karena harus membaca (*scan*) basis data berulang kali dan membangkitkan kombinasi kandidat ($C_k$) yang meledak secara kombinatorial. Sebaliknya, FP-Growth hanya melakukan dua kali pemindaian data (*two-pass scan*) dan memadatkan seluruh transaksi ke dalam struktur pohon **FP-Tree (*Frequent Pattern Tree*)**, sehingga penambangan pola sering dapat dilakukan secara langsung tanpa membangkitkan kandidat secara berulang."</em></p>
</div>

<h2>3.3 Pertanyaan: "Apa manfaat nyata dan kontribusi praktis dari penelitian ini?"</h2>
<div class="quote-box">
  <p><strong>Jawaban Rekomendasi:</strong><br>
  <em>"Manfaat penelitian kami terbagi menjadi dua aspek:
  <br>1. **Secara Praktis:** Mengubah tumpukan data transaksi mentah menjadi **kebijakan strategis (actionable insights)**, seperti penyusunan rekomendasi paket penjualan yang presisi (*sales script*) pada dealer motor atau pembuatan desain tata letak rak obat (*planogram*) pada apotek guna memangkas waktu pelayanan dan mencegah kekosongan stok.
  <br>2. **Secara Akademis:** Mengisi kesenjangan riset (*research gap*) di jurnal SINTA nasional dengan menyajikan model asosiasi multi-atribut berdimensi tinggi yang terbukti valid secara statistik ($\text{Lift Ratio} &gt; 1.0$) dan dapat dipertanggungjawabkan."</em></p>
</div>

<h2>3.4 Pertanyaan: "Mengapa nilai Lift Ratio sangat krusial dalam evaluasi kaidah?"</h2>
<div class="quote-box">
  <p><strong>Jawaban Rekomendasi:</strong><br>
  <em>"Nilai Support dan Confidence tinggi belum tentu mencerminkan hubungan yang benar. Jika suatu barang memang berstatus sangat laris (*top seller*), barang tersebut akan sering muncul bersama barang lain semata-mata karena faktor kebetulan (*spurious correlation*). Metrik **Lift Ratio** mengukur rasio antara frekuensi kemunculan bersama dibandingkan jika kedua barang tersebut muncul secara independen. Nilai $\text{Lift Ratio} &gt; 1.0$ adalah bukti mutlak bahwa kemunculan barang A secara nyata meningkatkan probabilitas terjadinya barang B."</em></p>
</div>

<div class="divider"></div>
<p style="text-align: center; font-size: 10pt; color: #555555;"><em>— Dokumen Akademis Resmi Mata Kuliah Penelitian Sistem Informasi UBSI Semester 5 —</em></p>

</body>
</html>
"""

    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Temporary HTML written to:", temp_html_path)
    
    # Try Chrome or Edge
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
        print("Error: No Chromium-based browser found!")
        return False
        
    print(f"Using browser: {browser_exe}")
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
        print(f"[SUCCESS] PDF successfully created: {output_pdf_path} ({os.path.getsize(output_pdf_path):,} bytes)")
        return True
    else:
        print("Failed to generate PDF. Return code:", res.returncode)
        print("Stderr:", res.stderr)
        return False

if __name__ == '__main__':
    generate_pdf()
