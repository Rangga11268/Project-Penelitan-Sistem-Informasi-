# MASTER KNOWLEDGE BASE: DATA MINING & METODOLOGI PENELITIAN
## SINTESIS KOMPREHENSIF MATERI SLIDE PROF. ROMI SATRIA WAHONO, Ph.D.
*(Rujukan Utama Kurikulum Data Mining & Penelitian Sistem Informasi UBSI)*

---

## 📑 DAFTAR ISI MASTER
1. **Bab 1: Pengantar & Fondasi Keilmuan Data Mining**
2. **Bab 2: 5 Peran Utama Data Mining & Pemetaannya**
3. **Bab 3: Standar Metodologi Riset Data Mining (CRISP-DM vs KDD)**
4. **Bab 4: Tahapan Pra-Pemrosesan Data (*Data Preprocessing*)**
5. **Bab 5: Algoritma Aturan Asosiasi (Apriori vs FP-Growth & 9 Tahap Baku Pak Romi)**
6. **Bab 6: Metrik Evaluasi & Pengujian Validitas (*Support, Confidence, Lift Ratio*)**
7. **Bab 7: Integrasi Materi Pak Romi ke Riset Kelompok 1 (SSM Motor)**
8. **Bab 8: Pedoman Menjawab Pertanyaan Dosen Penguji Berbasis Standar Pak Romi**

---

# BAB 1: PENGANTAR & FONDASI KEILMUAN DATA MINING

### 1.1 Mengapa Data Mining?
* **Fenomena Tsunami Data:** Manusia memproduksi data dalam jumlah eksponensial di berbagai sektor (bisnis, transaksi, IoT, sosial media, transportasi).
* **Masalah Inti:** *"We are drowning in data, but starving for knowledge"* (Kita kebanjiran data, tetapi miskin pengetahuan).
* **Definisi Data Mining:** Proses mengekstrak informasi dan pengetahuan tersembunyi (*hidden predictive information*) yang bermanfaat, baru (*novel*), dan dapat ditindaklanjuti (*actionable*) dari basis data berukuran besar.

### 1.2 Hirarki Data menuju Kebijakan (*The DIKW Pyramid*):
$$\mathbf{Data} \xrightarrow{\text{Diproses}} \mathbf{Informasi} \xrightarrow{\text{Ditambang (Data Mining)}} \mathbf{Pengetahuan (Knowledge)} \xrightarrow{\text{Diterapkan}} \mathbf{Kebijakan (Wisdom)}$$

1. **Data:** Fakta mentah yang tercatat (Contoh: `Faktur 26FJK0101925, Aerox Alpha, BAF, 35 Bulan, Bekasi`).
2. **Informasi:** Data yang telah diagregasi dan diberi konteks (Contoh: *Total penjualan Aerox bulan Juni adalah 108 unit di Bekasi*).
3. **Pengetahuan (*Knowledge / Patterns*):** Pola atau aturan tersembunyi yang dihasilkan oleh algoritma Data Mining:
   $$\text{IF } [\text{Motor: Aerox Alpha}, \text{Wilayah: Jakarta}] \rightarrow \text{THEN } [\text{Leasing: BAF}, \text{Tenor: 35 Bulan}] \quad (\text{Confidence: } 85\%)$$
4. **Kebijakan (*Wisdom / Decision*):** Keputusan manajerial strategis yang diambil berdasarkan pengetahuan tersebut (Contoh: *Dealer membuat promo subsidi DP bersama BAF khusus Aerox di Jakarta*).

---

# BAB 2: 5 PERAN UTAMA DATA MINING

Pak Romi mengklasifikasikan tugas data mining ke dalam 5 peran utama:

| No | Peran Data Mining | Tipe Pembelajaran (*Learning*) | Bentuk Output / Pengetahuan | Algoritma Utama |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Estimasi (*Estimation*)** | *Supervised Learning* (Ada Label Kontinu/Numerik) | Formula / Fungsi Matematis | *Linear Regression, Multiple Linear Regression, Neural Network* |
| 2 | **Prediksi / Peramalan (*Forecasting*)** | *Supervised Learning* (Data Runtun Waktu / *Time Series*) | Nilai Prediksi Masa Depan | *ARIMA, Linear Regression, Neural Network (LSTM)* |
| 3 | **Klasifikasi (*Classification*)** | *Supervised Learning* (Ada Label Kategori/Diskret) | Model Pohon Keputusan, Aturan Klasifikasi | *Decision Tree (C4.5/CART), Naïve Bayes, k-NN, SVM, Random Forest* |
| 4 | **Klasterisasi (*Clustering*)** | *Unsupervised Learning* (Tanpa Label Awal) | Pengelompokan Klaster (*Centroid / Hierarchy*) | *K-Means, K-Medoids, DBSCAN, Hierarchical Clustering* |
| 5 | **Aturan Asosiasi (*Association*)** | *Unsupervised Learning* (Data Transaksional) | Pola Aturan Implikasi (*IF Antecedent THEN Consequent*) | **FP-Growth, Apriori, Eclat** |

> 📌 **Catatan Khusus Topik Kita (Kelompok 1):**  
> Topik kita masuk ke **Peran No. 5: Aturan Asosiasi (*Association Rule Mining*)**, yang bersifat *Unsupervised Learning* pada basis data transaksi multi-atribut.

---

# BAB 3: STANDAR METODOLOGI RISET DATA MINING (CRISP-DM)

Standar proses industri de facto yang diajarkan oleh Pak Romi adalah **CRISP-DM (*Cross-Industry Standard Process for Data Mining*)**:

```
 ┌────────────────────────────────────────────────────────┐
 │ 1. Business Understanding  ⇄  2. Data Understanding    │
 │                 ⬇                                      │
 │        3. Data Preparation ⇄ 4. Modeling               │
 │                 ⬇                                      │
 │            5. Evaluation                               │
 │                 ⬇                                      │
 │            6. Deployment                               │
 └────────────────────────────────────────────────────────┘
```

1. **Business Understanding:** Menentukan tujuan bisnis dealer, menerjemahkan masalah kegagalan penjualan (*price shock*) menjadi masalah data mining.
2. **Data Understanding:** Mengumpulkan data mentah (3.113 transaksi SSM Motor), memeriksa sebaran data, mengidentifikasi tipe data numerik vs kategorikal.
3. **Data Preparation:** Pembersihan data kotor (*cleaning*), penanganan nilai hilang (*missing values*), pembentukan keranjang multi-atribut, dan konversi ke biner (*One-Hot Encoding*).
4. **Modeling:** Menjalankan algoritma **FP-Growth** untuk membentuk *FP-Tree* dan mengekstrak *Frequent Itemsets*.
5. **Evaluation:** Menguji kualitas aturan asosiasi menggunakan metrik *Support, Confidence*, dan *Lift Ratio* ($\text{Lift} > 1.0$).
6. **Deployment:** Mengemas aturan asosiasi ke dalam sistem/SOP sales dealer dan artikel publikasi jurnal.

---

# BAB 4: TAHAPAN PRA-PEMROSESAN DATA (*DATA PREPROCESSING*)

Data mentah di dunia nyata selalu memiliki masalah (*GIGO - Garbage In, Garbage Out*). Tahapan preprocessing menurut materi Pak Romi:

1. **Data Cleaning (Pembersihan Data):**
   * *Missing Values*: Membuang atau mengisi data kosong pada kolom vital.
   * *Noise & Outliers*: Memperbaiki nilai data anomali.
2. **Data Integration (Integrasi Data):** Menggabungkan tabel transaksi bulan Juni, Juli, dan Agustus 2026 menjadi satu kesatuan 3.113 baris.
3. **Data Transformation (Transformasi Data):**
   * *Discretization / Binning*: Mengelompokkan data numerik kontinu (misal: Tenor cicilan `11, 23, 30, 35` bulan; Umur `<25, 26-35, >35`).
   * *Binarization / One-Hot Encoding*: Mengonversi daftar item ke format biner (True/False atau 1/0) agar siap diproses oleh algoritma.
4. **Data Reduction (Reduksi Data):** Menyeleksi atribut yang relevan (*Feature Selection*) dan mengabaikan atribut teknis yang tidak relevan (seperti No. Rangka, No. Mesin, No. BPKB).

---

# BAB 5: ALGORITMA ATURAN ASOSIASI (APRIORI VS FP-GROWTH)

### 5.1 Mengapa FP-Growth Lebih Unggul dari Apriori? (Analisis Pak Romi Slide 585-597)
* **Kelemahan Algoritma Apriori:**
  1. *Multiple Database Scans*: Apriori harus membaca (*scan*) seluruh basis data berulang-ulang sebanyak $k$-itemset yang diuji.
  2. *Bottleneck Candidate Generation*: Membangkitkan kombinasi kandidat ($C_k$) yang jumlahnya meledak secara kombinatorial ($2^N - 1$), memakan memori RAM dan waktu komputasi yang sangat lama pada ribuan data.
* **Keunggulan Algoritma FP-Growth (*Frequent Pattern Growth*):**
  1. *Hanya 2 Kali Scan Database*: Scan ke-1 mencari item frekuensi tinggi, Scan ke-2 langsung membangun pohon terkompresi (**FP-Tree**).
  2. *Tanpa Candidate Generation*: Menggunakan strategi *Divide and Conquer* dengan membentuk basis pola bersyarat (**Conditional Pattern Base**) sehingga komputasi sangat cepat.

---

### 5.2 Sembilan (9) Langkah Baku Perhitungan FP-Growth (Pak Romi Slide 601–611):

```
1. Penyiapan Dataset Transaksi
       ⬇
2. Pencarian Frequent 1-Itemset (Filter Minimum Support)
       ⬇
3. Pengurutan Item Berdasarkan Frekuensi Tertinggi (Priority Header Table)
       ⬇
4. Pembuatan Pohon FP-Tree (Root {} ➔ Cabang Transaksi)
       ⬇
5. Pembangkitan Conditional Pattern Base (Jalur Prefix Bottom-Up)
       ⬇
6. Pembangkitan Conditional FP-Tree
       ⬇
7. Pembangkitan Frequent Pattern (Kombinasi Pola Sering Muncul)
       ⬇
8. Perhitungan Nilai Support Aturan
       ⬇
9. Perhitungan Nilai Confidence & Lift Ratio Aturan
```

1. **Tahap 1 (Dataset):** Menyiapkan 3.113 data keranjang multi-atribut.
2. **Tahap 2 (Frequent 1-Itemset):** Menghitung frekuensi kemunculan tiap item mandiri dan membuang item yang tidak memenuhi ambang batas *Minimum Support*.
3. **Tahap 3 (Priority Sorting):** Mengurutkan item pada setiap transaksi dari yang paling sering muncul ke yang paling jarang (*F-List descending*).
4. **Tahap 4 (FP-Tree Construction):** Membaca transaksi baris per baris dan menyisipkannya ke dalam struktur pohon (*Root node {}*). Jika jalur sudah ada, tambahkan *counter count*; jika belum, buat cabang baru.
5. **Tahap 5 (Conditional Pattern Base):** Membaca FP-Tree dari item paling bawah (*bottom-up* pada Header Table) dan mencari seluruh jalur awalan (*prefix path*) yang menuju ke item tersebut.
6. **Tahap 6 (Conditional FP-Tree):** Menghitung akumulasi frekuensi item pada prefix path dan membuang item yang di bawah ambang batas.
7. **Tahap 7 (Frequent Pattern Generation):** Mengombinasikan item target dengan conditional FP-tree untuk menghasilkan *Frequent $k$-Itemsets*.
8. **Tahap 8 (Support Calculation):** Menghitung proporsi kemunculan kombinasi $A$ dan $B$ terhadap total transaksi.
9. **Tahap 9 (Confidence & Lift Calculation):** Menghitung rasio kepastian aturan dan membuktikan signifikansi keterkaitannya.

---

# BAB 6: METRIK EVALUASI ATURAN ASOSIASI

Menurut materi Pak Romi (Slide 612–618), evaluasi aturan asosiasi $A \rightarrow B$ wajib menggunakan 3 metrik utama:

### 1. Support
Probabilitas bahwa transaksi mengandung itemset $A$ dan $B$ secara bersamaan:
$$\text{Support}(A \rightarrow B) = P(A \cup B) = \frac{\text{Count}(A \cup B)}{N}$$

### 2. Confidence
Tingkat kepastian bahwa jika transaksi mengandung $A$, maka transaksi tersebut juga mengandung $B$:
$$\text{Confidence}(A \rightarrow B) = P(B|A) = \frac{\text{Support}(A \cup B)}{\text{Support}(A)} = \frac{\text{Count}(A \cup B)}{\text{Count}(A)}$$

### 3. Lift Ratio (Korelasi & Signifikansi Statistik)
Mengukur seberapa jauh kemunculan $A$ dan $B$ saling bergantung satu sama lain dibanding jika keduanya muncul secara independen:
$$\text{Lift}(A \rightarrow B) = \frac{\text{Confidence}(A \rightarrow B)}{\text{Support}(B)} = \frac{P(A \cup B)}{P(A) \times P(B)}$$

* **Interpretasi Nilai Lift Ratio (Wajib Dipahami):**
  * **$\text{Lift} > 1.0$**: **Korelasi Positif Kuat (Valid & Signifikan)**. Pembelian $A$ secara nyata meningkatkan kemungkinan pembelian $B$. Ini adalah aturan emas yang bernilai bisnis tinggi.
  * **$\text{Lift} = 1.0$**: **Independen (Netral)**. Kemunculan $A$ dan $B$ tidak saling memengaruhi (hanya kebetulan).
  * **$\text{Lift} < 1.0$**: **Korelasi Negatif**. Pembelian $A$ justru menurunkan kemungkinan pembelian $B$ (saling menggantikan / tolak).

---

# BAB 7: INTEGRASI KE RISET KELOMPOK 1 (SSM MOTOR)

Berdasarkan seluruh kaidah di atas, riset kita pada Dealer SSM Motor telah memenuhi standar ilmiah sempurna:

1. **Objek Penelitian:** PT. SSM Motor (Dealer Resmi Yamaha – GD.SSM Bekasi & SSM Motor).
2. **Dataset:** 3.113 transaksi riil (Juni – Agustus 2026).
3. **Penerapan Multi-Atribut:** Keranjang transaksi tidak hanya berupa barang fisik, tetapi gabungan keputusan:
   $$\mathbf{Basket} = \{\text{Model Motor}, \text{Warna}, \text{Leasing}, \text{Tenor}, \text{Wilayah}\}$$
4. **Hasil Aturan Asosiasi Nyata ($\text{Lift} > 1.0$):**
   * *Pola 1 (Komuter Bekasi)*:
     $$\text{IF } [\text{Wilayah: Bekasi}, \text{Bayar: CASH}] \rightarrow \text{THEN } [\text{Motor: MIO M3 CW}] \quad (\text{Confidence: } 66.2\%, \text{Lift: } 4.75)$$
   * *Pola 2 (Sport Lifestyle Jakarta)*:
     $$\text{IF } [\text{Wilayah: Jakarta Selatan}, \text{Motor: AEROX ALPHA}] \rightarrow \text{THEN } [\text{Leasing: BAF}, \text{Tenor: 30-35 Bulan}] \quad (\text{Confidence: } 78\%, \text{Lift: } 3.37)$$
   * *Pola 3 (Moped Sport Hobi)*:
     $$\text{IF } [\text{Motor: MX KING 150}] \rightarrow \text{THEN } [\text{Pembayaran: CASH}] \quad (\text{Confidence: } 100\%, \text{Lift: } 1.58)$$

---

# BAB 8: PEDOMAN MENJAWAB PERTANYAAN DOSEN (STANDAR PAK ROMI)

Jika Bu Syifa menguji menggunakan standar materi Pak Romi, berikut jawaban kuncinya:

1. **Dosen:** *"Mengapa penelitian ini termasuk Data Mining dan bukan Statistik Deskriptif biasa?"*
   * **Jawaban:** *"Izin Ibu, statistik deskriptif hanya merangkum data masa lalu (seperti total penjualan per bulan). Sedangkan penelitian kita menggunakan Data Mining peran **Aturan Asosiasi (FP-Growth)** untuk menemukan **pengetahuan pola relasi implikasi tersembunyi (Knowledge/Pattern Discovery)** antar-variabel keputusan konsumen yang memiliki nilai prediktif bagi strategi masa depan."*
2. **Dosen:** *"Kenapa memilih FP-Growth dibanding Apriori?"*
   * **Jawaban:** *"Sesuai dengan konsep algoritma asosiasi, Apriori mengalami kendala komputasi pada *candidate generation* dan *multiple database scanning*. FP-Growth hanya memindai database **2 kali saja** dan memampatkan data ke dalam struktur pohon **FP-Tree**, sehingga proses penambangan pola berulang menjadi jauh lebih efisien pada 3.113 data transaksi kita."*
3. **Dosen:** *"Bagaimana membuktikan aturan asosiasi ini tidak bias atau kebetulan?"*
   * **Jawaban:** *"Kami mengujinya menggunakan metrik **Lift Ratio**. Sesuai teori, aturan dinyatakan valid dan berkorelasi positif hanya jika nilai **$\text{Lift} > 1.0$**. Pada eksperimen data riil SSM Motor kami, seluruh aturan yang lolos memiliki nilai **Lift antara 1.58 hingga 4.76**."*
