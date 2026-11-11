# Contekan Presentasi & Asistensi Bab IV (Untuk Darell, Megi, & Wahyu)

Panduan cepat buat jawab pertanyaan Ibu Syifa tentang isi **19 Tabel + 4 Gambar** di Bab IV, plus jurus jawab santai tapi tepat kalau ditanya: *"Kenapa tabel ini gak ditaruh di Bab 3?"*

---

## 1. Daftar Singkat Isi 19 Tabel & 4 Gambar di Bab IV

### 4.1 Data Understanding (Bagian Darell)
- **Tabel 4.1 — Metadata 12 Kolom Asli Y-DMS:** Isi database mentah dealer sebelum disaring (ada tanggal, nomor faktur, model, warna, leasing, tenor, DP, harga, kota, umur, cabang).
- **Tabel 4.2 — Top 10 Model Terlaris:** 44 model unik. Juara 1 **Aerox Alpha** (15,03%), #2 **Mio M3 CW** (13,94%), #3 **Gear 125** (10,44%). Sepuluh teratas pegang 75% penjualan.
- **Tabel 4.3 — Top 10 Warna Terpopuler:** 22 warna. **Hitam** paling mendominasi (42,31% / 1.317 unit), disusul Biru (11,21%).
- **Tabel 4.4 — Skema Bayar & Leasing:** **Tunai (Cash) 63,25%** vs **Kredit 36,75%**. Di segmen kredit, **BAF mendominasi 73,78%**.
- **Tabel 4.5 — Durasi Tenor Cicilan:** Mayoritas ambil tunai (0 bln), tapi yang kredit **83,13% pilih tenor panjang (30–35 bulan)** biar cicilan bulanan ringan.
- **Tabel 4.6 — Wilayah Domisili Pembeli:** Pembeli **64,63% dari DKI Jakarta**, padahal dealer ada di Bekasi (Bekasi Raya 26,18%).
- **Gambar 4.1 — Grafik 4-in-1 Deskriptif:** Visual batang & pie chart dari Tabel 4.2 s.d. 4.5 (warnanya sudah pakai warna asli motor & korporasi leasing).

### 4.2 Data Preparation (Bagian Wahyu)
- **Tabel 4.7 — Rekap Cleaning & Anonimisasi:** Bukti 3.113 data bersih 100% (0 batal/kosong) & kolom sensitif (NIK, nama, HP, no rangka) sudah dibuang.
- **Tabel 4.8 — Sampel Data Setelah Standarisasi:** Contoh 5 faktur nyata (`26FJK0101925` s.d. `26FJK0101929`) yang format teks & kelompoknya sudah rapi.
- **Tabel 4.9 — Sampel Keranjang Multiatribut:** Bentuk data setelah diubah ke format pasangan `{Atribut=Nilai}` karena 1 faktur cuma beli 1 motor.
- **Tabel 4.10 — Matriks Insidensi Biner (`3.113 × 89`):** Contoh isi matriks angka `1` dan `0` sebagai input wajib algoritma FP-Growth.

### 4.3 Modeling FP-Growth (Bagian Megi)
- **Tabel 4.11 — Rekap Panjang *k-Itemset*:** Dari *Min Support* 2% lahir **263 pola** (terbanyak kombinasi 2 atribut = 107 pola, sampai kombinasi lengkap 5 atribut = 5 pola).
- **Tabel 4.12 — Top 15 Frequent Itemsets:** Kombinasi yang paling sering muncul, juaranya `{Leasing=CASH, Tenor=0_BULAN_CASH}` (63,25%) dan `{Warna=HITAM}` (42,31%).

### 4.4 Evaluation Tri-Metrik (Bagian Megi & Wahyu)
- **Tabel 4.13 — Rekap Seleksi Tri-Metrik:** Dari **401 aturan mentah** (*Min Conf* 50%), **3 gugur** karena *Lift* ≤ 1,0, tersisa **398 aturan valid**.
- **Gambar 4.2 — *Scatter Plot* & Histogram *Lift*:** Membuktikan sebaran aturan valid ada di atas batas *Confidence* 50% dan *Lift* > 1,0 (puncak hingga 9,58).
- **Tabel 4.14 — Rekap 5 Klaster Manajerial:** Pengelompokan 398 aturan ke 5 tema bisnis (*Geo-Marketing* paling banyak = 232 aturan / 58,29%).
- **Tabel 4.15 — Top 20 Aturan Terbaik:** 20 aturan dengan *Lift* tertinggi (juaranya warna Hijau Perak → Gear 125 dengan *Confidence* 100% & *Lift* `9,578`).

### 4.5 Deployment / Rekomendasi Bisnis (Bagian Darell)
- **Tabel 4.16 — Matriks Alokasi Stok Gudang:** Persentase warna favorit di 5 model terlaris (misal Aerox Hitam 59,06%).
- **Gambar 4.3 — Grafik Alokasi Warna Riil:** Visual acuan pengadaan stok pakai rumus **4 : 2 : 1** untuk cegah *dead stock*.
- **Tabel 4.17 — *Smart Sales Script*:** Panduan sales menawar: kalau customer cari NMAX/Fazzio langsung tawari kredit BAF 30–35 bln; kalau Aerox/Mio/Gear tawari promo tunai.
- **Tabel 4.18 — Matriks Penetrasi Wilayah (%):** Persentase pembeli per model berdasarkan kawasan (Gear 125 hampir 100% dibeli warga DKI Jakarta).
- **Gambar 4.4 — *Heatmap* Wilayah (*Geo-Marketing*):** Peta panas sebaran model vs kawasan (mendukung rekomendasi kirim unit gratis & urus STNK kilat Jakarta).
- **Tabel 4.19 — Peta Jalan Bisnis (*Roadmap*):** Rangkuman akhir 3 strategi, target KPI, dan PIC divisi yang bertanggung jawab.

---

## 2. Jurus Jawab Singkat Kalau Ditanya Bu Syifa: *"Kenapa Tabel Ini Gak Ditaruh di Bab 3?"*

Intinya pegang satu prinsip santai ini saja:
> **"Bab 3 itu *rencana & caranya* sebelum data diolah. Bab 4 itu *hasil buktinya* setelah data beneran kita run di Python."**

Kalau Bu Syifa nunjuk tabel tertentu, jawab pakai skrip singkat di bawah ini:

### 1. Kalau ditanya soal **Tabel 4.1 (Metadata 12 Kolom Y-DMS)**
> *"Di Bab 3 kami baru jelasin rencana 5 variabel yang mau dipakai, Bu. Nah, pas file database Y-DMS dari dealer kami buka di tahap awal olah data (Data Understanding), ternyata isi mentahnya ada 12 kolom lengkap dengan contoh nilai aslinya seperti di Tabel 4.1 ini. Karena ini hasil ngecek isi file asli di lapangan, jadi kami taruh di Bab 4.1, Bu."*

### 2. Kalau ditanya soal **Tabel 4.7 – 4.10 (Cleaning, Standarisasi, Basket, Matriks Biner)**
> *"Di Bab 3 kami jelasin konsep sama langkah rencananya, Bu—misalnya rencana mau dibersihkan, dianonimkan, sama diubah ke biner. Kalau Tabel 4.7 sampai 4.10 ini isinya hasil nyata setelah kodingan Python-nya dijalankan, Bu. Contohnya baru ketahuan kalau transaksi batalnya 0 (Tabel 4.7), wujud faktur aslinya kayak `26FJK0101925` (Tabel 4.8), dan hasil akhir kolom binernya pas jadi **3.113 × 89** (Tabel 4.10). Karena itu hasil eksekusi program, masuknya ke Bab 4.2, Bu."*

### 3. Kalau ditanya soal **Rumus Persamaan (4.2)–(4.4) di Bab 4.4 (*Support, Confidence, Lift*)**
> *"Betul di Bab 3 sudah ada teorinya, Bu. Di Bab 4.4 kami cantumkan ulang secara singkat sebagai pengantar langsung sebelum Tabel 4.13, supaya pembaca gampang lihat kaitan rumusnya sama angka hasil saringan nyatanya: dari 401 aturan mentah, 3 gugur, dan 398 yang lolos validasi."*

### 4. Kalau ditanya soal **Tabel 4.16 – 4.19 (Rekomendasi Bisnis & *Roadmap*)**
> *"Di Bab 3 kami baru merancang kerangka 3 pilar strateginya (fase Deployment CRISP-DM). Nah di Bab 4.5, tabel-tabel ini sudah berisi angka presisi hasil hitungan dataset aslinya—misal rasio stok 59% Hitam atau 99,69% Gear 125 dibeli orang Jakarta—yang gak mungkin ada di Bab 3 sebelum datanya selesai ditambang."*
