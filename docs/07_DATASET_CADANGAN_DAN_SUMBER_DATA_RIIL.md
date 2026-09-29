# KATALOG DATASET BISNIS RIIL CADANGAN & PANDUAN PENGAMBILAN DATA
## MATA KULIAH PENELITIAN SISTEM INFORMASI (UBSI)

Dokumen ini disusun sebagai **Rencana Cadangan (Plan B / Alternative Datasets)** jika kelompok atau dosen memerlukan perbandingan dataset riil tambahan selain **Dataset Utama SSM Motor (3.113 transaksi)**.

---

### 1. Dataset Transaksi Perusahaan Riil Publik (Terverifikasi & Legal)

| No | Nama Platform / Perusahaan | Format & Atribut Utama | Volume Data | Kesesuaian FP-Growth | Tautan Akses Legal |
| :-: | :--- | :--- | :-: | :-: | :--- |
| 1 | **Olist E-Commerce** *(Marketplace Terbesar Brazil)* | `order_id`, `product_category_name`, `payment_type` (Credit Card/Boleto/Voucher), `payment_installments` (1–24 bln), `customer_city`, `price`. | **100.000+ Pesanan Riil** | **Sangat Sempurna (10/10):** Memiliki dimensi produk, metode bayar, tenor cicilan, dan kota (sangat mirip dengan kasus SSM Motor). | [Kaggle - Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |
| 2 | **Dunnhumby** *(Perusahaan Analitik Ritel Global - "The Complete Journey")* | `BASKET_ID`, `HOUSEHOLD_KEY`, `PRODUCT_ID`, `DEPARTMENT`, `COMMODITY_DESC`, `SALES_VALUE`, `QUANTITY`. | **2 Tahun Riwayat Kasir Supermarket** | **Sangat Tinggi (9.5/10):** Data riil kasir supermarket untuk *Market Basket Analysis*. | [Dunnhumby Source Files](https://www.dunnhumby.com/source-files/) |
| 3 | **Instacart** *(Layanan Pesan-Antar Ritel Daring AS)* | `order_id`, `product_name`, `aisle_id`, `department`, `add_to_cart_order`, `order_dow`. | **3.000.000+ Pesanan Keranjang Belanja** | **Gold Standard (9.5/10):** Sangat cocok untuk menguji efisiensi algoritma FP-Growth skala besar. | [Kaggle - Instacart Dataset](https://www.kaggle.com/c/instacart-market-basket-analysis) |
| 4 | **UCI Online Retail II** *(Perusahaan Cinderamata Ritel Inggris)* | `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`. | **541.909 Baris Transaksi** | **Sangat Tinggi (9/10):** Standar emas rujukan artikel Jurnal SINTA 1 & SINTA 2. | [UCI Machine Learning - Online Retail](https://archive.ics.uci.edu/dataset/352/online+retail) |

---

### 2. Dataset Bisnis & Ritel Lokal Indonesia di Repositori Ilmiah

* **Mendeley Data (`data.mendeley.com`):**
  * *Kata Kunci:* `"transaksi apotek"`, `"retail transaction Indonesia"`, atau `"POS market basket"`.
  * *Contoh Data:* Data transaksi kasir apotek lokal (resep dokter, obat OTC, vitamin) dan data penjualan koperasi ritel.
* **Zenodo (`zenodo.org`):**
  * *Kata Kunci:* `"data transaksi minimarket" OR "market basket indonesia"`.
  * *Lisensi:* Creative Commons Attribution (CC BY 4.0) — legal untuk publikasi jurnal.
* **Kaggle Indonesia Collection:**
  * *Building Supply Store Sales Indonesia:* Transaksi penjualan bahan bangunan antar-kota di Indonesia (`Invoice_ID`, `Item_Purchased`, `Payment_Method`, `Unit_Price`).

---

### 3. Portal Data Terbuka Pemerintah & BUMN Indonesia

1. **Satu Data Indonesia (`data.go.id`):** Portal data nasional seluruh kementerian & BUMN.
2. **Open Data Jakarta (`data.jakarta.go.id`):** Data komoditas pangan dan logistik Perumda Pasar Jaya.
3. **PST BPS (`pst.bps.go.id`):** Layanan Mikrodata Badan Pusat Statistik untuk permohonan data penelitian mahasiswa.
4. **Layanan PPID BUMN (Permohonan Data Resmi):**
   * *PT KAI (Persero):* [ppid.kai.id](https://ppid.kai.id) – Log transaksi pemesanan tiket kereta.
   * *PT Pos Indonesia (Persero):* [ppid.posindonesia.co.id](https://www.posindonesia.co.id) – Log transaksi layanan pengiriman.
   * *PT Jasa Marga (Persero) Tbk:* [jasamarga.com](https://www.jasamarga.com) – Log transaksi gerbang tol (*Origin-Destination*).

---

### 4. Prosedur Permohonan Data Riset ke UMKM / Perusahaan Lokal

Jika ingin mengambil data Point of Sales (POS) dari toko komputer, apotek, swalayan, atau bengkel lokal:
1. Mengurus **Surat Pengantar Riset Resmi** dari Program Studi Sistem Informasi UBSI.
2. Melampirkan pernyataan anonimitas (seluruh data nama pembeli dan nomor kontak pribadi dihapus/dianonimkan).
3. Menawarkan timbal balik (*feedback*) berupa laporan analisis pola transaksi dan rekomendasi strategi penjualan secara cuma-cuma kepada pihak manajemen toko.
