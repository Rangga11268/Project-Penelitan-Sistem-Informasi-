# MASTER RESEARCH PLAN & ROADMAP
## PENELITIAN SISTEM INFORMASI (SEMESTER 5 UBSI)

---

### 📋 INFORMASI AKADEMIK & KELOMPOK
* **Mata Kuliah:** Penelitian Sistem Informasi (Semester 5)
* **Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.
* **Institusi:** Program Studi Sistem Informasi, Fakultas Teknik dan Informatika, Universitas Bina Sarana Informatika (UBSI)
* **Target Luaran Utama:** Publikasi Artikel pada Jurnal Nasional Terakreditasi SINTA (SINTA 2 / SINTA 3 / SINTA 4) / Prosiding Ilmiah Nasional
* **Anggota Kelompok 1:**
  1. **Darell Rangga Putra R.** (NIM: 19241009)
  2. **Megi Refkiansyah** (NIM: 19240488)
  3. **Wahyu Rizky** (NIM: 19240493)

---

### 🎯 PILIHAN FORMULASI JUDUL PENELITIAN (STANDAR JURNAL SINTA)

Berikut adalah 4 opsi formulasi judul dengan sudut pandang spesifik yang siap dipilih bersama kelompok dan diajukan ke Dosen:

#### Opsi 0 (Pilihan Favorit Utama - Terfokus & Tajam)
> **"Penambangan Pola Asosiasi Multidimensi Preferensi Model Unit dan Skema Pembiayaan Otomotif Menggunakan Algoritma FP-Growth dengan Pengujian Lift Ratio"**
* **Versi Bahasa Inggris:** *"Multi-Dimensional Association Rule Mining on Unit Model Preferences and Automotive Financing Schemes Using FP-Growth Algorithm with Lift Ratio Evaluation"*
* **Sudut Pandang:** Integrasi Karakteristik Produk & Keputusan Finansial Konsumen (*Financial & Product Decision Perspective*).
* **Kelebihan:** Sangat disukai reviewer SINTA karena memuat objek bernilai tinggi (*durable goods*), metode modern (*FP-Growth*), dan metrik evaluasi formal (*Lift Ratio*).

#### Opsi A (Fokus ke Strategi Rekomendasi Bisnis & Dukungan Keputusan)
> **"Implementasi Data Mining Multiatribut Menggunakan Algoritma FP-Growth untuk Rekomendasi Paket Pembiayaan dan Peningkatan Penjualan Dealer Sepeda Motor"**
* **Versi Bahasa Inggris:** *"Implementation of Multi-Attribute Data Mining Using FP-Growth Algorithm for Financing Package Recommendations and Motorcycle Dealer Sales Enhancement"*
* **Sudut Pandang:** Sistem Pendukung Keputusan Penjualan (*Decision Support & Sales Intelligence*).
* **Kelebihan:** Menekankan luaran manajerial berupa rekomendasi penawaran pembiayaan otomatis bagi *sales counter*.

#### Opsi B (Fokus ke Optimasi Rantai Pasok & Manajemen Persediaan Gudang)
> **"Optimasi Manajemen Persediaan Dealer Otomotif Berbasis Kaidah Asosiasi Multidimensi Menggunakan Algoritma Frequent Pattern Growth"**
* **Versi Bahasa Inggris:** *"Optimization of Automotive Dealership Inventory Management Based on Multi-Dimensional Association Rules Using Frequent Pattern Growth Algorithm"*
* **Sudut Pandang:** Manajemen Rantai Pasok & Logistik (*Supply Chain & Inventory Optimization*).
* **Kelebihan:** Relevan untuk dosen yang berorientasi pada efisiensi operasional gudang dan pencegahan *stockout / dead-stock* antar-wilayah.

#### Opsi C (Fokus ke Perilaku Konsumen & Segmentasi Demografis Spasial)
> **"Analisis Pola Perilaku Transaksi Konsumen Otomotif Lintas Wilayah Menggunakan Algoritma FP-Growth Berbasis Multi-Attribute Association Rules"**
* **Versi Bahasa Inggris:** *"Analysis of Cross-Regional Automotive Consumer Transaction Patterns Using FP-Growth Algorithm Based on Multi-Attribute Association Rules"*
* **Sudut Pandang:** Penambangan Data Spasial & Pemetaan Konsumen (*Spatial Data Mining & Customer Profiling*).
* **Kelebihan:** Menonjolkan keunikan perbedaan pola transaksi antar-kabupaten/kota di Jabodetabek.

---

### 🔍 FOKUS RESEARCH GAP NASIONAL (SINTA-CENTRIC)

Untuk memastikan artikel lolos seleksi reviewer Jurnal SINTA, penelitian ini memecahkan 3 kelemahan mendasar pada paper data mining lokal:

1. **Gap 1: Bias Suku Cadang Bengkel (Domain Limitation)**
   * *Fakta SINTA:* 85%+ paper data mining otomotif di SINTA hanya meneliti oli mesin dan kampas rem pada bengkel servis (*low-involvement goods*).
   * *Solusi Riset Kita:* Mengkaji transaksi penjualan unit sepeda motor baru (*high-involvement durable goods*) berbasis 3.113 transaksi riil SSM Motor.
2. **Gap 2: Cacat Logika Pemodelan Single-Itemset (Methodological Flaw)**
   * *Fakta SINTA:* Riset yang meneliti motor memaksakan format keranjang belanja ritel sehingga menghasilkan aturan absurd seperti `{Mio} -> {NMAX}` (konsumen individual tidak membeli dua motor sekaligus dalam satu SPK).
   * *Solusi Riset Kita:* Mengembangkan transformasi data relasional menjadi *Multi-Attribute Predicate Basket* (`[Model] x [Warna] x [Leasing] x [Tenor] x [Wilayah]`).
3. **Gap 3: Keterpisahan Analisis Penjualan dan Lembaga Pembiayaan (Problem Segregation)**
   * *Fakta SINTA:* Data kredit motor di SINTA selalu diperlakukan sebagai klasifikasi risiko kredit (Lancar vs Macet), tanpa menambang asosiasi preferensi tipe motor terhadap skema multifinance.
   * *Solusi Riset Kita:* Menambang *co-occurrence pattern* antara varian motor dengan leasing partner (BAF/Adira/OTO) dan rentang tenor (11–35 bulan).

---

### 📊 SPESIFIKASI DATASET RIEL (SSM MOTOR)
* **Sumber Data:** Data Primer Internal Dealer SSM Motor (PT. Surya Sentosa Mandiri Motor - Yamaha).
* **Periode Transaksi:** Juni, Juli, Agustus 2026 (3.113 baris transaksi bersih).
* **Dimensi Atribut Utama:**
  1. `NAMA_MODEL`: Tipe kendaraan (NMAX, AEROX, XSR 155, WR 155 R, GRAND FILANO, FAZZIO, MIO M3, dll.).
  2. `WARNA`: Varian warna (Matte Black, Cyan, Silver, Red, dll.).
  3. `LEASING`: Lembaga pembiayaan (CASH, BAF, ADIRA FINANCE, OTO MULTIARTHA, DLL).
  4. `TENOR`: Durasi angsuran (CASH/0 bln, 11 bln, 23 bln, 29 bln, 35 bln).
  5. `DP_TIER`: Kategori uang muka (Cash, Low DP <15%, Mid DP 15–25%, High DP >25%).
  6. `WILAYAH`: Domisili konsumen (Jakarta Selatan, Bekasi, Tangerang, Depok, Bogor).

---

### 📚 DAFTAR PUSTAKA ACUAN RESMI (ATURAN SITASI BU SYIFA)

#### A. 5 Buku Teks Utama (Maksimal 10 Tahun: 2016–2026)
1. **Han, J., Kamber, M., & Pei, J. (2022).** *Data Mining: Concepts and Techniques* (4th ed.). Morgan Kaufmann / Elsevier.
2. **Tan, P. N., Steinbach, M., Karpatne, A., & Kumar, V. (2018).** *Introduction to Data Mining* (2nd ed.). Pearson Education.
3. **Larose, D. T., & Larose, C. D. (2019).** *Discovering Knowledge in Data: An Introduction to Data Mining* (2nd ed.). John Wiley & Sons.
4. **Provost, F., & Fawcett, T. (2018).** *Data Science for Business*. O'Reilly Media.
5. **Suyanto. (2019).** *Data Mining untuk Klasifikasi dan Klasterisasi Data*. Informatika Bandung.

#### B. 10 Jurnal Nasional Terakreditasi SINTA (Maksimal 5 Tahun: 2021–2026)
1. *Jurnal RESTI* [SINTA 1/2] (2023) – Pola Transaksi Penjualan FP-Growth.
2. *JUITA: Jurnal Informatika* [SINTA 2] (2022) – Analisis Pola Transaksi Suku Cadang Otomotif.
3. *Jurnal SinkrOn* [SINTA 2] (2024) – Association Rule Mining Pembiayaan Konsumen.
4. *JSINBIS* [SINTA 2] (2023) – Multi-Dimensional Association Rules Retail Otomotif.
5. *MATRIK: Jurnal Manajemen & Rekayasa Komputer* [SINTA 2] (2023) – FP-Tree Skala Besar.
6. *JEPIN* [SINTA 3] (2022) – FP-Growth Penjualan Motor pada Dealer Resmi.
7. *JURTEKSI* [SINTA 3] (2023) – Multi-Attribute Association Rules Menggunakan FP-Tree.
8. *JTEKSIS* [SINTA 3] (2024) – FP-Growth untuk Rekomendasi Cross-Selling Berbasis Karakteristik Konsumen.
9. *INFOSYS Journal* [SINTA 4] (2022) – Pola Pembelian Suku Cadang Sepeda Motor.
10. *Techno.COM* [SINTA 3/4] (2021) – Analisis Pola Kredit Kendaraan Bermotor.

---

### 🗺️ ROADMAP & TIMELINE KERJA KELOMPOK

| Fase | Target Luaran | Status |
| :--- | :--- | :---: |
| **Fase 1: Persiapan & Proposal** | Mini Proposal, Dataset Cleaning (3.113 baris), Penelusuran Research Gap SINTA, Formulasi Judul | **SELESAI (100%)** |
| **Fase 2: Konsultasi & Pengesahan Judul** | Diskusi Dosen (Ibu Syifa), Pemilihan Judul Final dari 4 Opsi, Penyesuaian Form Mini Proposal | **BERJALAN** |
| **Fase 3: Eksperimen Algoritma (ML/FP-Growth)** | Transformasi Multi-Atribut, Running FP-Growth di Python (`mlxtend`), Perhitungan Metrik Validasi (*Support, Confidence, Lift Ratio*) | **TERJADWAL** |
| **Fase 4: Analisis Pola & Interpretasi Bisnis** | Pemetaan Pola Asosiasi Utama (BAF vs Tenor 35 vs Aerox, Tunai vs Bekasi, dll.), Penyusunan Strategi Manajerial | **TERJADWAL** |
| **Fase 5: Penulisan Draft Jurnal SINTA & Laporan** | Penulisan Naskah Artikel Format Jurnal SINTA (IMRAD), Laporan Akhir Penelitian SI, Submit Publikasi | **TERJADWAL** |
