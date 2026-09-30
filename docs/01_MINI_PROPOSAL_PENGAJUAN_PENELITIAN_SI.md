# MINI PROPOSAL PENGAJUAN PENELITIAN SISTEM INFORMASI
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5)  
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Program Studi:** Sistem Informasi — Fakultas Teknik dan Informatika, Universitas Bina Sarana Informatika (UBSI)  
**Target Luaran:** Submit Jurnal Terakreditasi SINTA (SINTA 2–4) / Prosiding Seminar Nasional  

---

## 👥 IDENTITAS KELOMPOK (KELOMPOK 1)
1. **Darell Rangga Putra R.** (NIM: 19241009)
2. **Megi Refkiansyah** (NIM: 19240488)
3. **Wahyu Rizky** (NIM: 19240493)

---

## 📌 JUDUL UTAMA PROPOSAL PENELITIAN (REKOMENDASI #1)
> ### **"Penerapan Algoritma FP-Growth dalam Multi-Attribute Association Rule Mining untuk Analisis Pola Pembelian Sepeda Motor dan Preferensi Skema Pembiayaan Konsumen (Studi Kasus: PT. Sinar Surya Matahari)"**
* **Versi Bahasa Inggris:** *"Application of FP-Growth Algorithm in Multi-Attribute Association Rule Mining for Motorcycle Purchase Patterns and Consumer Financing Scheme Preferences (Case Study: PT. Sinar Surya Matahari)"*

---

## 📝 ABSTRAK
Penjualan kendaraan bermotor roda dua pada jaringan dealer resmi tergolong transaksi bernilai tinggi (*high-involvement purchase*) yang sangat dipengaruhi oleh fasilitas pembiayaan konsumen (*multifinance/leasing*). Penelitian ini bertujuan menganalisis pola keterkaitan multidimensi antara karakteristik produk fisik kendaraan, skema pembiayaan, tenor cicilan, uang muka (DP), dan demografi wilayah konsumen pada PT. Sinar Surya Matahari (Dealer Resmi Sepeda Motor Yamaha). Dataset yang digunakan merupakan **3.113 data transaksi empiris riil** periode Juni hingga Agustus 2026. 

Metode penelitian menggunakan siklus standar *Cross-Industry Standard Process for Data Mining (CRISP-DM)* dengan algoritma **Frequent Pattern Growth (FP-Growth)**. Berbeda dari analisis keranjang belanja konvensional, pendekatan *Multi-Attribute Association Rules* mengintegrasikan dimensi model motor, varian warna, lembaga pembiayaan (CASH, BAF, ADIRA, OTO), tenor kredit (11, 23, 30, 35 bulan), besaran DP, dan domisili ke dalam satu entitas transaksi. Validitas aturan diuji menggunakan metrik *Support*, *Confidence*, dan *Lift Ratio* (> 1.0). Hasil penelitian ini ditargetkan menghasilkan rekomendasi strategi penjualan cerdas (*smart sales script*), perumusan paket promo bersama leasing, optimalisasi alokasi stok antar-cabang, serta dipublikasikan pada **Jurnal Terakreditasi SINTA**.

**Kata Kunci:** Data Mining, FP-Growth, Multi-Attribute Association Rules, CRISP-DM, PT. Sinar Surya Matahari, Pembiayaan Konsumen, Multifinance, Lift Ratio.

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang & Masalah Bisnis
1. **Fenomena Price Shock & Lost Sales:** Calon pembeli motor matik premium (Aerox/NMAX) membatalkan pesanan karena pramuniaga salah menyodorkan simulasi cicilan awal atau tenor yang tidak sesuai dengan daya bayar konsumen.
2. **Leasing Mismatch:** Pemilihan mitra leasing dilakukan secara coba-coba sehingga proses verifikasi kredit lambat atau ditolak (*reject*).
3. **Inventory Imbalance:** Ketidakseimbangan stok unit motor antar-cabang akibat tidak adanya analisis preferensi warna dan model per wilayah domisili.

### 1.2 Rumusan Masalah
1. Bagaimana menerapkan algoritma FP-Growth pada aturan asosiasi multiatribut transaksi penjualan PT. Sinar Surya Matahari?
2. Pola kombinasi produk motor dan skema pembiayaan apa yang terbentuk dari 3.113 transaksi riil?
3. Bagaimana tingkat validitas kaidah asosiasi berdasarkan pengujian *Support*, *Confidence*, dan *Lift Ratio* (> 1.0)?

### 1.3 Tujuan Penelitian & Target Luaran
* Mengekstrak aturan asosiasi multiatribut dari 3.113 transaksi riil PT. Sinar Surya Matahari.
* Menghasilkan solusi manajerial terapan: panduan sales cerdas (*smart sales script*), paket promo bersama leasing, dan optimasi stok.
* **Target Luaran:** Artikel ilmiah untuk publikasi pada **Jurnal Nasional Terakreditasi SINTA (SINTA 2–4)**.

---

## 2. METODE PENELITIAN & LANDASAN TEORI

### 2.1 Kerangka Kerja CRISP-DM
Mengadopsi siklus 6 tahap standar: *Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment*.

### 2.2 FP-Growth & Kaidah Asosiasi Multiatribut
Memetakan transaksi faktur sebagai keranjang multiatribut:
$$\text{Basket ID} = \{ \text{Model Motor, Varian Warna, Lembaga Leasing, Tenor Angsuran, Range DP, Domisili} \}$$
FP-Growth memadatkan data transaksi ke dalam struktur pohon *FP-Tree* hanya dengan 2 kali pemindaian data (*two-pass scan*) tanpa pembangkitan kandidat berulang (*no candidate generation*).

### 2.3 Metrik Validasi Tri-Metrik
$$\text{Support} = \frac{\text{Kemunculan } (A \cap B)}{N = 3.113}, \quad \text{Confidence} = \frac{P(A \cap B)}{P(A)}, \quad \text{Lift Ratio} = \frac{P(A \cap B)}{P(A) \times P(B)} \quad (\text{Syarat: } \text{Lift} > 1.0)$$
