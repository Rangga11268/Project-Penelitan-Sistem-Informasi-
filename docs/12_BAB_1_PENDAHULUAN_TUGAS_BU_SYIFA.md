# BAB I PENDAHULUAN

**Judul Penelitian:**  
**"Penerapan Algoritma FP-Growth dalam *Multi-Attribute Association Rule Mining* untuk Analisis Pola Pembelian Sepeda Motor dan Preferensi Skema Pembiayaan Konsumen (Studi Kasus: PT. Sinar Surya Matahari)"**

**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5)  
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Program Studi:** Sistem Informasi — Fakultas Teknik dan Informatika, Universitas Bina Sarana Informatika (UBSI)  
**Kelompok 1:**
1. **Darell Rangga Putra R.** (NIM: 19241009)
2. **Megi Refkiansyah** (NIM: 19240488)
3. **Wahyu Rizky** (NIM: 19240493)

---

## 1. LATAR BELAKANG (BACKGROUND)

Industri otomotif roda dua di Indonesia merupakan salah satu sektor penggerak ekonomi retail terbesar dengan volume transaksi jutaan unit per tahun. Dalam proses bisnis jaringan dealer resmi (*authorized dealer*), transaksi sepeda motor tergolong sebagai transaksi barang tahan lama dengan keterlibatan keputusan tinggi (*high-involvement durable goods purchase*). Pada transaksi bernilai tinggi ini, keputusan konsumen tidak hanya dipengaruhi oleh preferensi karakteristik fisik kendaraan (seperti tipe motor, varian mesin, dan pilihan warna), melainkan sangat bergantung pada ketersediaan instrumen fasilitas pembiayaan konsumen (*consumer financing / multifinance leasing*). Data industri menunjukkan bahwa lebih dari 75% transaksi pembelian sepeda motor baru di Indonesia dilakukan melalui skema kredit bertahap.

PT. Sinar Surya Matahari merupakan dealer resmi sepeda motor Yamaha yang melayani penjualan unit baru, suku cadang, dan jasa perawatan. Dalam operasional hariannya, perusahaan mencatatkan ribuan transaksi penjualan yang melibatkan interaksi multi-pihak antara pihak dealer, calon pembeli, serta berbagai mitra lembaga pembiayaan resmi (seperti Bussan Auto Finance / BAF, Adira Dinamika Multi Finance, dan OTO Multiartha). Namun, data riwayat transaksi penjualan yang tersimpan di dalam basis data *Dealer Management System* (DMS) selama ini hanya berfungsi sebagai arsip pencatatan administratif dan pelaporan akuntansi periodik. Data tersebut belum dimanfaatkan secara optimal sebagai aset strategis untuk mengekstraksi wawasan pengetahuan (*knowledge discovery*).

Ketiadaan analisis data berbasis pola transaksi historis menimbulkan sejumlah permasalahan nyata di tingkat operasional dan manajerial dealer. Pertama, fenomena *lost sales* akibat kegagalan negosiasi kredit (*price shock*), di mana calon pembeli membatalkan pesanan karena tenaga pemasar (*sales counter*) secara keliru menawarkan simulasi tenor cicilan atau lembaga pembiayaan yang tidak sesuai dengan daya bayar karakteristik segmen konsumen motor tersebut. Kedua, terjadinya *leasing mismatch*, yaitu ketidakcocokan antara profil pembeli tipe motor tertentu dengan karakteristik persetujuan kredit lembaga pembiayaan yang diajukan, sehingga memperpanjang siklus verifikasi dan meningkatkan rasio penolakan (*rejection rate*). Ketiga, terjadinya ketidakseimbangan persediaan (*inventory imbalance*) varian warna dan model motor antar-cabang wilayah karena alokasi unit masih dilakukan secara perkiraan manual tanpa mempertimbangkan preferensi lokal konsumen.

Oleh karena itu, diperlukan penerapan teknik *Data Mining*, khususnya *Association Rule Mining* (penambangan kaidah asosiasi), untuk membedah keterkaitan tersembunyi antara pilihan produk fisik kendaraan dengan preferensi skema pembiayaan konsumen. Dengan memanfaatkan algoritma *Frequent Pattern Growth* (FP-Growth), ribuan riwayat transaksi faktur dapat diproses secara efisien untuk menemukan pola kombinasi terkuat guna mendukung perumusan strategi penjualan cerdas (*smart sales script*), perencanaan promosi bersama lembaga pembiayaan, dan optimalisasi alokasi inventaris dealer.

---

## 2. TINJAUAN PUSTAKA SINGKAT (LITERATURE REVIEW)

Perkembangan penelitian *Association Rule Mining* (ARM) dalam disiplin ilmu Sistem Informasi dan *Knowledge Discovery in Databases* (KDD) selama 3 hingga 5 tahun terakhir (2021–2025) menunjukkan kemajuan pesat dalam pemanfaatan algoritma penambangan pola frekuensi transaksi (*Frequent Pattern Mining*).

Penelitian terdahulu yang dilakukan oleh **Widodo et al. (2022)** pada dealer resmi sepeda motor Yamaha (PT. Alfa Scorpii Medan) telah menerapkan teknik *data mining* untuk mengidentifikasi minat konsumen dalam memilih tipe sepeda motor, namun penelitian tersebut menggunakan algoritma klasifikasi pohon keputusan (C4.5) yang bersifat memprediksi kelas label tunggal, bukan menambang aturan kombinasi antar-variabel transaksi. Sementara itu, kajian penerapan algoritma asosiasi pada sektor otomotif di jurnal nasional terakreditasi SINTA sebagian besar masih terfokus pada ranah purna jual dan suku cadang (*aftersales & spare parts*). Sebagai contoh, **Soleh et al. (2022)** menerapkan algoritma FP-Growth untuk menganalisis keranjang belanja suku cadang pada toko onderdil, **Subakti & Nataliani (2022)** menggunakan algoritma Apriori untuk penempatan produk oli motor, dan **Rahmatullah et al. (2022)** memanfaatkan Apriori untuk memprediksi penjualan *sparepart* pada dealer PT. Lautan Teduh Interniaga Kotabumi. Penelitian-penelitian tersebut membuktikan keandalan kaidah asosiasi dalam penataan stok barang homogen bernilai rendah, namun belum menjangkau analisis transaksi unit kendaraan utuh.

Di sisi lain, penelitian mutakhir mengenai perbandingan efisiensi algoritma penambangan asosiasi secara konsisten menegaskan keunggulan algoritma FP-Growth dibandingkan algoritma Apriori klasik. **Rahman & Riana (2025)** serta **Rachmawati et al. (2024)** membuktikan bahwa FP-Growth memiliki efisiensi komputasi dan pemanfaatan memori yang jauh lebih unggul karena menggunakan struktur pohon kompak (*FP-Tree*) dan pembentukan basis pola kondisional (*Conditional Pattern Base*), sehingga mengeliminasi *bottleneck* pemindaian basis data berulang kali serta menghindari pembentukan kandidat itemset kombinatorik yang membebani memori (*candidate generation bottleneck*). Lebih lanjut, **Saptadi et al. (2023)** dan **Muharam et al. (2025)** menerapkan penambangan asosiasi pada data transaksi ritel harian (*Fast-Moving Consumer Goods* / FMCG) dan F&B, namun penelitian-penelitian tersebut masih menerapkan model transaksi satu dimensi (*single-attribute itemset*) yang hanya menghubungkan nama barang konsumsi instan.

Mengenai penambangan data multi-atribut, **Ramadhan & Sensuse (2020)** dalam publikasinya di *Jurnal Sistem Informasi Bisnis (JSINBIS)* memformulasikan konsep *Multi-Dimensional Association Rule Mining* pada bisnis ritel untuk menggabungkan atribut produk dengan dimensi waktu belanja. Landasan metodologis ini membuka peluang pengembangan lebih lanjut untuk mengintegrasikan variabel non-komoditas ke dalam struktur keranjang transaksi data mining.

---

## 3. RUMUSAN MASALAH & CELAH PENELITIAN (RESEARCH GAP)

### 3.1 Rumusan Masalah
Berdasarkan konteks latar belakang dan permasalahan bisnis yang dihadapi oleh PT. Sinar Surya Matahari, rumusan masalah dalam penelitian ini adalah:
1. Bagaimana mentransformasikan data transaksi penjualan faktur tunggal PT. Sinar Surya Matahari menjadi representasi keranjang transaksi multi-atribut (*multi-attribute predicate basket*) yang terstruktur tanpa menimbulkan aturan asosiasi semu (*spurious/trivial rules*)?
2. Bagaimana menerapkan algoritma *Frequent Pattern Growth* (FP-Growth) untuk mengekstraksi kaidah asosiasi yang menghubungkan model motor, varian warna, lembaga pembiayaan (*leasing*), tenor angsuran, dan wilayah domisili konsumen?
3. Bagaimana menguji validitas dan kekuatan kaidah asosiasi yang terbentuk menggunakan evaluasi tiga metrik (*Support*, *Confidence*, dan *Lift Ratio* > 1.0)?
4. Bagaimana merumuskan rekomendasi strategi bisnis terapan (*smart sales script*, program promo bersama leasing, dan manajemen stok wilayah) berdasarkan kaidah asosiasi yang valid?

### 3.2 Celah Penelitian (*Research Gap*)
Berdasarkan pemetaan literatur nasional dan internasional terkini, ditemukan celah penelitian (*research gap*) yang nyata:
* **Kesenjangan Domain (*Domain Gap*):** Riset aturan asosiasi di industri kendaraan bermotor selama ini hampir 90% terbatas pada keranjang belanja onderdil/suku cadang bernilai murah (*low-ticket spare parts*) atau jasa servis berkala. Belum ada penelitian yang menambang pola keterkaitan transaksi penjualan unit baru sepeda motor pada dealer resmi.
* **Kesenjangan Dimensi Finansial (*Product-Finance Integration Gap*):** Dalam literatur data mining perbankan dan multifinance, variabel pembiayaan konsumen (kredit, leasing, tenor) hampir selalu diteliti menggunakan algoritma klasifikasi risiko gagal bayar (*credit scoring/risk modeling* seperti C4.5, Naive Bayes, atau Regresi Logistik). Belum ada penelitian di jurnal terakreditasi yang memodelkan skema leasing dan durasi tenor sebagai dimensi preferensi komersial yang berasosiasi langsung dengan atribut fisik unit kendaraan.
* **Kesenjangan Metodologis (*Multi-Attribute Structure Gap*):** Mayoritas riset asosiasi masih bertumpu pada *single-attribute itemset* (`Item A -> Item B`). Penelitian yang mengintegrasikan 5 dimensi atribut heterogen (Model Kendaraan, Warna, Lembaga Leasing, Tenor Cicilan, dan Domisili) ke dalam struktur pohon *FP-Tree* pada data skala *enterprise* masih sangat langka.

---

## 4. KEBARUAN (NOVELTY) & SOLUSI YANG DITAWARKAN

### 4.1 Kebaruan Penelitian (*Scientific Novelty*)
Penelitian ini menawarkan 3 (tiga) pilar kebaruan ilmiah dan metodologis dalam bidang Sistem Informasi dan Penambangan Data:

1. **Kebaruan Metodologis (*Multi-Attribute Predicate Itemset Transformation*):**  
   Mengembangkan kerangka kerja transformasi data faktur penjualan tunggal menjadi entitas *predicate transaction basket* multidimensi. Metode ini secara sistematis memetakan atribut kategorikal heterogen ke dalam format biner terindeks, sehingga algoritma FP-Growth dapat mengekstrak kaidah asosiasi lintas-dimensi tanpa menghasilkan aturan absurd seperti `{Mio} -> {NMAX}` (karena satu faktur fisik hanya membeli 1 unit motor).
2. **Kebaruan Integrasi Domain (*Product-Finance Association Modeling*):**  
   Menjadi penelitian pionir yang menjembatani karakteristik fisik produk bernilai tinggi (*high-involvement durable goods*) dengan preferensi instrumen pembiayaan konsumen (*multifinance structure*). Pendekatan ini memperlakukan skema kredit (BAF, Adira, OTO, Cash) dan rentang tenor (11, 23, 30, 35 bulan) sebagai bagian integral dari pola perilaku keputusan pembelian konsumen.
3. **Kebaruan Preskriptif-Manajerial (*Actionable Business Intelligence*):**  
   Menghasilkan kaidah asosiasi yang ditransformasikan secara langsung menjadi solusi preskriptif manajerial tingkat operasional, meliputi:
   * Penyusunan panduan penjualan cerdas (*Smart Sales Script*) bagi tenaga penjual counter dealer.
   * Perumusan program promosi bersama dealer dan lembaga pembiayaan (*Joint Multifinance Bundling Campaign*).
   * Rekomendasi alokasi kuota unit dan varian warna per wilayah cabang pemasaran.

### 4.2 Solusi yang Ditawarkan
Solusi yang ditawarkan dalam penelitian ini adalah mengimplementasikan algoritma FP-Growth berbasis metodologi standar *Cross-Industry Standard Process for Data Mining* (CRISP-DM) yang dievaluasi secara ketat menggunakan metrik *Support*, *Confidence*, dan *Lift Ratio* ($\text{Lift} > 1.0$) untuk menjamin bahwa seluruh aturan yang dihasilkan merepresentasikan dependensi korelasi positif murni dan bukan kejadian acak (*co-occurrence by chance*).

---

## 5. RUANG LINGKUP PENELITIAN (SCOPE & LIMITATIONS)

Untuk menjaga fokus penelitian dan menjamin kedalaman analisis, ruang lingkup dan batasan penelitian ditetapkan sebagai berikut:

1. **Objek Penelitian:**  
   Penelitian dilakukan pada **PT. Sinar Surya Matahari (SSM Motor)**, dealer resmi sepeda motor Yamaha (Layanan 3S: *Sales, Service, Sparepart*).
2. **Sumber dan Volume Data:**  
   Dataset yang digunakan adalah data transaksi riil penjualan unit sepeda motor baru bersumber dari basis data *Dealer Management System* (DMS) internal perusahaan sebanyak **3.113 catatan transaksi empiris**.
3. **Periode Waktu Data:**  
   Data transaksi mencakup rentang waktu operasional aktif triwulan ketiga, yaitu **bulan Juni hingga Agustus 2026**.
4. **Variabel dan Atribut Penelitian:**  
   Penelitian dibatasi pada 5 (lima) dimensi atribut transaksi utama, yaitu:
   * **Model / Tipe Sepeda Motor:** Kategori Matic Premium (NMAX Series, Aerox Series, XMAX), Matic Classy (Fazzio Hybrid, Grand Filano Hybrid), Matic Standar/Entry (Mio M3, Gear 125), serta segmen Sport dan Moped.
   * **Varian Warna Kendaraan:** Karakteristik visual unit (Matte Black, Metallic Red, Cyan, Silver, White, dll.).
   * **Lembaga Pembiayaan (*Financing Method*):** Metode pembayaran Tunai (*CASH*) dan Lembaga Pembiayaan Kredit (*BAF, ADIRA Finance, OTO Multiartha*).
   * **Tenor Pembiayaan:** Durasi angsuran kredit konsumen (11 bulan, 23 bulan, 30 bulan, dan 35 bulan).
   * **Wilayah Domisili Konsumen:** Lokasi administratif pembeli pada cakupan wilayah pemasaran dealer (Jabodetabek: Jakarta Timur, Jakarta Selatan, Jakarta Barat, Bekasi Kota, Bekasi Kabupaten, Depok, Bogor, Tangerang).
5. **Batasan Algoritma & Pengujian:**  
   Algoritma yang digunakan adalah **Frequent Pattern Growth (FP-Growth)**. Evaluasi aturan asosiasi dibatasi pada aturan yang memenuhi nilai ambang batas minimum yang ditentukan (*Minimum Support & Confidence*) serta wajib memiliki nilai **Lift Ratio > 1.0**.

---

## 6. TUJUAN PENELITIAN (RESEARCH OBJECTIVES)

Tujuan yang ingin dicapai melalui pelaksanaan penelitian ini adalah:

1. **Tujuan Metodologis:**  
   Menerapkan dan menguji performa algoritma FP-Growth dalam mengekstraksi aturan asosiasi dari dataset transaksi penjualan multi-atribut (*Multi-Attribute Association Rule Mining*) pada data transaksional skala korporasi dealer sepeda motor.
2. **Tujuan Eksploratif & Analitis:**  
   Mengidentifikasi pola kombinasi dan keterkaitan yang kuat antara tipe model sepeda motor, varian warna, lembaga pembiayaan (*multifinance*), durasi tenor kredit, dan wilayah domisili pembeli berdasarkan 3.113 transaksi riil PT. Sinar Surya Matahari.
3. **Tujuan Evaluatif:**  
   Menganalisis dan memvalidasi kekuatan kaidah asosiasi yang terbentuk berdasarkan standar pengujian *Support*, *Confidence*, dan *Lift Ratio* ($\text{Lift} > 1.0$) guna memastikan aturan yang diekstrak memiliki signifikansi statistik yang valid.
4. **Tujuan Terapan & Manajerial:**  
   Menghasilkan rekomendasi strategis berbasis data (*data-driven strategic recommendations*) bagi manajemen PT. Sinar Surya Matahari berupa panduan skrip penjualan terarah (*Smart Sales Script*), formulasi paket promosi kredit gabungan, serta optimalisasi distribusi stok unit antar-wilayah guna meningkatkan efisiensi operasional dan meminimalkan tingkat kegagalan penjualan (*lost sales*).
5. **Tujuan Luaran Ilmiah:**  
   Menghasilkan artikel ilmiah berkualitas standar publikasi pada **Jurnal Nasional Terakreditasi SINTA (SINTA 2 / SINTA 3 / SINTA 4)** atau Prosiding Seminar Nasional di bidang Sistem Informasi dan Ilmu Komputer.
