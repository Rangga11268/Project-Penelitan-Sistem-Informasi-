# PANDUAN PENGGUNAAN DATASET CADANGAN (PLAN B): DATA TRANSAKSI FARMASI INDONESIA

Folder ini merupakan **Rencana Cadangan (Plan B / Alternative Backup Dataset)** jika penelitian utama pada dealer SSM Motor menghadapi kendala persetujuan dosen.

---

### 1. Identitas & Legalitas Dataset
* **Nama Dataset:** *Retail Sales Dataset of a Pharmacy in Indonesia*
* **Sumber Repositori:** Mendeley Data ([data.mendeley.com/datasets/2ym7v78wtd/1](https://data.mendeley.com/datasets/2ym7v78wtd/1))
* **DOI Resmi:** `10.17632/2ym7v78wtd.1`
* **Peneliti Asal:** Dr. Rendra Gustriansyah
* **Lisensi:** *Creative Commons Attribution 4.0 International (CC BY 4.0)* — **100% Legal & Sah untuk Publikasi Ilmiah SINTA/Skripsi**.

---

### 2. File Dataset yang Tersedia
📁 **[`DATASET_FARMASI_INDONESIA_RAPI_DAN_MUDAH_DIBACA.xlsx`](./DATASET_FARMASI_INDONESIA_RAPI_DAN_MUDAH_DIBACA.xlsx)**
Berisi 5 Worksheets terformat rapi dengan tata letak profesional:
1. **`Ringkasan_Dataset`**: Statistik ringkas, volume data, dan metadata.
2. **`Top_50_Obat_Terlaris`**: Daftar 50 obat paling banyak diresepkan (Neurodex, Lansoprazole, RL, Paracetamol, dll.).
3. **`Keranjang_Resep_Multi_Item`**: Format keranjang belanja (*Market Basket*) per nomor resep faktur.
4. **`Detail_Transaksi_Obat`**: Detail per item transaksi (Harga, Qty, Satuan, Status Racik).
5. **`Katalog_Master_Obat`**: Master katalog 1.000 jenis obat di Indonesia.

---

### 3. Formulasi Judul & Metode Jika Menggunakan Dataset Ini (Plan B)
* **Pilihan Judul Jurnal SINTA:**
  > *"Penerapan Algoritma FP-Growth untuk Analisis Pola Peresepan Obat dan Rekomendasi Manajemen Persediaan Farmasi Berbasis Market Basket Analysis (Studi Kasus: Data Transaksi Apotek Indonesia)"*
* **Algoritma:** FP-Growth / Apriori dengan metrik *Support*, *Confidence*, dan validasi *Lift Ratio*.
* **Contoh Aturan Asosiasi Kuat yang Ditemukan:**
  * $\{\text{Glucobay 50 mg}\} \rightarrow \{\text{Glucodex 80 mg}\}$ *(Confidence: 69.38%, Lift Ratio: 46.25)*
  * $\{\text{Methylprednisolone 4 mg}, \text{Osteocal 500 mg}\} \rightarrow \{\text{Allopurinol 100 mg}\}$ *(Confidence: 79.55%, Lift Ratio: 25.28)*
  * $\{\text{Spironolacton 25 mg}\} \rightarrow \{\text{Furosemide 40 mg}\}$ *(Confidence: 32.28%, Lift Ratio: 17.76)*
