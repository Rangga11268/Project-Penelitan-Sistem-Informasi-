# BAB V KESIMPULAN DAN SARAN

**Judul Penelitian:**  
*"Multi-Attribute Association Rule Mining Menggunakan Algoritma FP-Growth: Analisis Pola Pembelian dan Preferensi Pembiayaan Konsumen Sepeda Motor"*  
*(Studi Kasus: PT. Sinar Surya Matahari)*  
**Kelompok 1:** Darell Rangga Putra R., Megi Refkiansyah, Wahyu Rizky  
**Program Studi:** Sistem Informasi — Fakultas Teknik dan Informatika, Universitas Bina Sarana Informatika (UBSI)

---

## 5.1 Kesimpulan

Berdasarkan hasil analisis, komputasi penambangan data (*data mining*) dengan algoritma *Frequent Pattern Growth* (FP-Growth), evaluasi tri-metrik, serta interpretasi manajerial yang telah dilakukan terhadap 3.113 rekaman data faktur riil *Yamaha Dealer Management System* (Y-DMS) PT. Sinar Surya Matahari periode Juni hingga Agustus 2026, maka kesimpulan penelitian dirumuskan secara terstruktur untuk menjawab ketiga rumusan masalah dan tujuan penelitian sebagai berikut:

1. **Keberhasilan Konstruksi Representasi Keranjang Multiatribut:**  
   Penelitian ini membuktikan bahwa kendala struktural transaksi otomotif yang bersifat penjualan unit tunggal (*single-unit retail*) berhasil diatasi melalui skema pemetaan pasangan predikat diskret `{Atribut=Nilai}` pada 5 dimensi keputusan pembelian (Model, Varian Warna, Lembaga Pembiayaan/*Leasing*, Durasi Tenor, dan Wilayah Domisili). Transformasi ini menghasilkan matriks insidensi biner (*binary incidence matrix*) berdimensi 3.113 baris transaksi dan 87 predikat biner unik. Pendekatan *Multi-Attribute Association Rule Mining* terbukti secara efektif mencegah terbentuknya aturan semu (*spurious rules*) dan mengeliminasi keterbatasan penelitian terdahulu yang hanya bertumpu pada analisis satu dimensi (Ubaidillah & Sumiati, 2025).

2. **Kekuatan dan Validitas Ilmiah Kaidah Asosiasi Berbasis Tri-Metrik:**  
   Penerapan algoritma FP-Growth dengan parameter ambang batas *Minimum Support* 2,0% (ekuivalen $\ge 62$ transaksi) dan *Minimum Confidence* 50,0% berhasil mengekstraksi 263 *frequent itemsets* dan menghasilkan **398 kaidah asosiasi valid**. Berdasarkan uji validasi ilmiah tiga metrik objektif (*Tri-Metric Validation*), seluruh 398 kaidah (100%) memiliki nilai *Lift Ratio* di atas 1,0 (berkisar antara 1,002 hingga 9,578) tanpa ditemukan satupun aturan berkorelasi negatif atau independen acak ($Lift \le 1,0$) (Tan et al., 2018). Kaidah asosiasi terkuat dicirikan oleh keterikatan deterministik varian warna eksklusif terhadap model kendaraan tertentu dengan tingkat kepastian sempurna (*Confidence* 100%), seperti warna Hijau Perak terhadap Yamaha Gear 125 ($Lift = 9,578$), warna Perak Hijau terhadap Yamaha Mio M3 CW ($Lift = 7,173$ s.d. $7,189$), serta warna Ungu Muda terhadap Grand Filano Hybrid Neo ($Lift = 9,194; Confidence = 62,32\%$).

3. **Perumusan Rekomendasi Preskriptif Manajerial Terpadu (*Deployment*):**  
   Hasil penambangan kaidah asosiasi berhasil dihilirisasi menjadi instrumen sistem pendukung keputusan (*Decision Support System*) operasional dealer yang terbagi ke dalam tiga pilar strategis (Sharda et al., 2020):
   - **a. Manajemen Persediaan Unit (*Inventory Optimization*):** Diterapkannya formula rasio alokasi stok gudang preskriptif **4 : 2 : 1** (Hitam *fast-moving* 50%–60%, Biru/Perak penyeimbang 25%–30%, dan warna aksen 10%–15%) yang terbukti secara simulasi mampu menekan risiko kerugian barang mati (*dead stock*) dan memangkas waktu tunggu konsumen (*lead time*) (Salu et al., 2022).
   - **b. Panduan Penjualan Cerdas (*Smart Sales Script*):** Matriks komunikasi tenaga pemasar (*sales counter*) yang membedakan pendekatan penawaran: menyodorkan paket cicilan terjangkau rekanan BAF tenor 30–35 bulan untuk segmen matik Classy dan Maxi (NMAX Neo S dan Fazzio Hybrid), serta insentif potongan harga tunai (*cashback*) dan bonus servis berkala untuk segmen komuter *entry-level* (Aerox Alpha dan Mio M3 CW) (Widodo et al., 2022).
   - **c. Penetrasi Pemasaran Spasial (*Geo-Marketing Strategy*):** Fakta empiris bahwa 64,6% pembeli berdomisili di DKI Jakarta Raya kendati dealer berlokasi operasional di Kota Bekasi melahirkan rekomendasi penyediaan fasilitas pengiriman unit digital lintas wilayah secara gratis (*free cross-region delivery*) serta percepatan biro jasa administrasi STNK plat B DKI Jakarta dengan batas target maksimal 14 hari kerja.

---

## 5.2 Saran

Berdasarkan kesimpulan dan temuan empiris dalam penelitian ini, diajukan beberapa saran konstruktif yang ditujukan bagi pihak manajemen dealer PT. Sinar Surya Matahari serta bagi pengembangan penelitian selanjutnya di bidang penambangan data sistem informasi:

### 1. Saran Praktis bagi Manajemen PT. Sinar Surya Matahari
- **a. Integrasi Sistem Analitik ke Basis Data Y-DMS:**  
  Manajemen disarankan mengembangkan antarmuka pemrograman aplikasi (*Application Programming Interface* / API) yang menghubungkan modul algoritma FP-Growth secara langsung dengan basis data Y-DMS, sehingga pembaruan aturan asosiasi dan pemantauan rasio stok gudang dapat dilakukan secara dinamis (*real-time analytics*).
- **b. Standarisasi Operasional Tenaga Pemasar (SOP Sales Counter):**  
  Mengadopsi matriks *Smart Sales Script* ke dalam kurikulum pelatihan berkala tenaga pramuniaga dan surveyor kredit guna memitigasi risiko pembatalan pesanan akibat ketidaksesuaian penawaran skema pembiayaan (*leasing mismatch*).
- **c. Peningkatan Kemitraan Strategis Bersama Lembaga Pembiayaan (BAF):**  
  Mengingat keterikatan kredit yang sangat dominan pada Bussan Auto Finance (73,8% dari total transaksi pembiayaan), manajemen dealer perlu merumuskan nota kesepahaman promosi bersama (*joint promotion MOU*) berupa subsidi uang muka (*Down Payment*) khusus pada unit-unit unggulan tenor 30–35 bulan.

### 2. Saran Akademis untuk Penelitian Selanjutnya
- **a. Perluasan Cakupan Temporal Data Secara Longitudinal:**  
  Penelitian selanjutnya disarankan memperluas rentang waktu pengamatan data menjadi periode tahunan (12 hingga 24 bulan) guna menangkap dinamika musiman (*seasonal patterns*), seperti lonjakan permintaan pada momentum menjelang Hari Raya Idul Fitri dan penutupan tahun anggaran.
- **b. Eksplorasi Pendekatan Hibrida (*Hybrid Data Mining*):**  
  Mengombinasikan algoritma aturan asosiasi FP-Growth dengan algoritma klasterisasi (*K-Means Clustering* atau segmentasi model *Recency, Frequency, Monetary* / RFM) untuk menganalisis profil loyalitas konsumen pasca-pembelian unit dan transaksi servis suku cadang secara terpadu.
- **c. Pengayaan Variabel Demografis Konsumen:**  
  Mengintegrasikan atribut demografis tambahan (seperti rentang usia pembeli, tingkat pendapatan bulanan, dan profil pekerjaan) dengan tetap mengedepankan etika privasi dan kepatuhan terhadap Undang-Undang Pelindungan Data Pribadi (UU PDP).
