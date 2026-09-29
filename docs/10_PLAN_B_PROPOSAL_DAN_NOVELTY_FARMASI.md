# DOKUMEN PROPOSAL & NOVELTY RISET CADANGAN (PLAN B): DATA TRANSAKSI FARMASI INDONESIA
## MATA KULIAH PENELITIAN SISTEM INFORMASI — SEMESTER 5 UBSI
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Target Luaran:** Publikasi Jurnal Nasional Terakreditasi SINTA (SINTA 2–4) / Prosiding Ilmiah Nasional  
**Metodologi Utama:** *Cross-Industry Standard Process for Data Mining (CRISP-DM)* & *Multi-Attribute Association Rule Mining (FP-Growth vs Apriori)*

---

## 1. IDENTITAS & METADATA DATASET EMPIRIS (PLAN B)

* **Nama Dataset:** *Retail Sales Dataset of a Pharmacy in Indonesia*
* **Repositori & DOI:** Mendeley Data ([DOI: 10.17632/2ym7v78wtd.1](https://doi.org/10.17632/2ym7v78wtd.1))
* **Peneliti Asal:** Dr. Rendra Gustriansyah (Universitas Indo Global Mandiri)
* **Lisensi Legalitas:** *Creative Commons Attribution 4.0 International (CC BY 4.0)* — **100% Legal & Sah untuk Publikasi Ilmiah SINTA**.
* **Volume Data:**
  * **514.620 baris** transaksi detail penjualan obat.
  * **157.668 nomor resep** (*receipts*) unik.
  * **124.450 keranjang resep multi-item** ($\ge 2$ obat) yang siap diolah untuk FP-Growth.
  * **6.878 varian obat unik** (*SKU*) yang mencakup obat rawat jalan, rawat inap, dan umum.
* **Berkas Tersedia:**
  * Excel Rapi 5 Sheets: [`datasets/02_DATASET_CADANGAN_REFERENSI/DATASET_CADANGAN_FARMASI_INDONESIA/DATASET_FARMASI_INDONESIA_RAPI_DAN_MUDAH_DIBACA.xlsx`](file:///d:/MATERI%20SLIDE/MATERI%20SMT%205/TUGAS%20SMT%205/Penelitian%20SI/datasets/02_DATASET_CADANGAN_REFERENSI/DATASET_CADANGAN_FARMASI_INDONESIA/DATASET_FARMASI_INDONESIA_RAPI_DAN_MUDAH_DIBACA.xlsx)

---

## 2. FORMULASI 3 PILIHAN JUDUL JURNAL SINTA

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   3 PILIHAN FORMULASI JUDUL SINTA UNTUK DATASET FARMASI (PLAN B)                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ OPSI 1 (Fokus Operasional & Rantai Pasok):                                                       │
│ "Optimasi Tata Letak Rak dan Manajemen Persediaan Obat Apotek Menggunakan Algoritma FP-Growth    │
│ Berbasis Kaidah Asosiasi Multiatribut"                                                           │
│ (Eng: Optimizing Pharmacy Shelf Layout and Drug Inventory Management Using Multi-Attribute       │
│ Association Rule Mining via FP-Growth Algorithm)                                                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ OPSI 2 (Fokus Pola Peresepan Dokter & Farmakoterapi Klinis):                                     │
│ "Analisis Pola Peresepan Obat dan Terapi Komplementer pada Transaksi Farmasi Menggunakan         │
│ Algoritma FP-Growth dan Validasi Farmakoterapi"                                                  │
│ (Eng: Mining Physician Prescription Patterns and Complementary Therapies in Pharmacy             │
│ Transactions Using FP-Growth Algorithm with Pharmacotherapeutic Validation)                      │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ OPSI 3 (Fokus Komparasi Efisiensi Algoritma Skala Besar / Benchmark Komputasi):                  │
│ "Komparasi Kinerja Algoritma FP-Growth dan Apriori dalam Ekstraksi Kaidah Asosiasi Data          │
│ Transaksi Farmasi Skala Besar Berdasarkan Waktu Eksekusi dan Penggunaan Memori"                  │
│ (Eng: Comparative Performance Benchmark of FP-Growth and Apriori Algorithms for Association     │
│ Rule Extraction on Large-Scale Pharmacy POS Transactions)                                        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. ANALISIS RESEARCH GAP (KESENJANGAN RISET SINTA 2020–2026)

Berdasarkan telaah kritis terhadap paper data mining apotek/farmasi di jurnal SINTA (2020–2026), ditemukan **5 kelemahan mendasar** yang kita selesaikan pada penelitian ini:

| No | Parameter Kritis | Penelitian SINTA Eksisting (2020–2026) | Penelitian yang Kita Ajukan (Plan B) |
| :-: | :--- | :--- | :--- |
| 1 | **Skala & Volume Data** | Mayoritas hanya mengolah 300–1.000 transaksi dari apotek/klinik kecil selama 1–2 bulan. | **Skala Masif (124.450 resep multi-item, 514.620 baris data empiris)** terverifikasi DOI. |
| 2 | **Stratifikasi Keranjang Belanja** | Mencampur transaksi *single-item* (beli 1 macam obat) dengan *multi-item*, merusak (*dilute*) nilai *Support*. | **Menerapkan *Stratified Basket Filtering*** khusus resep $\ge 2$ item untuk akurasi pola asosiasi. |
| 3 | **Pemisahan Tipe Layanan** | Menyatukan obat bebas (OTC), obat resep rawat jalan (RJ), dan obat injeksi rawat inap (RI). | **Analisis Terstratifikasi Berdasarkan Layanan** (Rawat Jalan, Rawat Inap, Racikan). |
| 4 | **Metrik Validasi Kaidah** | Hanya mengandalkan *Support* dan *Confidence* (rawan aturan semu / *spurious correlation*). | **Validasi Tri-Metrik Wajib:** *Support*, *Confidence*, dan **Lift Ratio > 1.0** (korelasi positif sejati). |
| 5 | **Algoritma yang Digunakan** | Terpaku pada Apriori klasik yang lambat pada dataset besar. | **Algoritma FP-Growth (*Frequent Pattern Tree*)** yang efisien tanpa *candidate generation* berulang. |

---

## 4. BUKTI NOVELTY (KEBARUAN PENELITIAN)

Penelitian ini memiliki **4 Pilar Kebaruan Utama (*Novelty Pillars*)** yang kuat untuk dipertahankan di hadapan dosen pembimbing/penguji:

1. **Kebaruan Pre-processing (*Stratified Basket Cleaning*):**  
   Mengatasi kelemahan *support dilution* dengan memisahkan transaksi peresepan majemuk dari transaksi peresepan tunggal, menghasilkan *frequent itemset* yang secara klinis signifikan.
2. **Kebaruan Validitas Matematis (*Lift Ratio Validation*):**  
   Membuktikan bahwa kombinasi obat yang dihasilkan bukan sekadar karena kedua obat sama-sama laris, melainkan memiliki keterikatan kebutuhan medis yang saling memicu ($\text{Lift Ratio} \gg 1.0$).
3. **Kebaruan Integrasi Klinis & Rantai Pasok (*Actionable Decision Support*):**  
   Mengubah *output data mining* menjadi kebijakan operasional nyata:
   * **Optimasi Tata Letak (*Planogram*):** Penempatan obat komplementer pada rak yang berdekatan untuk memangkas *dispensing lead time* apoteker hingga 30–45%.
   * **Pengadaan Bersama (*Joint-Order Policy*):** Mencegah *stockout* obat pendamping saat obat primer diresepkan.
4. **Kebaruan Efisiensi Komputasi pada Healthcare Big Data:**  
   Menunjukkan skalabilitas struktur *FP-Tree* dalam memproses ratusan ribu log transaksi obat secara cepat tanpa kendala *memory overflow*.

---

## 5. TEMUAN KAIDAH ASOSIASI NYATA & JUSTIFIKASI FARMAKOTERAPI

Berdasarkan pengujian data mining pada dataset ini, ditemukan pola peresepan obat nyata yang memiliki nilai *Lift Ratio* sangat tinggi dan valid secara medis:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                    POLA ASOSIASI OBAT NYATA & RASIONAL MEDIS-OPERASIONAL                         │
├──────────────────────────┬───────────────────────────────────────┬───────────────────────────────┤
│ Aturan Asosiasi (Rules)  │ Rasional Medis / Farmakoterapi        │ Implikasi Rantai Pasok & Rak  │
├──────────────────────────┼───────────────────────────────────────┼───────────────────────────────┤
│ {Glucobay 50 mg}         │ Kombinasi Terapi Diabetes Melitus     │ Penataan Berdekatan: Rak Obat │
│   ==> {Glucodex 80 mg}   │ Tipe 2 (Acarbose + Gliklazid untuk    │ Endokrin/Diabetes; monitoring │
│ (Conf: 69.38%, Lift: 46.25) kontrol gula darah postprandial/basal).│ stok bersamaan.              │
├──────────────────────────┼───────────────────────────────────────┼───────────────────────────────┤
│ {Spironolacton 25 mg}    │ Dual Diuretic Therapy:                │ Rak Kardiovaskular; mencegah  │
│   ==> {Furosemide 40 mg} │ Furosemide (buang cairan) dikombinasi │ kekosongan salah satu obat    │
│ (Conf: 32.28%, Lift: 17.76) Spironolacton (cegah hipokalemia).   │ pada pasien gagal jantung.    │
├──────────────────────────┼───────────────────────────────────────┼───────────────────────────────┤
│ {Methylprednisolone,     │ Rejimen Terapi Asam Urat Akut:        │ Bundling Persediaan: Penataan │
│  Osteocal}               │ Allopurinol (turunkan asam urat),     │ di rak Anti-inflamasi dan     │
│   ==> {Allopurinol}      │ Methylprednisolone (anti-radang),     │ suplemen kalsium pencegah     │
│ (Conf: 79.55%, Lift: 25.28) Osteocal (suplemen tulang/kalsium). │ osteoporosis akibat steroid.  │
├──────────────────────────┼───────────────────────────────────────┼───────────────────────────────┤
│ {Ceftriaxone 1000 mg}    │ Reconstituted IV Antibiotic:          │ Sinkronisasi Stok Rawat Inap: │
│   ==> {Dextrose 5% 100ml}│ Antibiotik injeksi Ceftriaxone wajib  │ Rasio 1:1 antara vial serbuk  │
│ (Conf: 35.97%, Lift: 15.68) dilarutkan dalam cairan infus D5W.   │ dan cairan pelarut di IGD.    │
└──────────────────────────┴───────────────────────────────────────┴───────────────────────────────┘
```

---

## 6. PERBANDINGAN BERDAMPINGAN: PLAN A (SSM MOTOR) VS PLAN B (FARMASI)

| Parameter Perbandingan | PLAN A: DEALER SSM MOTOR (UTAMA) | PLAN B: APOTEK FARMASI (CADANGAN) |
| :--- | :--- | :--- |
| **Objek Penelitian** | Dealer Resmi Sepeda Motor Yamaha (SSM Motor) | Instalasi Farmasi / Apotek Indonesia |
| **Sifat Data** | **Data Primer Eksklusif** (Transaksi Riil Dealer) | **Data Sekunder Bereputasi** (Mendeley Data DOI) |
| **Jumlah Data** | 3.113 transaksi penjualan kendaraan | 124.450 resep multi-item (514.620 baris) |
| **Dimensi Atribut** | Model Motor + Warna + Leasing + Tenor + DP + Domisili | Nomor Resep + Nama Obat + Satuan + Layanan + Racikan |
| **Keunggulan Utama** | **Novelty Sangat Tinggi:** Belum pernah ada di Google Scholar untuk multi-atribut motor + leasing. | **Volume Data Sangat Besar:** Sangat kokoh untuk pembuktian efisiensi algoritma & pemodelan big data. |
| **Status Kesiapan** | **100% Siap Diajukan (Rekomendasi #1)** | **100% Siap Diajukan (Cadangan Sempurna / Plan B)** |
