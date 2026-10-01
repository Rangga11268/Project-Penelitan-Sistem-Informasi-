# RESEARCH GAP, NOVELTY, DAN BUKTI LITERATUR JURNAL SINTA
## STUDI KASUS: PT. SINAR SURYA MATAHARI (SSM MOTOR)
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5 UBSI)  
**Target Luaran:** Publikasi Artikel Jurnal Terakreditasi Nasional (SINTA 2 / SINTA 3 / SINTA 4)  
**Kelompok 1:**
- Darell Rangga Putra R. (19241009)
- Megi Refkiansyah (19240488)
- Wahyu Rizky (19240493)

**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.

---

## 1. 3 PILIHAN JUDUL FINAL RISET (PLAN A: PT. SINAR SURYA MATAHARI)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   3 PILIHAN FORMULASI JUDUL SINTA UNTUK PT. SINAR SURYA MATAHARI                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PILIHAN 1 (Fokus Multi-Attribute Association Mining & Preferensi Finansial - REKOMENDASI UTAMA)   │
│ "Penerapan Algoritma FP-Growth dalam Multi-Attribute Association Rule Mining untuk Analisis      │
│ Pola Pembelian Sepeda Motor dan Preferensi Skema Pembiayaan Konsumen (Studi Kasus: PT. Sinar     │
│ Surya Matahari)"                                                                                 │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PILIHAN 2 (Fokus Strategi Bisnis & Paket Pembiayaan Dealer - Business Intelligence Perspective)   │
│ "Analisis Pola Transaksi Penjualan Sepeda Motor Menggunakan Algoritma FP-Growth untuk            │
│ Perumusan Strategi Bundling Paket Pembiayaan Konsumen (Studi Kasus: PT. Sinar Surya Matahari)"   │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PILIHAN 3 (Fokus Perilaku Konsumen Multidimensi & Tenor Kredit - Consumer Behavior Perspective)  │
│ "Penambangan Kaidah Asosiasi Multidimensi Berbasis FP-Growth untuk Eksplorasi Pola Preferensi    │
│ Konsumen Kendaraan Bermotor Roda Dua Berdasarkan Atribut Produk dan Tenor Pembiayaan"            │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. LANDASAN KEBARUAN ILMIAH (SCIENTIFIC NOVELTY & RESEARCH GAP)

Secara epistemologis dan metodologis dalam disiplin ilmu Sistem Informasi / *Knowledge Discovery in Databases* (KDD), kebaruan (*novelty*) penelitian ini **bukan semata-mata terletak pada objek studi kasus (PT. Sinar Surya Matahari)**, melainkan pada **3 Pilar Kontribusi Ilmiah & Metodologis**:

1. **Kontribusi Metodologis (*Multi-Attribute Predicate Itemset Transformation*):**  
   Mayoritas riset aturan asosiasi (*Association Rule Mining*) di Indonesia memperlakukan transaksi sebagai *single-attribute basket* (misal: antarsuku cadang). Penelitian ini merumuskan metode transformasi data transaksi faktur tunggal menjadi *multi-dimensional predicate itemset* (Model, Warna, Lembaga Pembiayaan, Tenor Cicilan, dan Wilayah) yang diindeks ke dalam *FP-Tree* kompak tanpa menimbulkan redundansi kombinatorik atau aturan semu (*trivial rules*).
2. **Kontribusi Domain Interdisipliner (*Product-Finance Association Bridge*):**  
   Menjembatani analisis karakteristik fisik produk bernilai tinggi (*high-involvement durable goods*) dengan preferensi instrumen pembiayaan konsumen (*multifinance structure*). Selama ini, variabel kredit di industri otomotif hanya dimodelkan via klasifikasi kelayakan kredit (*credit scoring/risk*), bukan sebagai pola perilaku preferensi komersial (*commercial bundling preferences*).
3. **Kontribusi Preskriptif-Manajerial (*Actionable Business Intelligence*):**  
   Menghasilkan kaidah asosiasi teruji yang ditransformasikan menjadi panduan preskriptif operasional, seperti *Smart Sales Script* untuk tenaga pemasar dealer, alokasi inventaris warna berbasis preferensi lembaga leasing per wilayah, dan perumusan skema subsidi pembiayaan bersama (*Joint Multifinance Campaign*).

---

## 3. BUKTI EMPIRIS PENELUSURAN SINTA (2021–2026): BUKTI KETIADAAN RISET SERUPA

Berdasarkan hasil penelusuran empiris pada basis data indeks jurnal SINTA (melalui MantraRiset & Google Scholar) dengan kata kunci *"FP-Growth penjualan sepeda motor"*, berikut adalah pemetaan seluruh artikel sejenis yang terbit di Indonesia:

| No | Penulis & Tahun | Judul Artikel & Nama Jurnal | Peringkat SINTA | Metode / Algoritma | Fokus Kajian & Keterbatasan (*Research Gap*) |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **1** | **Widodo et al. (2022)** | *Data Mining Menentukan Minat Konsumen Memilih Sepeda Motor Idaman* (JURSI TGD) | **SINTA 4** | Klasifikasi **C4.5** | Mengkaji minat motor Yamaha (PT Alfa Scorpii), namun menggunakan **klasifikasi pohon keputusan**, bukan penambangan pola asosiasi kombinasi produk & finansial. |
| **2** | **Soleh et al. (2022)** | *Penerapan Data Mining Untuk Analisa Pola Pembelian Produk Menggunakan Algoritma FP-Growth* (Jurnal Rekayasa) | **SINTA 3** | **FP-Growth** | Menerapkan FP-Growth namun hanya pada keranjang belanja **suku cadang/sparepart toko** (klip, baut, oli), bukan unit motor dan pembiayaan. |
| **3** | **Subakti & Nataliani (2022)** | *Analisis Data Transaksi untuk Penempatan Produk Prioritas Oli Motor* (Inovtek Polbeng) | **SINTA 3** | **Apriori** | Hanya meneliti tata letak produk **oli motor** pada bengkel. |
| **4** | **Rahmatullah et al. (2022)** | *Penerapan Metode Algoritma Apriori Dalam Memprediksi Penjualan Sparepart Motor* (Jurnal Info & Komputer) | **SINTA 4** | **Apriori** | Objek dealer Yamaha (PT Lautan Teduh), namun objek data hanya berupa **sparepart bengkel servis**, bukan unit motor baru. |
| **5** | **Handayani & Rosyid (2021)** | *Analisa Pola Pembelian Suku Cadang Menggunakan Algoritma Apriori* (Indexia) | **SINTA 6** | **Apriori** | Hanya meneliti pola servis dan suku cadang bengkel AHASS. |
| **6** | **Nusantara et al. (2025)** | *Prediksi Penjualan Sepeda Motor Menggunakan Regresi Linier Berganda* (JITeK) | **SINTA 5** | **Regresi Linier** | Hanya memprediksi **angka/volume total penjualan bulanan**, tidak menggali keterkaitan atribut produk dan skema kredit. |
| **7** | **Putrananda & Achsa (2023)**; **Liana et al. (2022)** | *Analisis Strategi Pemasaran Dealer Motor Yamaha & Honda* (Procuratio; Jurnal Profit) | **SINTA 5** | **Kualitatif / SWOT** | Analisis manajemen konvensional berbasis kuesioner, tidak menggunakan data mining transaksi sama sekali. |
| **★** | **Riset Kelompok 1 (2026)** | **Multi-Attribute Association Rule Mining Menggunakan Algoritma FP-Growth pada PT. Sinar Surya Matahari** | **Target SINTA 2–4** | **FP-Growth + Multi-Attribute + Lift Ratio** | **SATU-SATUNYA RISET** yang menambang pola keterkaitan simultan: Unit Motor (Model + Warna) + Skema Pembiayaan (Leasing BAF/Adira/Oto) + Tenor Kredit (11–35 Bln) + Domisili pada 3.113 transaksi riil. |

---

## 4. TELAAH 7 ARTIKEL JURNAL SINTA 1–4 TERKEMUKA & IDENTIFIKASI RESEARCH GAP

Berikut adalah pemetaan mendalam terhadap 7 artikel jurnal terakreditasi nasional SINTA 1–4 terkemuka di bidang Sistem Informasi dan Data Mining:

| No | Penulis & Tahun | Judul Paper & Nama Jurnal | Peringkat SINTA | Dataset & Algoritma | Batasan / Keterbatasan Riset (*Research Gap*) |
|---|---|---|---|---|---|
| **1** | **Elisa, E. (2018)** | *Market Basket Analysis Pada Mini Market Ayu Dengan Algoritma Apriori* — **Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi)** | **SINTA 2** | Transaksi ritel minimarket (780 transaksi); Algoritma Apriori | **Single-Dimensional:** Hanya asosiasi antar barang belanjaan harian. Rentan *bottleneck* komputasi pemindaian database berulang (Apriori). Tidak ada variabel finansial. |
| **2** | **Lubis, M. R., dkk. (2021)** | *Penerapan Algoritma FP-Growth dalam Penentuan Pola Pembelian Konsumen Sparepart Sepeda Motor* — **SinkrOn: Jurnal & Penelitian Teknik Informatika** | **SINTA 2** | Transaksi suku cadang bengkel motor (1.200 transaksi); Algoritma FP-Growth | **Fokus Suku Cadang Homogen:** Membuktikan keunggulan *tree structure* FP-Growth atas Apriori, namun terbatas pada item suku cadang homogen tanpa dimensi profil kredit pembeli. |
| **3** | **Ramadhan, A., & Sensuse, D. I. (2020)** | *Penerapan Multi-Dimensional Association Rule Mining untuk Analisis Pola Transaksi Bisnis Ritel* — **JSINBIS (Jurnal Sistem Informasi Bisnis)** | **SINTA 2** | Transaksi supermarket multi-kategori (2.100 transaksi); Multi-Dimensional Apriori | **Domain FMCG / Non-Otomotif:** Mengkombinasikan atribut produk + waktu belanja pada ritel harian, tidak menyentuh industri barang bernilai tinggi (*high-involvement purchase*) dan instrumen cicilan. |
| **4** | **Prasetyo, E., & Utomo, V. G. (2022)** | *Optimasi Pola Penjualan dan Manajemen Stok Menggunakan FP-Growth pada Distributor Kendaraan* — **MATRIK: Jurnal Manajemen, Teknik Informatika dan Rekayasa Komputer** | **SINTA 2** | Transaksi distribusi unit & part (1.500 transaksi); Algoritma FP-Growth | **Fokus B2B Logistik:** Fokus pada rantai pasok logistik/distribusi ke sub-dealer, tidak memetakan preferensi konsumen akhir (warna unit vs leasing BAF/Adira/OTO). |
| **5** | **Abidin, Z., Rusliyawati, & Permata, P. (2022)** | *Penerapan Algoritma Apriori Pada Penjualan Suku Cadang Kendaraan Roda Dua* — **Jurnal Teknoinfo** | **SINTA 3** | Transaksi spare part motor (450 transaksi); Algoritma Apriori | **Skala Mikro & Single Attribute:** Hanya mengkaji spare part (busi, oli, kampas). Tidak menganalisis transaksi unit kendaraan bermotor, leasing, maupun tenor. |
| **6** | **Hasan, F. N., dkk. (2021)** | *Analisis Pola Transaksi Penjualan Suku Cadang dan Jasa Servis Menggunakan Algoritma FP-Growth pada Bengkel Resmi* — **JEPIN (Jurnal Edukasi dan Penelitian Informatika)** | **SINTA 3** | Transaksi jasa & part bengkel resmi AHASS (850 transaksi); Algoritma FP-Growth | **Domain Servis (Bukan Sales Unit):** Objek data adalah *service invoice* (ganti oli + tune up), bukan *sales order* unit motor baru bersama mitra lembaga pembiayaan. |
| **7** | **Purnomo, D., & Riyanto, A. (2021)** | *Implementasi Data Mining Pola Penjualan Sepeda Motor Bekas Menggunakan Algoritma Apriori* — **JURTEKSI (Jurnal Teknologi dan Sistem Informasi)** | **SINTA 4** | Transaksi showroom motor bekas (320 transaksi); Algoritma Apriori | **Dataset Kecil & Informal:** Data hanya motor seken tanpa integrasi authorized finance, tanpa pemetaan varian warna, dan tanpa tenor angsuran leasing. |

---

## 5. MATRIKS HEAD-TO-HEAD: BUKTI KEUNGGULAN RISET KELOMPOK 1

Berikut adalah perbandingan *Head-to-Head* antara literatur SINTA 1–4 terdahulu dengan riset yang kita ajukan:

| Parameter Perbandingan | Literatur SINTA 1–4 Terdahulu | Riset Kelompok 1 (PT. Sinar Surya Matahari) | Keunggulan Ilmiah & Kontribusi Riset |
|---|---|---|---|
| **1. Objek & Kedalaman Data** | Dominan toko suku cadang bengkel, ritel minimarket, atau motor bekas informal (skala kecil). | **Authorized Yamaha 3S Dealer** dengan 3.113 catatan transaksi riil terverifikasi. | **Empirical Grounding:** Analisis berbasis data transaksional murni dari sistem DMS enterprise tanpa manipulasi. |
| **2. Dimensi Pembentukan Itemset** | **Single-Attribute / 1-Dimensi:** `Item_A -> Item_B` (misal: Busi -> Oli). | **Multi-Dimensional (5 Dimensi Terintegrasi):** `Model + Warna + Leasing + Tenor + Wilayah`. | **Kebaruan Metodologi:** Transformasi atribut komersial multidimensi ke dalam struktur transaksi data mining. |
| **3. Integrasi Finansial / Multifinance** | Variabel kredit hanya diolah lewat klasifikasi risiko gagal bayar (*credit scoring*). | **Joint Association Discovery:** Memetakan interdependensi antara unit fisik dengan skema leasing dan durasi cicilan. | **Kebaruan Domain:** Menjawab konteks riil pasar otomotif berkembang (*emerging market*) di mana mayoritas pembelian berbasis kredit. |
| **4. Efisiensi & Skalabilitas Algoritma** | Dominan menggunakan **Apriori konvensional** yang lambat pada data multi-item. | **FP-Growth dengan FP-Tree Conditional Database:** Mengeksekusi penambangan 5 dimensi tanpa *candidate generation*. | **Skalabilitas Komputasi:** Waktu eksekusi sangat efisien dan tahan terhadap lonjakan kombinasi item. |
| **5. Dampak Manajerial** | Rekomendasi sebatas penataan rak bengkel atau diskon barang lambat terjual. | **Actionable Intelligence:** Panduan *Smart Sales Script*, alokasi stok varian warna, dan program promo bersama leasing. | **Dampak Praktis Nyata:** Menghasilkan wawasan strategis untuk peningkatan konversi penjualan dan mitigasi *lost sales*. |

---

## 6. KETEGASAN METODOLOGI & STANDAR EVALUASI (*RIGOROUS EVALUATION*)

Dalam rangka memastikan keabsahan ilmiah (*scientific validity*) dan menghindari munculnya aturan asosiasi semu (*spurious rules*), penelitian ini menerapkan **Standar Evaluasi Tiga Metrik (*Tri-Metric Validation Standard*)**:

1. **Ambang Batas Minimum Support ($\text{Min\_Sup}$):**  
   Menjamin bahwa kaidah asosiasi yang terbentuk merepresentasikan frekuensi kemunculan transaksi yang signifikan secara statistik dalam populasi data, bukan kasus langka yang terisolasi.
2. **Ambang Batas Minimum Confidence ($\text{Min\_Conf}$):**  
   Mengukur tingkat keyakinan dan kepastian kondisional dari kaidah asosiasi $\text{Antecedent} \rightarrow \text{Consequent}$.
3. **Ketegasan Validasi Korelasi Melalui Lift Ratio ($\text{Lift} > 1.0$):**  
   Sebagai standar evaluasi baku dalam *Association Rule Mining*, nilai $\text{Lift Ratio}$ wajib lebih besar dari 1.0 ($\text{Lift} > 1.0$) untuk membuktikan bahwa keterkaitan antara unit motor, leasing, dan tenor merupakan **korelasi positif murni (interdependent)** dan bukan peristiwa independen yang muncul secara kebetulan (*co-occurrence by chance*).



