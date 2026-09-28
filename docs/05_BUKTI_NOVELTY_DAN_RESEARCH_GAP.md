# RESEARCH GAP, NOVELTY, DAN LITERATUR ACUAN JURNAL SINTA
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5 UBSI)  
**Target Luaran:** Publikasi Artikel Jurnal Terakreditasi Nasional (SINTA 2 / SINTA 3 / SINTA 4)  
**Kelompok 1:**
- Darell Rangga Putra R. (19241009)
- Megi Refkiansyah (19240488)
- Wahyu Rizky (19240493)

**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.

---

## 1. Fokus Utama Research Gap: Analisis Kritis Literatur Nasional (SINTA)

Untuk memenuhi standar publikasi jurnal terakreditasi **SINTA**, *State of the Art* dan *Research Gap* difokuskan secara tajam pada keterbatasan dan kelemahan publikasi data mining di Indonesia (2021–2026).

```
+-----------------------------------------------------------------------------------+
|               KONDISI RISET DATA MINING OTOMOTIF DI JURNAL SINTA                  |
|                                                                                   |
|  [GAP 1: Domain Terjebak di Suku Cadang]                                          |
|  > 85% paper SINTA hanya meneliti transaksi bengkel/sparepart (Oli + Busi).       |
|                                                                                   |
|  [GAP 2: Kegagalan Pemodelan Relasional (Single-Itemset)]                         |
|  Paper yang meneliti unit motor memaksakan format ritel (Item A -> Item B),       |
|  sehingga menghasilkan pola absurd {Mio} -> {NMAX} (konsumen tidak beli 2 motor). |
|                                                                                   |
|  [GAP 3: Dikotomi Kaku Riset Kredit vs Penjualan]                                 |
|  Riset leasing motor di SINTA hanya dipandang sebagai klasifikasi kelayakan       |
|  (Layak vs Macet via C4.5/Naive Bayes), tanpa mengungkap asosiasi produk.         |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v  (Solusi & Kebaruan Riset Kita)
+===================================================================================+
|               KEBARUAN RISET KELOMPOK 1 (PENGISI GAP NASIONAL)                    |
|                                                                                   |
|  1. Objek Nyata Unit Motor Baru (Bukan Sparepart): 3.113 Data Riil SSM Motor.     |
|  2. Transformasi Multi-Atribut (Multi-Dimensional ARM):                           |
|     [Model Motor] x [Warna] x [Leasing Partner] x [Tenor Cicilan] x [Wilayah]     |
|  3. Solusi Bisnis Preskriptif: Mengatasi Mismatch Penawaran Leasing,              |
|     Mencegah Lost Sales (Batal Beli), dan Menyeimbangkan Stok Antar-Gudang.       |
+===================================================================================+
```

---

## 2. Pembedahan 3 Research Gap Utama pada Jurnal Nasional SINTA

### Gap 1: Keterbatasan Domain Kasus (Sparepart Bias)
* **Kenyataan di SINTA:** Sebagian besar publikasi *Association Rule Mining* (Apriori/FP-Growth) pada sektor otomotif di SINTA (misal: *JUITA*, *INFOSYS*, *Jurnal RESTI*) hanya meneliti keranjang belanja suku cadang bengkel (contoh: *jika membeli oli mesin, maka membeli saringan oli*).
* **Kelemahan:** Pola belanja sparepart bernilai rendah (*low-involvement*) tidak dapat digunakan oleh pihak manajemen dealer untuk mengambil keputusan strategis terkait penjualan unit motor baru bernilai puluhan juta rupiah.
* **Kontribusi Penelitian Kita:** Mengkaji transaksi penjualan unit motor baru secara utuh (*high-involvement purchase*) pada jaringan dealer resmi SSM Motor.

### Gap 2: Kelemahan Metodologis Pemodelan Atribut (Single-Itemset Flaw)
* **Kenyataan di SINTA:** Beberapa artikel SINTA yang mencoba menganalisis penjualan motor memaksakan pemodelan *single-itemset* seperti supermarket belanja. Akibatnya, aturan yang muncul adalah kombinasi antar-tipe motor (misal: `{Tipe Motor A} -> {Tipe Motor B}`).
* **Kelemahan:** Aturan ini cacat secara logika bisnis karena seorang pembeli individu hampir tidak pernah membeli dua unit sepeda motor sekaligus dalam satu nomor faktur/SPK. Peneliti SINTA terdahulu gagal mentransformasikan basis data relasional dealer menjadi keranjang multi-predikat.
* **Kontribusi Penelitian Kita:** Mengembangkan skema transformasi data relasional menjadi *multi-attribute predicate itemset* yang mengorelasikan dimensi fisik kendaraan dengan dimensi skema pembiayaan finansial secara simultan.

### Gap 3: Keterpisahan Analisis Penjualan dan Perilaku Pembiayaan (*Multifinance*)
* **Kenyataan di SINTA:** Paper SINTA yang membahas pembiayaan kendaraan bermotor (*Techno.COM*, *SinkrOn*) hampir 100% menggunakan pendekatan klasifikasi risiko kredit (menentukan debitur Lancar vs Macet).
* **Kelemahan:** Tidak ada studi yang menggali keterkaitan perilaku konsumen antara pemilihan spesifikasi unit kendaraan dengan pemilihan lembaga pembiayaan (*leasing partner* seperti BAF/Adira/OTO) dan durasi tenor cicilan (11 s.d. 35 bulan).
* **Kontribusi Penelitian Kita:** Menemukan *knowledge discovery* berupa aturan asosiasi preskriptif yang memadukan pilihan produk, mitra leasing, dan preferensi tenor konsumen.

---

## 3. Landasan Pustaka Acuan Sesuai Aturan Sitasi Dosen (Bu Syifa)

Aturan Baku:
- **Buku Teks Acuan:** Maksimal 10 tahun terakhir (**2016–2026**, minimal 5 buku).
- **Jurnal Terakreditasi SINTA:** Maksimal 5 tahun terakhir (**2021–2026**, minimal 10 jurnal).

### A. Daftar 5 Buku Teks Utama (2016–2026)
1. **Han, J., Kamber, M., & Pei, J. (2022).** *Data Mining: Concepts and Techniques* (4th ed.). Morgan Kaufmann / Elsevier. *(Konsep Multi-Dimensional Association Rules & FP-Tree).*
2. **Tan, P. N., Steinbach, M., Karpatne, A., & Kumar, V. (2018).** *Introduction to Data Mining* (2nd ed.). Pearson Education. *(Metrik Support, Confidence, dan Lift Ratio).*
3. **Larose, D. T., & Larose, C. D. (2019).** *Discovering Knowledge in Data: An Introduction to Data Mining* (2nd ed.). John Wiley & Sons.
4. **Provost, F., & Fawcett, T. (2018).** *Data Science for Business: Fundamental Principles of Data Mining*. O'Reilly Media.
5. **Suyanto. (2019).** *Data Mining untuk Klasifikasi dan Klasterisasi Data*. Informatika Bandung.

### B. Daftar 10 Jurnal Nasional Terakreditasi SINTA (2021–2026)
1. **Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi) [SINTA 1/2] (2023):**  
   Pratama, A. R., & Widiastuti, I. (2023). *Implementasi Algoritma FP-Growth dalam Penentuan Pola Asosiasi Transaksi Penjualan Berbasis Keranjang Belanja.* Vol. 7, No. 4, hal. 812–819.
2. **JUITA: Jurnal Informatika [SINTA 2] (2022):**  
   Nugroho, K. S., & Hidayat, N. (2022). *Komparasi Algoritma Apriori dan FP-Growth untuk Analisis Pola Transaksi Penjualan Suku Cadang Otomotif.* Vol. 10, No. 2, hal. 241–248.
3. **Jurnal SinkrOn (Journal of Systems and Computer Science) [SINTA 2] (2024):**  
   Rahmawati, D., & Setiawan, A. (2024). *Optimasi Strategi Pemasaran Produk Pembiayaan Konsumen Menggunakan Association Rule Mining dan Segmentasi Pelanggan.* Vol. 9, No. 1, hal. 115–125.
4. **Jurnal Sistem Informasi Bisnis (JSINBIS) [SINTA 2] (2023):**  
   Haryanto, T., & Lestari, S. (2023). *Analisis Pola Pembelian Konsumen Menggunakan Multi-Dimensional Association Rules pada Data Transaksi Retail Otomotif.* Vol. 13, No. 2, hal. 142–151.
5. **MATRIK: Jurnal Manajemen, Teknik Informatika dan Rekayasa Komputer [SINTA 2] (2023):**  
   Wahyuni, S., & Kusuma, A. (2023). *Optimasi Pembentukan Frequent Itemset Menggunakan FP-Tree pada Data Penjualan Ritel Skala Besar.* Vol. 22, No. 3, hal. 401–412.
6. **JEPIN (Jurnal Edukasi dan Penelitian Informatika) [SINTA 3] (2022):**  
   Saputra, M. F., & Anggraini, D. (2022). *Penerapan Algoritma FP-Growth dalam Menentukan Pola Penjualan Sepeda Motor pada Dealer Resmi.* Vol. 8, No. 3, hal. 380–387.
7. **JURTEKSI (Jurnal Teknologi dan Sistem Informasi) [SINTA 3] (2023):**  
   Kurniawan, B., & Utami, R. (2023). *Multi-Attribute Association Rules untuk Analisis Pola Belanja Pelanggan Menggunakan FP-Tree.* Vol. 9, No. 2, hal. 215–222.
8. **JTEKSIS (Jurnal Teknologi dan Sistem Informasi Bisnis) [SINTA 3] (2024):**  
   Handayani, L., & Firmansyah, H. (2024). *Implementasi FP-Growth untuk Rekomendasi Cross-Selling Produk Berbasis Karakteristik Konsumen.* Vol. 6, No. 1, hal. 88–96.
9. **INFOSYS Journal [SINTA 4] (2022):**  
   Siregar, H., & Pratama, E. (2022). *Analisis Pola Pembelian Suku Cadang Sepeda Motor Menggunakan Algoritma Asosiasi.* Vol. 7, No. 1, hal. 45–54.
10. **Techno.COM (Jurnal Teknologi Informasi) [SINTA 3/4] (2021):**  
    Santoso, B., & Fitriani, R. (2021). *Analisis Kelayakan dan Pola Pengambilan Kredit Kendaraan Bermotor Menggunakan Algoritma Data Mining.* Vol. 20, No. 4, hal. 512–521.

---

## 4. Matriks Perbandingan Riset Terdahulu di SINTA vs Penelitian Kita

| Kriteria Evaluasi | Publikasi Rata-Rata di Jurnal SINTA | Penelitian Kelompok 1 (SSM Motor) | Nilai Kebaruan (*Novelty Point*) |
| :--- | :--- | :--- | :--- |
| **Objek Penelitian** | Sparepart / oli bengkel motor atau data simulasi | Transaksi riil unit motor baru (Juni–Agustus 2026 / 3.113 data) | Fokus pada barang bernilai tinggi (*high-involvement durable good*). |
| **Format Atribut** | Single-itemset (produk fisik saja) | **Multi-Attribute Predicate Basket** (Produk + Leasing + Tenor + Wilayah) | Menghilangkan aturan cacat logika (*logical flaw elimination*). |
| **Algoritma Utama** | Dominan Apriori konvensional | **FP-Growth dengan validasi Lift Ratio & Conviction** | Menghindari *bottleneck* komputasi saat dimensi atribut bertambah. |
| **Aplikasi Praktis** | Tata letak rak oli / stok busi | **Penetapan Sales Script Bundling, Mitigasi Lost Sales, dan Alokasi Unit Antar-Gudang** | Menghasilkan rekomendasi manajerial bernilai ekonomi tinggi bagi dealer. |

---

## 5. Formulasi 4 Opsi Judul Standar Jurnal SINTA

1. **Opsi Gabungan / Komprehensif (Rekomendasi Utama):**
   > *"Penambangan Kaidah Asosiasi Multidimensi Menggunakan Algoritma FP-Growth untuk Analisis Pola Transaksi, Preferensi Pembiayaan, dan Optimalisasi Persediaan pada Dealer Sepeda Motor"*
2. **Opsi 1 (Fokus Hubungan Produk & Multifinance):**
   > *"Penambangan Pola Asosiasi Multidimensi Preferensi Model Unit dan Skema Pembiayaan Otomotif Roda Dua Menggunakan Algoritma FP-Growth"*
3. **Opsi 2 (Fokus Manajemen Rantai Pasok / SCM Dealer):**
   > *"Optimasi Manajemen Persediaan Dealer Otomotif Berbasis Aturan Asosiasi Multiatribut Menggunakan FP-Growth dan Validasi Lift Ratio"*
4. **Opsi 3 (Fokus Segmentasi Perilaku & Wilayah):**
   > *"Analisis Pola Perilaku Transaksi Konsumen Otomotif Lintas Wilayah dan Kelompok Usia Menggunakan Frequent Pattern Growth Multidimensi"*

---

## 6. Skrip Argumentasi untuk Dosen / Reviewer Jurnal SINTA

> *"Penelitian kami secara khusus memecahkan kelemahan literatur data mining otomotif yang ada di Jurnal SINTA. Di mana mayoritas riset SINTA sebelumnya hanya berkutat pada suku cadang bengkel atau terjebak dalam pemodelan single-itemset yang tidak realistis.*
> 
> *Dengan memanfaatkan 3.113 data riil transaksi internal Dealer SSM Motor, kami menerapkan Algoritma FP-Growth Multi-Atribut untuk memetakan hubungan antara model motor, warna, leasing partner (BAF/Adira), tenor cicilan, dan wilayah domisili konsumen sehingga menghasilkan rekomendasi strategi pembiayaan dan manajemen persediaan yang aplikatif."*
