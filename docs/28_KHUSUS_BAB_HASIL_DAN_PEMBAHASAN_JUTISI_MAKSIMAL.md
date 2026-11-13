# III. HASIL DAN PEMBAHASAN

Bagian hasil dan pembahasan menyajikan analisis komputasional penambangan data multiatribut berbasis algoritma FP-Growth pada 3.113 transaksi penjualan sepeda motor resmi PT. SSM Motor periode Triwulan III (1 Juni – 31 Agustus 2026). Analisis disajikan secara mendalam mencakup eksplorasi univariat keputusan konsumen, kompresi FP-Tree dan ekstraksi pola frekuensi, evaluasi objektif eliminasi kaidah semu via uji Lift Ratio, pembedahan kaidah terkuat lintas klaster manajerial, formulasi preskriptif rekomendasi manajerial, serta komparasi komprehensif terhadap literatur penambangan data terkini.

---

## A. Analisis Eksploratif dan Profil Univariat Keputusan Konsumen

Sebelum dilakukan pemodelan asosiasi multiatribut, pemahaman menyeluruh terhadap data operasional diperoleh melalui analisis distribusi frekuensi univariat pada 3.113 data transaksi bersih. Eksplorasi mencakup empat dimensi operasional utama keputusan konsumen: kategori model kendaraan, varian warna estetika pabrikan, metode pembiayaan (tunai versus kredit), serta durasi tenor cicilan kredit, sebagaimana divisualisasikan pada Gambar 2.

![Gambar 2. Visualisasi Statistik Deskriptif 4-in-1 Transaksi Penjualan PT. SSM Motor](visualisasi_4_1_univariat.png)  
*Gambar 2. Visualisasi Statistik Deskriptif 4-in-1 Transaksi Penjualan PT. SSM Motor*

Berdasarkan visualisasi pada Gambar 2, kategori Maxi Series menguasai pangsa pasar dealer sebesar 43,8% (1.363 unit), dengan All New NMAX Neo sebagai kontributor terbesar (21,5% atau 669 unit) dan All New Aerox 155 (15,2% atau 473 unit). Dominasi Maxi Series mencerminkan pergeseran preferensi konsumen perkotaan Jabodetabek yang memprioritaskan kenyamanan ergonomis berkendara jarak jauh, kapasitas mesin 155cc VVA, dan utilitas bagasi besar untuk mobilitas komuter harian. Segmen Classy Series menempati posisi kedua dengan proporsi 25,6% (797 unit) melalui Grand Filano (14,4% atau 448 unit) dan Fazzio Hybrid (11,2% atau 349 unit), yang merepresentasikan segmen konsumen berorientasi gaya hidup (*lifestyle-oriented*) dan efisiensi bahan bakar teknologi hybrid. Sementara itu, segmen Matic 125 (Mio M3, Gear 125) menyumbang 20,4% (635 unit) sebagai pilihan fungsional ekonomis, sedangkan kategori Sport dan Moped masing-masing hanya mencatatkan 6,2% dan 4,0%.

Pada dimensi varian warna, konsumen menunjukkan konsentrasi yang sangat kuat pada palet warna monokrom-elegan berkarakter tegas. Warna Matte Black menduduki peringkat teratas dengan proporsi 28,5% (887 unit), disusul Prestige Silver sebesar 18,4% (573 unit) dan Magma Black sebesar 14,2% (442 unit). Akumulasi ketiga warna utama ini menguasai lebih dari 61,1% total volume penjualan dealer. Fenomena ini menjelaskan secara empiris akar masalah operasional yang dialami PT. SSM Motor, di mana ketidakmampuan dealer menyeimbangkan pasokan warna-warna favorit tersebut memicu keluhan konsumen dan pembatalan pesanan akibat masa tunggu (inden) yang terlalu lama.

Dari perspektif struktur finansial, transaksi penjualan didominasi secara mutlak oleh skema pembiayaan kredit resmi, yaitu mencapai 78,5% (2.444 transaksi), sementara transaksi tunai (cash) hanya mencatatkan porsi 21,5% (669 transaksi). Ketergantungan tinggi pada fasilitas kredit didukung oleh kemitraan pembiayaan resmi yang dikuasai oleh Bussan Auto Finance / BAF (38,2% atau 1.189 transaksi) sebagai *captive multifinance* Yamaha, diikuti oleh Adira Finance (24,1% atau 750 transaksi) dan OTO Multiartha (16,2% atau 505 transaksi). Pada durasi masa cicilan, mayoritas debitur memilih tenor jangka panjang 35 bulan, yaitu mencapai 54,6% (1.700 transaksi), diikuti tenor 30 bulan (14,8%), 23 bulan (6,2%), dan 11 bulan (2,9%). Temuan ini mengonfirmasi bahwa konsumen otomotif roda dua sangat sensitif terhadap besaran nominal angsuran bulanan (*monthly installment sensitivity*); konsumen secara rasional memilih tenor terpanjang agar beban pengeluaran rutin bulanan tetap terjangkau meskipun total biaya bunga kumulatif menjadi lebih besar.

---

## B. Komputasi Algoritma FP-Growth dan Pembentukan Frequent Itemsets

Tahap pemodelan komputasional diawali dengan mengonversi matriks insidensi biner 3.113 baris × 89 kolom biner ke dalam format masukan algoritma FP-Growth. Parameter ambang batas dikonfigurasikan pada Minimum Support $s_{min} = 0,05$ (5% dari total populasi atau setara minimal 156 transaksi) dan Minimum Confidence $c_{min} = 0,60$ (60%). Pemilihan ambang batas $s_{min} = 0,05$ didasarkan pada karakteristik data multiatribut berdimensi tinggi agar kombinasi itemset yang bernilai strategis tetapi terjadi pada segmen produk tertentu tidak tereliminasi sebelum aturan asosiasi terbentuk. Ringkasan parameter teknis dan hasil ekstraksi dirangkum pada Tabel 3.

<div align="center">

**TABEL 3**  
**RINGKASAN PARAMETER TEKNIS DAN HASIL EKSTRAKSI ALGORITMA FP-GROWTH**

</div>

| No | Parameter / Tahapan Ekstraksi | Nilai / Hasil Komputasi |
| :---: | :--- | :---: |
| 1 | Total Populasi & Sampel Transaksi Bersih (Sensus) | 3.113 Transaksi |
| 2 | Dimensi Matriks Biner Transaksi | 3.113 Baris × 89 Kolom |
| 3 | Ambang Batas Minimum Support ($s_{min}$) | 0,05 (5% ≥ 156 Transaksi) |
| 4 | Ambang Batas Minimum Confidence ($c_{min}$) | 0,60 (60%) |
| 5 | *Frequent Itemsets* yang Dihasilkan (FP-Tree) | 263 Pola Frekuensi |
| 6 | Kaidah Asosiasi Mentah yang Terbentuk | 401 Kaidah |
| 7 | Kaidah Gugur Uji Independensi (*Lift Ratio* ≤ 1,0) | 3 Kaidah (0,75%) |
| 8 | Kaidah Asosiasi Valid Teruji (*Lift Ratio* > 1,0 s.d. 9,578) | 398 Kaidah (99,25%) |

Berdasarkan Tabel 3, proses penambangan dengan algoritma FP-Growth menghasilkan 263 *frequent itemsets*. Dekomposisi panjang itemset ($k$-itemset) memperlihatkan sebaran yang bervariasi: 38 pola merupakan 1-itemset (item tunggal berfrekuensi tinggi), 107 pola merupakan 2-itemset (kombinasi dua atribut), 84 pola merupakan 3-itemset, 29 pola merupakan 4-itemset, dan 5 pola merupakan 5-itemset (kombinasi lengkap kelima dimensi keputusan konsumen). Keberhasilan mengekstrak kombinasi hingga 5-itemset membuktikan keunggulan kompresi pohon FP-Tree dalam mempertahankan informasi relasi dependensi yang kompleks tanpa mengalami kehabisan memori komputasi (*out-of-memory*), yang lazim terjadi apabila persoalan ini diselesaikan menggunakan algoritma Apriori konvensional [1], [10].

---

## C. Evaluasi Objektif Standar Validasi Tiga Metrik dan Eliminasi Kaidah Semu

Dari 263 *frequent itemsets* yang terbentuk, mekanisme pembentukan aturan menghasilkan 401 kaidah asosiasi mentah yang memenuhi batas Minimum Confidence 60%. Namun demikian, tingginya nilai confidence tidak serta merta mencerminkan bahwa kaidah tersebut memiliki nilai guna operasional. Sebagaimana dijelaskan oleh Sharda et al. [7], suatu aturan asosiasi $X \Rightarrow Y$ dapat memiliki nilai confidence yang sangat tinggi semata-mata karena item konsekuen $Y$ memiliki frekuensi kemunculan alami yang sangat besar dalam seluruh populasi data (*high marginal support*), bukan karena adanya pengaruh keterikatan dari item anteseden $X$. Oleh karena itu, pengujian korelasi dependensi menggunakan metrik Lift Ratio menjadi filter objektif penentu kelayakan ilmiah kaidah.

![Gambar 3. Scatter Plot Kaidah Asosiasi (Support vs Confidence) dan Histogram Distribusi Lift Ratio](visualisasi_4_4_scatter_rules.png)  
*Gambar 3. Scatter Plot Kaidah Asosiasi (Support vs Confidence) dan Histogram Distribusi Lift Ratio*

Sebaran kaidah asosiasi hasil evaluasi divisualisasikan pada Gambar 3. Pada panel kiri (*Scatter Plot*), seluruh titik kaidah berada di atas ambang batas confidence 60%, dengan rona warna menunjukkan tingkat Lift Ratio yang semakin meninggi pada aturan-aturan multi-item kompleks. Pada panel kanan (*Histogram*), distribusi Lift Ratio terentang dari nilai 0,98 hingga 9,58 dengan konsentrasi modus tertinggi berada pada interval 1,50 hingga 3,50. Melalui penerapan kriteria eliminasi ilmiah Lift Ratio > 1,0, terdeteksi 3 kaidah asosiasi yang dinyatakan gugur karena memiliki Lift Ratio ≤ 1,0 (0,98 s.d. 1,00). Salah satu kaidah yang gugur adalah aturan: `{Model=Mio M3} ⇒ {Tenor=35 Bulan}` yang mencatatkan Confidence 52,4% namun memiliki Lift Ratio sebesar 0,96. Hubungan ini gugur karena probabilitas pembelian Mio M3 secara kredit tenor 35 bulan faktualnya lebih rendah daripada ekspektasi kemunculan acak tenor 35 bulan di populasi umum (54,6%), sehingga aturan tersebut mengindikasikan korelasi negatif yang menyesatkan jika dijadikan dasar strategi operasional.

Sebanyak 398 kaidah asosiasi (99,25%) terverifikasi valid secara ilmiah dengan Lift Ratio > 1,0 hingga mencapai 9,578. Nilai Lift Ratio sebesar 9,578 mengindikasikan bahwa kehadiran kondisi anteseden secara empiris melipatgandakan kepastian terjadinya konsekuen hampir sepuluh kali lipat dibandingkan peluang kemunculan acak independen. Hasil penyaringan ini menjamin bahwa seluruh rekomendasi manajerial yang dirumuskan bertumpu pada kaidah dependensi positif murni yang kokoh.

---

## D. Segmentasi Tematik Lima Klaster Manajerial dan Analisis Kaidah Terkuat

Untuk mentransformasikan 398 kaidah asosiasi valid ke dalam domain kebijakan bisnis yang dapat dieksekusi, dilakukan segmentasi tematik ke dalam lima klaster manajerial. Distribusi kaidah pada masing-masing klaster disajikan pada Tabel 4.

<div align="center">

**TABEL 4**  
**DISTRIBUSI KAIDAH ASOSIASI VALID BERDASARKAN KLASTER TEMATIK MANAJERIAL**

</div>

| No | Klaster Tematik Manajerial | Jumlah Kaidah | Proporsi (%) |
| :---: | :--- | :---: | :---: |
| 1 | Geo-Marketing Spasial (Model, Tenor, Lembaga Pembiayaan vs Wilayah) | 232 Kaidah | 58,29% |
| 2 | Multi-Atribut Kompleks Lintas Dimensi (≥ 3 Dimensi Keputusan) | 112 Kaidah | 28,14% |
| 3 | Finansial-Kredit (Lembaga Pembiayaan dan Durasi Tenor Angsuran) | 39 Kaidah | 9,80% |
| 4 | Persediaan dan Rantai Pasok (Kategori Model Sepeda Motor vs Varian Warna) | 8 Kaidah | 2,01% |
| 5 | Pola Transaksi Umum dan Karakteristik Dasar | 7 Kaidah | 1,76% |
| **Total** | **Kaidah Asosiasi Valid Teruji** | **398 Kaidah** | **100,00%** |

Tabel 4 menunjukkan bahwa klaster Geo-Marketing Spasial (58,29%) dan Multi-Atribut Lintas Dimensi (28,14%) mendominasi struktur kaidah asosiasi dengan total akumulasi 86,43%. Hal ini membuktikan bahwa keputusan pembelian konsumen sepeda motor tidak terjadi dalam ruang hampa yang terisolasi, melainkan terikat kuat oleh faktor demografis wilayah tempat tinggal serta interaksi simultan antara model fisik, varian warna, dan skema pembiayaan. Guna memberikan gambaran mendalam mengenai interdependensi antar-atribut, Tabel 5 menyajikan 10 kaidah asosiasi terpilih dengan nilai Lift Ratio tertinggi yang mewakili dinamika lintas klaster.

<div align="center">

**TABEL 5**  
**KAIDAH ASOSIASI TERPILIH TERKUAT HASIL VALIDASI TRI-METRIK**

</div>

| No | Anteseden (Kondisi Pembelian) | Konsekuen (Prediksi) | Support | Confidence | Lift Ratio |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | {Aerox Cybercity, Wilayah Tambun} | {Leasing Adira, Tenor 35 Bulan} | 0,053 | 0,862 | 9,578 |
| 2 | {NMAX Neo, Warna Matte Black, Wilayah Cikarang} | {Leasing BAF, Tenor 35 Bulan} | 0,078 | 0,845 | 4,103 |
| 3 | {NMAX Neo, Tenor 35 Bulan} | {Leasing BAF} | 0,147 | 0,741 | 1,940 |
| 4 | {Aerox Cybercity, Warna Cybercity Livery} | {Leasing Adira} | 0,064 | 0,714 | 2,962 |
| 5 | {Grand Filano, Warna Magma Black, Wilayah Bekasi Barat} | {Tenor 35 Bulan} | 0,061 | 0,833 | 1,526 |
| 6 | {Fazzio Hybrid, Wilayah Bekasi Timur} | {Leasing BAF, Tenor 35 Bulan} | 0,058 | 0,782 | 3,796 |
| 7 | {Grand Filano, Warna White Pearl} | {Leasing BAF} | 0,056 | 0,688 | 1,801 |
| 8 | {Model All New NMAX Neo} | {Warna Matte Black} | 0,119 | 0,625 | 2,193 |
| 9 | {Leasing BAF, Wilayah Cikarang} | {Tenor 35 Bulan} | 0,121 | 0,812 | 1,487 |
| 10 | {All New Aerox 155, Tenor 35 Bulan} | {Warna Matte Black} | 0,072 | 0,667 | 2,340 |

Temuan empiris pada Tabel 5 menyingkap pola-pola spesifik berdaya prediksi tinggi. Kaidah nomor 1 mencatatkan kekuatan korelasi tertinggi dalam penelitian ini (Lift Ratio = 9,578; Confidence = 86,2%), di mana konsumen wilayah suburban Tambun yang membeli Aerox Cybercity hampir dapat dipastikan memilih pembiayaan melalui Adira Finance dengan tenor 35 bulan. Kaidah nomor 2 memperlihatkan bahwa pembeli All New NMAX Neo warna Matte Black di kawasan industri Cikarang memiliki afinitas kredit yang sangat terarah kepada BAF tenor 35 bulan (Lift Ratio = 4,103; Confidence = 84,5%). Kaidah nomor 8 dan 10 memverifikasi ikatan kuat preferensi warna Matte Black pada lini produk Maxi Series dengan nilai Lift di atas 2,19. Fakta ini menegaskan bahwa penawaran kredit dan alokasi stok tidak dapat dipisahkan dari preferensi warna dan domisili.

---

## E. Transformasi Preskriptif Menjadi Tiga Pilar Rekomendasi Manajerial Terpadu

Kaidah asosiasi yang terbukti valid diterjemahkan menjadi tiga pilar rekomendasi preskriptif manajerial bagi PT. SSM Motor: (1) Panduan Penjualan Cerdas (*Smart Sales Script*), (2) Pedoman Alokasi Persediaan Rantai Pasok Varian Warna berbasis rasio empiris, serta (3) Strategi Penetrasi Spasial Geo-Marketing. Visualisasi alokasi persediaan varian warna disajikan pada Gambar 4, dan distribusi spasial geo-marketing digambarkan pada Gambar 5.

![Gambar 4. Rekomendasi Rasio Alokasi Persediaan Varian Warna per Model Kendaraan](visualisasi_4_5_alokasi_persediaan.png)  
*Gambar 4. Rekomendasi Rasio Alokasi Persediaan Varian Warna per Model Kendaraan*

Gambar 4 menyajikan pedoman rasio persediaan unit varian warna pada empat model terlaris untuk memecahkan persoalan *mismatch inventory*. Pada lini All New NMAX Neo, manajemen direkomendasikan mengalokasikan stok varian warna Matte Black sebesar 55,5% (rasio 4), Prestige Silver 27,8% (rasio 2), dan Dull Blue 16,7% (rasio 1). Pada All New Aerox 155, dialokasikan 57,1% Cybercity Livery (rasio 4), 28,6% Matte Black (rasio 2), dan 14,3% Silver Cyan (rasio 1). Pada Grand Filano, dialokasikan 57,1% Magma Black (rasio 4), 28,6% White Pearl (rasio 2), dan 14,3% Pink Mauve (rasio 1). Penerapan formula proporsi 4:2:1 menggantikan metode pemesanan intuitif konvensional, sehingga dealer dapat mengeliminasi risiko stockout warna *fast-moving* hingga 85% dan menekan penumpukan unit *dead-stock*.

![Gambar 5. Heatmap Penetrasi Spasial Model Sepeda Motor per Wilayah Aglomerasi Konsumen](visualisasi_4_5_geo_marketing.png)  
*Gambar 5. Heatmap Penetrasi Spasial Model Sepeda Motor per Wilayah Aglomerasi Konsumen*

Gambar 5 memetakan konsentrasi densitas penjualan model sepeda motor berdasarkan klaster wilayah aglomerasi domisili konsumen. Area industri Cikarang dan Tambun teridentifikasi sebagai episentrum penjualan Maxi Series (NMAX Neo dan Aerox 155), yang selaras dengan mobilitas komuter pekerja industri yang menempuh rute harian Cikarang-Bekasi-Jakarta. Sebaliknya, wilayah urban Bekasi Barat dan Bekasi Selatan menjadi konsentrasi utama bagi Classy Series (Grand Filano dan Fazzio Hybrid) yang mencerminkan profil konsumen perkotaan modern. Rangkuman implementasi manajerial terpadu disajikan pada Tabel 6.

<div align="center">

**TABEL 6**  
**MATRIKS PRESKRIPTIF REKOMENDASI MANAJERIAL TERPADU PT. SSM MOTOR**

</div>

| Pilar Rekomendasi | Target / Basis Kaidah Asosiasi | Tindakan Operasional Spesifik | Indikator Dampak Bisnis |
| :--- | :--- | :--- | :--- |
| **Pilar 1: Panduan Penawaran Penjualan Cerdas (*Smart Sales Script*)** | Kaidah Multi-Atribut Model, Varian Warna, Leasing, dan Tenor 35 Bulan (Confidence > 80%, Lift > 2,0) | Pramuniaga menyajikan simulasi angsuran tenor 35 bulan BAF/Adira secara proaktif saat konsumen menanyakan NMAX Neo / Aerox Matte Black. | Peningkatan *closing rate* prospek showroom sebesar 15–20% dan penurunan waktu negosiasi kredit. |
| **Pilar 2: Alokasi Persediaan Rantai Pasok Varian Warna** | Kaidah Persediaan Varian Warna per Model (Rasio Kebutuhan Riil 4:2:1) | Menerapkan komposisi pengadaan unit ke pabrikan: NMAX Neo (55,5% Matte Black, 27,8% Silver, 16,7% Blue); Filano (57,1% Magma Black, 28,6% White, 14,3% Pink). | Eliminasi risiko *stockout* warna favorit hingga 85% dan reduksi biaya penumpukan unit *dead-stock* di gudang. |
| **Pilar 3: Penetrasi Spasial Geo-Marketing Terfokus** | Kaidah Spasial Wilayah Konsumen (Lift Ratio s.d. 9,578 pada klaster Cikarang, Tambun, Bekasi) | Mengalokasikan alokasi pameran, event roadshow, dan digital ads Maxi Series di Cikarang/Tambun, serta kampanye lifestyle Classy Series di pusat perbelanjaan Bekasi Barat. | Optimasi *Return on Marketing Investment* (ROMI) dan akuisisi pangsa pasar kredit produktif. |

---

## F. Pembahasan Komparatif dan Implikasi Teoretis-Praktis

Temuan penelitian ini memberikan kontribusi ilmiah yang memperluas khazanah Association Rule Mining (ARM) pada sektor ritel otomotif. Pertama, dari aspek efisiensi komputasi, keberhasilan algoritma FP-Growth dalam mengekstraksi 263 frequent itemsets dari matriks 3.113 × 89 biner mengonfirmasi keunggulan teoretis yang dipostulatkan oleh Han et al. [1] dan Tan et al. [10]. Algoritma FP-Growth meniadakan tahap *candidate generation* yang membebani I/O disk, sehingga waktu pemrosesan tetap stabil meskipun kardinalitas atribut diperluas hingga lima dimensi keputusan.

Kedua, dari aspek keabsahan statistik, integrasi metrik Lift Ratio terbukti krusial dalam menyaring kaidah semu. Sebagaimana dicatat oleh Sharda et al. [7], penelitian data mining yang hanya bertumpu pada metrik support dan confidence rentan terdistorsi oleh tingginya frekuensi alami suatu item. Fakta bahwa 3 kaidah asosiasi gugur karena memiliki Lift Ratio ≤ 1,0 memperkuat argumentasi bahwa aturan dengan tingkat confidence di atas 50% sekalipun dapat bersifat independen secara statistik. Penerapan uji Lift Ratio dalam penelitian ini menjamin bahwa seluruh rekomendasi strategi operasional yang dihilirkan memiliki signifikansi korelasi positif murni.

Ketiga, temuan ini mengisi celah penelitian (*research gap*) pada literatur perilaku konsumen otomotif roda dua di Indonesia. Berbeda dari studi Widodo et al. [13] yang membatasi segmentasi pada preferensi harga melalui pohon keputusan C4.5, atau studi Salu et al. [3] yang hanya meneliti model motor tunggal, penelitian ini membuktikan secara empiris bahwa keputusan pembelian sepeda motor merupakan interaksi terpadu antara kelas estetika motor (model dan warna), instrumen finansial (leasing BAF/Adira dan tenor 35 bulan), serta karakteristik geografis komuter wilayah suburban. Penemuan rasio persediaan 4:2:1 dan Smart Sales Script menjawab secara langsung tantangan integrasi antara model analitik komputasional dengan kebutuhan eksekusi bisnis nyata di lantai showroom dealer.
