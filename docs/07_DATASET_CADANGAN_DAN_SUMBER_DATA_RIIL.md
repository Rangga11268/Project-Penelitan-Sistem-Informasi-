# KATALOG DATASET BISNIS RIIL CADANGAN & PANDUAN PENGAMBILAN DATA
## MATA KULIAH PENELITIAN SISTEM INFORMASI (UBSI)

Dokumen ini disusun sebagai **Rencana Cadangan (Plan B / Alternative Datasets)** khusus untuk metode **Association Rule Mining (FP-Growth / Apriori / Market Basket Analysis)** jika kelompok atau dosen memerlukan perbandingan dataset riil tambahan selain **Dataset Utama SSM Motor (3.113 transaksi)**.

---

### 1. Dataset Transaksi Keranjang Belanja Riil (100% Valid, Aktif, & Legal)

| No | Nama Dataset & Sektor | URL Akses Langsung (Valid & Aktif) | Format & Ukuran Data | Struktur Kolom / Format Transaksi | Kesesuaian FP-Growth / Apriori |
| :-: | :--- | :--- | :-: | :--- | :--- |
| 1 | **UCI Online Retail II**<br>*(Ritel Kado & Suvenir UK)* | [archive.ics.uci.edu/dataset/502/online+retail+ii](https://archive.ics.uci.edu/dataset/502/online+retail+ii)<br>*(DOI: `10.24432/C5CG6D`)* | XLSX / CSV<br>**1.067.371 baris** | `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country` | **Standar Emas (10/10):** `InvoiceNo` mengelompokkan item belanja riil. Standar rujukan jurnal SINTA 1 & 2. |
| 2 | **Kaggle Groceries Market Basket**<br>*(Supermarket POS)* | [kaggle.com/datasets/heeraldedhia/groceries-dataset](https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset) | CSV<br>**38.765 baris** (167 item unik) | `Member_number`, `Date`, `itemDescription` *(cth: whole milk, rolls/buns, sausage, yogurt)* | **Sangat Tinggi (10/10):** Sangat mudah diolah menjadi matriks transaksi (*One-Hot Encoding*). |
| 3 | **Kaggle The Bread Basket**<br>*(Point of Sales Bakery & Cafe)* | [kaggle.com/datasets/sulmansarwar/transactions-from-a-bakery](https://www.kaggle.com/datasets/sulmansarwar/transactions-from-a-bakery) | CSV<br>**21.293 baris** | `Transaction`, `Item` *(Bread, Coffee, Pastry, Tea)*, `Date`, `Time` | **Sangat Tinggi (9.5/10):** Menghasilkan aturan asosiasi cross-selling makanan & minuman yang sangat intuitif. |
| 4 | **Indonesian Pharmacy POS**<br>*(Mendeley Data Indonesia)* | [data.mendeley.com/datasets/2ym7v78wtd/1](https://data.mendeley.com/datasets/2ym7v78wtd/1)<br>*(DOI: `10.17632/2ym7v78wtd.1`)* | XLSX / CSV<br>**Transaksi Apotek Riil** | `Receipt_No`, `Transaction_Date`, `Product_Code`, `Product_Name`, `Qty`, `Price` | **Sangat Tinggi (10/10):** Data riil apotek Indonesia karya peneliti Rendra Gustriansyah (CC BY 4.0). |
| 5 | **Kaggle Olist E-Commerce**<br>*(Marketplace Brazil)* | [kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) | CSV Multi-Tabel<br>**100.000 pesanan** | `order_id`, `product_category_name`, `payment_type`, `payment_installments` (1–24), `customer_city` | **Sangat Sempurna (10/10):** Memiliki atribut produk + metode bayar + tenor cicilan (identik dengan riset SSM Motor). |
| 6 | **Retail Benchmark Dataset**<br>*(Mendeley Data / FIMI)* | [data.mendeley.com/datasets/rjj84brk2p/1](https://data.mendeley.com/datasets/rjj84brk2p/1)<br>*(DOI: `10.17632/rjj84brk2p.1`)* | DAT / TXT<br>**88.125 transaksi** | Space-separated item transaction IDs (Standar FIMI) | **Khusus Benchmark (9/10):** Sangat cocok untuk menguji efisiensi komputasi FP-Growth vs Apriori. |

---

### 2. Mengapa Portal Open Data Pemerintah Kurang Cocok untuk Asosiasi?

Berdasarkan investigasi pada portal pemerintah seperti **Satu Data Jakarta (`satudata.jakarta.go.id`)** atau **Open Data Jabar (`opendata.jabarprov.go.id`)**:
* **Karakteristik Data:** Mayoritas berupa **Data Agregat / Statistik Rekapitulasi Tahunan** (contoh: *Jumlah total penumpang Transjakarta per koridor per bulan* atau *Jumlah UMKM per kecamatan*).
* **Kendala Asosiasi:** Algoritma FP-Growth / Apriori **membutuhkan log transaksi mikro per struk/kejadian** (`Transaction ID` + daftar item). Data agregat hanya cocok untuk metode Regresi, Visualisasi Dashboard, atau Clustering Sektoral.

---

### 3. Komparasi Terhadap Dataset Utama Kita (SSM Motor)

| Parameter Evaluasi | Dataset Utama (SSM Motor) | Dataset Cadangan Publik (UCI / Kaggle / Mendeley) |
| :--- | :--- | :--- |
| **Status Kepemilikan** | **Data Primer Eksklusif** (Dealer Resmi Yamaha) | Data Sekunder Terbuka (Public Benchmark) |
| **Dimensi Multi-Atribut** | Produk (Tipe/Warna) + Leasing + Tenor + DP + Domisili | Dominan Produk saja (Kecuali Olist & SSM Motor) |
| **Peluang Publikasi SINTA** | **Sangat Tinggi (Novelty Kuat, Belum Ada di Google Scholar)** | Sedang - Tinggi (Perlu pembuktian komparasi algoritma) |
| **Kesiapan Data** | Sudah bersih & rapi di folder `datasets/01_...` | Siap diunduh via tautan resmi terlampir |

---

### 4. Prosedur Permohonan Data Tambahan ke UMKM / Perusahaan Lokal

Jika ingin mengambil data Point of Sales (POS) tambahan dari minimarket, apotek, swalayan, atau bengkel lokal:
1. Mengurus **Surat Pengantar Riset Resmi** dari Program Studi Sistem Informasi UBSI.
2. Melampirkan pernyataan anonimitas data (nama pembeli dan kontak pribadi dihapus/dianonimkan).
3. Memberikan timbal balik (*feedback*) laporan analisis pola asosiasi dan rekomendasi strategi bisnis kepada manajemen toko secara cuma-cuma.
