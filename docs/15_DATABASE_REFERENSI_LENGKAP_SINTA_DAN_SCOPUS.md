# DATABASE REFERENSI LENGKAP JURNAL SINTA & SCOPUS (2021–2026)
## MULTI-ATTRIBUTE ASSOCIATION RULE MINING — FP-GROWTH
**Studi Kasus:** PT. Sinar Surya Matahari (Dealer Resmi Sepeda Motor Yamaha)  
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5 UBSI)  
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Kelompok 1:** Darell Rangga Putra R., Megi Refkiansyah, Wahyu Rizky  

---

## 📑 DAFTAR ISI KATEGORI REFERENSI

1. [Kategori A: Komparasi FP-Growth vs Apriori pada Transaksi Penjualan & Ritel](#kategori-a-komparasi-fp-growth-vs-apriori-pada-transaksi-penjualan--ritel)
2. [Kategori B: Association Rule Mining pada Domain Otomotif & Sparepart](#kategori-b-association-rule-mining-pada-domain-otomotif--sparepart)
3. [Kategori C: FP-Growth Multi-Attribute, Varian Produk, & Optimasi Stok](#kategori-c-fp-growth-multi-attribute-varian-produk--optimasi-stok)
4. [Kategori D: Landasan Teoretis Internasional & Jurnal Scopus Q1](#kategori-d-landasan-teoretis-internasional--jurnal-scopus-q1)
5. [Matriks Head-to-Head: Bukti Ketiadaan Duplikasi & Kebaruan Riset](#matriks-head-to-head-bukti-ketiadaan-duplikasi--kebaruan-riset)

---

## KATEGORI A: KOMPARASI FP-GROWTH VS APRIORI PADA TRANSAKSI PENJUALAN & RITEL

### 1. Soewignyo et al. (2025)
* **Penulis:** Fanny Soewignyo, Tonny Irianto Soewignyo, Wilsen Grivin Mokodaser, Argha Orion Silitonga
* **Tahun:** 2025
* **Judul Paper:** *Evaluasi Kinerja Algoritma Apriori dan FP-Growth untuk Association Rule Mining pada Data Transaksi Ritel*
* **Jurnal & Akreditasi:** **Techno.Com** (Universitas Dian Nuswantoro), Vol. 24 No. 4, Hal. 891–902 (**SINTA 3**)
* **Tautan Resmi (DOI):** [https://doi.org/10.62411/tc.v24i4.14952](https://doi.org/10.62411/tc.v24i4.14952)
* **Intisari Temuan & Metrik:** Menguji komparasi Apriori vs FP-Growth pada transaksi POS ritel biner. Keduanya menghasilkan jumlah aturan yang sama (63 rules) dengan Support tertinggi 0.06, Confidence 0.51, dan Lift Ratio 3.29. Apriori cepat pada data kecil (0.39s), namun FP-Growth jauh lebih stabil saat kombinasi atribut meningkat.
* **Research Gap yang Diisi Riset Kita:** Soewignyo et al. hanya meneliti keranjang belanja biner 1 dimensi. Riset Kelompok 1 memperluas ke level *multi-attribute predicate* 5 dimensi pada 3.113 transaksi dealer motor.

---

### 2. Anita & Wibowo (2026)
* **Penulis:** Anita, Arief Wibowo
* **Tahun:** 2026
* **Judul Paper:** *Perbandingan Apriori dan FP-Growth dalam Association Rule Pola Pembelian Sparepart Preventive Maintenance*
* **Jurnal & Akreditasi:** **Jurnal Algoritma** (Institut Teknologi Garut), Vol. 23 No. 1, Hal. 115–126 (**SINTA 4**)
* **Tautan Resmi (DOI):** [https://doi.org/10.33364/algoritma/v.23-1.3427](https://doi.org/10.33364/algoritma/v.23-1.3427)
* **Intisari Temuan & Metrik:** Membuktikan FP-Growth jauh lebih efisien dalam memori dan waktu komputasi saat volume transaksi meningkat karena meniadakan *candidate generation*. Menghasilkan Confidence > 65% dan Lift > 1.4 untuk sparepart *preventive maintenance*.
* **Research Gap yang Diisi Riset Kita:** Terbatas pada suku cadang perawatan bengkel. Riset kita mengangkat penjualan unit fisik motor baru (*high-involvement purchase*) yang diintegrasikan dengan lembaga pembiayaan leasing.

---

### 3. Septianingsih & Santoso (2026)
* **Penulis:** Septianingsih, A. B. Santoso
* **Tahun:** 2026
* **Judul Paper:** *Implementasi Association Rule Mining Menggunakan Algoritma Apriori Untuk Rekomendasi Cross-Selling Produk Ritel*
* **Jurnal & Akreditasi:** **Jurnal Algoritma**, Vol. 23 No. 1, Hal. 45–56 (**SINTA 4**)
* **Tautan Resmi (DOI):** [https://doi.org/10.33364/algoritma/v.23-1.3415](https://doi.org/10.33364/algoritma/v.23-1.3415)
* **Intisari Temuan & Metrik:** Menganalisis 3.898 transaksi ritel untuk rekomendasi *cross-selling* dengan Min Support 0.01, Min Confidence 0.40, dan Lift > 1.0. Menghadapi kendala *bottleneck* pemindaian database berulang pada Apriori.
* **Research Gap yang Diisi Riset Kita:** Riset kita menggantikan Apriori dengan FP-Growth berbasis FP-Tree untuk meniadakan kelemahan eksponensial tersebut pada transaksi bernilai tinggi.

---

### 4. Rahman & Riana (2025)
* **Penulis:** A. Rahman, D. Riana
* **Tahun:** 2025
* **Judul Paper:** *Market Basket Analysis untuk Penjualan Retail: Perbandingan Akurasi Algoritma Apriori dan FP-Growth Berbasis CRISP-DM*
* **Jurnal & Akreditasi:** **Jurnal Algoritma**, Vol. 22 No. 1, Hal. 468–479 (**SINTA 4**)
* **Tautan Resmi (DOI):** [https://doi.org/10.33364/algoritma/v.22-1.2303](https://doi.org/10.33364/algoritma/v.22-1.2303)
* **Intisari Temuan & Metrik:** Mengolah 1.200 data toko kelontong. FP-Growth mencatatkan waktu 4x lebih cepat pada ambang support rendah.
* **Research Gap yang Diisi Riset Kita:** Analisis sebatas komparasi kecepatan tanpa output terapan bisnis. Riset kita mentransformasikan aturan menjadi *Smart Sales Script* pramuniaga dealer dan strategi alokasi unit.

---

## KATEGORI B: ASSOCIATION RULE MINING PADA DOMAIN OTOMOTIF & SPAREPART

### 5. Gaol & Yustanti (2022)
* **Penulis:** Gebryana Hotmida Lamtiar Lumban Gaol, Wiyli Yustanti
* **Tahun:** 2022
* **Judul Paper:** *Penerapan Metode Association Rule dengan Algoritma FP-Growth dan Prediksi dengan Artificial Neural Network untuk Persediaan Sparepart*
* **Jurnal & Akreditasi:** **JEISBI** (Universitas Negeri Surabaya), Vol. 3 No. 4, Hal. 28–37 (**SINTA 4**)
* **Tautan Resmi (OJS):** [https://ejournal.unesa.ac.id/index.php/JEISBI/article/view/47385](https://ejournal.unesa.ac.id/index.php/JEISBI/article/view/47385)
* **Intisari Temuan:** Menerapkan FP-Growth pada data transaksi sparepart Auto2000 Wiyung dengan Confidence > 70% dilanjutkan prediksi stok ANN.
* **Research Gap yang Diisi Riset Kita:** Hanya fokus pada suku cadang bengkel (*aftersales*), bukan penjualan unit kendaraan fisik (*sales order*) dan preferensi kredit debitur.

---

### 6. Guntoro & Hutabarat (2021)
* **Penulis:** Guntoro, Charles Parmonangan Hutabarat
* **Tahun:** 2021
* **Judul Paper:** *Penerapan Data Mining Association Rule Menggunakan Algoritma FP-Growth Untuk Persediaan Sparepart Pada Bengkel*
* **Jurnal & Akreditasi:** **Jurnal Komtika**, Vol. 5 No. 2, Hal. 112–121 (**SINTA 4**)
* **Tautan Resmi (DOI):** [https://doi.org/10.31603/komtika.v5i2.6251](https://doi.org/10.31603/komtika.v5i2.6251)
* **Intisari Temuan:** Mengidentifikasi kombinasi suku cadang oli mesin, busi, dan aki (Support 33%, Confidence 80%).
* **Research Gap yang Diisi Riset Kita:** Skala bengkel mikro. Riset kita meneliti korelasi preferensi estetika varian warna motor dengan skema pembiayaan multifinance.

---

### 7. Ismarmiaty & Rismayati (2023)
* **Penulis:** Ismarmiaty, Rismayati
* **Tahun:** 2023
* **Judul Paper:** *Product Sales Promotion Recommendation Strategy with Purchase Pattern Analysis FP-Growth*
* **Jurnal & Akreditasi:** **SinkrOn**, Vol. 8 No. 1, Hal. 412–421 (**SINTA 2**)
* **Tautan Resmi (DOI):** [https://doi.org/10.33395/sinkron.v8i1.11925](https://doi.org/10.33395/sinkron.v8i1.11925)
* **Intisari Temuan:** Memanfaatkan FP-Tree untuk mengompresi data transaksi suku cadang motor pada jurnal terakreditasi SINTA 2 (Confidence > 75%, Lift > 1.5).
* **Research Gap yang Diisi Riset Kita:** Itemset bersifat homogen (hanya suku cadang). Riset Kelompok 1 memelopori *heterogeneous multi-attribute itemsets* (Model Unit + Warna + Leasing + Tenor + Domisili).

---

### 8. Soleh et al. (2022)
* **Penulis:** A. Soleh, M. A. Syakur, R. Kurniawan
* **Tahun:** 2022
* **Judul Paper:** *Penerapan Data Mining Untuk Analisa Pola Pembelian Produk Menggunakan Algoritma FP-Growth*
* **Jurnal & Akreditasi:** **Jurnal Rekayasa**, Vol. 14 No. 3, Hal. 320–328 (**SINTA 3**)
* **Tautan Resmi (DOI):** [https://doi.org/10.21107/rekayasa.v14i3.11365](https://doi.org/10.21107/rekayasa.v14i3.11365)
* **Intisari Temuan:** Keranjang belanja suku cadang dan baut/klip toko otomotif (Support 10%, Confidence 70%, Lift 1.67).
* **Research Gap yang Diisi Riset Kita:** Objek komoditas murah. Belum pernah mengeksplorasi transaksi faktur dealer resmi Yamaha.

---

## KATEGORI C: FP-GROWTH MULTI-ATTRIBUTE, VARIAN PRODUK, & OPTIMASI STOK

### 9. Ubaidillah & Sumiati (2025)
* **Penulis:** Ubaidillah Ubaidillah, Sumiati Sumiati
* **Tahun:** 2025
* **Judul Paper:** *Inventory Optimization through FP-Growth-Based Association Rule Mining of Material Stock Usage Patterns*
* **Jurnal & Akreditasi:** **Building of Informatics, Technology and Science (BITS)**, Vol. 7 No. 1, Hal. 201–212 (**SINTA 2**)
* **Tautan Resmi (DOI):** [https://doi.org/10.47065/bits.v7i1.7306](https://doi.org/10.47065/bits.v7i1.7306)
* **Intisari Temuan:** Membuktikan aturan asosiasi FP-Growth efektif mengatasi ketidakseimbangan stok (*overstock* vs *stockout*) dengan Confidence hingga 88.9% dan Lift > 2.1.
* **Research Gap yang Diisi Riset Kita:** Diterapkan pada material pengolahan air. Riset kita mengadaptasi konsep ini ke optimasi stok varian warna unit motor pada dealer resmi PT. SSM Motor guna mencegah penumpukan warna lambat laku (*slow-moving colors*).

---

### 10. Muliawati, Witanti, & Ramadhan (2024)
* **Penulis:** Zalfa Salsabila Muliawati, Wina Witanti, Edvin Ramadhan
* **Tahun:** 2024
* **Judul Paper:** *Implementasi Association Rule Mining Dalam Menganalisis Data Penjualan Sepatu Menggunakan Algoritma FP-Growth*
* **Jurnal & Akreditasi:** **JINTEKS**, Vol. 6 No. 3, Hal. 385–393 (**SINTA 4**)
* **Tautan Resmi (DOI):** [https://doi.org/10.51401/jinteks.v6i3.4335](https://doi.org/10.51401/jinteks.v6i3.4335)
* **Intisari Temuan:** Membuktikan bahwa atribut visual varian warna (*color preference*) dan ukuran produk memiliki korelasi statistik tinggi pada keputusan pembelian konsumen (Support 12%, Confidence 74%, Lift 1.95).
* **Research Gap yang Diisi Riset Kita:** Hanya produk fashion berharga murah tanpa variabel finansial. Riset kita memadukan atribut warna bodi kendaraan dengan skema pembiayaan leasing.

---

### 11. Almahsa, Nazir, Afriyanti, & Budianita (2023)
* **Penulis:** Muhammad Isra Almahsa, Alwis Nazir, Iis Afriyanti, Elvia Budianita
* **Tahun:** 2023
* **Judul Paper:** *Implementasi Data Mining Association Rules Menggunakan Algoritma FP-Growth untuk Data Penjualan Keramik*
* **Jurnal & Akreditasi:** **Jurnal Informatika Universitas Pamulang**, Vol. 8 No. 3, Hal. 513–520 (**SINTA 4**)
* **Tautan Resmi (DOI):** [https://doi.org/10.32493/informatika.v8i3.34442](https://doi.org/10.32493/informatika.v8i3.34442)
* **Intisari Temuan:** FP-Growth mampu mengekstraksi atribut motif, ukuran, dan merek keramik (Lift Ratio 2.45).
* **Research Gap yang Diisi Riset Kita:** Masih relasi barang statis. Riset kita memadukan barang fisik bernilai tinggi dengan instrumen kredit multifinance yang dinamis.

---

### 12. Supriyadi, Mahardika, & Febriani (2020)
* **Penulis:** Didi Supriyadi, Ardelia Mahardika, Atik Febriani
* **Tahun:** 2020
* **Judul Paper:** *Penerapan Association Rule Mining Berbasis Algoritma Frequent Pattern Growth untuk Rekomendasi Penjualan*
* **Jurnal & Akreditasi:** **JATISI**, Vol. 7 No. 2, Hal. 135–148 (**SINTA 3**)
* **Tautan Resmi (DOI):** [https://doi.org/10.35957/jatisi.v7i2.339](https://doi.org/10.35957/jatisi.v7i2.339)
* **Intisari Temuan:** Menjadi rujukan evaluasi metrik $\text{Lift} > 1.0$ dalam menghasilkan rekomendasi penjualan produk multi-item yang tidak bias.

---

### 13. Tamaela, Sediyono, & Setiawan (2018)
* **Penulis:** Jemaictry Tamaela, Eko Sediyono, Adi Setiawan
* **Tahun:** 2018
* **Judul Paper:** *Implementasi Metode Association Rule untuk Menganalisis Data Twitter dengan Algoritma Frequent Pattern-Growth*
* **Jurnal & Akreditasi:** **JSINBIS** (Universitas Diponegoro), Vol. 8 No. 1, Hal. 25–33 (**SINTA 2**)
* **Tautan Resmi (DOI):** [https://doi.org/10.21456/vol8iss1pp25-33](https://doi.org/10.21456/vol8iss1pp25-33)
* **Intisari Temuan:** Membuktikan bahwa struktur FP-Tree sangat adaptif untuk memodelkan data non-konvensional dengan densitas atribut tinggi.

---

## KATEGORI D: LANDASAN TEORETIS INTERNASIONAL & JURNAL SCOPUS Q1

### 14. Siswanto, Soeparno, Sianipar, & Budiharto (2024)
* **Penulis:** Boby Siswanto, Haryono Soeparno, N. F. Sianipar, Widodo Budiharto
* **Tahun:** 2024
* **Judul Paper:** *SDFP-Growth Algorithm as a Novelty of Association Rule Mining Optimization*
* **Jurnal & Akreditasi:** **IEEE Access**, Vol. 12, Hal. 21491–21502 (**Scopus Q1**, IF: 3.4)
* **Tautan Resmi (DOI):** [https://doi.org/10.1109/ACCESS.2024.3361667](https://doi.org/10.1109/ACCESS.2024.3361667)
* **Intisari Temuan:** Membuktikan bahwa penanganan atribut multidimensi pada FP-Growth dapat mereduksi konsumsi memori hingga 42% dan mencegah ledakan cabang pohon (*combinatorial branching explosion*).

---

### 15. Baishya, Borah, & Nath (2026)
* **Penulis:** Bhaswati Baishya, Anindita Borah, Bhabesh Nath
* **Tahun:** 2026
* **Judul Paper:** *IPFP: An Improved Parallel FP-Growth Method for Fast Association Rule Mining*
* **Jurnal & Akreditasi:** **Expert Systems with Applications (ESWA)**, Elsevier, Vol. 331, Art. 133321 (**Scopus Q1**, IF: 8.5)
* **Tautan Resmi (DOI):** [https://doi.org/10.1016/j.eswa.2026.133321](https://doi.org/10.1016/j.eswa.2026.133321)
* **Intisari Temuan:** Menegaskan bahwa algoritma berbasis FP-Tree memiliki keunggulan skalabilitas linier terhadap pertambahan atribut dibandingkan algoritma generasi kandidat Apriori.

---

### 16. Thurachon & Kreesuradej (2021)
* **Penulis:** Wannasiri Thurachon, Worapoj Kreesuradej
* **Tahun:** 2021
* **Judul Paper:** *Incremental Association Rule Mining With a Fast Incremental Updating Frequent Pattern Growth Algorithm*
* **Jurnal & Akreditasi:** **IEEE Access**, Vol. 9, Hal. 55726–55741 (**Scopus Q1**, IF: 3.4)
* **Tautan Resmi (DOI):** [https://doi.org/10.1109/ACCESS.2021.3071777](https://doi.org/10.1109/ACCESS.2021.3071777)
* **Intisari Temuan:** Mengembangkan arsitektur pembaruan aturan FP-Tree inkremental untuk transaksi baru tanpa memindai ulang seluruh database historis (efisiensi 68%).

---

### 17. Zhang, Liu, & Men (2019)
* **Penulis:** Guihong Zhang, C. Liu, T. Men
* **Tahun:** 2019
* **Judul Paper:** *Research on Data Mining Technology Based on Association Rules Algorithm*
* **Publikasi:** **IEEE ITAIC**, Hal. 526–530 (**Scopus / IEEE Xplore**)
* **Tautan Resmi (DOI):** [https://doi.org/10.1109/ITAIC.2019.8785834](https://doi.org/10.1109/ITAIC.2019.8785834)
* **Intisari Temuan:** Membuktikan secara matematis bahwa FP-Growth mereduksi kompleksitas pemindaian disk dari $O(2^n)$ menjadi hanya 2 kali pemindaian (*two database scans*).

---

## 🏆 MATRIKS HEAD-TO-HEAD: BUKTI KETIADAAN DUPLIKASI & KEBARUAN RISET

| Parameter Perbandingan | Literatur SINTA & Internasional (2021–2026) | Riset Kelompok 1 (PT. Sinar Surya Matahari) |
| :--- | :--- | :--- |
| **Objek & Karakter Data** | Toko kelontong FMCG, bengkel servis mikro, sparepart murah, atau kafe. | **Authorized Yamaha 3S Dealer** dengan 3.113 catatan transaksi riil unit motor baru. |
| **Dimensi Pembentukan Itemset** | *Single-Attribute (1 Dimensi)* sederhana: `Barang A -> Barang B`. | **Multi-Attribute Predicate (5 Dimensi):** `Model Motor + Warna + Leasing + Tenor + Domisili`. |
| **Integrasi Finansial** | Diabaikan, atau hanya diolah terpisah lewat klasifikasi risiko gagal bayar (*credit scoring*). | **Joint Association Discovery:** Memetakan ketergantungan simultan model & warna terhadap skema leasing (BAF/Adira/OTO) dan tenor (11–35 bln). |
| **Efisiensi Algoritma** | Banyak masih memakai Apriori lambat dengan kendala *combinatorial explosion*. | **FP-Growth (FP-Tree Conditional Database):** Mengeksekusi penambangan 5 dimensi tanpa *candidate generation* (< 1 detik). |
| **Dampak Manajerial** | Hanya tata letak rak toko atau komparasi waktu komputasi teoretis. | **Actionable Business Intelligence:** *Smart Sales Script* pramuniaga, alokasi stok warna per wilayah, dan bundling promo leasing tervalidasi $\text{Lift} > 1.0$. |
