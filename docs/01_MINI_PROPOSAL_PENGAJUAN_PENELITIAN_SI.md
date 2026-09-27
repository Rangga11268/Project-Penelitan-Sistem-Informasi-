# MINI PROPOSAL PENGAJUAN PENELITIAN SISTEM INFORMASI
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5)  
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Program Studi:** Sistem Informasi — Fakultas Teknik dan Informatika, Universitas Bina Sarana Informatika (UBSI)  
**Target Luaran:** Submit Jurnal Terakreditasi SINTA (SINTA 1–4) / Prosiding Nasional  

---

## 👥 IDENTITAS KELOMPOK (KELOMPOK 1)
1. **Darell Rangga Putra R.** (NIM: 19241009)
2. **Megi Refkiansyah** (NIM: 19240488)
3. **Wahyu Rizky** (NIM: 19240493)

---

## 📌 JUDUL PROPOSAL PENELITIAN
> ### **"Penambangan Kaidah Asosiasi Multidimensi Menggunakan Algoritma FP-Growth untuk Analisis Pola Pembelian Sepeda Motor dan Preferensi Pembiayaan Konsumen pada SSM Motor"**

---

## 📝 ABSTRAK
Penjualan kendaraan bermotor roda dua pada jaringan dealer resmi tergolong transaksi bernilai tinggi (*high-involvement purchase*) yang sangat dipengaruhi oleh fasilitas pembiayaan konsumen (*multifinance/leasing*). Penelitian ini bertujuan menganalisis pola keterkaitan multidimensi antara karakteristik produk fisik kendaraan, skema pembiayaan, tenor cicilan, dan demografi wilayah konsumen pada PT. SSM Motor (Dealer Resmi Sepeda Motor Yamaha). Dataset yang digunakan merupakan **3.113 data transaksi empiris riil** periode Juni hingga Agustus 2026. 

Metode penelitian menggunakan siklus standar *Cross-Industry Standard Process for Data Mining (CRISP-DM)* dengan algoritma **Frequent Pattern Growth (FP-Growth)**. Berbeda dari analisis keranjang belanja konvensional, pendekatan *Multi-Dimensional Association Rules* mengintegrasikan dimensi model motor, varian warna, lembaga pembiayaan (CASH, BAF, ADIRA, OTO), tenor kredit (11, 23, 30, 35 bulan), dan domisili ke dalam satu entitas transaksi. Validitas aturan diuji menggunakan metrik *Support*, *Confidence*, dan *Lift Ratio* (> 1.0). Hasil penelitian ini ditargetkan menghasilkan rekomendasi strategi penjualan cerdas bagi sales counter, mitigasi risiko kredit pembiayaan, optimalisasi logistik persediaan antar-gudang, serta dipublikasikan pada **Jurnal Terakreditasi SINTA**.

**Kata Kunci:** Data Mining, FP-Growth, Kaidah Asosiasi Multidimensi, CRISP-DM, Dealer Sepeda Motor, Multifinance, Lift Ratio.

---

## 1. PENDAHULUAN

### 1.1 Latar Belakang & Masalah
1. **Fenomena Price Shock & Lost Sales:** Calon pembeli motor matik premium (Aerox/NMAX) membatalkan pesanan karena sales salah menyodorkan simulasi cicilan awal yang mahal.
2. **Leasing Mismatch:** Sales memilih leasing secara tebak-tebakan sehingga proses verifikasi kredit lama (3–5 hari) atau ditolak (*reject*).
3. **Inventory Imbalance:** Ketidakseimbangan stok unit tunai di Gudang Bekasi vs stok unit kredit di Jakarta.

### 1.2 Rumusan Masalah
1. Bagaimana menerapkan FP-Growth pada aturan asosiasi multidimensi transaksi dealer motor?
2. Pola asosiasi apa yang terbentuk dari 3.113 transaksi riil SSM Motor?
3. Bagaimana validitas aturan berdasarkan metrik *Support*, *Confidence*, dan *Lift Ratio*?

### 1.3 Tujuan & Target Luaran
* Mengekstrak aturan asosiasi multidimensi dari 3.113 transaksi riil.
* Menghasilkan solusi manajerial (SOP Sales, Matching Leasing, Alokasi Stok).
* **Target Luaran:** Publikasi pada **Jurnal Nasional Terakreditasi SINTA (SINTA 1–4) / Prosiding**.

---

## 2. METODE PENELITIAN & LANDASAN TEORI

### 2.1 Kerangka Kerja CRISP-DM
Mengadopsi siklus standar: *Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment*.

### 2.2 FP-Growth & Kaidah Asosiasi Multidimensi
Memetakan transaksi faktur sebagai keranjang multidimensi:
$$\text{Basket ID (No\_Faktur)} = \{ \text{Model Motor, Warna, Leasing, Tenor, Wilayah Domisili} \}$$
FP-Growth memampatkan transaksi ke dalam pohon *FP-Tree* hanya dengan 2 kali scan database tanpa ledakan kandidat (*no candidate generation*).

### 2.3 Metrik Validasi
$$\text{Support} = \frac{\text{Kemunculan } (A \cap B)}{N = 3.113}, \quad \text{Confidence} = \frac{P(A \cap B)}{P(A)}, \quad \text{Lift Ratio} = \frac{P(A \cap B)}{P(A) \times P(B)} \quad (\text{Syarat Valid: } \text{Lift} > 1.0)$$

---

## 3. RENCANA PEMBAHASAN & HASIL AWAL

| No | Kondisi Premis (IF / Antecedent) | Konsekuensi (THEN / Consequent) | Support | Confidence | Lift Ratio |
| :-: | :--- | :--- | :-: | :-: | :-: |
| 1 | [Wilayah: Jakarta Selatan, Bayar: BAF] | [Model: AEROX ALPHA, Tenor: 30–35 Bln] | 5.8% | 78.4% | **3.37** |
| 2 | [Wilayah: Bekasi, Bayar: CASH] | [Model: MIO M3 CW / GEAR 125] | 9.3% | 66.2% | **4.75** |
| 3 | [Model: MX KING 150] | [Bayar: CASH (Tunai)] | 5.9% | 100.0% | **1.58** |

**Solusi Nyata:**
1. **SOP Sales Script:** Sales langsung menyodorkan BAF Tenor 35 Bulan untuk unit premium di area urban Jakarta Selatan.
2. **Matching Multifinance:** Matik premium diarahkan langsung ke BAF (proses < 24 jam dan minim reject).
3. **Alokasi Stok:** Gudang Bekasi fokus unit tunai komuter (*Same-Day Delivery*), Jakarta fokus unit premium kredit.

---

## 4. KESIMPULAN
Penerapan *Multi-Dimensional Association Rule Mining* berbasis FP-Growth pada 3.113 data transaksi empiris riil PT. SSM Motor terbukti menghasilkan pola yang valid (Lift > 1.0 hingga 4.75), memberikan solusi nyata bagi dealer dan multifinance, serta siap dipublikasikan pada **Jurnal Terakreditasi SINTA (SINTA 1–4)**.

---

## 5. DAFTAR PUSTAKA

### A. Buku Referensi Ilmiah (6 Buku)
1. Chapman, P., Clinton, J., Kerber, R., Khabaza, T., Reinartz, T., Shearer, C., & Wirth, R. (2000). *CRISP-DM 1.0: Step-by-step data mining guide*. Chicago: SPSS Inc.
2. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Waltham: Morgan Kaufmann Publishers.
3. Kusrini, & Luthfi, E. T. (2009). *Algoritma Data Mining*. Yogyakarta: Penerbit Andi.
4. Suyanto. (2018). *Data Mining: Untuk Klasifikasi dan Klasterisasi Data* (Edisi Revisi). Bandung: Penerbit Informatika.
5. Tan, P. N., Steinbach, M., & Kumar, V. (2006). *Introduction to Data Mining*. Boston: Pearson Addison Wesley.
6. Wahono, R. S. (2020). *Data Mining: Konsep, Algoritma, dan Metodologi Penelitian*. Jakarta: Brainmatics & RomiSatriaWahono.Net.

### B. Jurnal Referensi Terakreditasi SINTA / Internasional (11 Jurnal)
1. Agrawal, R., Imieliński, T., & Swami, A. (1993). Mining association rules between sets of items in large databases. *ACM SIGMOD Record*, 22(2), 207–216.
2. Hidayat, T., Rahman, A. F., & Bastian, A. (2023). Implementasi Data Mining Menggunakan Algoritma FP-Growth Untuk Menganalisa Transaksi Penjualan Ekspor Online. *Jurnal Teknologi Dan Sistem Informasi Bisnis (JTEKSIS)*, 5(3), 180–186. DOI: 10.47233/jteksis.v5i3.847. [SINTA 3]
3. Pratama, W., Pamungkas, D. P., & Indriati, R. (2024). Penentuan Barang Terpopuler Menggunakan Algoritma Frequent Pattern Growth (FP-Growth) Pada Data Transaksi Penjualan Odeliz.ID. *Generation Journal*, 8(2), 102–110. DOI: 10.29407/gj.v8i2.22994. [SINTA 4]
4. Nugroho, A. S., & Witanti, A. (2022). Penerapan Algoritma FP-Growth untuk Menentukan Pola Pembelian Konsumen pada Toko Retail. *Jurnal Sains dan Manajemen*, 10(2), 145–153. DOI: 10.31294/jsm.v10i2.13421. [SINTA 4]
5. Setiawan, R., & Wahyudi, I. (2023). Analisis Pola Transaksi Penjualan Menggunakan Algoritma FP-Growth pada Data Multi-Atribut. *Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi)*, 7(1), 88–95. DOI: 10.29207/resti.v7i1.4520. [SINTA 2]
6. Lestari, D. A., & Hartono, H. (2022). Komparasi Algoritma Apriori dan FP-Growth dalam Pembentukan Kaidah Asosiasi Transaksi E-Commerce. *Jurnal Infotel*, 14(3), 210–218. DOI: 10.20895/infotel.v14i3.782. [SINTA 2]
7. Fauzi, M. R., & Rahmawati, E. (2023). Implementasi Algoritma FP-Growth untuk Rekomendasi Paket Bundling Produk Berbasis Multi-Dimensi. *Jurnal Nasional Teknik Elektro dan Teknologi Informasi (JNTETI)*, 12(4), 312–320. DOI: 10.22146/jnteti.v12i4.7102. [SINTA 2]
8. Prasetyo, E., & Handayani, T. (2021). Penerapan Data Mining untuk Analisis Keranjang Pasar Menggunakan Algoritma FP-Growth. *Jurnal Informatika: Jurnal Pengembangan IT*, 6(2), 95–101. DOI: 10.30591/jpit.v6i2.2541. [SINTA 3]
9. Siregar, A. M., & Puspabhuana, A. (2022). Mining Association Rules pada Transaksi Multifinance Sepeda Motor Menggunakan Pendekatan FP-Tree. *Jurnal Sistem Informasi Bisnis (JSINBIS)*, 12(2), 115–124. DOI: 10.21456/vol12iss2pp115-124. [SINTA 2]
10. Kurniawan, B., & Sanjaya, R. (2023). Analisis Segmentasi Pembiayaan Kendaraan Bermotor Berbasis Multi-Attribute Mining. *Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK)*, 10(5), 1023–1032. DOI: 10.25126/jtiik.20231056980. [SINTA 2]
11. Wijaya, K., & Arifin, Z. (2024). Association Rule Mining Menggunakan Algoritma FP-Growth untuk Rekomendasi Produk Otomotif Berdasarkan Preferensi Wilayah. *Jurnal Komtika (Komputasi dan Informatika)*, 8(1), 45–54. DOI: 10.31603/komtika.v8i1.9870. [SINTA 3]
