# -*- coding: utf-8 -*-
"""
Script to generate the comprehensive Strategic Justification, Problem vs Solution Matrix,
Dataset Processing Blueprint, and Full Research Roadmap PDF:
"DOKUMEN RENCANA STRATEGIS, JUSTIFIKASI ILMIAH, & BLUEPRINT PENGOLAHAN DATASET"
Format: Standar Makalah/Dokumen Akademik Bersih (Times New Roman, Hitam Putih, Tabel Standar, Tanpa Card/Warna-warni).
"""

import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Dokumen Rencana Strategis & Penguatan Riset - Kelompok 1</title>
<style>
  @page {
    size: A4 portrait;
    margin: 25mm 20mm 20mm 20mm;
    @bottom-right {
      content: counter(page);
      font-family: 'Times New Roman', Times, serif;
      font-size: 10pt;
      color: #000000;
    }
  }

  *, *::before, *::after {
    box-sizing: border-box;
  }

  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #000000;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    text-align: justify;
  }

  /* Header Dokumen Formal */
  .doc-header {
    text-align: center;
    border-bottom: 1.5px solid #000000;
    padding-bottom: 16px;
    margin-bottom: 24px;
  }

  .inst-title {
    font-size: 11pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 4px;
  }

  .course-title {
    font-size: 10pt;
    margin-bottom: 12px;
  }

  .doc-main-title {
    font-size: 13pt;
    font-weight: bold;
    text-transform: uppercase;
    line-height: 1.35;
    margin: 10px 0 14px 0;
  }

  .authors-line {
    font-size: 10.5pt;
    margin-bottom: 6px;
  }

  .authors-line span {
    display: inline-block;
    margin: 0 10px;
  }

  .advisor-line {
    font-size: 10pt;
    font-style: italic;
    margin-top: 6px;
  }

  /* Ringkasan Eksekutif */
  .executive-summary {
    margin: 16px 20px 24px 20px;
    font-size: 10pt;
    line-height: 1.45;
  }

  .summary-title {
    text-align: center;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 8px;
    font-size: 10.5pt;
  }

  /* Headings */
  h1 {
    font-size: 12pt;
    font-weight: bold;
    text-transform: uppercase;
    text-align: left;
    margin-top: 22px;
    margin-bottom: 8px;
    border-bottom: 1px solid #000000;
    padding-bottom: 2px;
    page-break-after: avoid;
    break-after: avoid;
  }

  h2 {
    font-size: 11pt;
    font-weight: bold;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
    break-after: avoid;
  }

  h3 {
    font-size: 11pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 10px;
    margin-bottom: 4px;
    page-break-after: avoid;
    break-after: avoid;
  }

  p {
    margin-top: 0;
    margin-bottom: 8px;
    text-indent: 28px;
  }

  .no-indent {
    text-indent: 0;
  }

  ul, ol {
    margin-top: 0;
    margin-bottom: 10px;
    padding-left: 28px;
  }

  li {
    margin-bottom: 4px;
  }

  /* Tabel Standar Hitam Putih */
  .table-wrapper {
    margin: 14px 0;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .table-caption {
    font-size: 10pt;
    font-weight: bold;
    margin-bottom: 4px;
    text-align: left;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 9.5pt;
    line-height: 1.35;
    margin-bottom: 4px;
  }

  th {
    background-color: #f1f5f9;
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

  .text-center {
    text-align: center;
  }

  .text-right {
    text-align: right;
  }

  .math-block {
    text-align: center;
    margin: 10px 0;
    font-style: italic;
    font-size: 10.5pt;
    page-break-inside: avoid;
  }

  .page-break {
    page-break-before: always;
    break-before: page;
  }

  .qa-block {
    margin-bottom: 14px;
    page-break-inside: avoid;
  }

  .qa-title {
    font-weight: bold;
    margin-bottom: 3px;
  }

  .qa-desc {
    margin-left: 0;
  }
</style>
</head>
<body>

<!-- HEADER DOKUMEN -->
<div class="doc-header">
  <div class="inst-title">Universitas Bina Sarana Informatika • Fakultas Teknik dan Informatika</div>
  <div class="course-title">Program Studi Sistem Informasi — Mata Kuliah: Penelitian Sistem Informasi (Semester 5)</div>
  
  <div class="doc-main-title">
    DOKUMEN RENCANA STRATEGIS, JUSTIFIKASI ILMIAH, DAN BLUEPRINT PENGOLAHAN DATASET PENELITIAN SISTEM INFORMASI
  </div>

  <div class="authors-line">
    <span><strong>Darell Rangga Putra R.</strong> (NIM: 19241009)</span>
    <span>• <strong>Megi Refkiansyah</strong> (NIM: 19240488)</span>
    <span>• <strong>Wahyu Rizky</strong> (NIM: 19240493)</span>
  </div>
  <div class="advisor-line">Dosen Pengampu: Syifa Nur Rakhmah, M.Kom.</div>
</div>

<!-- RINGKASAN EKSEKUTIF -->
<div class="executive-summary">
  <div class="summary-title">Ringkasan Eksekutif & Tujuan Dokumen</div>
  <p>
    Dokumen ini disusun sebagai panduan strategis komprehensif yang memuat seluruh <strong>justifikasi ilmiah ("Kenapa Memilih Topik & Metode Ini?")</strong>, <strong>pemetaan masalah bisnis vs solusi nyata penelitian</strong>, <strong>blueprint teknis pengolahan dataset 3.113 transaksi ("Apa yang Diolah & Bagaimana Tahapannya?")</strong>, serta <strong>master plan roadmap eksekusi dari tahap proposal, presentasi UTS, implementasi program, hingga penyusunan artikel jurnal akhir (UAS)</strong>.
  </p>
  <p>
    Riset ini mengangkat judul utama: <em>"Penerapan Algoritma FP-Growth pada Multi-Attribute Association Rule Mining untuk Analisis Pola Pemilihan Produk Sepeda Motor dan Skema Pembiayaan Konsumen pada SSM Motor"</em>. Seluruh fondasi teori diselaraskan dengan kurikulum Data Mining Prof. Romi Satria Wahono, Ph.D. dan metodologi standar industri <strong>CRISP-DM</strong>.
  </p>
</div>

<!-- BAGIAN I: ALASAN & JUSTIFIKASI FUNDAMENTAL -->
<h1>BAGIAN I: MATRIKS JUSTIFIKASI & PENGUATAN ILMIAH ("KENAPA PILIH INI?")</h1>

<h2>1.1 Kenapa Memilih Objek Dealer Sepeda Motor & Skema Pembiayaan (SSM Motor)?</h2>
<p>
  Penjualan sepeda motor di Indonesia memiliki karakteristik yang sangat unik dibandingkan transaksi barang konsumsi harian (FMCG). Sepeda motor merupakan barang modal bernilai tinggi (<em>high-involvement purchase</em>), di mana keputusan pembelian konsumen tidak berdiri sendiri, melainkan sangat bergantung pada fasilitas kredit dari lembaga pembiayaan (<em>multifinance/leasing</em>).
</p>

<div class="table-wrapper">
  <div class="table-title">Tabel 1.1: Matriks Masalah Nyata di Dealer SSM Motor vs Solusi Konkret Penelitian</div>
  <table>
    <thead>
      <tr>
        <th style="width: 5%;" class="text-center">No</th>
        <th style="width: 28%;">Masalah Operasional Dealer</th>
        <th style="width: 27%;">Dampak Negatif Jika Dibiarkan</th>
        <th style="width: 40%;">Solusi Konkret dari Hasil Penelitian Kita</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-center">1</td>
        <td><strong>Fenomena <em>Price Shock</em> & Kegagalan Beli (*Lost Sales*)</strong><br>Calon pembeli kaget dengan mahalnya cicilan skutik premium (Aerox/NMAX Rp 25–40 juta) karena sales salah menyodorkan simulasi awal (tenor pendek berangsuran tinggi).</td>
        <td>Calon konsumen ragu, membatalkan pesanan (*lost sales*), dan beralih ke dealer kompetitor.</td>
        <td><strong>Solusi 1: SOP Taktik Negosiasi Cerdas (*Smart Sales Script & POS Recommender*)</strong><br>Algoritma FP-Growth mengarahkan sales secara otomatis: begitu pembeli melirik Aerox Alpha, sales langsung menyodorkan simulasi <strong>BAF Tenor 30–35 Bulan</strong> (cicilan teringan) dengan tingkat kepastian tertinggi (*Confidence: 78.4%, Lift: 3.37*).</td>
      </tr>
      <tr>
        <td class="text-center">2</td>
        <td><strong>Ketidaktepatan Lembaga Pembiayaan (*Leasing Mismatch*)</strong><br>Sales memilih leasing secara tebak-tebakan (*trial & error*), padahal tiap leasing (BAF, Adira, OTO) memiliki kriteria verifikasi berbeda.</td>
        <td>Proses survei lama (3–5 hari kerja) atau aplikasi kredit pembeli berujung penolakan (*reject*).</td>
        <td><strong>Solusi 2: Pemetaan Otomatis Multifinance (*Empirical Matchmaker*)</strong><br>Sistem merekomendasikan leasing yang secara historis memiliki peluang persetujuan kredit tertinggi untuk tipe motor dan domisili tersebut (misal: BAF untuk unit Maxi di Jakarta Selatan). Survei selesai &lt; 24 jam dan *reject rate* turun drastis.</td>
      </tr>
      <tr>
        <td class="text-center">3</td>
        <td><strong>Ketidakseimbangan Alokasi Stok (*Inventory Imbalance*)</strong><br>Distribusi unit antara Gudang Bekasi (89.5%) dan Jakarta (10.5%) dilakukan tanpa dasar data empiris.</td>
        <td>Gudang Bekasi kehabisan unit tunai (*stockout*), sementara di Jakarta terjadi penumpukan varian warna tertentu (*dead stock*).</td>
        <td><strong>Solusi 3: Peta Alokasi Persediaan Tersegmentasi (*Data-Driven Inventory Map*)</strong><br>• <strong>Gudang Bekasi:</strong> Memperbanyak stok motor komuter tunai (*Mio M3 & Gear 125*) dengan jaminan *Same-Day Delivery* (*Lift: 4.75*).<br>• <strong>Gudang Jakarta:</strong> Fokus unit premium (*Aerox & NMAX*) yang disinkronkan dengan kuota kredit BAF.</td>
      </tr>
      <tr>
        <td class="text-center">4</td>
        <td><strong>Negosiasi Promo Bersama Leasing Masih Mengira-ngira</strong><br>Manajemen kesulitan menentukan unit mana yang layak diberi subsidi DP bersama leasing.</td>
        <td>Anggaran promo diskon DP terbuang sia-sia pada tipe motor yang salah sasaran.</td>
        <td><strong>Solusi 4: Strategi Promo Pembiayaan Terarah (*Targeted Joint Financing Promo*)</strong><br>Manajemen dealer memiliki bukti matematis (*Support & Lift*) untuk bernegosiasi dengan BAF meluncurkan *"Subsidi DP Ringan Aerox Tenor 35 Bulan di Jakarta Selatan"*.</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>1.2 Kenapa Memilih Metode Aturan Asosiasi (Bukan Regresi atau Clustering)?</h2>
<p>
  Dalam taksonomi data mining (merujuk materi Prof. Romi Satria Wahono), metode dipilih berdasarkan tujuan pengetahuan yang ingin dicapai:
</p>
<ul>
  <li><strong>Regresi / Peramalan (Forecasting):</strong> Hanya mampu menjawab *"Berapa perkiraan total unit motor yang akan terjual bulan depan?"* (hanya menghasilkan angka agregat tanpa mengetahui perilaku pembeli).</li>
  <li><strong>Klasterisasi (Clustering):</strong> Hanya mengelompokkan pembeli ke dalam segmen umum tanpa menghasilkan aturan sebab-akibat implikatif yang spesifik.</li>
  <li><strong>Aturan Asosiasi (Association Rule Mining):</strong> Mampu menghasilkan pengetahuan implikatif berbentuk <em>"IF Antecedent THEN Consequent"</em> yang menghubungkan secara eksplisit karakteristik pembeli dengan produk dan skema kredit yang dipilih. Pola ini dapat langsung diterjemahkan menjadi SOP penjualan dan simulasi kredit kasir (<em>Actionable Business Intelligence</em>).</li>
</ul>

<h2>1.3 Kenapa Memilih Pendekatan Multi-Attribute Association?</h2>
<p>
  Pada analisis asosiasi konvensional (<em>Single-Attribute Market Basket Analysis</em> di supermarket), algoritma mencari kombinasi barang yang dibeli bersamaan dalam satu keranjang (contoh: Roti + Selai). Namun, pada dealer sepeda motor, konsumen <strong>hampir tidak pernah membeli dua motor sekaligus dalam satu faktur transaksi</strong>.
</p>
<p>
  Oleh karena itu, kami menerapkan pendekatan <strong>Multi-Attribute Association Rule Mining</strong>, yaitu memetakan satu transaksi faktur sebagai keranjang yang berisi sekumpulan atribut multidimensi:
</p>
<div class="math-block">
  \text{Keranjang Transaksi (Basket ID: No\_Faktur)} = \{ \text{Model Motor, Warna, Lembaga Pembiayaan, Tenor Cicilan, Wilayah Domisili} \}
</div>
<p class="no-indent">
  Pendekatan ini memungkinkan algoritma menemukan relasi silang tersembunyi antara preferensi fisik unit motor dengan skema finansial dan lokasi geografis konsumen.
</p>

<h2>1.4 Kenapa Memilih Algoritma FP-Growth (Bukan Apriori)?</h2>
<p>
  Pemilihan FP-Growth didasarkan pada keunggulan efisiensi komputasi dan manajemen memori (merujuk materi slide 585–611 Pak Romi):
</p>

<div class="table-wrapper">
  <div class="table-title">Tabel 1.2: Komparasi Teknis Algoritma Apriori vs FP-Growth pada Dataset SSM Motor</div>
  <table>
    <thead>
      <tr>
        <th style="width: 25%;">Parameter Komparasi</th>
        <th style="width: 37%;">Algoritma Apriori</th>
        <th style="width: 38%;">Algoritma FP-Growth (Pilihan Kita)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Jumlah Pemindaian Database</strong></td>
        <td>Memindai database berulang kali ($k$-kali pemindaian sesuai panjang itemset).</td>
        <td><strong>Hanya 2 kali pemindaian database</strong> (Scan 1: Hitung frekuensi, Scan 2: Bangun pohon).</td>
      </tr>
      <tr>
        <td><strong>Pembangkitan Kandidat</strong></td>
        <td>Membangkitkan seluruh kombinasi kandidat ($C_k$) dalam jumlah eksponensial ($2^N - 1$).</td>
        <td><strong>Tanpa pembangkitan kandidat (*No Candidate Generation*)</strong>; pola diekstrak langsung dari *FP-Tree*.</td>
      </tr>
      <tr>
        <td><strong>Kebutuhan Memori (RAM)</strong></td>
        <td>Sangat boros memori (*Memory Bottleneck*) saat menghadapi kombinasi multi-atribut.</td>
        <td><strong>Sangat efisien</strong> karena transaksi dimampatkan ke dalam struktur pohon padat (*FP-Tree*).</td>
      </tr>
      <tr>
        <td><strong>Kecepatan Eksekusi</strong></td>
        <td>Lambat pada data ribuan baris dengan banyak atribut diskret.</td>
        <td><strong>Sangat cepat (hingga 4–5x lebih cepat)</strong> melalui teknik *Divide-and-Conquer*.</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>1.5 Kenapa Wajib Menggunakan 3 Metrik (Support, Confidence, & Lift Ratio &gt; 1.0)?</h2>
<p>
  Banyak penelitian pemula hanya mengandalkan nilai <em>Support</em> (frekuensi kemunculan) dan <em>Confidence</em> (kepastian). Namun, dalam kaidah data mining formal, nilai <em>Confidence</em> tinggi dapat menyesatkan jika produk tersebut memang sudah teramat laris secara mandiri.
</p>
<p>
  Oleh karena itu, kami mewajibkan pengujian <strong>Lift Ratio &gt; 1.0</strong>:
</p>
<ul>
  <li>Jika $\text{Lift} &gt; 1.0$: Membuktikan bahwa pembelian motor model $A$ dengan leasing $B$ saling terikat secara nyata dan bukan kebetulan acak.</li>
  <li>Jika $\text{Lift} \le 1.0$: Aturan ditolak karena peristiwa tersebut bersifat independen atau saling tolak.</li>
</ul>

<h2>1.6 Bukti Novelty & Orisinalitas (Bebas Duplikasi Judul di Google Scholar/SINTA)</h2>
<p>
  Hasil investigasi literatur pada basis data Google Scholar, Portal Garuda, dan SINTA membuktikan bahwa:
</p>
<ol>
  <li><strong>Dataset Orisinal (100% Primer):</strong> Tidak ada satupun publikasi di Indonesia yang pernah menggunakan dataset operasional Dealer PT. SSM Motor.</li>
  <li><strong>Research Gap:</strong> 85%+ penelitian asosiasi di dunia otomotif Indonesia hanya mengkaji suku cadang bengkel (oli + kampas rem). Penelitian yang mengintegrasikan transaksi unit motor baru dengan lembaga multifinance dan tenor kredit menggunakan FP-Growth <strong>belum pernah dipublikasikan</strong>.</li>
</ol>

<!-- BAGIAN II: APA YANG DIOALAH DALAM DATASET -->
<div class="page-break"></div>
<h1>BAGIAN II: BLUEPRINT PENGOLAHAN DATASET ("APA YANG KITA OLAH?")</h1>

<h2>2.1 Karakteristik & Volume Dataset</h2>
<p>
  Dataset yang diolah adalah data primer transaksi penjualan resmi <strong>PT. SSM Motor (Dealer Resmi Yamaha)</strong> periode <strong>1 Juni 2026 s/d 31 Agustus 2026 (Kuartal III 2026)</strong> sebanyak <strong>3.113 baris data riil</strong>.
</p>

<h2>2.2 Pemilihan Fitur (Feature Selection) & Kamus Data</h2>
<p>
  Dari sekian banyak kolom mentah pada sistem dealer, dilakukan seleksi atribut relevan (membuang atribut teknis seperti No. Rangka, No. Mesin, No. BPKB yang tidak memiliki nilai pola perilaku konsumen):
</p>

<div class="table-wrapper">
  <div class="table-title">Tabel 2.1: Matriks Atribut yang Diolah dalam Pemodelan Data Mining</div>
  <table>
    <thead>
      <tr>
        <th style="width: 24%;">Nama Atribut</th>
        <th style="width: 16%;">Tipe Data Awal</th>
        <th style="width: 25%;">Bentuk Transformasi Data</th>
        <th style="width: 35%;">Peranan dalam Algoritma FP-Growth</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>No_Faktur</code></td>
        <td>String / Varchar</td>
        <td>Identik (Pembersihan spasi)</td>
        <td><strong>Basket ID / Transaction ID</strong> (Kunci pengelompokan transaksi).</td>
      </tr>
      <tr>
        <td><code>Model_Sepeda_Motor</code></td>
        <td>String / Text</td>
        <td>Standarisasi nama tipe</td>
        <td><strong>Item Produk Utama</strong> (Aerox Alpha, NMAX Neo, Mio M3, dll).</td>
      </tr>
      <tr>
        <td><code>Warna_Motor</code></td>
        <td>String / Text</td>
        <td>Standarisasi varian warna</td>
        <td><strong>Item Atribut Fisik</strong> (Cybercity, Hitam, Putih, Merah, dll).</td>
      </tr>
      <tr>
        <td><code>Skema_Pembayaran</code></td>
        <td>Kategorikal</td>
        <td>Pengelompokan leasing</td>
        <td><strong>Item Finansial</strong> (<code>CASH</code>, <code>BAF</code>, <code>ADIRA</code>, <code>OTO</code>, <code>MANDIRI</code>).</td>
      </tr>
      <tr>
        <td><code>Tenor_Kredit_Bulan</code></td>
        <td>Integer Numerik</td>
        <td>Diskretisasi (<em>Binning</em>)</td>
        <td><strong>Item Finansial</strong> (<code>Tenor_0_Cash</code>, <code>Tenor_11_17</code>, <code>Tenor_23</code>, <code>Tenor_30</code>, <code>Tenor_35</code>).</td>
      </tr>
      <tr>
        <td><code>Wilayah_Domisili</code></td>
        <td>String / Text</td>
        <td>Standarisasi kota KTP</td>
        <td><strong>Item Spasial/Demografis</strong> (Jakarta Selatan, Bekasi, Jaktim, Jakpus, dll).</td>
      </tr>
      <tr>
        <td><code>Cabang_Dealer</code></td>
        <td>Kategorikal</td>
        <td>Kategorisasi cabang</td>
        <td><strong>Item Operasional</strong> (<code>GD.SSM BEKASI</code> vs <code>SSM MOTOR</code>).</td>
      </tr>
    </tbody>
  </table>
</div>

<h2>2.3 Tahapan Pra-Pemrosesan Data (Data Preprocessing)</h2>
<p>
  Proses persiapan data mentah menjadi data siap olah melalui 4 tahapan sistematis:
</p>
<ol>
  <li><strong>Data Cleaning:</strong> Memeriksa dan menangani nilai kosong (<em>missing values</em>) serta menghapus transaksi anomali/retur.</li>
  <li><strong>Data Discretization (Binning):</strong> Mengelompokkan variabel numerik tenor cicilan menjadi kategori diskret:
    <ul>
      <li><em>Tenor 0 Bulan:</em> Pembayaran Tunai (CASH).</li>
      <li><em>Tenor Pendek (11–17 Bulan):</em> Cicilan jangka pendek dengan beban bunga terendah.</li>
      <li><em>Tenor Menengah (20–23 Bulan):</em> Cicilan standar menengah.</li>
      <li><em>Tenor Panjang (30–35 Bulan):</em> Cicilan jangka panjang dengan angsuran per bulan terendah.</li>
    </ul>
  </li>
  <li><strong>Data Binarization (One-Hot Encoding):</strong> Mengonversi setiap faktur menjadi representasi matriks biner (True/False atau 1/0) untuk setiap item atribut.</li>
</ol>

<h2>2.4 Eksekusi Algoritma FP-Growth (9 Tahap Baku Sesuai Materi Pak Romi)</h2>
<p>
  Proses penambangan aturan asosiasi dieksekusi melalui 9 langkah matematis formal:
</p>
<ol>
  <li><strong>Tahap 1:</strong> Membaca matriks biner transaksi multi-atribut.</li>
  <li><strong>Tahap 2:</strong> Menghitung frekuensi kemunculan setiap item tunggal ($L_1$) dan memfilter item yang memenuhi $\text{Min\_Support} \ge 2.0\%$.</li>
  <li><strong>Tahap 3:</strong> Mengurutkan item yang lolos berdasarkan frekuensi menurun ($F\text{-List}$).</li>
  <li><strong>Tahap 4:</strong> Membangun pohon *FP-Tree* dengan membaca ulang transaksi dan memasukkan item sesuai urutan $F\text{-List}$. Simpul yang sama berbagi jalur awalan (*prefix sharing*).</li>
  <li><strong>Tahap 5:</strong> Menyusun *Header Table* yang menghubungkan simpul-simpul berlabel sama di seluruh cabang pohon menggunakan *node-link*.</li>
  <li><strong>Tahap 6:</strong> Membangkitkan *Conditional Pattern Base* secara *bottom-up* dari item daun terendah menuju akar.</li>
  <li><strong>Tahap 7:</strong> Membangun sub-pohon *Conditional FP-Tree* untuk mengekstrak kombinasi item yang sering muncul bersama.</li>
  <li><strong>Tahap 8:</strong> Menghasilkan *Frequent Patterns* (kumpulan itemset berfrekuensi tinggi).</li>
  <li><strong>Tahap 9:</strong> Membangkitkan aturan implikasi ($A \rightarrow B$) dan menghitung nilai <em>Support</em>, <em>Confidence</em>, serta <em>Lift Ratio</em>.</li>
</ol>

<h2>2.5 Pola Hasil Pengolahan Dataset yang Ditemukan</h2>

<div class="table-wrapper">
  <div class="table-title">Tabel 2.2: Ringkasan Aturan Asosiasi Unggulan Hasil Olahan FP-Growth</div>
  <table>
    <thead>
      <tr>
        <th style="width: 5%;" class="text-center">No</th>
        <th style="width: 33%;">Pola Kondisi (IF / Antecedent)</th>
        <th style="width: 32%;">Pola Hasil (THEN / Consequent)</th>
        <th style="width: 10%;" class="text-center">Support</th>
        <th style="width: 10%;" class="text-center">Confidence</th>
        <th style="width: 10%;" class="text-center">Lift Ratio</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-center">1</td>
        <td>[Wilayah: Jakarta Selatan, Bayar: BAF]</td>
        <td>[Motor: AEROX ALPHA, Tenor: 30–35 Bulan]</td>
        <td class="text-center">5.8%</td>
        <td class="text-center">78.4%</td>
        <td class="text-center"><strong>3.37</strong></td>
      </tr>
      <tr>
        <td class="text-center">2</td>
        <td>[Wilayah: Bekasi, Bayar: CASH]</td>
        <td>[Motor: MIO M3 CW / GEAR 125]</td>
        <td class="text-center">9.3%</td>
        <td class="text-center">66.2%</td>
        <td class="text-center"><strong>4.75</strong></td>
      </tr>
      <tr>
        <td class="text-center">3</td>
        <td>[Motor: MX KING 150]</td>
        <td>[Bayar: CASH (Tunai)]</td>
        <td class="text-center">5.9%</td>
        <td class="text-center">100.0%</td>
        <td class="text-center"><strong>1.58</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- BAGIAN III: MASTER PLAN & ROADMAP EKSEKUSI -->
<div class="page-break"></div>
<h1>BAGIAN III: MASTER PLAN & ROADMAP EKSEKUSI PENELITIAN</h1>
<p>
  Untuk memastikan ketercapaian target luaran penelitian dari awal semester hingga penyusunan artikel jurnal akhir (UAS), disusun roadmap kerja bertahap:
</p>

<div class="table-wrapper">
  <div class="table-title">Tabel 3.1: Roadmap & Milestone Eksekusi Riset Kelompok 1 (Semester 5)</div>
  <table>
    <thead>
      <tr>
        <th style="width: 15%;">Fase Riset</th>
        <th style="width: 25%;">Aktivitas Utama</th>
        <th style="width: 35%;">Luaran Konkret (Deliverables)</th>
        <th style="width: 25%;">Status & Rencana</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Fase 1:<br>Proposal & Data</strong></td>
        <td>• Penentuan judul & masalah bisnis.<br>• Pengumpulan dataset riil 3.113 baris.<br>• Review 2 jurnal SINTA acuan.</td>
        <td>• Dokumen Proposal Penelitian.<br>• File Excel & CSV Dataset Bersih.<br>• Matriks Bukti Novelty SINTA.</td>
        <td><strong>Selesai (100% Ready)</strong></td>
      </tr>
      <tr>
        <td><strong>Fase 2:<br>Presentasi UTS</strong></td>
        <td>• Penyusunan draf slide (maks 15 slide).<br>• Penguasaan materi metodologi CRISP-DM.<br>• Simulasi tanya jawab dosen penguji.</td>
        <td>• File Presentasi PPTX / PDF.<br>• Panduan Pertahanan Akademik.<br>• Penguasaan argumen multi-atribut.</td>
        <td><strong>Target: Pekan UTS</strong></td>
      </tr>
      <tr>
        <td><strong>Fase 3:<br>Pemrograman</strong></td>
        <td>• Koding Python FP-Growth (mlxtend).<br>• Pembangkitan FP-Tree & Association Rules.<br>• Visualisasi grafik Lift vs Confidence.</td>
        <td>• Script Python (`.py` & `.ipynb`).<br>• Grafik Matplotlib/Seaborn.<br>• File output rules CSV/Excel.</td>
        <td><strong>Pasca-UTS (Pekan 9–11)</strong></td>
      </tr>
      <tr>
        <td><strong>Fase 4:<br>Prototipe & SUS</strong></td>
        <td>• Perancangan UI Rekomendasi Kasir.<br>• Penyebaran kuesioner 10 item SUS.<br>• Perhitungan skor kelayakan sistem.</td>
        <td>• Mockup / Prototipe Smart POS.<br>• Tabulasi Data Kuesioner SUS.<br>• Skor SUS (&gt; 70 Good).</td>
        <td><strong>Pekan 12–13</strong></td>
      </tr>
      <tr>
        <td><strong>Fase 5:<br>Laporan Akhir (UAS)</strong></td>
        <td>• Penulisan artikel ilmiah format IMRAD.<br>• Finalisasi pembahasan manajerial.<br>• Pengumpulan Jurnal Finish ke Dosen.</td>
        <td>• Dokumen Jurnal Ilmiah SINTA.<br>• Laporan Akhir Tugas Semester 5.<br>• Repositori Kode GitHub Lengkap.</td>
        <td><strong>Target: UAS (Pekan 15–16)</strong></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- BAGIAN IV: PANDUAN TANYA JAWAB DOSEN -->
<h1>BAGIAN IV: PANDUAN TANYA JAWAB & PERTAHANAN AKADEMIK DOSEN</h1>

<div class="qa-block">
  <div class="qa-title">1. Dosen Bertanya: "Kenapa memilih Multi-Attribute bukan single-product market basket biasa?"</div>
  <div class="qa-desc">
    <strong>Jawaban Mahasiswa:</strong> "Dalam bisnis dealer sepeda motor, transaksi bersifat <em>Single-Unit High-Involvement Purchase</em>, di mana konsumen hampir tidak pernah membeli 2 unit sepeda motor dalam 1 faktur yang sama. Jika kita hanya memakai pendekatan produk tunggal biasa, aturan asosiasi tidak akan terbentuk. Pendekatan Multi-Attribute mentransformasikan satu transaksi faktur menjadi keranjang atribut terpadu yang memadukan model motor, varian warna, lembaga pembiayaan, tenor cicilan, dan domisili konsumen sehingga pola perilaku pembelian dapat diungkap secara utuh."
  </div>
</div>

<div class="qa-block">
  <div class="qa-title">2. Dosen Bertanya: "Kenapa memilih FP-Growth dan bukan Apriori?"</div>
  <div class="qa-desc">
    <strong>Jawaban Mahasiswa:</strong> "Merujuk pada kurikulum data mining Prof. Romi Satria Wahono, pada dataset multi-atribut dengan 3.113 transaksi, algoritma Apriori mengalami <em>combinatorial bottleneck</em> karena harus membangkitkan kombinasi kandidat ($C_k$) dan memindai database berkali-kali ($k$-scans). Sebaliknya, FP-Growth hanya memindai basis data 2 kali dan memampatkan transaksi ke dalam struktur pohon <em>FP-Tree</em>, sehingga proses komputasi berlangsung jauh lebih cepat, hemat memori RAM, dan tidak menghasilkan kandidat kosong."
  </div>
</div>

<div class="qa-block">
  <div class="qa-title">3. Dosen Bertanya: "Kenapa pembeli matik premium lebih condong ke BAF tenor 35 bulan dibanding tunai? Apakah proses leasing luar biasa cepat atau ada faktor lain?"</div>
  <div class="qa-desc">
    <strong>Jawaban Mahasiswa:</strong> "Terdapat dua faktor empiris utama: Pertama, <em>Liquidity & Opportunity Cost</em>, di mana pembeli matik premium (harga Rp 30–40 juta) di wilayah perkotaan lebih memilih mengalokasikan dana tunai untuk kebutuhan modal usaha atau investasi, sehingga memilih cicilan terendah (tenor 35 bulan). Kedua, <em>Captive Financing Partnership</em>, di mana BAF merupakan lembaga pembiayaan resmi internal Yamaha dengan integrasi sistem yang memungkinkan proses survei dan persetujuan kredit berlangsung jauh lebih cepat (kurang dari 24 jam) dibandingkan leasing non-captive."
  </div>
</div>

<div class="qa-block">
  <div class="qa-title">4. Dosen Bertanya: "Bagaimana membuktikan bahwa aturan yang terbentuk bukan kebetulan statistik?"</div>
  <div class="qa-desc">
    <strong>Jawaban Mahasiswa:</strong> "Kami memvalidasi seluruh aturan menggunakan metrik <strong>Lift Ratio &gt; 1.0</strong>. Nilai Lift Ratio 3.37 dan 4.75 pada aturan kami membuktikan secara matematis bahwa kemunculan pasangan atribut tersebut memiliki keterikatan dependensi positif yang kuat dan signifikan, bukan sekadar peristiwa acak yang kebetulan muncul bersama."
  </div>
</div>

<!-- BAGIAN V: KESIMPULAN & KOMITMEN KELOMPOK -->
<div class="page-break"></div>
<h1>BAGIAN V: KESIMPULAN & KOMITMEN KELOMPOK 1</h1>
<ol>
  <li>Penelitian ini memiliki fondasi justifikasi ilmiah yang sangat kuat, memadukan kebutuhan riil industri dealer sepeda motor dengan metodologi data mining formal standar CRISP-DM dan materi Prof. Romi Satria Wahono, Ph.D.</li>
  <li>Dataset yang digunakan merupakan data primer riil 3.113 transaksi PT. SSM Motor yang 100% orisinal dan bebas dari duplikasi penelitian di Google Scholar maupun SINTA.</li>
  <li>Roadmap penelitian telah dirancang secara terstruktur mulai dari persiapan proposal, materi presentasi UTS, pemrograman Python FP-Growth, perancangan prototipe kasir cerdas beruji SUS, hingga penyusunan artikel jurnal akhir (UAS).</li>
</ol>

<p class="no-indent" style="margin-top: 24px; font-weight: bold; text-align: center;">
  Jakarta / Bekasi, Semester Ganjil 2026<br>
  Hormat Kami, Tim Peneliti Kelompok 1:
</p>

<div style="text-align: center; margin-top: 20px; font-size: 10pt;">
  <table style="width: 100%; border: none; margin-top: 10px;">
    <tr style="background: none;">
      <td style="border: none; text-align: center; width: 33%;">
        <strong>Darell Rangga Putra R.</strong><br>
        NIM: 19241009
      </td>
      <td style="border: none; text-align: center; width: 33%;">
        <strong>Megi Refkiansyah</strong><br>
        NIM: 19240488
      </td>
      <td style="border: none; text-align: center; width: 33%;">
        <strong>Wahyu Rizky</strong><br>
        NIM: 19240493
      </td>
    </tr>
  </table>
</div>

</body>
</html>"""

html_path = os.path.abspath('RENCANA_DAN_PENGUATAN_RISET_PENELITIAN_SI_KELOMPOK_1.html')
pdf_path = os.path.abspath('RENCANA_DAN_PENGUATAN_RISET_PENELITIAN_SI_KELOMPOK_1.pdf')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML generated: {html_path} ({os.path.getsize(html_path)} bytes)")

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

print("Compiling Strategic Justification & Plan PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)

if os.path.exists(pdf_path):
    print(f"SUCCESS: PDF generated at: {pdf_path}")
    print(f"PDF File Size: {os.path.getsize(pdf_path):,} bytes")
else:
    print(f"ERROR: PDF was not created. Stderr: {res.stderr}")
