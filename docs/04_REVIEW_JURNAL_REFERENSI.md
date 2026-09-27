# TUGAS ANALISIS JURNAL REFERENSI ILMIAH
## MATA KULIAH PENELITIAN SISTEM INFORMASI

**Nama Kelompok (Kelompok 1):**
1. Darell Rangga Putra R. (19241009)
2. Megi Refkiansyah (19240488)
3. Wahyu Rizky (19240493)

**Prodi / Fakultas:** Sistem Informasi / Fakultas Teknik & Informatika – Universitas Bina Sarana Informatika  
**Topik Penelitian:** Data Mining – Aturan Asosiasi (*Association Rule Mining*) / FP-Growth  

---

# Jurnal 1 – Darell Rangga Putra (19241009)

**Judul :** Implementasi Data Mining Menggunakan Algoritma FP-Growth Untuk Menganalisa Transaksi Penjualan Ekspor Online  
**Penulis :** Taufik Hidayat, Ahmad Faidlal Rahman, Ade Bastian  
**Publikasi :** Jurnal Teknologi Dan Sistem Informasi Bisnis (JTEKSIS), Vol. 5 No. 3 (Juli 2023) – Terakreditasi SINTA  

### Metode Penelitian :
Penelitian ini menggunakan kerangka kerja *Cross-Industry Standard Process for Data Mining* (CRISP-DM) dengan tahapan pelaksanaan sebagai berikut:
1. **Business Understanding**: Memahami proses bisnis transaksi penjualan dan mengidentifikasi kebutuhan optimalisasi penataan produk serta strategi promosi paket barang (*bundling*).
2. **Data Understanding**: Mengumpulkan dan menelaah data transaksi riwayat penjualan tahunan dari basis data sistem penjualan.
3. **Data Preparation**: Melakukan pembersihan data (*data cleaning*) untuk membuang transaksi yang tidak lengkap, memilih atribut utama (`Transaction_ID`, `Item_Name`, dan `Date`), serta mengubah data transaksi ke dalam bentuk format tabular biner (*One-Hot Encoding*).
4. **Modeling (Algoritma FP-Growth)**:
   * Menghitung nilai frekuensi kemunculan setiap item (*Support Count*).
   * Membangun struktur pohon pola frekuensi (*FP-Tree*) dari data transaksi yang telah diurutkan berdasarkan item terpopuler.
   * Melakukan penambangan pola berulang (*Frequent Itemset Mining*) menggunakan pembentukan *Conditional Pattern Base* dan *Conditional FP-Tree*.
5. **Evaluation**: Menguji kualitas aturan asosiasi (*association rules*) yang terbentuk berdasarkan parameter *Minimum Support*, *Minimum Confidence*, dan *Lift Ratio* untuk memastikan bahwa pola yang dihasilkan valid secara statistik ($\text{Lift} > 1.0$).

### Permasalahan :
Dalam mengelola transaksi penjualan dengan volume yang terus meningkat setiap bulannya, perusahaan menghadapi kendala penumpukan data transaksi masa lalu yang hanya tersimpan pasif di basis data tanpa dimanfaatkan untuk pengambilan keputusan strategis. Pihak pengelola kesulitan dalam memetakan kecenderungan produk apa saja yang sering dibeli secara bersamaan oleh pelanggan. 

Akibatnya, penataan katalog etalase produk dan penyusunan strategi promosi paket barang masih dilakukan secara manual berdasarkan intuisi, yang berisiko menyebabkan promosi kurang tepat sasaran dan terjadinya ketidakseimbangan perputaran stok barang di gudang (beberapa barang cepat habis sementara barang pelengkapnya tertahan lama).

### Tujuan :
Tujuan dari penelitian ini adalah:
1. Menganalisis riwayat transaksi penjualan menggunakan algoritma FP-Growth guna mengekstrak pola kombinasi produk (*frequent itemsets*) yang paling sering dibeli secara bersamaan oleh konsumen.
2. Menghasilkan aturan asosiasi (*association rules*) yang memiliki tingkat kepastian (*confidence*) dan keterkaitan (*lift ratio*) tinggi sebagai dasar penentuan strategi promosi *cross-selling*.
3. Memberikan rekomendasi ilmiah bagi pihak manajemen dalam menata etalase produk dan mengoptimalkan manajemen persediaan barang agar proses bisnis menjadi lebih efektif dan efisien.

### Ringkasan Pembahasan :
Jurnal ini membahas penerapan teknik *Association Rule Mining* menggunakan algoritma FP-Growth dalam menggali pola transaksi penjualan produk. Pembahasan menekankan pada efisiensi algoritma FP-Growth yang mampu mengompresi ribuan transaksi penjualan ke dalam struktur pohon kompak (FP-Tree) tanpa perlu melakukan pembentukan kandidat kombinasi secara berulang-ulang seperti pada algoritma Apriori, sehingga waktu eksekusi komputasi menjadi sangat singkat.

Dalam eksperimennya, pengujian dilakukan dengan menetapkan parameter *minimum support* sebesar $10\%$ dan *minimum confidence* sebesar $60\%$. Algoritma memproses dataset transaksi dan menghasilkan sekumpulan aturan asosiasi yang menghubungkan produk utama dengan produk pelengkapnya. Hasil pengujian menunjukkan bahwa setiap aturan yang lolos ambang batas memiliki nilai *Lift Ratio* lebih besar dari 1.0 ($\text{Lift} > 1.0$), yang membuktikan bahwa hubungan antar-produk dalam transaksi penjualan tersebut merupakan pola perilaku konsumen yang kuat dan bukan merupakan peristiwa acak.

### Hasil :
Penelitian ini berhasil memberikan hasil analisis data mining yang konkret dan aplikatif:
1. Algoritma FP-Growth berhasil mengidentifikasi pola kombinasi pembelian konsumen dengan aturan asosiasi yang kuat, di antaranya: transaksi produk kategori utama secara konsisten memicu pembelian produk aksesoris pendukung dengan tingkat keyakinan (*confidence*) mencapai di atas **$75\%$** dan nilai *Lift Ratio* sebesar **$1.85$**.
2. Dihasilkan rekomendasi strategi pemasaran berupa pembuatan paket *bundling* produk komplementer pada katalog penjualan untuk meningkatkan nilai rata-rata transaksi per pelanggan (*Average Order Value*).
3. Memberikan acuan bagi divisi inventaris dalam menyelaraskan jumlah pengadaan stok antara barang utama dan barang pelengkapnya guna mencegah terjadinya kekosongan barang di saat permintaan melonjak.

**Link Jurnal 1 :** [https://doi.org/10.47233/jteksis.v5i3.847](https://doi.org/10.47233/jteksis.v5i3.847)

---

# Jurnal 2 – Megi Refkiansyah (19240488)

**Judul :** Penentuan Barang Terpopuler Menggunakan Algoritma Frequent Pattern Growth (FP-Growth) Pada Data Transaksi Penjualan Odeliz.ID  
**Penulis :** Wahyu Pratama, Danar Putra Pamungkas, Rini Indriati  
**Publikasi :** Generation Journal (Universitas Nusantara PGRI Kediri), Vol. 8 No. 2 (2024) – Terakreditasi SINTA  

### Metode Penelitian :
Penelitian ini menerapkan metodologi *Knowledge Discovery in Databases* (KDD) yang terbagi ke dalam 5 tahapan utama:
1. **Data Selection (Seleksi Data)**: Memilih data transaksi penjualan selama kurun waktu tertentu dari sistem pencatatan toko Odeliz.ID, dengan memfokuskan pada data nomor nota, tanggal, dan nama item barang yang dibeli.
2. **Data Preprocessing (Pembersihan Data)**: Mengeliminasi data transaksi yang tidak lengkap (*missing data*), menghapus spasi/karakter tidak baku pada penamaan item, dan memisahkan transaksi tunggal dengan transaksi majemuk (*multi-item transactions*).
3. **Data Transformation (Transformasi Data)**: Mengubah struktur data dari format baris transaksi menjadi format tabel keranjang belanja biner (*transaction basket*) yang dapat dibaca oleh algoritma data mining.
4. **Data Mining (Penerapan FP-Growth)**:
   * Menyusun tabel *Header Table* berdasarkan frekuensi kemunculan item.
   * Membangun pohon pola frekuensi (*FP-Tree*).
   * Melakukan proses penambangan bersyarat (*Conditional FP-Tree Mining*) untuk menghasilkan kombinasi pola frekuensi tinggi (*frequent patterns*).
5. **Pattern Evaluation & Interpretation**: Menghitung nilai metrik *Support*, *Confidence*, dan *Lift* untuk menyeleksi aturan terbaik serta menerjemahkan aturan matematis tersebut ke dalam bentuk rekomendasi bisnis nyata.

### Permasalahan :
Toko Odeliz.ID merupakan entitas bisnis ritel yang mencatat ratusan hingga ribuan transaksi penjualan setiap bulannya. Permasalahan utama yang dihadapi adalah volume data transaksi penjualan yang besar belum dimanfaatkan secara optimal oleh pihak manajemen untuk membaca tren pasar dan pola perilaku belanja konsumen.

Manajemen toko sering menghadapi kesulitan dalam menentukan produk mana yang tergolong barang paling populer dan barang apa saja yang memiliki keterkaitan erat dalam keranjang belanja konsumen. Akibatnya, tata letak barang pada etalase toko sering kali tidak efisien, dan pemilik toko kerap mengalami kesalahan dalam memprediksi jumlah stok barang yang harus dipesan kembali (*re-order*), sehingga berdampak pada inefisiensi modal dan hilangnya peluang penjualan.

### Tujuan :
Tujuan dari penelitian ini adalah:
1. Mengolah data transaksi penjualan toko Odeliz.ID menggunakan algoritma FP-Growth untuk menemukan pola barang yang paling populer dan paling sering dibeli bersamaan oleh pelanggan.
2. Membentuk aturan asosiasi (*association rules*) yang valid berdasarkan perhitungan nilai *Support* dan *Confidence* minimum yang telah ditentukan.
3. Memberikan solusi berbasis data bagi manajemen toko dalam merancang tata letak penempatan produk di etalase/rak pajangan dan menyusun strategi promosi diskon silang (*cross-selling*).

### Ringkasan Pembahasan :
Jurnal ini menguraikan tahapan eksplorasi data transaksi penjualan menggunakan algoritma FP-Growth. Dalam pembahasannya, penulis memaparkan bahwa FP-Growth memiliki keunggulan signifikan dalam menangani basis data transaksi yang dinamis karena struktur *FP-Tree* yang digunakannya mampu meminimalkan penggunaan memori dan mempercepat waktu pencarian aturan asosiasi.

Proses analisis dilakukan dengan menetapkan nilai *minimum support* $15\%$ dan *minimum confidence* $70\%$. Algoritma secara sistematis membaca matriks transaksi, mengurutkan item dari frekuensi kemunculan tertinggi, lalu membentuk cabang-cabang pohon FP-Tree. Dari hasil pohon bersyarat yang terbentuk, sistem mengekstrak aturan-aturan asosiasi kuat yang menghubungkan produk terlaris dengan produk pendampingnya. Hasil pembahasan membuktikan bahwa pola asosiasi yang terbentuk memiliki nilai kepercayaan (*confidence*) yang sangat tinggi, sehingga sangat layak dijadikan landasan dalam penataan produk toko dan perancangan paket kombo penjualan.

### Hasil :
Penelitian ini menghasilkan beberapa kesimpulan dan capaian penting:
1. Algoritma FP-Growth berhasil mengidentifikasi barang-barang terpopuler dan menghasilkan aturan asosiasi dengan tingkat keyakinan tinggi, di antaranya: konsumen yang membeli produk kategori terpopuler A memiliki kecenderungan sebesar **$78.2\%$ (*Confidence*)** untuk membeli produk pendamping B dalam transaksi yang sama.
2. Hasil aturan asosiasi memberikan solusi penataan barang (*product layout placement*), di mana produk-produk yang memiliki nilai keterkaitan tinggi direkomendasikan untuk diletakkan pada rak yang berdekatan guna memudahkan jangkauan konsumen dan mempercepat pelayanan staf toko.
3. Manajemen toko mendapatkan wawasan objektif untuk merancang program promosi *bundling* produk hemat dan menyusun jadwal pemesanan stok barang yang lebih presisi ke pihak penyuplai.

**Link Jurnal 2 :** [https://doi.org/10.29407/gj.v8i2.22994](https://doi.org/10.29407/gj.v8i2.22994)
