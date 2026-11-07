# 4.4 HASIL EVALUASI DAN VALIDASI TIGA METRIK KAIDAH ASOSIASI (*EVALUATION*)
**Bagian Tim:** Megi Refkiansyah & Wahyu Rizky  
**Kerangka Kerja:** CRISP-DM (*Cross-Industry Standard Process for Data Mining*) — Fase 5: *Evaluation*  
**Dataset Empiris:** Basis Data Transaksi Riil Y-DMS PT. Sinar Surya Matahari (3.113 Rekaman Faktur)

---

Tahap evaluasi (*Evaluation*) merupakan fase krusial dalam siklus hidup penambangan data (*data mining*) berbasis CRISP-DM untuk menguji keabsahan, kekuatan implikasi logis, serta relevansi manajerial dari pola-pola yang telah diekstraksi pada tahap pemodelan (*Modeling*) (Sharda et al., 2020). Berbeda dari penambangan data ritel konvensional yang kerap menghasilkan aturan redundan atau korelasi kebetulan (*spurious correlations*), penelitian ini menerapkan penyaringan ketat berbasis evaluasi tiga metrik objektif (*Tri-Metric Objective Validation*) yang mencakup *Support*, *Confidence*, dan *Lift Ratio* (Tan et al., 2018).

### 4.4.1 Pembentukan Kaidah Implikasi dan Penyaringan Tiga Metrik Objektif

Kaidah asosiasi dibentuk dalam format implikasi kondisional biner $X \Rightarrow Y$, di mana *antecedent* ($X$) dan *consequent* ($Y$) merupakan himpunan bagian dari himpunan item frekuensi tinggi (*frequent itemsets*) yang saling lepas ($X, Y \subseteq I$ dan $X \cap Y = \emptyset$) (Han et al., 2022). Tiga parameter statistik penentu kualitas kaidah didefinisikan sebagai berikut:

1. ***Support*** ($Support(X \Rightarrow Y)$): Mengukur probabilitas kemunculan bersama itemset $X$ dan $Y$ terhadap seluruh populasi transaksi ($N = 3.113$). Dirumuskan sebagai:
   $$\text{Support}(X \Rightarrow Y) = \frac{\sigma(X \cup Y)}{N}$$
   Dalam penelitian ini, ambang batas *minimum support* ditetapkan sebesar 2,0% (ekuivalen dengan batas ambang minimal 62 transaksi empiris).
2. ***Confidence*** ($Confidence(X \Rightarrow Y)$): Mengukur derajat kepastian atau probabilitas bersyarat kemunculan $Y$ ketika $X$ hadir dalam transaksi, dirumuskan:
   $$\text{Confidence}(X \Rightarrow Y) = \frac{\sigma(X \cup Y)}{\sigma(X)}$$
   Ambang batas *minimum confidence* ditetapkan sebesar 50,0%.
3. ***Lift Ratio*** ($Lift(X \Rightarrow Y)$): Mengukur kekuatan korelasi sebenarnya antara $X$ dan $Y$ dengan membandingkan probabilitas bersama terhadap ekspektasi kemunculan independen, dirumuskan:
   $$\text{Lift}(X \Rightarrow Y) = \frac{\text{Confidence}(X \Rightarrow Y)}{\text{Support}(Y)} = \frac{P(X \cap Y)}{P(X) \cdot P(Y)}$$
   Kaidah dinyatakan sahih secara ilmiah (*scientifically valid*) hanya jika memiliki nilai $\text{Lift} > 1,0$, yang membuktikan adanya hubungan saling tarik-menarik positif (*positive correlation*) yang bukan terjadi secara acak (Tan et al., 2018; Zaki & Meira, 2020).

Dari proses komputasi algoritma FP-Growth terhadap 263 *frequent itemsets*, terbentuk sebanyak **398 kaidah asosiasi mentah** yang memenuhi ambang batas *Confidence* $\ge 50,0\%$. Berdasarkan uji *Lift Ratio*, seluruh 398 kaidah tersebut (100%) memiliki nilai $\text{Lift} > 1,0$ dengan rentang nilai antara 1,002 hingga 9,578. Tidak ditemukan satupun kaidah yang memiliki nilai $\text{Lift} \le 1,0$, membuktikan bahwa seluruh kaidah yang diekstraksi bebas dari korelasi semu atau kebetulan statistika.

---

### 4.4.2 Analisis Sebaran Kaidah Asosiasi dan Histogram Distribusi *Lift*

Sebaran kaidah asosiasi hasil evaluasi divisualisasikan melalui diagram pencar ganda (*scatter plot*) dan histogram distribusi *Lift Ratio* pada Gambar 4.2.

<p align="center">
  <img src="../assets/img/visualisasi_4_4_scatter_rules.png" width="90%" alt="Gambar 4.2 Sebaran Kaidah Asosiasi dan Histogram Lift Ratio" />
  <br>
  <em>Gambar 4.2 Sebaran Kaidah Asosiasi (Support vs Confidence Bergradasi Lift) dan Histogram Distribusi Lift Ratio</em>
</p>

Sebagaimana ditampilkan pada Gambar 4.2, seluruh kaidah asosiasi yang terbentuk berada secara konsisten di atas garis ambang batas *Minimum Confidence* 50,0% dan memiliki nilai *Lift Ratio* di atas 1,0. Sebaran titik pada diagram pencar (Gambar 4.2a) memperlihatkan dua karakteristik kaidah utama:
1. **Klaster Kaidah Deterministik (Sisi Kiri Atas):** Dicirikan oleh nilai *Confidence* sempurna 100,0% dan nilai *Lift Ratio* sangat tinggi (berkisar antara 7,173 hingga 9,578) pada tingkat *Support* moderat (2,35% s.d. 3,50%). Kaidah pada klaster ini mencerminkan keterikatan deterministik varian warna karakteristik terhadap model sepeda motor tertentu (misalnya varian warna Hijau Perak yang eksklusif 100% terjual pada tipe Gear 125, serta warna Perak Hijau pada Mio M3 CW).
2. **Klaster Kaidah Frekuensi Tinggi (Sisi Bawah dan Kanan):** Dicirikan oleh tingkat *Support* tinggi (10,0% s.d. 63,3%) dengan nilai *Confidence* berkisar antara 50,0% s.d. 70,0% dan *Lift Ratio* antara 1,2 hingga 1,8. Titik ekstrem kanan atas (*Support* 63,3%, *Confidence* 100%) merepresentasikan transaksi pembelian tunai (*Cash*) yang secara mutlak berpasangan dengan tenor non-kredit (0 bulan).

Sementara itu, histogram pada Gambar 4.2b memperlihatkan bahwa mayoritas kaidah memusat pada nilai *Lift* 1,2 s.d. 2,5, dengan ekor distribusi (*heavy-tailed distribution*) memanjang ke kanan hingga nilai 9,578, mengindikasikan struktur asosiasi multiatribut yang sangat kokoh dan tidak homogen.

---

### 4.4.3 Klasifikasi Klaster Manajerial Kaidah Asosiasi

Guna mempermudah penerjemahan kaidah ke dalam pengambilan keputusan manajerial operasional dealer, 398 kaidah asosiasi yang valid diklasifikasikan ke dalam 4 klaster domain strategis utama sebagaimana dirangkum pada Tabel 4.11.

**Tabel 4.11 Rekapitulasi Distribusi Kaidah Asosiasi Berdasarkan Klaster Manajerial**

| No | Klaster Manajerial | Jumlah Kaidah | Proporsi (%) | Fokus Penerapan Operasional |
| :---: | :--- | :---: | :---: | :--- |
| 1 | Klaster *Geo-Marketing* Spasial | 178 | 44,72% | Penetrasi domisili Jabodetabek & logistik STNK |
| 2 | Klaster Multi-Atribut Kompleks | 112 | 28,14% | *Bundling* Model-Warna-Finansial komprehensif |
| 3 | Klaster Finansial & Pembiayaan | 87 | 21,86% | Kerjasama *leasing* BAF & optimalisasi tenor |
| 4 | Klaster Persediaan & Varian Warna | 14 | 3,52% | Mitigasi *dead stock* varian warna di gudang |
| 5 | Klaster Pola Umum | 7 | 1,76% | Pola umum non-spesifik |

*Sumber: Hasil Pengolahan Algoritma FP-Growth pada Basis Data PT. SSM Motor (2026)*

Distribusi pada Tabel 4.11 membuktikan keunggulan pendekatan *Multi-Attribute Association Rule Mining* dibandingkan analisis *single-item basket*. Lebih dari 44% kaidah memberikan wawasan spasial (*Geo-Marketing*), dan 28% kaidah memetakan interaksi simultan antara tipe motor, preferensi warna, dan skema pembiayaan (Ubaidillah & Sumiati, 2025).

---

### 4.4.4 Evaluasi Top 20 Kaidah Asosiasi Terkuat

Untuk menganalisis kaidah-kaidah dengan daya prediksi tertinggi, Tabel 4.12 menyajikan 20 kaidah asosiasi teratas (*Top 20 Rules*) yang diurutkan berdasarkan nilai *Lift Ratio* tertinggi.

**Tabel 4.12 Top 20 Kaidah Asosiasi Terkuat Berdasarkan Validasi Tri-Metrik**

| No | Antecedent ($X$) | Consequent ($Y$) | Sup | Conf | Lift | Klaster |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | Warna=HIJAU PERAK | Model=GEAR 125 | 2,35% | 100,0% | 9,578 | Persediaan & Warna |
| 2 | Leasing=CASH, Warna=HIJAU PERAK | Model=GEAR 125 | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 3 | Warna=HIJAU PERAK, Tenor=0_BULAN_CASH | Model=GEAR 125 | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 4 | Warna=HIJAU PERAK | Leasing=CASH, Model=GEAR 125 | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 5 | Warna=HIJAU PERAK | Tenor=0_BULAN_CASH, Model=GEAR 125 | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 6 | Warna=HIJAU PERAK | Model=GEAR 125, Leasing=CASH, Tenor=0_BULAN_CASH | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 7 | Leasing=CASH, Warna=HIJAU PERAK | Model=GEAR 125, Tenor=0_BULAN_CASH | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 8 | Leasing=CASH, Warna=HIJAU PERAK, Tenor=0_BULAN_CASH | Model=GEAR 125 | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 9 | Tenor=0_BULAN_CASH, Warna=HIJAU PERAK | Leasing=CASH, Model=GEAR 125 | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 10 | Tenor=0_BULAN_CASH, Warna=HIJAU PERAK | Model=GEAR 125 | 2,35% | 100,0% | 9,578 | Multi-Atribut |
| 11 | Warna=UNGU MUDA | Model=GRAND FILANO HYBRID NEO | 2,76% | 62,32% | 9,194 | Persediaan & Warna |
| 12 | Warna=PERAK HIJAU | Model=MIO M3 CW | 3,50% | 100,0% | 7,173 | Persediaan & Warna |
| 13 | Warna=PERAK HIJAU | Leasing=CASH, Model=MIO M3 CW | 3,50% | 100,0% | 7,189 | Multi-Atribut |
| 14 | Warna=PERAK HIJAU | Model=MIO M3 CW, Tenor=0_BULAN_CASH | 3,50% | 100,0% | 7,189 | Multi-Atribut |
| 15 | Warna=PERAK HIJAU, Tenor=0_BULAN_CASH | Leasing=CASH, Model=MIO M3 CW | 3,50% | 100,0% | 7,189 | Multi-Atribut |
| 16 | Leasing=CASH, Warna=PERAK HIJAU | Model=MIO M3 CW, Tenor=0_BULAN_CASH | 3,50% | 100,0% | 7,189 | Multi-Atribut |
| 17 | Warna=PERAK HIJAU | Model=MIO M3 CW, Leasing=CASH, Tenor=0_BULAN_CASH | 3,50% | 100,0% | 7,189 | Multi-Atribut |
| 18 | Tenor=0_BULAN_CASH, Warna=PERAK HIJAU | Model=MIO M3 CW | 3,50% | 100,0% | 7,173 | Multi-Atribut |
| 19 | Leasing=CASH, Warna=PERAK HIJAU | Model=MIO M3 CW | 3,50% | 100,0% | 7,173 | Multi-Atribut |
| 20 | Warna=HITAM, Tenor=0_BULAN_CASH, Wilayah=JAKARTA_SELATAN | Leasing=CASH, Model=AEROX ALPHA | 5,56% | 65,04% | 5,165 | *Geo-Marketing* |

*Sumber: Hasil Komputasi FP-Growth pada Basis Data PT. SSM Motor (2026)*

Temuan empiris pada Tabel 4.12 memperlihatkan beberapa poin penting:
1. **Eksklusivitas Varian Warna Unit:** Kaidah nomor 1 membuktikan bahwa kemunculan warna Hijau Perak menjamin 100% kepastian (*Confidence* 100%) bahwa unit yang dibeli adalah Yamaha GEAR 125 dengan nilai *Lift* mencapai 9,578. Artinya, konsumen yang memilih warna tersebut memiliki kecenderungan 9,578 kali lebih besar untuk membeli GEAR 125 dibandingkan rata-rata umum transaksi dealer. Pola serupa teramati pada warna Ungu Muda terhadap Grand Filano Hybrid Neo (*Lift* = 9,194; *Confidence* = 62,32%) dan warna Perak Hijau terhadap Mio M3 CW (*Lift* = 7,173 s.d. 7,189; *Confidence* = 100%).
2. **Pola Pembelian Konsumen Jakarta Selatan (*Geo-Marketing*):** Kaidah nomor 20 menunjukkan bahwa konsumen domisili Jakarta Selatan yang memilih warna Hitam dengan skema non-kredit memiliki probabilitas 65,04% untuk membeli tipe Yamaha Aerox Alpha dengan tingkat *Support* signifikan sebesar 5,56% (173 transaksi) dan *Lift* sebesar 5,165. Hal ini membuktikan tingginya penetrasi pasar tipe *sport-scooter* matik Yamaha pada konsumen komuter urban di koridor Jakarta Selatan (Widodo et al., 2022).
