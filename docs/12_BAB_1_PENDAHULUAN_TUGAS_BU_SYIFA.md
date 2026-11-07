# BAB I PENDAHULUAN

**Judul Penelitian:**  
**"Multi-Attribute Association Rule Mining Menggunakan Algoritma FP-Growth: Analisis Pola Pembelian dan Preferensi Pembiayaan Konsumen Sepeda Motor"**  
*(Studi Kasus: PT. Sinar Surya Matahari)*

**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5)  
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Program Studi:** Sistem Informasi — Fakultas Teknik dan Informatika, Universitas Bina Sarana Informatika (UBSI)  
**Kelompok 1:**
1. **Darell Rangga Putra R.** (NIM: 19241009)
2. **Megi Refkiansyah** (NIM: 19240488)
3. **Wahyu Rizky** (NIM: 19240493)

---

## 1.1 LATAR BELAKANG
Data transaksi penjualan merupakan salah satu aset informasi krusial yang dapat dioptimalkan perusahaan untuk mendukung pengambilan keputusan strategis. Data tersebut tidak hanya berfungsi sebagai rekam jejak historis, tetapi juga menyimpan pola pembelian dan keterkaitan antaratribut produk yang tersembunyi. Oleh karena itu, diperlukan teknik pengolahan data yang mampu mengekstraksi wawasan berharga bagi perusahaan, salah satunya melalui pendekatan *Data Mining* dengan metode *Association Rule Mining*.

PT. Sinar Surya Matahari (SSM Motor), sebagai dealer resmi sepeda motor Yamaha (layanan 3S: *Sales, Service, Sparepart*) di wilayah Jabodetabek, memiliki akumulasi data transaksi penjualan unit kendaraan yang masif. Sepanjang periode aktif operasional Juni hingga Agustus 2026, tercatat sebanyak 3.113 data faktur transaksi penjualan riil di sistem *Dealer Management System* (DMS). Data ini mencakup lima dimensi atribut utama: model sepeda motor, varian warna, metode pembayaran atau lembaga pembiayaan (*multifinance*), tenor angsuran kredit, dan wilayah domisili konsumen. Namun, selama ini data tersebut hanya mengendap sebagai arsip administratif tanpa dianalisis lebih lanjut. Akibatnya, dealer menghadapi kendala operasional seperti pramuniaga yang salah menawarkan simulasi cicilan sehingga memicu pembatalan pembelian (*price shock & lost sales*), ketidaksesuaian pengajuan lembaga pembiayaan (*leasing mismatch*), serta ketidakseimbangan distribusi alokasi stok varian warna antarcabang (*inventory imbalance*).

Penerapan metode asosiasi dalam industri otomotif telah dilakukan oleh beberapa studi terdahulu. Soleh et al. (2022) menerapkan algoritma FP-Growth pada Avindo Motor dan berhasil mengidentifikasi kombinasi item suku cadang yang paling sering dibeli bersamaan (seperti oli mesin dan busi), namun penelitian tersebut terbatas pada barang bernilai rendah (*low-involvement goods*) dan tidak mengkaji transaksi unit kendaraan baru. Sementara itu, Salu et al. (2022) menganalisis pola penjualan sepeda motor pada dealer Yamaha Jaya Baru Motor dan menemukan preferensi model terlaris, namun penelitian tersebut hanya menggunakan data satu dimensi (*single-attribute*) tanpa mengintegrasikan skema pembiayaan kredit maupun durasi tenor cicilan konsumen.

Untuk melengkapi keterbatasan penelitian sebelumnya, penelitian ini menerapkan algoritma *Frequent Pattern Growth* (FP-Growth) berbasis *Multi-Attribute Association Rule Mining* pada 3.113 data faktur PT. Sinar Surya Matahari. Hasil ekstraksi pola asosiasi ini ditujukan untuk menghasilkan wawasan berbasis data (*data-driven*) berupa panduan penjualan cerdas (*Smart Sales Script*) bagi pramuniaga, optimasi alokasi persediaan varian warna antargudang cabang, serta perumusan paket promosi pembiayaan bersama lembaga rekanan.

---

## 1.2 TINJAUAN PUSTAKA

Algoritma *Frequent Pattern Growth* (FP-Growth) merupakan metode penambangan aturan asosiasi (*Association Rule Mining*) yang dirancang untuk menemukan pola kombinasi item yang sering muncul bersamaan dalam suatu basis data transaksi secara efisien (Han, Pei, & Tong, 2022). Algoritma ini bekerja dengan cara memadatkan seluruh rekaman data transaksi ke dalam struktur pohon di memori (*in-memory tree*) yang disebut *Frequent Pattern Tree* (FP-Tree) hanya melalui dua kali pemindaian data (*2-pass scan*) (Tan, Steinbach, Karpatne, & Kumar, 2018).

Fungsi utama dari algoritma FP-Growth adalah mengekstraksi kaidah asosiasi secara langsung melalui pembentukan basis pola bersyarat (*Conditional Pattern Base*) menggunakan pendekatan *divide-and-conquer* tanpa melalui tahapan pembangkitan kombinasi kandidat (*zero candidate generation*) (Zaki & Meira, 2020). Karakteristik ini membuat FP-Growth memiliki keunggulan signifikan dalam kecepatan waktu komputasi dan efisiensi penggunaan memori dibandingkan algoritma klasik Apriori, khususnya saat diterapkan untuk menambang pola keterikatan pada data transaksi berdimensi majemuk (*multi-attribute*).

---

## 1.3 CELAH PENELITIAN & RUMUSAN MASALAH

### 1.3.1 Celah Penelitian (Research Gap)
Berdasarkan kajian komprehensif terhadap literatur jurnal nasional terakreditasi SINTA dalam rentang waktu 2021 hingga 2026, teridentifikasi tiga celah penelitian (*research gap*) utama. Pertama, dari aspek ranah kajian (*domain gap*), mayoritas penelitian aturan asosiasi pada sektor otomotif terdahulu hanya berfokus pada transaksi suku cadang murah bengkel (*low-involvement goods*) dan belum pernah mengeksplorasi transaksi penjualan unit fisik sepeda motor baru bernilai tinggi (*high-involvement durable goods*). Kedua, dari aspek integrasi instrumen finansial (*product-finance gap*), penelitian pembiayaan perbankan selama ini umumnya hanya menggunakan algoritma klasifikasi seperti C4.5 untuk memprediksi risiko kredit macet secara defensif dan buta terhadap jenis produk, sehingga belum ada studi yang memodelkan keterikatan tipe motor fisik dengan preferensi lembaga *leasing* dan durasi tenor secara komersial-ofensif. Ketiga, dari aspek struktur data (*multi-attribute gap*), publikasi terdahulu masih bertumpu pada relasi satu dimensi (*single-attribute*), padahal pada transaksi fisik dealer motor, satu lembar faktur hanya memuat satu unit kendaraan sehingga secara mutlak memerlukan skema representasi keranjang transaksi multi-atribut lima dimensi.

### 1.3.2 Rumusan Masalah
Berdasarkan latar belakang dan celah penelitian tersebut, rumusan masalah dalam penelitian ini dirumuskan sebagai berikut:
1. Bagaimana mentransformasikan data faktur transaksi penjualan tunggal (*single-unit sales*) pada PT. Sinar Surya Matahari menjadi format keranjang transaksi multi-atribut (*multi-attribute predicate basket*) tanpa memicu kaidah asosiasi semu (*spurious rules*)?
2. Bagaimana menguji validitas dan signifikansi keterikatan kaidah asosiasi multi-atribut yang dihasilkan menggunakan evaluasi metrik *Support*, *Confidence*, dan *Lift Ratio* > 1,0?
3. Bagaimana merumuskan rekomendasi strategi bisnis preskriptif (*Smart Sales Script*, alokasi persediaan varian warna berbasis wilayah, dan program bundling pembiayaan) dari kaidah asosiasi yang terbukti valid?

---

## 1.4 KEBARUAN (NOVELTY) & SOLUSI YANG DITAWARKAN

Kebaruan ilmiah (*scientific novelty*) penelitian ini terletak pada integrasi lintas-domain (*cross-domain product-finance bridge*) yang menjembatani karakteristik fisik sepeda motor baru (model dan warna) dengan struktur preferensi fasilitas pembiayaan konsumen (*multifinance* dan durasi tenor) ke dalam representasi keranjang transaksi multi-atribut lima dimensi, serta mentransformasikannya secara preskriptif menjadi panduan pramuniaga cerdas (*Smart Sales Script*) dan pedoman optimasi alokasi stok cabang.

Solusi yang ditawarkan dalam penelitian ini adalah mengimplementasikan algoritma *Frequent Pattern Growth* (FP-Growth) berbasis kerangka kerja CRISP-DM (*Cross-Industry Standard Process for Data Mining*). Seluruh kaidah asosiasi yang terbentuk dievaluasi secara ketat menggunakan Standar Validasi Tiga Metrik (*Support*, *Confidence*, dan *Lift Ratio* > 1,0) guna membuktikan korelasi positif murni antaratribut dan mengeliminasi aturan asosiasi semu (*spurious rules*).

---

## 1.5 RUANG LINGKUP PENELITIAN
Guna menjaga fokus penelitian dan menjamin kedalaman analisis dalam koridor ilmiah yang terkontrol, ruang lingkup dan batasan penelitian ini ditetapkan sebagai berikut:
1. **Objek Penelitian:** Penelitian difokuskan pada dealer resmi sepeda motor Yamaha PT. Sinar Surya Matahari (SSM Motor) dengan cakupan pasar konsumen di wilayah pemasaran Jabodetabek.
2. **Sumber dan Volume Data:** Data yang digunakan adalah rekaman data transaksi empiris penjualan unit baru (*single-unit sales*) yang bersumber langsung dari basis data *Dealer Management System* (DMS) perusahaan sebanyak **3.113 catatan faktur penjualan**.
3. **Periode Waktu Pengamatan:** Batasan waktu transaksi mencakup rentang operasional triwulan ketiga, yaitu periode **Juni hingga Agustus 2026**.
4. **Variabel dan Atribut Analisis:** Variabel dibatasi secara spesifik pada 5 (lima) atribut utama keputusan pembelian konsumen, meliputi: model sepeda motor, varian warna unit, metode pembayaran atau lembaga pembiayaan (*CASH, BAF, Adira, OTO*), durasi tenor angsuran (*11, 23, 30, 35 bulan*), serta wilayah domisili konsumen.
5. **Metode dan Parameter Evaluasi:** Pemodelan penambangan pola keterikatan dibatasi pada implementasi algoritma *Frequent Pattern Growth* (FP-Growth) berbasis struktur *FP-Tree*, di mana kaidah asosiasi yang dihasilkan wajib divalidasi memiliki nilai korelasi positif murni dengan **Lift Ratio > 1,0**.

---

## 1.6 TUJUAN PENELITIAN
Berdasarkan rumusan masalah yang telah ditetapkan, tujuan yang hendak dicapai dalam penelitian ini adalah:
1. Mengonstruksi skema transformasi data faktur transaksi penjualan tunggal (*single-unit sales*) PT. Sinar Surya Matahari ke dalam format representasi keranjang transaksi multi-atribut (*multi-attribute predicate basket*) terstruktur guna mengeliminasi potensi terbentuknya kaidah asosiasi semu (*spurious rules*).
2. Menguji validitas empiris dan kekuatan keterikatan kaidah asosiasi yang terbentuk menggunakan standar evaluasi tiga metrik (*Support*, *Confidence*, dan *Lift Ratio* > 1,0) guna memastikan signifikansi korelasi dependensi antaratribut.
3. Merumuskan rekomendasi strategi bisnis preskriptif bagi manajemen PT. Sinar Surya Matahari berupa panduan pramuniaga cerdas (*Smart Sales Script*), optimasi alokasi persediaan varian warna berbasis wilayah cabang, serta formulasi paket *bundling* promosi pembiayaan bersama lembaga rekanan.
