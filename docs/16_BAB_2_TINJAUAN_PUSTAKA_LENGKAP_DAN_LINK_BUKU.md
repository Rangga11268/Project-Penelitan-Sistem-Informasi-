# BAB II: TINJAUAN PUSTAKA (LITERATURE REVIEW)
## MULTI-ATTRIBUTE ASSOCIATION RULE MINING BERBASIS ALGORITMA FP-GROWTH
**Studi Kasus:** PT. Sinar Surya Matahari (Dealer Resmi Sepeda Motor Yamaha)  
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5 UBSI)  
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Kelompok 1:** Darell Rangga Putra R., Megi Refkiansyah, Wahyu Rizky  

> **STANDAR KELAYAKAN SITASI AKADEMIK UBSI:**  
> 1. **Buku Rujukan Teori:** Maksimal 10 tahun terakhir dari 2026 (**2016–2026**).  
> 2. **Artikel Jurnal Empiris:** Maksimal 5 tahun terakhir dari 2026 (**2021–2026**).  
> Seluruh sitasi di bawah ini telah disesuaikan 100% memenuhi standar tersebut dengan tautan resmi penerbit aktif.

---

## 📑 DAFTAR STRUKTUR SUB-BAB TINJAUAN PUSTAKA

* **2.1 Konsep Dasar Data Mining & Association Rule Mining (ARM)**
* **2.2 Metrik Evaluasi Kaidah Asosiasi (Support, Confidence, dan Lift Ratio)**
* **2.3 Algoritma FP-Growth dan Mekanisme Struktur Data FP-Tree**
* **2.4 Multi-Attribute Association Rule Mining pada Keputusan Produk & Pembiayaan Konsumen**
* **2.5 Pemetaan Literatur Empiris Terdahulu (SINTA 2021–2026) & Celah Riset**
* **2.6 Daftar Pustaka Buku Rujukan Utama (2016–2026) & Tautan Resmi Penerbit**

---

## 2.1 Konsep Dasar Data Mining & Association Rule Mining (ARM)

### 2.1.1 Definisi dan Paradigma Data Mining
Data Mining didefinisikan oleh Han, Pei, dan Tong (2022), Tan et al. (2018), serta Zaki dan Meira (2020) sebagai proses penemuan pola implisit, belum diketahui sebelumnya (*previously unknown*), dan berpotensi bernilai guna (*potentially useful*) dari basis data berskala besar melalui integrasi ilmu basis data, statistik, dan *machine learning*. Dalam kerangka *Knowledge Discovery in Databases* (KDD), data mining menempati fase inti ekstraksi pola (*pattern extraction*) setelah tahapan pembersihan data (*data cleaning*), integrasi, dan transformasi data (Witten et al., 2017).

### 2.1.2 Formalisasi Matematis Association Rule Mining (ARM)
Association Rule Mining (ARM) adalah teknik pembelajaran mesin *unsupervised* yang bertujuan menemukan aturan implikasi probabilistik antar-atribut dalam basis data transaksi (Tan et al., 2018; Zaki & Meira, 2020).

Secara formal matematis:
1. Misalkan himpunan seluruh item/atribut direpresentasikan sebagai:
   $$I = \{i_1, i_2, \dots, i_m\}$$
2. Misalkan basis data transaksi $D$ terdiri dari sekumpulan transaksi:
   $$D = \{T_1, T_2, \dots, T_n\}$$
   di mana setiap transaksi $T_k \subseteq I$ dan memiliki pengenal unik *Transaction ID* (TID).
3. Suatu himpunan bagian $X \subseteq I$ disebut sebagai *itemset*. Sebuah *itemset* yang beranggotakan $k$ item disebut sebagai *$k$-itemset*.
4. Kaidah asosiasi (*Association Rule*) diekspresikan dalam bentuk implikasi logis:
   $$X \Rightarrow Y$$
   dengan syarat:
   $$X \subset I, \quad Y \subset I, \quad \text{dan} \quad X \cap Y = \emptyset$$
   di mana $X$ dinamakan *antecedent* (kondisi pendahulu / LHS), dan $Y$ dinamakan *consequent* (kondisi konsekuensi / RHS).

---

## 2.2 Metrik Evaluasi Kaidah Asosiasi (Support, Confidence, dan Lift Ratio)

Untuk memastikan kaidah asosiasi yang dihasilkan memiliki kekuatan inferensial yang valid dan bukan sekadar peristiwa kebetulan (*spurious correlation*), evaluasi dilakukan menggunakan standar tiga metrik (*Tri-Metric Validation*) (Tan et al., 2018; Zaki & Meira, 2020):

### 2.2.1 Support (Dukungan Frekuensi)
*Support* mengukur probabilitas kemunculan bersamaan itemset di dalam seluruh populasi basis data transaksi $D$:

- **Support Itemset ($X$):**
  $$\text{Support}(X) = \frac{|\{T \in D \mid X \subseteq T\}|}{|D|} = P(X)$$

- **Support Kaidah Asosiasi ($X \Rightarrow Y$):**
  $$\text{Support}(X \Rightarrow Y) = \frac{|\{T \in D \mid (X \cup Y) \subseteq T\}|}{|D|} = P(X \cap Y)$$

Kaidah asosiasi wajib memenuhi ambang batas minimum: $\text{Support}(X \Rightarrow Y) \ge \text{Min\_Support}$.

### 2.2.2 Confidence (Tingkat Kepastian / Kepercayaan Kondisional)
*Confidence* mengukur derajat kepastian bersyarat kemunculan item $Y$ apabila item $X$ telah terjadi dalam transaksi:

$$\text{Confidence}(X \Rightarrow Y) = \frac{\text{Support}(X \cup Y)}{\text{Support}(X)} = \frac{P(X \cap Y)}{P(X)} = P(Y \mid X)$$

Kaidah asosiasi wajib memenuhi ambang batas: $\text{Confidence}(X \Rightarrow Y) \ge \text{Min\_Confidence}$.

### 2.2.3 Lift Ratio (Kekuatan Korelasi Dependensi Positif)
*Lift Ratio* mengukur rasio perbandingan antara probabilitas kemunculan bersama aktual terhadap ekspektasi kemunculan jika $X$ dan $Y$ diasumsikan saling bebas (*statistically independent*):

$$\text{Lift}(X \Rightarrow Y) = \frac{\text{Confidence}(X \Rightarrow Y)}{\text{Support}(Y)} = \frac{P(X \cap Y)}{P(X) \cdot P(Y)}$$

**Interpretasi Nilai Lift Ratio:**
* $\text{Lift}(X \Rightarrow Y) > 1.0$: **Korelasi Positif Kuat (Interdependent)**. Keberadaan $X$ meningkatkan peluang kemunculan $Y$ secara nyata di atas faktor kebetulan.
* $\text{Lift}(X \Rightarrow Y) = 1.0$: **Independen**. Tidak ada keterikatan hubungan asosiasi ($P(X \cap Y) = P(X)P(Y)$).
* $\text{Lift}(X \Rightarrow Y) < 1.0$: **Korelasi Negatif (Substitutif)**. Keberadaan $X$ justru menurunkan kemungkinan terjadinya $Y$.

---

## 2.3 Algoritma FP-Growth dan Mekanisme Struktur Data FP-Tree

Algoritma *Frequent Pattern Growth* (FP-Growth) mengatasi kelemahan fundamental algoritma klasik Apriori yang mengalami penurunan performa drastis akibat pemindaian basis data berulang kali (*multiple database scans*) serta ledakan kombinasi kandidat eksponensial ($2^k - 1$) (Han, Pei, & Tong, 2022; Zaki & Meira, 2020).

```
Alur Eksekusi FP-Growth:
1. Scan Database ke-1 ──> Hitung Frekuensi 1-Itemset ──> Eliminasi Item < Min_Support
2. Urutkan Item L-List secara Descending Support Freq
3. Scan Database ke-2 ──> Bangun Frequent Pattern Tree (FP-Tree) & Header Table
4. Divide-and-Conquer ──> Bangun Conditional Pattern Base (CPB) secara Bottom-Up
5. Bentuk Conditional FP-Tree ──> Ekstraksi Frequent Itemsets & Aturan Valid (Lift > 1.0)
```

### 2.3.1 Struktur Data FP-Tree (Frequent Pattern Tree)
FP-Tree adalah struktur data pohon prefiks padat (*extended prefix-tree*) yang menyimpan ringkasan informasi transaksi di memori (*in-memory*) (Han et al., 2022):
1. **Root Node:** Simpul akar berlabel `null`.
2. **Item Prefix Subtree:** Setiap simpul merepresentasikan item dengan atribut `item-name`, `count` (frekuensi jalur yang melintas), dan `node-link` (pointer horizontal ke simpul sejenis).
3. **Header Table:** Tabel kepala yang menyimpan daftar item berfrekuensi tinggi terurut menurun beserta pointer ke simpul pertama pada FP-Tree untuk mempercepat penelusuran tanpa pemindaian ulang.

### 2.3.2 Prosedur Penambangan Rekursif (Conditional Pattern Base)
1. Penelusuran pohon dilakukan mulai dari item dengan frekuensi terendah pada Header Table (*bottom-up*).
2. Membentuk **Conditional Pattern Base (CPB)** yang memuat kumpulan jalur prefiks (*prefix paths*) menuju item yang sedang dievaluasi.
3. Mengonstruksi **Conditional FP-Tree** dari CPB dan mengekstraksi kombinasi pola secara rekursif hingga seluruh pola frekuensi tinggi ditemukan (Zaki & Meira, 2020).

---

## 2.4 Multi-Attribute Association Rule Mining pada Keputusan Produk & Pembiayaan Konsumen

Dalam domain sistem pendukung keputusan (*Decision Support Systems* - DSS) dan analitik bisnis modern (Sharda, Delen, & Turban, 2020), data transaksi tidak hanya berformat biner univariat (barang A dan barang B), melainkan berformat relasional multi-atribut (*multi-attribute predicate data*).

### 2.4.1 Formalisasi Transaksi Multi-Atribut
Setiap transaksi faktur penjualan dealer sepeda motor direpresentasikan sebagai tupel multidimensi:
$$T_k = \langle \text{Model Motor}, \text{Varian Warna}, \text{Lembaga Pembiayaan}, \text{Tenor Cicilan}, \text{Wilayah Domisili} \rangle$$

Kaidah asosiasi multi-atribut yang dihasilkan berbentuk:
$$\left(\text{Model} = \text{NMAX Turbo}\right) \wedge \left(\text{Warna} = \text{Hitam}\right) \wedge \left(\text{Domisili} = \text{Bekasi}\right) \Longrightarrow \left(\text{Leasing} = \text{BAF}\right) \wedge \left(\text{Tenor} = 35\text{ Bulan}\right)$$

### 2.4.2 Implikasi Manajerial & Nilai Terapan
Penerapan Multi-Attribute ARM berbasis FP-Growth menghasilkan 3 manfaat strategis bagi dealer:
1. **Smart Sales Script:** Pramuniaga showroom dapat menyodorkan simulasi angsuran yang paling diminati segmen pembeli model tersebut secara instan guna meningkatkan angka konversi penjualan (*closing rate*).
2. **Optimasi Alokasi Stok Unit & Varian Warna:** Mencegah terjadinya penumpukan stok (*overstock*) atau kekosongan unit (*stockout*) antar-gudang (GD. SSM Bekasi vs SSM Motor Jakarta).
3. **Joint Promotional Packaging:** Perumusan program subsidi uang muka (DP) dan diskon angsuran terarah antara dealer dengan mitra leasing (BAF, Adira, OTO).

---

## 2.5 Pemetaan Literatur Empiris Terdahulu (SINTA 2021–2026) & Celah Riset

Tabel berikut menyintesis telaah literatur artikel jurnal nasional terakreditasi SINTA 1–4 dalam rentang strictly 5 tahun terakhir (**2021–2026**):

| No | Penulis & Tahun | Judul Publikasi & Jurnal | SINTA | Objek & Metode | Temuan Kunci | Research Gap yang Diisi Riset Kelompok 1 |
| :-: | :--- | :--- | :---: | :--- | :--- | :--- |
| **1** | **Soewignyo et al. (2025)** | *Evaluasi Kinerja Apriori & FP-Growth Transaksi Ritel* (*Techno.Com*) | **SINTA 3** | POS Ritel; Apriori vs FP-Growth | 63 aturan valid, Lift 3.29. FP-Growth stabil saat kombinasi atribut membesar. | Hanya 1 dimensi barang ritel murah. Riset kita 5 dimensi pada 3.113 transaksi motor baru. |
| **2** | **Anita & Wibowo (2026)** | *Pola Pembelian Sparepart Preventive Maintenance* (*Jurnal Algoritma*) | **SINTA 4** | Sparepart Bengkel; FP-Growth | FP-Growth memangkas waktu komputasi & memori pada transaksi besar. | Terbatas sparepart bengkel. Riset kita menganalisis unit motor baru dan preferensi leasing. |
| **3** | **Ubaidillah & Sumiati (2025)** | *Inventory Optimization through FP-Growth ARM* (*BITS*) | **SINTA 2** | Material Industri; FP-Growth | Confidence 88.9%, Lift > 2.1 untuk mencegah overstock/stockout. | Diterapkan pada material pengolahan air. Riset kita mengadaptasi ke optimasi stok warna motor. |
| **4** | **Muliawati et al. (2024)** | *Pola Penjualan Sepatu dengan Algoritma FP-Growth* (*JINTEKS*) | **SINTA 4** | Fashion; FP-Growth Multi-Varian | Varian warna & ukuran memiliki korelasi tinggi pada keputusan beli (Lift 1.95). | Tanpa variabel finansial kredit. Riset kita menghubungkan warna bodi dengan leasing & tenor. |
| **5** | **Ismarmiaty & Rismayati (2023)** | *Pola Penjualan Suku Cadang Motor FP-Growth* (*SinkrOn*) | **SINTA 2** | Suku Cadang; FP-Growth | FP-Tree mengompresi data suku cadang secara efisien (Confidence > 75%, Lift > 1.5). | Itemset homogen sparepart. Riset kita memelopori integrasi produk fisik + skema pembiayaan. |

---

## 2.6 DAFTAR PUSTAKA BUKU RUJUKAN UTAMA (2016–2026) & TAUTAN RESMI PENERBIT

1. **Han, J., Pei, J., & Tong, H. (2022).**  
   *Data Mining: Concepts and Techniques* (4th ed.). Morgan Kaufmann / Elsevier.  
   - **Tahun Terbit:** 2022 (4 tahun dari 2026 — *Sangat Baru*)  
   - **ISBN-13:** 978-0-12-811760-6  
   - **Official ScienceDirect Link:** [https://www.sciencedirect.com/book/9780128117606/data-mining-concepts-and-techniques](https://www.sciencedirect.com/book/9780128117606/data-mining-concepts-and-techniques)  
   - **Google Books:** [https://books.google.com/books?id=U_d_EAAAQBAJ](https://books.google.com/books?id=U_d_EAAAQBAJ)

2. **Tan, P.-N., Steinbach, M., Karpatne, A., & Kumar, V. (2018).**  
   *Introduction to Data Mining* (2nd ed.). Pearson Education.  
   - **Tahun Terbit:** 2018 (8 tahun dari 2026)  
   - **ISBN-13:** 978-0-13-312890-1  
   - **Official Publisher (Pearson):** [https://www.pearson.com/en-us/subject-catalog/p/introduction-to-data-mining/P200000003300](https://www.pearson.com/en-us/subject-catalog/p/introduction-to-data-mining/P200000003300)  
   - **Google Books:** [https://books.google.com/books?id=019KDwAAQBAJ](https://books.google.com/books?id=019KDwAAQBAJ)

3. **Zaki, M. J., & Meira, W. (2020).**  
   *Data Mining and Machine Learning: Fundamental Concepts and Algorithms* (2nd ed.). Cambridge University Press.  
   - **Tahun Terbit:** 2020 (6 tahun dari 2026)  
   - **ISBN-13:** 978-1-108-47398-9 | **DOI:** [https://doi.org/10.1017/9781108564175](https://doi.org/10.1017/9781108564175)  
   - **Official Cambridge Link:** [https://www.cambridge.org/highereducation/books/data-mining-and-machine-learning/7D6D8AEFDDA666F53D1C84074251213D](https://www.cambridge.org/highereducation/books/data-mining-and-machine-learning/7D6D8AEFDDA666F53D1C84074251213D)  
   - **Google Books:** [https://books.google.com/books?id=9eLSDwAAQBAJ](https://books.google.com/books?id=9eLSDwAAQBAJ)

4. **Sharda, R., Delen, D., & Turban, E. (2020).**  
   *Analytics, Data Science, & Artificial Intelligence: Systems for Decision Support* (11th ed.). Pearson Education.  
   - **Tahun Terbit:** 2020 (6 tahun dari 2026)  
   - **ISBN-13:** 978-0-13-519201-6  
   - **Official Publisher (Pearson):** [https://www.pearson.com/en-us/subject-catalog/p/analytics-data-science-artificial-intelligence-systems-for-decision-support/P200000003502](https://www.pearson.com/en-us/subject-catalog/p/analytics-data-science-artificial-intelligence-systems-for-decision-support/P200000003502)  
   - **Google Books:** [https://books.google.com/books?id=OQy8DwAAQBAJ](https://books.google.com/books?id=OQy8DwAAQBAJ)

5. **Witten, I. H., Frank, E., Hall, M. A., & Pal, C. J. (2017).**  
   *Data Mining: Practical Machine Learning Tools and Techniques* (4th ed.). Morgan Kaufmann / Elsevier.  
   - **Tahun Terbit:** 2017 (9 tahun dari 2026)  
   - **ISBN-13:** 978-0-12-804291-5  
   - **Official ScienceDirect Link:** [https://www.sciencedirect.com/book/9780128042915/data-mining](https://www.sciencedirect.com/book/9780128042915/data-mining)  
   - **Google Books:** [https://books.google.com/books?id=bPB0CgAAQBAJ](https://books.google.com/books?id=bPB0CgAAQBAJ)
