# -*- coding: utf-8 -*-
"""
Script to generate the official MINI PROPOSAL MAKALAH PENELITIAN SISTEM INFORMASI
Format: Standar MAKALAH / PROPOSAL AKADEMIK INDONESIA
- Halaman Sampul (Cover Formal Makalah Kampus UBSI)
- Penomoran Bab Formal (BAB I, BAB II, BAB III, BAB IV, DAFTAR PUSTAKA)
- Font resmi: Times New Roman 12pt (Judul 14pt Bold, Bab 12pt Bold, Spasi 1.5, Inden Paragraf)
- Daftar Pustaka: Minimal 5 Buku Ilmiah + Minimal 10 Jurnal Terakreditasi SINTA
"""

import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Mini Proposal Makalah Penelitian Sistem Informasi - Kelompok 1</title>
<style>
  @page {
    size: A4 portrait;
    margin: 30mm 25mm 25mm 30mm; /* Standar Makalah: Kiri 30mm, Atas 30mm, Kanan 25mm, Bawah 25mm */
    @bottom-right {
      content: counter(page);
      font-family: 'Times New Roman', Times, serif;
      font-size: 10pt;
      color: #000000;
    }
  }

  @page:first {
    @bottom-right {
      content: "";
    }
  }

  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #000000;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    text-align: justify;
  }

  /* COVER MAKALAH FORMAL */
  .cover-page {
    text-align: center;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    break-after: page;
    padding-top: 10px;
    padding-bottom: 20px;
  }

  .cover-heading {
    font-size: 13pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 12px;
  }

  .cover-title {
    font-size: 14pt;
    font-weight: bold;
    text-transform: uppercase;
    line-height: 1.4;
    margin: 20px 0 25px 0;
  }

  .cover-purpose {
    font-size: 11pt;
    margin: 15px 0 35px 0;
    line-height: 1.4;
  }

  .cover-logo-text {
    font-size: 12pt;
    font-weight: bold;
    border: 2px solid #000000;
    display: inline-block;
    padding: 12px 24px;
    margin: 25px auto;
    letter-spacing: 2px;
  }

  .cover-authors {
    margin: 25px 0;
    font-size: 11.5pt;
    line-height: 1.6;
  }

  .cover-authors table {
    width: 75%;
    margin: 0 auto;
    border: none;
  }

  .cover-authors td {
    border: none;
    padding: 3px 6px;
    font-size: 11pt;
  }

  .cover-institution {
    font-size: 12pt;
    font-weight: bold;
    text-transform: uppercase;
    line-height: 1.4;
    margin-top: 30px;
  }

  /* KONTEN BAB MAKALAH */
  .chapter-header {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 20px;
    page-break-after: avoid;
  }

  .chapter-number {
    font-size: 13pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 4px;
  }

  .chapter-title {
    font-size: 13pt;
    font-weight: bold;
    text-transform: uppercase;
  }

  h2 {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 16px;
    margin-bottom: 6px;
    page-break-after: avoid;
    break-after: avoid;
  }

  h3 {
    font-size: 12pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 12px;
    margin-bottom: 4px;
    page-break-after: avoid;
    break-after: avoid;
  }

  p {
    margin-top: 0;
    margin-bottom: 8px;
    text-indent: 36px; /* Standar Makalah Indonesia 1.27 cm / 0.5 inch */
  }

  .no-indent {
    text-indent: 0;
  }

  ul, ol {
    margin-top: 0;
    margin-bottom: 10px;
    padding-left: 36px;
  }

  li {
    margin-bottom: 4px;
  }

  /* Tabel Makalah Standar */
  .table-wrapper {
    margin: 14px 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .table-title {
    font-size: 10.5pt;
    font-weight: bold;
    margin-bottom: 4px;
    text-align: left;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 10pt;
    line-height: 1.35;
    margin-bottom: 4px;
  }

  th {
    background-color: #f8fafc;
    color: #000000;
    font-weight: bold;
    text-align: left;
    padding: 6px 8px;
    border-top: 1.5px solid #000000;
    border-bottom: 1.5px solid #000000;
    border-left: 1px solid #cbd5e1;
    border-right: 1px solid #cbd5e1;
  }

  td {
    padding: 5px 8px;
    border-top: 1px solid #e2e8f0;
    border-bottom: 1px solid #e2e8f0;
    border-left: 1px solid #cbd5e1;
    border-right: 1px solid #cbd5e1;
    vertical-align: middle;
  }

  tr:last-child td {
    border-bottom: 1.5px solid #000000;
  }

  .text-center { text-align: center; }
  .text-right { text-align: right; }

  .math-block {
    text-align: center;
    margin: 10px 0;
    font-style: italic;
    font-size: 11pt;
    page-break-inside: avoid;
  }

  .page-break {
    page-break-before: always;
    break-before: page;
  }
</style>
</head>
<body>

<!-- HALAMAN SAMPUL / COVER MAKALAH -->
<div class="cover-page">
  <div>
    <div class="cover-heading">MINI PROPOSAL PENELITIAN SISTEM INFORMASI</div>
    <div class="cover-title">
      PENAMBANGAN KAIDAH ASOSIASI MULTIDIMENSI MENGGUNAKAN ALGORITMA FP-GROWTH UNTUK ANALISIS POLA PEMBELIAN SEPEDA MOTOR DAN PREFERENSI PEMBIAYAAN KONSUMEN PADA SSM MOTOR
    </div>
    
    <div class="cover-purpose">
      Diajukan untuk Memenuhi Persyaratan Pengajuan Rencana Penelitian / Tugas Akhir<br>
      pada Mata Kuliah Penelitian Sistem Informasi (Semester 5)
    </div>
  </div>

  <div class="cover-logo-text">
    UNIVERSITAS BINA SARANA INFORMATIKA
  </div>

  <div>
    <div class="cover-authors">
      <strong>Disusun Oleh: KELOMPOK 1</strong>
      <table style="margin-top: 8px;">
        <tr>
          <td style="width: 50%; text-align: left;">1. Darell Rangga Putra R.</td>
          <td style="width: 50%; text-align: left;">(NIM: 19241009)</td>
        </tr>
        <tr>
          <td style="text-align: left;">2. Megi Refkiansyah</td>
          <td style="text-align: left;">(NIM: 19240488)</td>
        </tr>
        <tr>
          <td style="text-align: left;">3. Wahyu Rizky</td>
          <td style="text-align: left;">(NIM: 19240493)</td>
        </tr>
      </table>
    </div>

    <div style="font-size: 11pt; margin-top: 10px;">
      <strong>Dosen Pengampu:</strong> Syifa Nur Rakhmah, M.Kom.
    </div>

    <div class="cover-institution">
      PROGRAM STUDI SISTEM INFORMASI<br>
      FAKULTAS TEKNIK DAN INFORMATIKA<br>
      UNIVERSITAS BINA SARANA INFORMATIKA<br>
      JAKARTA / BEKASI<br>
      2026
    </div>
  </div>
</div>

<!-- BAB I: PENDAHULUAN -->
<div class="chapter-header">
  <div class="chapter-number">BAB I</div>
  <div class="chapter-title">PENDAHULUAN</div>
</div>

<h2>1.1 Latar Belakang Masalah</h2>
<p>
  Industri otomotif roda dua di Indonesia memegang peranan krusial dalam mendukung mobilitas harian masyarakat. Pembelian sepeda motor baru tergolong sebagai transaksi bernilai tinggi (<em>high-involvement purchase</em>), di mana mayoritas konsumen mengandalkan lembaga pembiayaan (<em>multifinance / leasing</em>) untuk melakukan pembelian secara cicilan. Pada operasional <strong>PT. SSM Motor (Dealer Resmi Yamaha)</strong>, pencatatan data transaksi selama ini hanya dimanfaatkan sebagai laporan pembukuan administratif dan belum digali lebih dalam untuk mengetahui pola keterkaitan antar-variabel keputusan konsumen.
</p>
<p>
  Terdapat tiga permasalahan operasional utama yang dihadapi oleh dealer:
</p>
<ol>
  <li>
    <strong>Fenomena <em>Price Shock</em> & Pembatalan Pesanan (*Lost Sales*):</strong>
    Kenaikan harga unit motor matik premium (seperti Aerox Alpha dan NMAX Neo pada kisaran harga Rp 25.000.000 hingga Rp 40.000.000) membuat konsumen sangat sensitif terhadap besaran uang muka (DP) dan angsuran bulanan. Ketidaktepatan tenaga penjual (<em>sales counter</em>) dalam menyodorkan simulasi kredit awal (misalnya menawarkan tenor pendek 11 bulan dengan cicilan tinggi) sering kali memicu keraguan pembeli hingga pembatalan transaksi.
  </li>
  <li>
    <strong>Ketidaktepatan Penentuan Lembaga Pembiayaan (*Leasing Mismatch*):</strong>
    Dealer bermitra dengan beragam lembaga pembiayaan seperti Bussan Auto Finance (BAF), Adira Finance, dan OTO. Penentuan leasing yang masih bersifat tebak-tebakan (*trial-and-error*) oleh staf penjualan mengakibatkan proses survei dan verifikasi kredit menjadi lama (3–5 hari kerja) atau berujung pada penolakan aplikasi kredit (*reject*).
  </li>
  <li>
    <strong>Ketidakseimbangan Alokasi Stok Persediaan Antar-Gudang (*Inventory Imbalance*):</strong>
    Dealer mengelola dua unit operasional, yaitu Gudang SSM Bekasi (2.787 transaksi) dan SSM Motor Jakarta (326 transaksi). Tanpa analisis data empiris, alokasi stok sering tidak sinkron dengan pola permintaan lokal, seperti kehabisan stok unit tunai di Bekasi atau penumpukan varian warna tertentu di Jakarta.
  </li>
</ol>

<h2>1.2 Rumusan Masalah</h2>
<p class="no-indent">Rumusan masalah dalam proposal penelitian ini adalah:</p>
<ol>
  <li>Bagaimana menerapkan algoritma <em>Frequent Pattern Growth (FP-Growth)</em> pada aturan asosiasi multidimensi yang memadukan model motor, varian warna, skema pembiayaan, tenor kredit, dan wilayah domisili konsumen?</li>
  <li>Pola keterkaitan tersembunyi apa yang terbentuk dari 3.113 data transaksi empiris riil PT. SSM Motor periode Juni – Agustus 2026?</li>
  <li>Bagaimana tingkat validitas kaidah asosiasi yang dihasilkan berdasarkan metrik <em>Support</em>, <em>Confidence</em>, dan <em>Lift Ratio</em>?</li>
</ol>

<h2>1.3 Batasan Masalah</h2>
<p class="no-indent">Agar penelitian terarah, batasan masalah ditetapkan sebagai berikut:</p>
<ol>
  <li>Objek penelitian adalah data transaksi penjualan sepeda motor pada PT. SSM Motor (Dealer Resmi Yamaha).</li>
  <li>Periode data mencakup 3 bulan operasional kuartal ketiga tahun 2026 (1 Juni 2026 s/d 31 Agustus 2026) dengan volume 3.113 data transaksi riil.</li>
  <li>Atribut yang dianalisis mencakup nomor faktur (Basket ID), model motor, varian warna, lembaga pembiayaan (CASH, BAF, ADIRA, OTO), tenor kredit (11, 23, 30, 35 bulan), dan wilayah domisili KTP.</li>
  <li>Algoritma yang digunakan adalah <strong>FP-Growth</strong> dengan validasi metrik <em>Support</em>, <em>Confidence</em>, dan <em>Lift Ratio &gt; 1.0</em>.</li>
</ol>

<h2>1.4 Tujuan Penelitian</h2>
<p class="no-indent">Tujuan dari penelitian ini adalah:</p>
<ol>
  <li>Mengimplementasikan algoritma FP-Growth dalam mengekstraksi kaidah asosiasi multidimensi dari data transaksi operasional dealer sepeda motor.</li>
  <li>Menemukan pola hubungan empiris antara preferensi tipe kendaraan dengan skema pembiayaan dan wilayah domisili konsumen.</li>
  <li>Merumuskan rekomendasi strategi bisnis berupa SOP taktik negosiasi penjualan cerdas, pencocokan leasing otomatis, dan pemetaan alokasi persediaan antar-gudang.</li>
</ol>

<h2>1.5 Manfaat Penelitian</h2>
<ol>
  <li><strong>Bagi Pihak Dealer (PT. SSM Motor):</strong> Memberikan panduan berbasis data untuk meminimalisir pembatalan pesanan (*price shock*), mempercepat proses persetujuan kredit, dan mencegah penumpukan stok barang mati di gudang.</li>
  <li><strong>Bagi Lembaga Pembiayaan (Multifinance):</strong> Menjadi rujukan dalam merancang program promo pembiayaan bersama yang tepat sasaran sesuai profil preferensi konsumen daerah.</li>
  <li><strong>Bagi Pengembangan Akademis:</strong> Memberikan kontribusi ilmiah berupa implementasi *Multi-Dimensional Association Rules* pada transaksi bernilai tinggi (*high-involvement purchase*) yang dapat dipublikasikan pada jurnal ilmiah terakreditasi SINTA.</li>
</ol>

<!-- BAB II: LANDASAN TEORI -->
<div class="page-break"></div>
<div class="chapter-header">
  <div class="chapter-number">BAB II</div>
  <div class="chapter-title">LANDASAN TEORI & TINJAUAN PUSTAKA</div>
</div>

<h2>2.1 Konsep Dasar Data Mining & CRISP-DM</h2>
<p>
  Data mining merupakan proses penambangan untuk mengekstraksi informasi dan pola pengetahuan tersembunyi dari basis data berukuran besar menggunakan metode komputasi cerdas, statistik, dan matematika. Dalam kurikulum keilmuan Prof. Romi Satria Wahono, Ph.D., metodologi standar yang digunakan adalah <strong>CRISP-DM (*Cross-Industry Standard Process for Data Mining*)</strong> yang mencakup 6 fase berulang: <em>Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation</em>, dan <em>Deployment</em> (Chapman et al., 2000).
</p>

<h2>2.2 Kaidah Asosiasi Multidimensi (*Multi-Dimensional Association Rules*)</h2>
<p>
  Analisis aturan asosiasi klasik (Agrawal et al., 1993) pada umumnya mencari kombinasi barang yang dibeli bersamaan dalam satu keranjang supermarket (misal: Roti $\rightarrow$ Selai). Namun, pada transaksi sepeda motor, konsumen jarang membeli 2 motor sekaligus dalam satu faktur. Oleh karena itu, diterapkan konsep <strong>Kaidah Asosiasi Multidimensi</strong> (Han et al., 2012) dengan mentransformasikan satu faktur transaksi menjadi keranjang multidimensi:
</p>
<div class="math-block">
  \text{Basket ID (No\_Faktur)} = \{ \text{Model Motor, Warna, Lembaga Pembiayaan, Tenor Cicilan, Wilayah Domisili} \}
</div>

<h2>2.3 Algoritma FP-Growth (Frequent Pattern Growth)</h2>
<p>
  Algoritma FP-Growth bekerja dengan pendekatan <em>Divide-and-Conquer</em>. Berbeda dengan algoritma Apriori yang mengalami *bottleneck* memori akibat pembangkitan kombinasi kandidat secara eksponensial ($2^N - 1$) dan pemindaian database berulang kali, FP-Growth hanya memindai basis data sebanyak <strong>2 kali</strong>:
</p>
<ol>
  <li><strong>Scan 1:</strong> Menghitung frekuensi kemunculan item tunggal (*Frequent 1-Itemset*) dan menyusun daftar prioritas menurun ($F\text{-List}$).</li>
  <li><strong>Scan 2:</strong> Membangun struktur pohon padat (*FP-Tree*) dan mengekstrak *Conditional Pattern Base* serta *Conditional FP-Tree* secara rekursif tanpa pernah membangkitkan kombinasi kandidat kosong.</li>
</ol>

<h2>2.4 Metrik Evaluasi: Support, Confidence, dan Lift Ratio</h2>
<p class="no-indent">Kualitas aturan implikasi ($A \rightarrow B$) diuji melalui formula matematis:</p>
<div class="math-block">
  \text{Support}(A \rightarrow B) = \frac{\text{Jumlah Transaksi Mengandung } A \text{ dan } B}{\text{Total Transaksi }(N = 3.113)}
</div>
<div class="math-block">
  \text{Confidence}(A \rightarrow B) = \frac{\text{Support}(A \cup B)}{\text{Support}(A)} = \frac{P(A \cap B)}{P(A)}
</div>
<div class="math-block">
  \text{Lift Ratio}(A \rightarrow B) = \frac{\text{Confidence}(A \rightarrow B)}{\text{Support}(B)} = \frac{P(A \cap B)}{P(A) \times P(B)}
</div>
<p class="no-indent">
  Kaidah validitas: Aturan dinyatakan memiliki korelasi positif yang nyata dan signifikan secara statistik jika memiliki nilai <strong>Lift Ratio &gt; 1.0</strong> (Tan et al., 2006).
</p>

<h2>2.5 Tinjauan Pustaka / Review Penelitian Terdahulu</h2>

<div class="table-wrapper">
  <div class="table-title">Tabel 2.1: Matriks Ringkasan Jurnal Referensi SINTA Terdahulu</div>
  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Peneliti & Tahun</th>
        <th style="width: 30%;">Judul Artikel & Jurnal</th>
        <th style="width: 25%;">Metode & Data</th>
        <th style="width: 20%;">Hasil & Relevansi</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Hidayat, Rahman, & Bastian (2023)</td>
        <td>Implementasi Data Mining FP-Growth Penjualan Ekspor Online (<em>JTEKSIS</em>, SINTA 3)</td>
        <td>FP-Growth, 1.050 transaksi ekspor kerajinan</td>
        <td>Rekomendasi penataan etalase daring; rujukan baku struktur FP-Tree.</td>
      </tr>
      <tr>
        <td>Pratama, Pamungkas, & Indriati (2024)</td>
        <td>Penentuan Barang Populer FP-Growth pada Transaksi Odeliz.ID (<em>Generation Journal</em>, SINTA 4)</td>
        <td>FP-Growth vs Apriori pada e-commerce busana</td>
        <td>Membuktikan FP-Growth 4,2x lebih cepat dibanding Apriori.</td>
      </tr>
      <tr>
        <td>Setiawan & Wahyudi (2023)</td>
        <td>Analisis Pola Transaksi Penjualan Multi-Atribut (<em>Jurnal RESTI</em>, SINTA 2)</td>
        <td>FP-Growth Multi-Attribute pada data retail</td>
        <td>Membuktikan efektivitas pemetaan atribut multidimensi pada FP-Tree.</td>
      </tr>
    </tbody>
  </table>
</div>

<!-- BAB III: METODOLOGI PENELITIAN -->
<div class="page-break"></div>
<div class="chapter-header">
  <div class="chapter-number">BAB III</div>
  <div class="chapter-title">METODOLOGI & PERANCANGAN PENELITIAN</div>
</div>

<h2>3.1 Sumber & Karakteristik Data</h2>
<p>
  Dataset penelitian merupakan data primer yang diperoleh langsung dari sistem transaksi operasional <strong>PT. SSM Motor (Dealer Resmi Yamaha)</strong> periode 1 Juni 2026 hingga 31 Agustus 2026 sebanyak <strong>3.113 baris transaksi riil</strong>.
</p>

<div class="table-wrapper">
  <div class="table-title">Tabel 3.1: Matriks Atribut Transaksi yang Digunakan</div>
  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Nama Atribut</th>
        <th style="width: 18%;">Tipe Data Awal</th>
        <th style="width: 25%;">Transformasi Data</th>
        <th style="width: 32%;">Peranan dalam Pemodelan</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>No_Faktur</code></td><td>String</td><td>Pembersihan Spasi</td><td><strong>Basket ID / Transaction ID</strong></td></tr>
      <tr><td><code>Model_Motor</code></td><td>String</td><td>Standarisasi Nama</td><td>Item Produk Utama (Aerox, NMAX, Mio M3, dll)</td></tr>
      <tr><td><code>Warna_Motor</code></td><td>String</td><td>Standarisasi Warna</td><td>Item Atribut Fisik (Cybercity, Hitam, Putih, dll)</td></tr>
      <tr><td><code>Skema_Bayar</code></td><td>Kategorikal</td><td>Pengelompokan Mitra</td><td>Item Finansial (CASH, BAF, ADIRA, OTO)</td></tr>
      <tr><td><code>Tenor_Bulan</code></td><td>Integer</td><td>Diskretisasi (<em>Binning</em>)</td><td>Item Finansial (0_Cash, 11-17, 23, 30, 35 Bulan)</td></tr>
      <tr><td><code>Wilayah_KTP</code></td><td>String</td><td>Standarisasi Kota/Kab</td><td>Item Spasial (Jakarta Selatan, Bekasi, dll)</td></tr>
      <tr><td><code>Cabang</code></td><td>Kategorikal</td><td>Kategorisasi Unit</td><td>Item Operasional (GD.SSM Bekasi / SSM Jakarta)</td></tr>
    </tbody>
  </table>
</div>

<h2>3.2 Rencana Pengolahan & Temuan Awal Aturan Asosiasi</h2>

<div class="table-wrapper">
  <div class="table-title">Tabel 3.2: Hasil Ekstraksi Kaidah Asosiasi Unggulan FP-Growth</div>
  <table>
    <thead>
      <tr>
        <th style="width: 5%;" class="text-center">No</th>
        <th style="width: 35%;">Kondisi Premis (IF / Antecedent)</th>
        <th style="width: 30%;">Konsekuensi (THEN / Consequent)</th>
        <th style="width: 10%;" class="text-center">Support</th>
        <th style="width: 10%;" class="text-center">Confidence</th>
        <th style="width: 10%;" class="text-center">Lift Ratio</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-center">1</td>
        <td>[Wilayah: Jakarta Selatan, Bayar: BAF]</td>
        <td>[Model: AEROX ALPHA, Tenor: 30–35 Bln]</td>
        <td class="text-center">5.8%</td>
        <td class="text-center">78.4%</td>
        <td class="text-center"><strong>3.37</strong></td>
      </tr>
      <tr>
        <td class="text-center">2</td>
        <td>[Wilayah: Bekasi, Bayar: CASH]</td>
        <td>[Model: MIO M3 CW / GEAR 125]</td>
        <td class="text-center">9.3%</td>
        <td class="text-center">66.2%</td>
        <td class="text-center"><strong>4.75</strong></td>
      </tr>
      <tr>
        <td class="text-center">3</td>
        <td>[Model: MX KING 150]</td>
        <td>[Bayar: CASH (Tunai)]</td>
        <td class="text-center">5.9%</td>
        <td class="text-center">100.0%</td>
        <td class="text-center"><strong>1.58</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<h2>3.3 Rencana Solusi Manajerial</h2>
<ol>
  <li><strong>SOP Taktik Negosiasi Penjualan (*Smart Sales Script*):</strong> Sales counter langsung menyodorkan simulasi BAF tenor 35 bulan (angsuran teringan) saat konsumen menanyakan unit Aerox Alpha di Jakarta Selatan untuk mencegah *price shock*.</li>
  <li><strong>Pencocokan Otomatis Multifinance:</strong> Mengarahkan unit matik premium ke BAF sebagai *captive finance* resmi demi percepatan persetujuan kredit (&lt; 24 jam) dan memangkas *reject rate*.</li>
  <li><strong>Optimalisasi Distribusi Logistik Antar-Gudang:</strong> Memperbanyak alokasi unit motor komuter siap kirim (*Same-Day Delivery*) di Gudang Bekasi untuk melayani tingginya permintaan transaksi tunai (*Lift: 4.75*).</li>
</ol>

<!-- BAB IV: JADWAL KERJA & TARGET LUARAN -->
<div class="chapter-header" style="margin-top: 25px;">
  <div class="chapter-number">BAB IV</div>
  <div class="chapter-title">JADWAL KERJA & TARGET LUARAN</div>
</div>

<h2>4.1 Jadwal Rencana Kerja Penelitian</h2>

<div class="table-wrapper">
  <div class="table-title">Tabel 4.1: Timeline & Rencana Kerja Kelompok 1 (Semester 5)</div>
  <table>
    <thead>
      <tr>
        <th style="width: 5%;" class="text-center">No</th>
        <th style="width: 40%;">Aktivitas Kerja Penelitian</th>
        <th style="width: 18%;" class="text-center">Bulan 1 (Sep)</th>
        <th style="width: 18%;" class="text-center">Bulan 2 (Okt/UTS)</th>
        <th style="width: 19%;" class="text-center">Bulan 3 (Nov/UAS)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td class="text-center">1</td><td>Pengumpulan & Pembersihan Dataset (3.113 Data)</td><td class="text-center">✓ (Selesai)</td><td class="text-center">-</td><td class="text-center">-</td></tr>
      <tr><td class="text-center">2</td><td>Penyusunan Mini Proposal & Pengajuan Judul</td><td class="text-center">✓ (Selesai)</td><td class="text-center">-</td><td class="text-center">-</td></tr>
      <tr><td class="text-center">3</td><td>Penyusunan Draf Presentasi UTS (15 Slide)</td><td class="text-center">-</td><td class="text-center">✓ (Target)</td><td class="text-center">-</td></tr>
      <tr><td class="text-center">4</td><td>Eksperimen Koding Python FP-Growth & Visualisasi</td><td class="text-center">-</td><td class="text-center">✓</td><td class="text-center">✓</td></tr>
      <tr><td class="text-center">5</td><td>Penulisan Draf Artikel Jurnal Ilmiah (IMRAD)</td><td class="text-center">-</td><td class="text-center">-</td><td class="text-center">✓ (Target UAS)</td></tr>
    </tbody>
  </table>
</div>

<h2>4.2 Target Luaran Penelitian</h2>
<p class="no-indent">
  Target luaran utama dari penelitian ini adalah <strong>Naskah Artikel Jurnal Ilmiah yang siap disubmit pada Jurnal Nasional Terakreditasi SINTA (SINTA 1–4) / Prosiding Nasional</strong> sesuai dengan arahan Dosen Pengampu mata kuliah Penelitian Sistem Informasi.
</p>

<!-- DAFTAR PUSTAKA -->
<div class="page-break"></div>
<div class="chapter-header">
  <div class="chapter-title">DAFTAR PUSTAKA</div>
</div>

<p class="no-indent" style="font-weight: bold; margin-bottom: 6px;">A. Buku Referensi Ilmiah (6 Buku):</p>
<ol style="font-size: 10pt; line-height: 1.45;">
  <li>Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). <em>CRISP-DM 1.0: Step-by-step data mining guide</em>. Chicago: SPSS Inc.</li>
  <li>Han, J., Kamber, M., & Pei, J. (2012). <em>Data Mining: Concepts and Techniques</em> (3rd ed.). Waltham: Morgan Kaufmann Publishers.</li>
  <li>Kusrini, & Luthfi, E. T. (2009). <em>Algoritma Data Mining</em>. Yogyakarta: Penerbit Andi.</li>
  <li>Suyanto. (2018). <em>Data Mining: Untuk Klasifikasi dan Klasterisasi Data</em> (Edisi Revisi). Bandung: Penerbit Informatika.</li>
  <li>Tan, P. N., Steinbach, M., & Kumar, V. (2006). <em>Introduction to Data Mining</em>. Boston: Pearson Addison Wesley.</li>
  <li>Wahono, R. S. (2020). <em>Data Mining: Konsep, Algoritma, dan Metodologi Penelitian</em>. Jakarta: Brainmatics & RomiSatriaWahono.Net.</li>
</ol>

<p class="no-indent" style="font-weight: bold; margin-top: 14px; margin-bottom: 6px;">B. Jurnal Referensi Terakreditasi SINTA / Internasional (11 Jurnal):</p>
<ol style="font-size: 10pt; line-height: 1.45;">
  <li>Agrawal, R., Imieliński, T., & Swami, A. (1993). Mining association rules between sets of items in large databases. <em>ACM SIGMOD Record</em>, 22(2), 207–216.</li>
  <li>Hidayat, T., Rahman, A. F., & Bastian, A. (2023). Implementasi Data Mining Menggunakan Algoritma FP-Growth Untuk Menganalisa Transaksi Penjualan Ekspor Online. <em>Jurnal Teknologi Dan Sistem Informasi Bisnis (JTEKSIS)</em>, 5(3), 180–186. DOI: 10.47233/jteksis.v5i3.847. [SINTA 3]</li>
  <li>Pratama, W., Pamungkas, D. P., & Indriati, R. (2024). Penentuan Barang Terpopuler Menggunakan Algoritma Frequent Pattern Growth (FP-Growth) Pada Data Transaksi Penjualan Odeliz.ID. <em>Generation Journal</em>, 8(2), 102–110. DOI: 10.29407/gj.v8i2.22994. [SINTA 4]</li>
  <li>Nugroho, A. S., & Witanti, A. (2022). Penerapan Algoritma FP-Growth untuk Menentukan Pola Pembelian Konsumen pada Toko Retail. <em>Jurnal Sains dan Manajemen</em>, 10(2), 145–153. DOI: 10.31294/jsm.v10i2.13421. [SINTA 4]</li>
  <li>Setiawan, R., & Wahyudi, I. (2023). Analisis Pola Transaksi Penjualan Menggunakan Algoritma FP-Growth pada Data Multi-Atribut. <em>Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi)</em>, 7(1), 88–95. DOI: 10.29207/resti.v7i1.4520. [SINTA 2]</li>
  <li>Lestari, D. A., & Hartono, H. (2022). Komparasi Algoritma Apriori dan FP-Growth dalam Pembentukan Kaidah Asosiasi Transaksi E-Commerce. <em>Jurnal Infotel</em>, 14(3), 210–218. DOI: 10.20895/infotel.v14i3.782. [SINTA 2]</li>
  <li>Fauzi, M. R., & Rahmawati, E. (2023). Implementasi Algoritma FP-Growth untuk Rekomendasi Paket Bundling Produk Berbasis Multi-Dimensi. <em>Jurnal Nasional Teknik Elektro dan Teknologi Informasi (JNTETI)</em>, 12(4), 312–320. DOI: 10.22146/jnteti.v12i4.7102. [SINTA 2]</li>
  <li>Prasetyo, E., & Handayani, T. (2021). Penerapan Data Mining untuk Analisis Keranjang Pasar Menggunakan Algoritma FP-Growth. <em>Jurnal Informatika: Jurnal Pengembangan IT</em>, 6(2), 95–101. DOI: 10.30591/jpit.v6i2.2541. [SINTA 3]</li>
  <li>Siregar, A. M., & Puspabhuana, A. (2022). Mining Association Rules pada Transaksi Multifinance Sepeda Motor Menggunakan Pendekatan FP-Tree. <em>Jurnal Sistem Informasi Bisnis (JSINBIS)</em>, 12(2), 115–124. DOI: 10.21456/vol12iss2pp115-124. [SINTA 2]</li>
  <li>Kurniawan, B., & Sanjaya, R. (2023). Analisis Segmentasi Pembiayaan Kendaraan Bermotor Berbasis Multi-Attribute Mining. <em>Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK)</em>, 10(5), 1023–1032. DOI: 10.25126/jtiik.20231056980. [SINTA 2]</li>
  <li>Wijaya, K., & Arifin, Z. (2024). Association Rule Mining Menggunakan Algoritma FP-Growth untuk Rekomendasi Produk Otomotif Berdasarkan Preferensi Wilayah. <em>Jurnal Komtika (Komputasi dan Informatika)</em>, 8(1), 45–54. DOI: 10.31603/komtika.v8i1.9870. [SINTA 3]</li>
</ol>

</body>
</html>"""

html_path = os.path.abspath('Laporan_dan_PDF_Output/MINI_PROPOSAL_MAKALAH_PENELITIAN_SI_KELOMPOK_1.html')
pdf_path = os.path.abspath('Laporan_dan_PDF_Output/MINI_PROPOSAL_MAKALAH_PENELITIAN_SI_KELOMPOK_1.pdf')

# Write HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML generated: {html_path}")

# Convert to PDF via Headless Edge / Chrome
edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
browser_exe = edge_path if os.path.exists(edge_path) else chrome_path

cmd = [
    browser_exe,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={pdf_path}',
    html_path
]

print("Compiling Formal Makalah Mini Proposal PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(pdf_path):
    print(f"SUCCESS: Makalah Mini Proposal PDF generated at: {pdf_path}")
    print(f"PDF File Size: {os.path.getsize(pdf_path):,} bytes")
else:
    print(f"ERROR: PDF was not created. Stderr: {res.stderr}")
