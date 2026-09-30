# PANDUAN PRESENTASI & SIMULASI TANYA JAWAB DOSEN PENGAMPU
## MATA KULIAH PENELITIAN SISTEM INFORMASI (SEMESTER 5 UBSI)
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Studi Kasus:** PT. Sinar Surya Matahari (Dealer Resmi Sepeda Motor Yamaha)  
**Tim Peneliti (Kelompok 1):**
1. Darell Rangga Putra R. (19241009)
2. Megi Refkiansyah (19240488)
3. Wahyu Rizky (19240493)

---

## 🎯 3 PILIHAN JUDUL FINAL SIAP DISODORKAN KE DOSEN

1. **Pilihan 1 (Rekomendasi Utama #1):**  
   *"Penerapan Algoritma FP-Growth dalam Multi-Attribute Association Rule Mining untuk Analisis Pola Pembelian Sepeda Motor dan Preferensi Skema Pembiayaan Konsumen (Studi Kasus: PT. Sinar Surya Matahari)"*
2. **Pilihan 2 (Fokus Bisnis & Bundling Promo):**  
   *"Analisis Pola Transaksi Penjualan Sepeda Motor Menggunakan Algoritma FP-Growth untuk Perumusan Strategi Bundling Paket Pembiayaan Konsumen (Studi Kasus: PT. Sinar Surya Matahari)"*
3. **Pilihan 3 (Fokus Consumer Behavior & Tenor):**  
   *"Penambangan Kaidah Asosiasi Multidimensi Berbasis FP-Growth untuk Eksplorasi Pola Preferensi Konsumen Kendaraan Bermotor Roda Dua Berdasarkan Atribut Produk dan Tenor Pembiayaan"*

---

## 🎯 DAFTAR PERTANYAAN KRITIS DOSEN & SKRIP JAWABAN AKADEMIK

---

### ❓ PERTANYAAN 1:
> *"Untuk apa mencari keterkaitan antara tipe motor dengan lembaga leasing dan tenor 35 bulan? Apa dampaknya bagi dealer?"*

#### 💡 Jawaban Rekomendasi:
> *"Izin menjawab Ibu Syifa,
> 
> Hubungan antara tipe motor, leasing, dan tenor ini memiliki **3 dampak nyata bagi bisnis dealer** PT. Sinar Surya Matahari:
> 
> 1. **Mencegah Kegagalan Closing Akibat Price Shock:** Motor matik premium (seperti Aerox dan NMAX) memiliki harga OTR puluhan juta. Jika pramuniaga langsung menyodorkan cicilan tenor pendek (11 bulan) yang angsurannya mahal, konsumen sering membatalkan pembelian. Dengan mengetahui bahwa pembeli tipe ini dominan memilih **tenor 35 bulan via BAF**, sales langsung menyodorkan paket cicilan paling ringan sejak awal.
> 2. **Optimalisasi Kecepatan Approval Kredit:** BAF adalah captive finance resmi Yamaha. Mengarahkan konsumen ke leasing rekanan yang sesuai membuat approval kredit selesai dalam hitungan jam sehingga unit motor bisa langsung dikirim.
> 3. **Kerjasama Promo Subsidi Bersama:** Dealer dan multifinance dapat merancang program subsidi DP yang tepat sasaran pada tipe motor tertentu."*

---

### ❓ PERTANYAAN 2:
> *"Kenapa menggunakan istilah 'Multi-Attribute Association Rule Mining'? Kenapa bukan Market Basket Analysis biasa?"*

#### 💡 Jawaban Rekomendasi:
> *"Izin menjawab Ibu, dalam literatur data mining, Market Basket Analysis klasik umumnya mengolah transaksi multi-barang ritel (seperti roti + mentega).
> 
> Sedangkan pada dealer kendaraan bermotor, konsumen membeli 1 unit fisik kendaraan, namun secara simultan membuat **kumpulan keputusan multiatribut** (Model Motor + Warna + Lembaga Leasing + Tenor Cicilan + DP + Domisili). Mengonversi atribut-atribut relasional ini menjadi entitas keranjang transaksi biner disebut secara formal sebagai **Multi-Attribute / Multi-Dimensional Association Rule Mining**."*

---

### ❓ PERTANYAAN 3:
> *"Kenapa memilih algoritma FP-Growth dibanding Apriori?"*

#### 💡 Jawaban Rekomendasi:
> *"Izin menjawab Ibu, ada 2 keunggulan teknis utama FP-Growth:
> 1. **Tanpa Pembangkitan Kandidat (No Candidate Generation):** Apriori harus memindai database berulang kali untuk setiap kombinasi kandidat (C_k), yang sangat lambat pada ribuan transaksi. Sebaliknya, **FP-Growth hanya memindai database 2 kali saja** dan memadatkan seluruh transaksi ke dalam struktur pohon **FP-Tree**.
> 2. **Efisiensi Waktu & Memori:** FP-Growth menggunakan pendekatan Divide and Conquer yang terbukti jauh lebih cepat pada data transaksi multiatribut."*

---

### ❓ PERTANYAAN 4:
> *"Bagaimana Anda membuktikan bahwa aturan asosiasi yang dihasilkan benar-benar valid dan bukan kebetulan?"*

#### 💡 Jawaban Rekomendasi:
> *"Izin Ibu, kami menggunakan metrik statistik **Lift Ratio**.
> 
> Syarat kaidah asosiasi yang valid secara ilmiah adalah **Lift Ratio > 1.0**.
> 
> Pada eksperimen dataset riil 3.113 transaksi PT. Sinar Surya Matahari, seluruh aturan yang lolos memiliki nilai **Lift Ratio antara 1.58 hingga 4.76**, yang membuktikan adanya korelasi positif nyata antar-atribut transaksi, bukan karena faktor kebetulan barang laris."*
