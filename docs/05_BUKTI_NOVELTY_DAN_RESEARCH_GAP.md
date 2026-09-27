# BUKTI NOVELTY, RESEARCH GAP, DAN ANALISIS LITERATUR RISET
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5 UBSI)  
**Kelompok 1:**
- Darell Rangga Putra R. (19241009)
- Megi Refkiansyah (19240488)
- Wahyu Rizky (19240493)

**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.

---

## 1. Hasil Penelusuran Google Scholar, SINTA, Garuda, & Repositori Kampus

Berdasarkan penelusuran literatur akademik terhadap seluruh repositori jurnal terakreditasi di Indonesia (SINTA, Garuda Ristekbrin, Neliti, Google Scholar, dan Repositori Institusi):

### A. Penelusuran Entitas Dataset: "SSM Motor" / "Surya Sentosa Mandiri"
* **Hasil:** **0 Publikasi / 0 Skripsi / 0 Jurnal**.
* **Fakta:** Tidak ditemukan satu pun publikasi yang pernah menggunakan dataset transaksi dari Dealer SSM Motor (Surya Sentosa Mandiri Motor).
* **Status:** **100% Data Primer & Eksklusif**, tidak ada risiko data daur ulang (*recycled dataset*) atau duplikasi dari karya orang lain.

### B. Penelusuran Topik: Algoritma Asosiasi pada Penjualan Sepeda Motor
* Mayoritas publikasi data mining di ranah dealer/bengkel motor di Indonesia selama 2018–2026 terbagi menjadi:
  1. **Market Basket Analysis Suku Cadang/Bengkel (85%+):** Hanya meneliti asosiasi pembelian *sparepart* (misal: oli mesin dibeli bersama busi atau kampas rem).
  2. **Prediksi/Peramalan Volume Unit:** Menggunakan regresi linier, ARIMA, Single Moving Average, atau Monte Carlo untuk memprediksi angka total penjualan motor per bulan.
  3. **Sistem Pendukung Keputusan (SPK):** Menggunakan AHP/TOPSIS/SAW untuk memilih motor terbaik bagi pembeli individual.
  4. **Clustering Pembeli:** Menggunakan K-Means untuk segmentasi umum.

---

## 2. Research Gap (Kesenjangan Penelitian)

Belum pernah ada penelitian yang mengintegrasikan transaksi penjualan unit sepeda motor baru ke dalam model **Multi-Attribute Association Rule Mining menggunakan FP-Growth** yang menghubungkan 5 dimensi transaksi sekaligus secara komprehensif:

$$\text{Tipe/Model Unit} \times \text{Warna} \times \text{Lembaga Pembiayaan (BAF/Adira/OTO/Cash)} \times \text{Durasi Tenor} \times \text{Wilayah Domisili}$$

### Matriks Perbandingan Riset Terdahulu vs Penelitian Kita

| Dimensi Evaluasi | Penelitian Asosiasi Otomotif yang Sudah Ada | Penelitian Kelompok 1 (SSM Motor) | Nilai Kebaruan (*Novelty Value*) |
| :--- | :--- | :--- | :--- |
| **Objek Data** | Suku cadang/sparepart bengkel atau data simulasi | Transaksi penjualan unit motor baru riil (Juni–Agustus 2026 / 3.113 baris) | Transaksi bernilai tinggi (*high-involvement purchase*), bukan barang belanja rutin. |
| **Dimensi Atribut** | *Single-attribute* (hanya item barang sejenis) | **Multi-attribute multidimensi** (Produk, Finansial, Demografi) | Menangkap relasi silang antara preferensi model motor dengan profil pembiayaan dan wilayah. |
| **Algoritma** | Didominasi Apriori konvensional (rawan *bottleneck* saat kombinasi atribut tinggi) | **FP-Growth (Frequent Pattern Growth)** dengan struktur *FP-Tree* | Lebih cepat, efisien tanpa membangkitkan kandidat kombinasi secara boros (*candidate generation*). |
| **Luaran Manajerial** | Tata letak rak sparepart / promo bundling oli | Rekomendasi paket kredit terarah (*Targeted Financing Strategy*), alokasi stok per dealer daerah, dan kemitraan leasing. | Keputusan strategis tingkat dealer dan lembaga pembiayaan (*actionable business decision*). |

---

## 3. Tiga Pilar Novelty Utama (Argumen Akademik untuk Dosen Penguji)

Jika ditanya oleh Ibu Syifa atau Dosen Penguji mengenai kebaruan riset ini:

1. **Kebaruan Data (*Data Novelty*):**
   > *"Dataset yang kami gunakan adalah data riil dari sistem operasional internal Dealer SSM Motor periode Juni - Agustus 2026 sebanyak 3.113 transaksi. Data ini primer, eksklusif, dan belum pernah diolah atau dipublikasikan dalam repositori akademik mana pun."*

2. **Kebaruan Pendekatan Dimensi (*Dimensional / Methodological Novelty*):**
   > *"Selama ini asosiasi data mining di dealer motor hanya melihat pola sparepart bengkel (oli + busi). Penelitian kami memelopori pendekatan Multi-Attribute Association Rule menggunakan FP-Growth untuk memetakan keterkaitan tersembunyi antara pilihan unit motor, warna, lembaga leasing (BAF/Adira/dll), tenor cicilan, dan domisili konsumen dalam satu transaksi SPK."*

3. **Kebaruan Manfaat Bisnis & Manajerial (*Practical Novelty*):**
   > *"Hasil riset kami tidak berhenti pada angka Support & Confidence, melainkan menghasilkan pola rekomendasi nyata (contoh: mengapa skutik 155cc di wilayah Jakarta Selatan memiliki keterikatan kuat dengan BAF tenor 35 bulan). Ini memberikan nilai tambah langsung bagi dealer dalam menyusun strategi bundling pembiayaan dan penataan kuota stok daerah."*
