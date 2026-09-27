# REPOSITORI PENELITIAN SISTEM INFORMASI (KELOMPOK 1)
**Program Studi Sistem Informasi — Fakultas Teknik dan Informatika — Universitas Bina Sarana Informatika (UBSI)**  
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5)  
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Target Luaran:** Publikasi Jurnal Nasional Terakreditasi SINTA (SINTA 1–4) / Prosiding  

---

## 👥 IDENTITAS TIM PENELITI (KELOMPOK 1)
1. **Darell Rangga Putra R.** (NIM: 19241009)
2. **Megi Refkiansyah** (NIM: 19240488)
3. **Wahyu Rizky** (NIM: 19240493)

---

## 📌 OPSI RENCANA FORMULASI JUDUL PENELITIAN (PLAN PROPOSAL)
*(Disusun sebagai draf opsi terstruktur untuk didiskusikan bersama tim dan diajukan ke Dosen Pengampu)*

### 🌟 OPSI GABUNGAN / HYBRID (Komprehensif & Menyeluruh):
> ### **"Penambangan Kaidah Asosiasi Multidimensi Menggunakan Algoritma FP-Growth untuk Analisis Pola Transaksi, Preferensi Pembiayaan, dan Optimalisasi Persediaan pada Dealer Sepeda Motor"**
> *(English: Multi-Dimensional Association Rule Mining Using FP-Growth Algorithm for Transaction Pattern Analysis, Financing Preferences, and Inventory Optimization in Motorcycle Dealership)*

---

### 🎯 3 PILIHAN SUDUT PANDANG SPESIFIK (ALTERNATIF):

| No | Sudut Pandang Riset | Usulan Judul Bahasa Indonesia & Inggris | Fokus Masalah Utama |
| :-: | :--- | :--- | :--- |
| **1** | **Finansial & Keputusan Produk** (*Financial & Product Decision*) | **"Penambangan Pola Asosiasi Multidimensi Preferensi Model Unit dan Skema Pembiayaan Otomotif Roda Dua Menggunakan Algoritma FP-Growth"**<br>*(Multi-Dimensional Association Rule Mining of Motorcycle Unit Preferences and Financing Schemes Using the FP-Growth Algorithm)* | Mencegah pembatalan beli (*price shock*) pada matik premium & mencocokkan profil kredit ke leasing secara tepat (*reducing reject rate*). |
| **2** | **Operasional & Manajemen Persediaan** (*Inventory & Supply Chain*) | **"Optimasi Manajemen Persediaan Dealer Otomotif Berbasis Aturan Asosiasi Multiatribut Menggunakan FP-Growth dan Validasi Lift Ratio"**<br>*(Optimization of Automotive Dealer Inventory Management Based on Multi-Attribute Association Rules Using FP-Growth and Lift Ratio Validation)* | Mengeliminasi risiko barang mati (*dead stock*) varian warna dan mencegah kehabisan stok (*stockout*) unit cepat laku. |
| **3** | **Perilaku Konsumen & Demografi Spasial** (*Consumer Behavior & Spatial*) | **"Analisis Pola Perilaku Transaksi Konsumen Otomotif Lintas Wilayah dan Kelompok Usia Menggunakan Frequent Pattern Growth Multidimensi"**<br>*(Analyzing Cross-Regional and Age-Cohort Transaction Behaviors in the Automotive Sector Using Multi-Dimensional Frequent Pattern Growth)* | Memetakan disparitas daya beli, preferensi adopsi teknologi mesin Hybrid vs Konvensional, dan perilaku pembelian antar-wilayah Jabodetabek. |

---

## 📊 PROFIL DATASET PENELITIAN
* **Objek Penelitian:** PT. SSM Motor (Dealer Resmi Sepeda Motor Yamaha)
* **Volume Data:** **3.113 Baris Transaksi Empiris Riil** (Periode: 1 Juni 2026 – 31 Agustus 2026 / Kuartal III 2026).
* **Atribut yang Ditambang:**
  * `No_Faktur` (Basket ID / Kunci Transaksi)
  * `Model_Sepeda_Motor` (Aerox Alpha, NMAX Neo, Mio M3, Gear 125, Grand Filano Hybrid, MX King 150, Fazzio, dll)
  * `Warna_Motor` (Cybercity, Hitam, Putih, Merah, Silver, Cyan, dll)
  * `Skema_Pembayaran_Leasing` (CASH, BAF, ADIRA, OTO, MANDIRI)
  * `Tenor_Kredit_Bulan` (0_Cash, 11-17 Bulan, 20-23 Bulan, 30-32 Bulan, 35 Bulan)
  * `Uang_Muka_DP_Rp` & `Harga_OTR_Rp`
  * `Umur_Konsumen`
  * `Wilayah_Domisili_Konsumen` (Jakarta Selatan, Bekasi, Jakarta Pusat, Jakarta Timur, Jakarta Barat, Depok, dll)
  * `Cabang_Dealer` (`GD.SSM BEKASI` & `SSM MOTOR`)

---

## 🔬 METODOLOGI & ALGORITMA PENELITIAN (CRISP-DM)
1. **Metodologi Induk:** *Cross-Industry Standard Process for Data Mining (CRISP-DM)*:
   $$\text{Business Understanding} \rightarrow \text{Data Understanding} \rightarrow \text{Data Preparation} \rightarrow \text{Modeling} \rightarrow \text{Evaluation} \rightarrow \text{Deployment}$$
2. **Algoritma Utama:** **FP-Growth (*Frequent Pattern Growth*)** dengan struktur pohon *FP-Tree* (efisiensi 2-pass scan tanpa *candidate generation*).
3. **Metrik Validasi Matematis:**
   $$\text{Support}(A \rightarrow B) = \frac{\text{Kemunculan } (A \cap B)}{N = 3.113}, \quad \text{Confidence}(A \rightarrow B) = \frac{P(A \cap B)}{P(A)}, \quad \text{Lift Ratio}(A \rightarrow B) = \frac{P(A \cap B)}{P(A) \times P(B)}$$
   *(Seluruh aturan wajib memenuhi syarat validitas: **Lift Ratio > 1.0**).*

---

## 📂 STRUKTUR DIREKTORI REPOSITORI

```
d:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Penelitian SI/
│
├── 📁 Laporan_dan_PDF_Output/           # Berkas Dokumen Output PDF & HTML Resmi
│   ├── 01_MINI_PROPOSAL_MAKALAH_PENELITIAN_SI_KELOMPOK_1.pdf  # PDF Mini Proposal Format Makalah Resmi
│   ├── 01_MINI_PROPOSAL_MAKALAH_PENELITIAN_SI_KELOMPOK_1.html # Source HTML Makalah
│   ├── 02_RENCANA_DAN_PENGUATAN_RISET_KELOMPOK_1.pdf          # PDF Rencana Strategis & Justifikasi
│   └── 02_RENCANA_DAN_PENGUATAN_RISET_KELOMPOK_1.html         # Source HTML Rencana Riset
│
├── 📁 datasets/                         # Dataset Penelitian Terstruktur
│   ├── 📁 01_DATASET_UTAMA_DIGUNAKAN/  # 3.113 Transaksi Riil Dealer SSM Motor (Juni–Agustus 2026)
│   │   ├── DATA_TRANSAKSI_SSM_MOTOR_JUN_AGST_2026_RAPI.xlsx   # File Excel Rapi 4 Sheet
│   │   ├── data_transaksi_dealer_jun_agst_2026_clean.csv      # File CSV Bersih Input Python
│   │   └── DATA JUN - AGST.xlsx                               # Sumber Mentah Asli Dealer
│   └── 📁 02_DATASET_CADANGAN_REFERENSI/
│       ├── 3_GAIKINDO_wholesales_data_janaug2026.pdf
│       ├── automobile_dataset.csv
│       └── cleaned_products.csv
│
├── 📁 docs/                             # Knowledge Base & Dokumentasi Analisis Terurut (.md)
│   ├── 01_MINI_PROPOSAL_PENGAJUAN_PENELITIAN_SI.md            # Naskah Mini Proposal Makalah
│   ├── 02_ANALISIS_DATASET_SSM_MOTOR.md                       # Profil Statistik 3.113 Data & Kamus Data
│   ├── 03_MATERI_PAK_ROMI_DATA_MINING_MASTER_GUIDE.md         # Sintesis 720+ Slide Prof. Romi Satria Wahono
│   ├── 04_REVIEW_JURNAL_REFERENSI.md                          # Review 2 Jurnal SINTA 2023–2024
│   ├── 05_BUKTI_NOVELTY_DAN_RESEARCH_GAP.md                   # Bukti Penelusuran Orisinalitas SINTA
│   ├── 06_PANDUAN_PRESENTASI_DAN_TANYA_JAWAB_DOSEN.md         # Amunisi Q&A Ujian Dosen Bu Syifa
│   └── 📁 Materi/                                             # Slide Master Data Mining Asli Pak Romi
│       ├── romi-dm-aug2020.pdf & .pptx
│       ├── romi-dm-apr2020.pdf & .pptx
│       └── romi-dm-mar2019.pptx
│
├── 📁 src/                              # Wadah Script Machine Learning & Data Mining (Python)
│   └── .gitkeep
│
├── 📁 scripts/                          # Script Generator PDF Headless Engine
│   ├── build_mini_proposal_makalah_pdf.py                     # Builder PDF Makalah Mini Proposal
│   └── build_justification_plan_pdf.py                        # Builder PDF Rencana & Penguatan
│
├── 📁 assets/                           # Media & Gambar Referensi
│   └── 📁 img/
│       └── ketentuanJurnal.jpeg                               # Foto Papan Tulis Instruksi Dosen Bu Syifa
│
├── 📄 .gitignore                        # Konfigurasi Git Ignore
├── 📄 requirements.txt                  # Daftar Dependensi Python
└── 📄 README.md                         # Navigator Utama Repositori
```

---

## 📚 DAFTAR PUSTAKA ACUAN (MIN. 5 BUKU + 10 JURNAL SINTA)
* 📖 **6 Buku Teks Utama:** Prof. Romi Satria Wahono (2020), Jiawei Han et al. (2012), Pang-Ning Tan et al. (2006), Chapman et al. (2000), Suyanto (2018), Kusrini (2009).
* 📑 **11 Jurnal Acuan:** JTEKSIS (SINTA 3), Generation Journal (SINTA 4), Jurnal RESTI (SINTA 2), JNTETI (SINTA 2), Jurnal Infotel (SINTA 2), JSINBIS (SINTA 2), JTIIK (SINTA 2), ACM SIGMOD, Jurnal Sains dan Manajemen, Jurnal Informatika, Jurnal Komtika.

---
*(Catatan: Repositori ini bersifat dinamis sebagai bagian dari pengerjaan tugas dan luaran publikasi mata kuliah Penelitian Sistem Informasi).*
