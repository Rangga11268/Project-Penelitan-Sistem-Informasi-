# ABSTRAK DAN ABSTRACT STANDAR JURNAL JuTISI 2026

> [!NOTE] Ketentuan Penulisan Abstrak & Abstract JuTISI 2026:
> 1. **Bilingual**: Disusun dalam Bahasa Indonesia dan Bahasa Inggris.
> 2. **Batas Kata**: Maksimum **250 kata** per abstrak (Abstrak Indonesia: **240 kata**, Abstract Inggris: **243 kata** — 100% aman dan lolos uji batas kata).
> 3. **Struktur IMRAD Tanpa Sitasi**: Mengandung latar belakang masalah & tujuan, metode (CRISP-DM & FP-Growth), temuan penting kuantitatif (validasi tri-metrik, 9 kaidah emas, keyakinan hingga 84,4%, lift hingga 2,86), dan implikasi/simpulan preskriptif. **Dilarang keras menyertakan rujukan pustaka**.
> 4. **Kata Kunci / Keywords**: 3 – 5 kata/frasa, diurutkan menurut abjad (alfabetis), dipisahkan tanda titik koma (`;`), tidak mencantumkan nama institusi.
> 5. **Tipografi Template**:
>    - Abstrak Indonesia: Times New Roman 9 pt **Bold**, rata kiri-kanan (*justified*), spasi 1.0, tanpa indentasi awal.
>    - Judul Inggris: Times New Roman *Italic*, maksimum 12 kata (10 kata: *Multi-Attribute Association Rule Mining of Motorcycle Sales Transactions Using FP-Growth*).
>    - Abstract Inggris: Times New Roman 9 pt **Bold and Italic**, rata kiri-kanan (*justified*), spasi 1.0, tanpa indentasi awal.

---

## 1. Versi Bahasa Indonesia

**Multi-Attribute Association Rule Mining Menggunakan Algoritma FP-Growth pada Transaksi Sepeda Motor**

**Darell Rangga Putra Rachman\* #1, Megi Refkiansyah Ananda Pratama Gumay#2, Wahyu Rizky Khoirudin#3, Syifa Nur Khasanah#4**  
*#1, #2, #3 Program Studi Sistem Informasi, Universitas Bina Sarana Informatika*  
*#4 Program Studi Teknologi Informasi, Universitas Bina Sarana Informatika*  
*Jl. Kramat Raya No.98, Senen, Jakarta Pusat 10450, Indonesia*  
`119241009@bsi.ac.id, 219240488@bsi.ac.id, 319240493@bsi.ac.id, 4syifa.snk@bsi.ac.id`  
\*Corresponding Author: `19241009@bsi.ac.id`

**Abstrak — Ketidakseimbangan alokasi persediaan (inventory mismatch) dan pembatalan pesanan akibat masa tunggu inden varian warna favorit menjadi kendala operasional utama pada dealer sepeda motor. Pendekatan analisis univariat terbukti belum mampu menangkap keterkaitan lintas-dimensi antara model kendaraan, varian warna, skema pembiayaan, tenor angsuran, dan wilayah konsumen. Penelitian ini bertujuan mengekstrak kaidah asosiasi multiatribut yang valid secara objektif guna merumuskan rekomendasi strategi bisnis preskriptif bagi dealer. Mengadopsi metodologi CRISP-DM, penelitian ini menganalisis sensus 3.113 data faktur penjualan resmi dari sistem Yamaha Dealer Management System (Y-DMS) PT. Sinar Surya Matahari periode Juni–Agustus 2026. Data ditransformasikan ke dalam representasi keranjang predikat multiatribut biner berdimensi 3.113 × 89 guna mengatasi kendala empty itemsets pada transaksi unit tunggal, kemudian dimodelkan menggunakan algoritma FP-Growth berbasis pohon FP-Tree. Kaidah asosiasi dievaluasi menggunakan Standar Validasi Tiga Metrik dengan ambang batas Minimum Support ≥ 1,0%, Minimum Confidence ≥ 60,0%, dan Lift Ratio > 1,0. Hasil penambangan mengekstrak 263 frequent itemsets dan menyaring 9 kaidah asosiasi unggul berkorelasi positif murni dengan tingkat Confidence hingga 84,4% dan Lift Ratio mencapai 2,86, sekaligus menyingkirkan belasan kaidah semu (Lift Ratio ≤ 1,0). Terungkap keterikatan kuat antara segmen Maxi Series (Aerox dan NMAX) dengan warna Matte Black serta tenor kredit 35 bulan via BAF, preferensi segmen Classy terhadap warna Prestige Silver, serta konsentrasi pembiayaan tunai di wilayah urban. Temuan empiris ini dihilirkan menjadi tiga rekomendasi manajerial: Smart Sales Script, pedoman Regional Inventory Allocation berbasis rasio stok 4:2:1 guna memangkas risiko stockout, serta program Joint Multifinance Bundling.**

**Kata kunci— algoritma FP-Growth; data mining; kaidah asosiasi multiatribut; optimasi persediaan; transaksi penjualan sepeda motor.**

---

## 2. Versi Bahasa Inggris (*English Version*)

***Multi-Attribute Association Rule Mining of Motorcycle Sales Transactions Using FP-Growth***

**Abstract — *Inventory mismatch and order cancellations due to prolonged waiting times for popular color variants represent critical operational challenges in motorcycle dealerships. Conventional univariate analysis fails to capture cross-dimensional behavioral dependencies among vehicle models, colors, financing schemes, installment tenors, and customer regional demographics. This study aims to objectively extract valid multi-attribute association rules to formulate prescriptive business strategies for dealership operations. Adopting the CRISP-DM framework, this research analyzes a census of 3,113 completed sales invoices from the Yamaha Dealer Management System (Y-DMS) database of PT. Sinar Surya Matahari covering June to August 2026. Single-unit transaction records were transformed into a multi-attribute predicate binary basket matrix (3,113 × 89) to resolve the empty itemsets limitation, followed by two-pass FP-Tree pattern growth mining using the FP-Growth algorithm. Generated association rules were rigorously filtered using the Tri-Metric Validation Standard with thresholds of Minimum Support ≥ 1.0%, Minimum Confidence ≥ 60.0%, and Lift Ratio > 1.0. The algorithm successfully extracted 263 frequent itemsets and distilled 9 robust golden rules with Confidence up to 84.4% and Lift Ratio reaching 2.86, while systematically eliminating spurious rules (Lift Ratio ≤ 1.0). Strong interdependencies were revealed between the commuter Maxi Series (Aerox and NMAX), Matte Black color, and 35-month credit tenors via BAF, as well as Classy segment preferences for Prestige Silver. These empirical findings were operationalized into three prescriptive pillars: Smart Sales Scripts, Regional Inventory Allocation guidelines with a 4:2:1 stocking ratio to mitigate stockout risks, and Joint Multifinance Bundling programs.***

**Keywords— *association rule mining; dealership inventory optimization; FP-Growth algorithm; motorcycle sales transactions; multi-attribute predicate basket.***
