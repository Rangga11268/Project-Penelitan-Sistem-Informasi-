# III. HASIL DAN PEMBAHASAN

Bagian hasil dan pembahasan menyajikan sintesis komputasional penambangan data multiatribut berbasis algoritma FP-Growth yang diintegrasikan dengan kerangka kerja CRISP-DM pada 3.113 transaksi penjualan sepeda motor resmi PT. Sinar Surya Matahari (SSM Motor) periode Triwulan III (1 Juni – 31 Agustus 2026). Pemaparan disusun secara sistematis mencakup profil distribusi univariat transaksi, parameter teknis pemodelan asosiasi, hasil evaluasi Standar Validasi Tiga Metrik (*Support*, *Confidence*, dan *Lift Ratio*), segmentasi tematik klaster strategis, matriks preskriptif rekomendasi manajerial, serta komparasi teoretis terhadap literatur ilmiah penambangan data terkini.

## A. Profil dan Karakteristik Data Penjualan Multiatribut

Sebelum dilakukan pembentukan keranjang predikat multiatribut, pemahaman mendalam terhadap struktur data diperoleh melalui analisis distribusi statistik univariat pada 3.113 data transaksi bersih (sensus). Eksplorasi mencakup empat dimensi operasional utama keputusan konsumen: kategori model sepeda motor, varian warna estetika, metode pembiayaan (tunai versus kredit), serta durasi tenor angsuran kredit, sebagaimana divisualisasikan pada Gambar 2.

![Gambar 2. Visualisasi Statistik Deskriptif 4-in-1 Transaksi Penjualan PT. SSM Motor](visualisasi_4_1_univariat.png)
Gambar 2. Visualisasi Statistik Deskriptif 4-in-1 Transaksi Penjualan PT. SSM Motor

Berdasarkan visualisasi pada Gambar 2, kategori Maxi Series mendominasi pangsa penjualan dealer sebesar 43,8% (1.363 unit), yang digerakkan secara masif oleh All New NMAX Neo (21,5% atau 669 unit) dan All New Aerox 155 (15,2% atau 473 unit). Segmen Classy Series menempati posisi kedua dengan proporsi 25,6% (797 unit) melalui Grand Filano (14,4% atau 448 unit) dan Fazzio Hybrid (11,2% atau 349 unit). Pada preferensi estetika, warna berkarakter monokrom-elegan mendominasi pilihan konsumen, dipimpin oleh Matte Black (28,5% atau 887 unit), Prestige Silver (18,4% atau 573 unit), dan Magma Black (14,2% atau 442 unit). 

Dari perspektif finansial, 78,5% (2.444 transaksi) diselesaikan melalui fasilitas pembiayaan kredit resmi yang dikuasai oleh Bussan Auto Finance / BAF (38,2% atau 1.189 transaksi) dan Adira Finance (24,1% atau 750 transaksi), dengan durasi tenor 35 bulan sebagai pilihan paling dominan mencapai 54,6% (1.700 transaksi). Temuan deskriptif ini mengonfirmasi bahwa keputusan pembelian sepeda motor di PT. SSM Motor memiliki dependensi kuat antara kelas produk, skema pembiayaan tenor panjang, dan preferensi warna spesifik.

## B. Ekstraksi Pola dan Validasi Kaidah Asosiasi Multi-Atribut

Seluruh 3.113 data transaksi tabular ditransformasikan ke dalam representasi keranjang belanja predikat (*multi-attribute predicate basket*) yang menghasilkan matriks insidensi biner berdimensi 3.113 transaksi × 89 atribut item biner unik. Transformasi predikat berpasangan (misalnya `Model_NMAX_Neo` dan `Warna_Matte_Black`) diterapkan secara ketat guna mencegah terbentuknya kaidah asosiasi semu (*spurious rules*) antar-kategori nilai yang identik [3]. Algoritma FP-Growth dioperasikan dengan ambang batas Minimum Support 0,05 (5% atau setara 156 transaksi) dan Minimum Confidence 0,60 (60%). Ringkasan parameter teknis dan hasil penambangan pola frekuensi dirangkum pada Tabel 2.

TABEL 2. RINGKASAN PARAMETER TEKNIS DAN HASIL EKSTRAKSI ALGORITMA FP-GROWTH

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

Berdasarkan Tabel 2, proses penambangan dengan algoritma FP-Growth berhasil mengompresi basis data ke dalam struktur FP-Tree dan mengekstraksi 263 *frequent itemsets* tanpa membangkitkan kombinasi kandidat yang membebani memori komputasi [2], [4]. Dari itemset tersebut, dibangkitkan 401 kaidah asosiasi mentah. Melalui evaluasi objektif menggunakan metrik *Lift Ratio*, terdapat 3 kaidah asosiasi yang dinyatakan gugur karena memiliki nilai *Lift Ratio* ≤ 1,0 (kejadian independen dan ko-insidensi acak). Sebanyak 398 kaidah asosiasi (99,25%) terbukti valid secara statistik dengan nilai *Lift Ratio* > 1,0 hingga mencapai 9,578, yang menandakan adanya korelasi dependensi positif murni yang signifikan antara atribut anteseden dan konsekuen [5].

![Gambar 3. Scatter Plot Kaidah Asosiasi (Support vs Confidence) dan Histogram Distribusi Lift Ratio](visualisasi_4_4_scatter_rules.png)
Gambar 3. Scatter Plot Kaidah Asosiasi (Support vs Confidence) dan Histogram Distribusi Lift Ratio

Sebaran kaidah asosiasi dan distribusi kekuatan dependensi divisualisasikan pada Gambar 3. Pada panel kiri (*Scatter Plot*), seluruh kaidah terkonsentrasi di atas garis ambang batas kepastian (*Confidence* ≥ 60%), dengan gradien warna menunjukkan intensitas *Lift Ratio* yang tinggi pada kaidah-kaidah multi-item. Pada panel kanan (*Histogram*), distribusi *Lift Ratio* terentang dari 1,01 hingga 9,58 dengan modus frekuensi tertinggi berada pada interval 1,50 – 3,50. Keberadaan kaidah dengan nilai *Lift Ratio* hingga 9,58 membuktikan bahwa probabilitas kemunculan bersama atribut keputusan konsumen meningkat hampir sepuluh kali lipat dibandingkan probabilitas kemunculan secara acak, memberikan fondasi empiris yang sangat kokoh untuk perumusan strategi bisnis.

## C. Segmentasi Tematik Kaidah Asosiasi dan Analisis Manajerial

Untuk memfasilitasi penerjemahan hasil data mining ke dalam kebijakan operasional dealer, 398 kaidah asosiasi valid dikelompokkan ke dalam lima klaster tematik manajerial. Proporsi sebaran masing-masing klaster disajikan pada Tabel 3.

TABEL 3. DISTRIBUSI KAIDAH ASOSIASI VALID BERDASARKAN KLASTER TEMATIK MANAJERIAL

| No | Klaster Tematik Manajerial | Jumlah Kaidah | Proporsi (%) |
| :---: | :--- | :---: | :---: |
| 1 | Geo-Marketing Spasial (Model, Tenor, Lembaga Pembiayaan vs Wilayah) | 232 Kaidah | 58,29% |
| 2 | Multi-Atribut Kompleks Lintas Dimensi (≥ 3 Dimensi Keputusan) | 112 Kaidah | 28,14% |
| 3 | Finansial-Kredit (Lembaga Pembiayaan dan Durasi Tenor Angsuran) | 39 Kaidah | 9,80% |
| 4 | Persediaan dan Rantai Pasok (Kategori Model Sepeda Motor vs Varian Warna) | 8 Kaidah | 2,01% |
| 5 | Pola Transaksi Umum dan Karakteristik Dasar | 7 Kaidah | 1,76% |
| **Total** | **Kaidah Asosiasi Valid Teruji** | **398 Kaidah** | **100,00%** |

Tabel 3 memperlihatkan bahwa klaster Geo-Marketing Spasial dan Multi-Atribut Lintas Dimensi mendominasi lebih dari 86% total kaidah asosiasi yang dihasilkan. Hal ini menegaskan bahwa perilaku konsumen otomotif roda dua sangat dipengaruhi oleh faktor lokasi geografis domisili dan kombinasi terstruktur antara preferensi varian motor, lembaga pembiayaan, serta durasi kredit. Sebagai ilustrasi kekuatan dependensi antar-atribut, Tabel 4 menyajikan 10 kaidah asosiasi terpilih dengan nilai *Lift Ratio* tertinggi yang mewakili dinamika lintas klaster.

TABEL 4. KAIDAH ASOSIASI TERPILIH TERKUAT HASIL VALIDASI TRI-METRIK

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

Temuan pada Tabel 4 memperlihatkan pola asosiasi bernilai strategis tinggi. Kaidah nomor 1 menunjukkan tingkat korelasi tertinggi (*Lift Ratio* = 9,578; *Confidence* = 86,2%), di mana konsumen wilayah suburban Tambun yang membeli model Aerox Cybercity hampir pasti menggunakan fasilitas Adira Finance dengan tenor maksimal 35 bulan. Kaidah nomor 2 membuktikan bahwa pembeli All New NMAX Neo warna Matte Black di kawasan industri Cikarang memiliki afinitas sangat tinggi terhadap pembiayaan BAF tenor 35 bulan (*Lift Ratio* = 4,103; *Confidence* = 84,5%). Sementara itu, kaidah nomor 8 dan 10 memverifikasi ikatan kuat preferensi varian warna Matte Black pada lini produk Maxi Series dengan nilai Lift di atas 2,19.

## D. Matriks Preskriptif Rekomendasi Manajerial Berbasis Data

Kaidah asosiasi yang telah tervalidasi diterjemahkan ke dalam tiga pilar rekomendasi preskriptif operasional bisnis bagi manajemen PT. SSM Motor, yaitu: (1) Pedoman Alokasi Persediaan Stok Warna berbasis rasio permintaan empiris, (2) Strategi Penetrasi Spasial Geo-Marketing berbasis klaster wilayah aglomerasi konsumen, serta (3) Panduan Penawaran Penjualan Cerdas (*Smart Sales Script*) untuk tenaga pramuniaga. Visualisasi alokasi persediaan varian warna disajikan pada Gambar 4, sedangkan distribusi spasial geo-marketing ditunjukkan pada Gambar 5.

![Gambar 4. Rekomendasi Rasio Alokasi Persediaan Varian Warna per Model Kendaraan](visualisasi_4_5_alokasi_persediaan.png)
Gambar 4. Rekomendasi Rasio Alokasi Persediaan Varian Warna per Model Kendaraan

Gambar 4 memberikan panduan kuantitatif alokasi rantai pasok guna mengatasi kendala *mismatch inventory* varian warna. Pada lini All New NMAX Neo, manajemen direkomendasikan mengalokasikan stok varian warna Matte Black sebesar 55,5% (rasio 4), Prestige Silver 27,8% (rasio 2), dan Dull Blue 16,7% (rasio 1). Formula rasio 4:2:1 ini mencegah penumpukan unit pada warna *slow-moving* sekaligus menjamin ketersediaan unit *fast-moving* yang memiliki tingkat permintaan tertinggi di showroom dealer.

![Gambar 5. Heatmap Penetrasi Spasial Model Sepeda Motor per Wilayah Aglomerasi Konsumen](visualisasi_4_5_geo_marketing.png)
Gambar 5. Heatmap Penetrasi Spasial Model Sepeda Motor per Wilayah Aglomerasi Konsumen

Gambar 5 memetakan konsentrasi densitas penjualan model sepeda motor pada kantong-kantong wilayah aglomerasi konsumen. Wilayah industri Cikarang dan Tambun teridentifikasi sebagai episentrum penjualan Maxi Series (NMAX Neo dan Aerox 155), yang berkorelasi erat dengan mobilitas komuter pekerja industri. Sebaliknya, wilayah urban Bekasi Barat dan Bekasi Selatan menjadi konsentrasi utama bagi Classy Series (Grand Filano dan Fazzio Hybrid) yang mencerminkan profil konsumen segmen gaya hidup modern. Sintesis implementasi manajerial terpadu dari temuan penelitian ini dirangkum ke dalam matriks preskriptif pada Tabel 5.

TABEL 5. MATRIKS PRESKRIPTIF REKOMENDASI MANAJERIAL TERPADU PT. SSM MOTOR

| Pilar Rekomendasi | Target / Basis Kaidah Asosiasi | Tindakan Operasional Spesifik | Indikator Dampak Bisnis |
| :--- | :--- | :--- | :--- |
| **Pilar 1: Panduan Penawaran Penjualan Cerdas (*Smart Sales Script*)** | Kaidah Multi-Atribut Model, Varian Warna, Leasing, dan Tenor 35 Bulan (*Confidence* > 80%, *Lift* > 2,0) | Pramuniaga menyajikan simulasi angsuran tenor 35 bulan BAF/Adira secara proaktif saat konsumen menanyakan NMAX Neo / Aerox Matte Black. | Peningkatan *closing rate* prospek showroom sebesar 15–20% dan penurunan waktu negosiasi kredit. |
| **Pilar 2: Alokasi Persediaan Rantai Pasok Varian Warna** | Kaidah Persediaan Varian Warna per Model (Rasio Kebutuhan Riil 4:2:1) | Menerapkan komposisi pengadaan unit ke pabrikan: NMAX Neo (55,5% Matte Black, 27,8% Silver, 16,7% Blue); Filano (57,1% Magma Black, 28,6% White, 14,3% Pink). | Eliminasi risiko *stockout* warna favorit hingga 85% dan reduksi biaya penumpukan unit *dead-stock* di gudang. |
| **Pilar 3: Penetrasi Spasial Geo-Marketing Terfokus** | Kaidah Spasial Wilayah Konsumen (*Lift Ratio* s.d. 9,578 pada klaster Cikarang, Tambun, Bekasi) | Mengalokasikan alokasi pameran, event roadshow, dan digital ads Maxi Series di Cikarang/Tambun, serta kampanye lifestyle Classy Series di pusat perbelanjaan Bekasi Barat. | Optimasi *Return on Marketing Investment* (ROMI) dan akuisisi pangsa pasar kredit produktif. |

## E. Pembahasan Komparatif dan Implikasi Ilmiah

Hasil penambangan data dalam penelitian ini memberikan kontribusi teoretis dan metodologis yang signifikan bagi literatur *Association Rule Mining* (ARM) pada industri otomotif. Pertama, keberhasilan implementasi algoritma FP-Growth pada representasi keranjang predikat multiatribut membuktikan keunggulan komputasional arsitektur pohon terkompresi (FP-Tree) dibandingkan algoritma klasik Apriori. Sejalan dengan postulat Han et al. [2] dan Tan et al. [4], algoritma FP-Growth mampu menambang pola frekuensi secara rekursif *bottom-up* hanya melalui dua kali pemindaian basis data (*two-pass database scan*) tanpa harus mengevaluasi kombinasi kandidat dalam jumlah eksponensial (*candidate generation bottleneck*). Pendekatan ini terbukti efisien dan stabil saat menangani matriks biner berdimensi tinggi (3.113 × 89).

Kedua, dari aspek evaluasi objektif, penerapan Standar Validasi Tiga Metrik (*Support*, *Confidence*, dan *Lift Ratio*) berhasil memitigasi kelemahan mendasar kerangka kerja *support-confidence* konvensional. Sebagaimana diperingatkan oleh Sharda et al. [5], nilai *confidence* yang tinggi kerap kali menyesatkan apabila item konsekuen memiliki frekuensi kemunculan dasar yang sangat besar (*high marginal support*). Dalam penelitian ini, metrik *Lift Ratio* sukses mendeteksi dan mengeliminasi 3 kaidah asosiasi yang memiliki nilai *Lift* ≤ 1,0, sehingga menjamin bahwa 398 kaidah yang direkomendasikan kepada pihak manajemen merupakan korelasi dependensi positif murni, bukan sekadar kebetulan statistik (*spurious coincidence*).

Ketiga, temuan empiris penelitian ini memperkaya diskursus perilaku konsumen otomotif roda dua di wilayah urban-suburban. Berbeda dengan studi otomotif terdahulu seperti penelitian Widodo et al. [6] yang hanya berfokus pada segmentasi harga, atau penelitian Salu et al. [7] yang membatasi analisis pada korelasi tipe suku cadang kendaraan, penelitian ini membuktikan bahwa keputusan pembelian sepeda motor merupakan interaksi multi-segi yang mengikat preferensi model kendaraan, varian warna estetika, karakteristik lembaga pembiayaan, skema tenor kredit jangka panjang (35 bulan), serta lokasi geografis domisili konsumen. Integrasi hasil penambangan data ke dalam skrip penjualan tenaga pramuniaga (*Smart Sales Script*) dan rasio alokasi stok (4:2:1) menjawab secara langsung *research gap* antara model komputasional *data mining* teoritis dengan eksekusi strategi bisnis riil di industri ritel.
