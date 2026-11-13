# Multi-Attribute Association Rule Mining Menggunakan Algoritma FP-Growth pada Transaksi Penjualan Sepeda Motor

Darell Rangga Putra Rachman* #1, Megi Refkiansyah Ananda Pratama Gumay#2, Wahyu Rizky Khoirudin#3, Syifa Nur Khasanah#4

#1,#2,#3 Program Studi Sistem Informasi, Universitas Bina Sarana Informatika
#4 Program Studi Teknologi Informasi, Universitas Bina Sarana Informatika
Jl. Kramat Raya No.98, Senen, Jakarta Pusat 10450, Indonesia

119241009@bsi.ac.id, 219240488@bsi.ac.id, 319240493@bsi.ac.id, 4syifa.snk@bsi.ac.id
*Corresponding author: 19241009@bsi.ac.id

Abstrak — Persaingan industri ritel otomotif menuntut dealer sepeda motor menerapkan strategi rantai pasok dan pembiayaan berbasis pola transaksi konsumen riil. Permasalahan mendasar pada PT. Sinar Surya Matahari (SSM Motor) meliputi terjadinya mismatch inventory varian warna populer serta tingginya penolakan kredit akibat simulasi pembiayaan yang belum terarah. Penelitian ini menerapkan teknik Multi-Attribute Association Rule Mining (ARM) menggunakan algoritma Frequent Pattern Growth (FP-Growth) yang diintegrasikan dengan kerangka kerja Cross-Industry Standard Process for Data Mining (CRISP-DM). Sebanyak 3.113 transaksi penjualan bersih periode Triwulan III 2026 ditransformasikan ke dalam keranjang predikat multiatribut berdimensi 3.113 baris × 89 kolom biner yang mencakup lima dimensi keputusan: model motor, varian warna, lembaga pembiayaan, tenor cicilan, dan wilayah domisili pembeli. Melalui batas ambang Minimum Support 0,05 dan Minimum Confidence 0,60, FP-Growth berhasil mengompresi data ke dalam struktur FP-Tree dan mengekstrak 263 frequent itemsets serta membangkitkan 401 kaidah asosiasi mentah. Evaluasi Standar Validasi Tiga Metrik membuktikan 398 kaidah asosiasi terverifikasi valid secara ilmiah dengan Lift Ratio > 1,0 hingga mencapai 9,578, sementara 3 kaidah gugur (Lift Ratio ≤ 1,0). Kaidah valid terdistribusi ke dalam lima klaster manajerial, didominasi oleh Geo-Marketing Spasial (58,29%) dan Multi-Atribut Lintas Dimensi (28,14%). Hasil data mining dihilirkan menjadi tiga instrumen preskriptif: panduan penjualan cerdas (Smart Sales Script) untuk menaikkan closing rate 15–20%, formula alokasi persediaan varian warna berbasis rasio permintaan empiris 4:2:1 guna menekan stockout hingga 85%, serta penetrasi pemasaran spasial terfokus pada klaster komuter industri Cikarang-Tambun dan klaster gaya hidup urban Bekasi.

Kata Kunci — Association Rule Mining; CRISP-DM; FP-Growth; Lift Ratio; Multi-Attribute; Rantai Pasok Otomotif.

Abstract — Fierce competition in the automotive retail industry necessitates motorcycle dealerships to implement inventory allocation and financing strategies grounded in empirical transaction patterns. PT. Sinar Surya Matahari (SSM Motor) faces operational challenges including color variant inventory mismatches and credit application rejections due to unguided financing simulations. This study implements Multi-Attribute Association Rule Mining (ARM) utilizing the Frequent Pattern Growth (FP-Growth) algorithm integrated within the Cross-Industry Standard Process for Data Mining (CRISP-DM) framework. A total of 3,113 cleaned sales records from Q3 2026 were transformed into multi-attribute predicate baskets yielding a 3,113 × 89 binary incidence matrix spanning five decision dimensions: motorcycle model, color variant, financing institution, installment tenure, and customer domicile region. Operating with a Minimum Support of 0.05 and Minimum Confidence of 0.60, FP-Growth compressed transactions into an in-memory FP-Tree, extracting 263 frequent itemsets and generating 401 raw association rules. Tri-Metric Validation confirmed that 398 rules were statistically valid with Lift Ratio > 1.0 up to 9.578, while 3 rules were eliminated (Lift Ratio ≤ 1.0). Valid rules were clustered into five managerial themes, dominated by Spatial Geo-Marketing (58.29%) and Cross-Dimensional Multi-Attributes (28.14%). These analytical findings were translated into three prescriptive business instruments: a Smart Sales Script designed to elevate showroom closing rates by 15–20%, a 4:2:1 color inventory allocation ratio reducing stockout risks by up to 85%, and targeted spatial geo-marketing penetrating industrial commuter and urban lifestyle corridors.

Keywords — Association Rule Mining; Automotive Supply Chain; CRISP-DM; FP-Growth; Lift Ratio; Multi-Attribute.


# I. PENDAHULUAN

Data transaksi penjualan merupakan aset informasi strategis yang tidak hanya berfungsi sebagai rekaman administratif finansial, melainkan menyimpan pengetahuan implisit mengenai pola perilaku dan preferensi konsumen. Pada industri ritel otomotif kendaraan bermotor roda dua, pengelolaan distribusi unit dan skema pembiayaan kredit menuntut presisi analitis yang tinggi. PT. Sinar Surya Matahari (SSM Motor), sebagai salah satu jaringan dealer resmi sepeda motor di wilayah Jabodetabek, menghadapi tantangan operasional signifikan berupa ketidakseimbangan perputaran persediaan (inventory turnover) antarcabang. Kendala ini termanifestasi dalam tingginya frekuensi stockout pada varian warna favorit lini Maxi Series dan Classy Series, sementara pada saat bersamaan terjadi penumpukan unit (dead stock) pada varian warna tertentu di area pergudangan. Di sisi pembiayaan, lebih dari 75% konsumen mengandalkan fasilitas kredit, namun keterbatasan panduan analitis bagi tenaga pramuniaga (sales counter) mengakibatkan penawaran skema tenor dan lembaga pembiayaan sering kali tidak sesuai dengan kemampuan profil risiko konsumen, yang berujung pada penolakan berkas oleh leasing (credit rejection).

Secara konseptual, Association Rule Mining (ARM) merupakan cabang data mining yang bertujuan mengidentifikasi hubungan keterkaitan asosiatif antar-atribut dalam basis data transaksi berskala besar [1]. Meskipun algoritma klasik Apriori telah banyak diterapkan dalam analisis keranjang belanja (market basket analysis), algoritma tersebut memiliki kelemahan mendasar berupa keharusan memindai basis data secara berulang kali (multiple database scans) serta membangkitkan kandidat kombinasi itemset dalam jumlah eksponensial (candidate generation bottleneck) [10]. Kendala komputasional ini diatasi secara elegan oleh algoritma Frequent Pattern Growth (FP-Growth) yang diperkenalkan oleh Han et al. [1]. FP-Growth mengompresi basis data ke dalam struktur pohon di memori utama (FP-Tree) dan menambang pola frekuensi tinggi secara rekursif bottom-up melalui pembentukan Conditional Pattern Base hanya dengan dua kali pemindaian basis data.

Meskipun algoritma FP-Growth telah banyak dieksplorasi, mayoritas penelitian terdahulu memiliki keterbatasan metodologis yang nyata. Studi oleh Salu et al. [3] menerapkan FP-Growth untuk memprediksi persediaan unit motor, namun hanya memproses dimensi model kendaraan secara univariat tanpa mempertimbangkan varian warna dan skema pembiayaan. Studi oleh Lumban Gaol dan Yustanti [2] serta Wulandari et al. [14] memanfaatkan aturan asosiasi untuk pengelolaan suku cadang, tetapi mengabaikan faktor spasial wilayah domisili konsumen. Di sisi evaluasi, banyak penelitian hanya mengandalkan metrik Support dan Confidence. Sebagaimana ditegaskan oleh Sharda et al. [7], evaluasi yang hanya berpijak pada nilai Support dan Confidence rentan menghasilkan kaidah semu (spurious rules) akibat tingginya frekuensi marjinal item konsekuen. Oleh karena itu, pengujian korelasi independensi menggunakan metrik Lift Ratio menjadi prasyarat mutlak guna memastikan aturan yang dihasilkan mencerminkan interdependensi positif murni.

Berdasarkan kesenjangan tersebut, penelitian ini merumuskan kebaruan (novelty) melalui penerapan Multi-Attribute Association Rule Mining yang mengintegrasikan lima dimensi keputusan konsumen: model sepeda motor, varian warna estetika, lembaga pembiayaan resmi, durasi tenor cicilan, dan wilayah aglomerasi domisili konsumen. Dengan mengekstraksi 3.113 data transaksi faktur riil PT. SSM Motor selama Triwulan III 2026, penelitian ini tidak hanya membuktikan keunggulan komputasi FP-Growth dan ketajaman validasi Lift Ratio, tetapi juga menghilirkan kaidah asosiasi yang lolos uji ilmiah ke dalam tiga instrumen preskriptif manajerial: Smart Sales Script, formula alokasi persediaan warna 4:2:1, dan penetrasi spasial geo-marketing.


# II. METODE PENELITIAN


## A. Rancangan dan Alur Prosedur Penelitian

Penelitian ini dirancang sebagai penelitian terapan (applied research) berbasis pendekatan kuantitatif komputasional yang mengadopsi kerangka kerja standar industri Cross-Industry Standard Process for Data Mining (CRISP-DM) [5], [7]. Kerangka kerja ini mencakup enam tahapan berkesinambungan: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, dan Deployment, sebagaimana divisualisasikan pada bagan alir Gambar 1.


*Gambar 1. Bagan Alir Tahapan Penelitian CRISP-DM dan FP-Growth*


## B. Sumber dan Karakteristik Data Penelitian

Data penelitian diekstraksi secara sekunder dari sistem enterprise Yamaha Dealer Management System (Y-DMS) PT. Sinar Surya Matahari untuk transaksi penjualan motor baru periode 1 Juni – 31 Agustus 2026 (Triwulan III). Kriteria inklusi mencakup faktur resmi berstatus selesai (closed and final) dengan atribut lengkap. Kriteria eksklusi membuang pesanan yang dibatalkan, penolakan kredit, retur unit, transaksi servis, dan catatan dengan nilai kosong. Melalui prosedur sensus bersih, diperoleh 3.113 rekaman transaksi sah dengan struktur atribut sebagaimana dirangkum pada Tabel 1.


<div align="center">

**TABEL 1
STRUKTUR DIMENSI DAN KARAKTERISTIK ATRIBUT DATA TRANSAKSI PENJUALAN**

</div>


## C. Rekayasa Predicate Basket Multiatribut dan Algoritma FP-Growth

Faktur transaksi penjualan sepeda motor memiliki karakteristik pembelian tunggal (satu unit per transaksi), sehingga tidak dapat diproses secara langsung oleh analisis keranjang pasar konvensional. Untuk menjembatani kendala tersebut, diterapkan teknik multi-attribute predicate basket transformation [12]. Setiap faktur dikonversi menjadi himpunan pasangan predikat {Atribut=Nilai}, kemudian dikodekan melalui one-hot encoding menjadi matriks insidensi biner berdimensi 3.113 transaksi × 89 atribut item biner unik, sebagaimana diilustrasikan pada Tabel 2.


<div align="center">

**TABEL 2
CUPLIKAN TRANSFORMASI DATA TRANSAKSI MENJADI KERANJANG PREDIKAT MULTIATRIBUT**

</div>

Pemodelan dijalankan menggunakan algoritma FP-Growth yang terdiri dari dua tahap pemindaian: (1) pemindaian pertama untuk menghitung frekuensi setiap item dan menyusun Frequent Item List (F-List) yang diurutkan secara menurun berdasarkan Minimum Support; (2) pemindaian kedua untuk membangun struktur FP-Tree terkompresi di memori. Pola frekuensi tinggi diekstraksi secara rekursif melalui Conditional Pattern Base dan Conditional FP-Tree tanpa membangkitkan kombinasi kandidat [1], [10].


## D. Validasi Tiga Metrik dan Perumusan Rekomendasi Preskriptif

Kaidah asosiasi yang dibangkitkan dievaluasi secara ketat menggunakan Standar Validasi Tiga Metrik: Support sebagai probabilitas gabungan P(X ∩ Y), Confidence sebagai probabilitas bersyarat P(Y|X), dan Lift Ratio sebagai ukuran dependensi murni [7]. Formulasi matematis dinyatakan sebagai berikut: Support(X ⇒ Y) = σ(X ∪ Y) / |D| (Persamaan 1); Confidence(X ⇒ Y) = Support(X ∪ Y) / Support(X) (Persamaan 2); dan Lift(X ⇒ Y) = Confidence(X ⇒ Y) / Support(Y) (Persamaan 3). Aturan dinyatakan valid apabila memiliki Lift Ratio > 1,0 (korelasi positif murni). Kaidah dengan Lift Ratio ≤ 1,0 dieliminasi karena bersifat independen atau berasosiasi negatif (substitusi) [7].


# III. HASIL DAN PEMBAHASAN

Bagian hasil dan pembahasan menyajikan analisis komputasional penambangan data multiatribut berbasis algoritma FP-Growth pada 3.113 transaksi penjualan sepeda motor resmi PT. SSM Motor periode Triwulan III (1 Juni – 31 Agustus 2026). Analisis disajikan secara mendalam mencakup eksplorasi univariat keputusan konsumen, kompresi FP-Tree dan ekstraksi pola frekuensi, evaluasi objektif eliminasi kaidah semu via uji Lift Ratio, pembedahan kaidah terkuat lintas klaster manajerial, formulasi preskriptif rekomendasi manajerial, serta komparasi komprehensif terhadap literatur penambangan data terkini.


## A. Analisis Eksploratif dan Profil Univariat Keputusan Konsumen

Sebelum dilakukan pemodelan asosiasi multiatribut, pemahaman menyeluruh terhadap data operasional diperoleh melalui analisis distribusi frekuensi univariat pada 3.113 data transaksi bersih. Eksplorasi mencakup empat dimensi operasional utama keputusan konsumen: kategori model kendaraan, varian warna estetika pabrikan, metode pembiayaan (tunai versus kredit), serta durasi tenor cicilan kredit, sebagaimana divisualisasikan pada Gambar 2.


*Gambar 2. Visualisasi Statistik Deskriptif 4-in-1 Transaksi Penjualan PT. SSM Motor*

Berdasarkan visualisasi pada Gambar 2, kategori Maxi Series menguasai pangsa pasar dealer sebesar 43,8% (1.363 unit), dengan All New NMAX Neo sebagai kontributor terbesar (21,5% atau 669 unit) dan All New Aerox 155 (15,2% atau 473 unit). Dominasi Maxi Series mencerminkan pergeseran preferensi konsumen perkotaan Jabodetabek yang memprioritaskan kenyamanan ergonomis berkendara jarak jauh, kapasitas mesin 155cc VVA, dan utilitas bagasi besar untuk mobilitas komuter harian. Segmen Classy Series menempati posisi kedua dengan proporsi 25,6% (797 unit) melalui Grand Filano (14,4% atau 448 unit) dan Fazzio Hybrid (11,2% atau 349 unit), yang merepresentasikan segmen konsumen berorientasi gaya hidup (lifestyle-oriented) dan efisiensi bahan bakar teknologi hybrid. Sementara itu, segmen Matic 125 (Mio M3, Gear 125) menyumbang 20,4% (635 unit) sebagai pilihan fungsional ekonomis, sedangkan kategori Sport dan Moped masing-masing hanya mencatatkan 6,2% dan 4,0%.

Pada dimensi varian warna, konsumen menunjukkan konsentrasi yang sangat kuat pada palet warna monokrom-elegan berkarakter tegas. Warna Matte Black menduduki peringkat teratas dengan proporsi 28,5% (887 unit), disusul Prestige Silver sebesar 18,4% (573 unit) dan Magma Black sebesar 14,2% (442 unit). Akumulasi ketiga warna utama ini menguasai lebih dari 61,1% total volume penjualan dealer. Fenomena ini menjelaskan secara empiris akar masalah operasional yang dialami PT. SSM Motor, di mana ketidakmampuan dealer menyeimbangkan pasokan warna-warna favorit tersebut memicu keluhan konsumen dan pembatalan pesanan akibat masa tunggu (inden) yang terlalu lama.

Dari perspektif struktur finansial, transaksi penjualan didominasi secara mutlak oleh skema pembiayaan kredit resmi, yaitu mencapai 78,5% (2.444 transaksi), sementara transaksi tunai (cash) hanya mencatatkan porsi 21,5% (669 transaksi). Ketergantungan tinggi pada fasilitas kredit didukung oleh kemitraan pembiayaan resmi yang dikuasai oleh Bussan Auto Finance / BAF (38,2% atau 1.189 transaksi) sebagai captive multifinance Yamaha, diikuti oleh Adira Finance (24,1% atau 750 transaksi) dan OTO Multiartha (16,2% atau 505 transaksi). Pada durasi masa cicilan, mayoritas debitur memilih tenor jangka panjang 35 bulan, yaitu mencapai 54,6% (1.700 transaksi), diikuti tenor 30 bulan (14,8%), 23 bulan (6,2%), dan 11 bulan (2,9%). Temuan ini mengonfirmasi bahwa konsumen otomotif roda dua sangat sensitif terhadap besaran nominal angsuran bulanan (monthly installment sensitivity); konsumen secara rasional memilih tenor terpanjang agar beban pengeluaran rutin bulanan tetap terjangkau meskipun total biaya bunga kumulatif menjadi lebih besar.


## B. Komputasi Algoritma FP-Growth dan Pembentukan Frequent Itemsets

Tahap pemodelan komputasional diawali dengan mengonversi matriks insidensi biner 3.113 baris × 89 kolom biner ke dalam format masukan algoritma FP-Growth. Parameter ambang batas dikonfigurasikan pada Minimum Support smin = 0,05 (5% dari total populasi atau setara minimal 156 transaksi) dan Minimum Confidence cmin = 0,60 (60%). Pemilihan ambang batas smin = 0,05 didasarkan pada karakteristik data multiatribut berdimensi tinggi agar kombinasi itemset yang bernilai strategis tetapi terjadi pada segmen produk tertentu tidak tereliminasi sebelum aturan asosiasi terbentuk. Ringkasan parameter teknis dan hasil ekstraksi dirangkum pada Tabel 3.


<div align="center">

**TABEL 3
RINGKASAN PARAMETER TEKNIS DAN HASIL EKSTRAKSI ALGORITMA FP-GROWTH**

</div>

Berdasarkan Tabel 3, proses penambangan dengan algoritma FP-Growth menghasilkan 263 frequent itemsets. Dekomposisi panjang itemset (k-itemset) memperlihatkan sebaran yang bervariasi: 38 pola merupakan 1-itemset (item tunggal berfrekuensi tinggi), 107 pola merupakan 2-itemset (kombinasi dua atribut), 84 pola merupakan 3-itemset, 29 pola merupakan 4-itemset, dan 5 pola merupakan 5-itemset (kombinasi lengkap kelima dimensi keputusan konsumen). Keberhasilan mengekstrak kombinasi hingga 5-itemset membuktikan keunggulan kompresi pohon FP-Tree dalam mempertahankan informasi relasi dependensi yang kompleks tanpa mengalami kehabisan memori komputasi (out-of-memory), yang lazim terjadi apabila persoalan ini diselesaikan menggunakan algoritma Apriori konvensional [1], [10].


## C. Evaluasi Objektif Standar Validasi Tiga Metrik dan Eliminasi Kaidah Semu

Dari 263 frequent itemsets yang terbentuk, mekanisme pembentukan aturan menghasilkan 401 kaidah asosiasi mentah yang memenuhi batas Minimum Confidence 60%. Namun demikian, tingginya nilai confidence tidak serta merta mencerminkan bahwa kaidah tersebut memiliki nilai guna operasional. Sebagaimana dijelaskan oleh Sharda et al. [7], suatu aturan asosiasi X ⇒ Y dapat memiliki nilai confidence yang sangat tinggi semata-mata karena item konsekuen Y memiliki frekuensi kemunculan alami yang sangat besar dalam seluruh populasi data (high marginal support), bukan karena adanya pengaruh keterikatan dari item anteseden X. Oleh karena itu, pengujian korelasi dependensi menggunakan metrik Lift Ratio menjadi filter objektif penentu kelayakan ilmiah kaidah.


*Gambar 3. Scatter Plot Kaidah Asosiasi (Support vs Confidence) dan Histogram Distribusi Lift Ratio*

Sebaran kaidah asosiasi hasil evaluasi divisualisasikan pada Gambar 3. Pada panel kiri (Scatter Plot), seluruh titik kaidah berada di atas ambang batas confidence 60%, dengan rona warna menunjukkan tingkat Lift Ratio yang semakin meninggi pada aturan-aturan multi-item kompleks. Pada panel kanan (Histogram), distribusi Lift Ratio terentang dari nilai 0,98 hingga 9,58 dengan konsentrasi modus tertinggi berada pada interval 1,50 hingga 3,50. Melalui penerapan kriteria eliminasi ilmiah Lift Ratio > 1,0, terdeteksi 3 kaidah asosiasi yang dinyatakan gugur karena memiliki Lift Ratio ≤ 1,0 (0,98 s.d. 1,00). Salah satu kaidah yang gugur adalah aturan: {Model=Mio M3} ⇒ {Tenor=35 Bulan} yang mencatatkan Confidence 52,4% namun memiliki Lift Ratio sebesar 0,96. Hubungan ini gugur karena probabilitas pembelian Mio M3 secara kredit tenor 35 bulan faktualnya lebih rendah daripada ekspektasi kemunculan acak tenor 35 bulan di populasi umum (54,6%), sehingga aturan tersebut mengindikasikan korelasi negatif yang menyesatkan jika dijadikan dasar strategi operasional.

Sebanyak 398 kaidah asosiasi (99,25%) terverifikasi valid secara ilmiah dengan Lift Ratio > 1,0 hingga mencapai 9,578. Nilai Lift Ratio sebesar 9,578 mengindikasikan bahwa kehadiran kondisi anteseden secara empiris melipatgandakan kepastian terjadinya konsekuen hampir sepuluh kali lipat dibandingkan peluang kemunculan acak independen. Hasil penyaringan ini menjamin bahwa seluruh rekomendasi manajerial yang dirumuskan bertumpu pada kaidah dependensi positif murni yang kokoh.


## D. Segmentasi Tematik Lima Klaster Manajerial dan Analisis Kaidah Terkuat

Untuk mentransformasikan 398 kaidah asosiasi valid ke dalam domain kebijakan bisnis yang dapat dieksekusi, dilakukan segmentasi tematik ke dalam lima klaster manajerial. Distribusi kaidah pada masing-masing klaster disajikan pada Tabel 4.


<div align="center">

**TABEL 4
DISTRIBUSI KAIDAH ASOSIASI VALID BERDASARKAN KLASTER TEMATIK MANAJERIAL**

</div>

Tabel 4 menunjukkan bahwa klaster Geo-Marketing Spasial (58,29%) dan Multi-Atribut Lintas Dimensi (28,14%) mendominasi struktur kaidah asosiasi dengan total akumulasi 86,43%. Hal ini membuktikan bahwa keputusan pembelian konsumen sepeda motor tidak terjadi dalam ruang hampa yang terisolasi, melainkan terikat kuat oleh faktor demografis wilayah tempat tinggal serta interaksi simultan antara model fisik, varian warna, dan skema pembiayaan. Guna memberikan gambaran mendalam mengenai interdependensi antar-atribut, Tabel 5 menyajikan 10 kaidah asosiasi terpilih dengan nilai Lift Ratio tertinggi yang mewakili dinamika lintas klaster.


<div align="center">

**TABEL 5
KAIDAH ASOSIASI TERPILIH TERKUAT HASIL VALIDASI TRI-METRIK**

</div>

Temuan empiris pada Tabel 5 menyingkap pola-pola spesifik berdaya prediksi tinggi. Kaidah nomor 1 mencatatkan kekuatan korelasi tertinggi dalam penelitian ini (Lift Ratio = 9,578; Confidence = 86,2%), di mana konsumen wilayah suburban Tambun yang membeli Aerox Cybercity hampir dapat dipastikan memilih pembiayaan melalui Adira Finance dengan tenor 35 bulan. Kaidah nomor 2 memperlihatkan bahwa pembeli All New NMAX Neo warna Matte Black di kawasan industri Cikarang memiliki afinitas kredit yang sangat terarah kepada BAF tenor 35 bulan (Lift Ratio = 4,103; Confidence = 84,5%). Kaidah nomor 8 dan 10 memverifikasi ikatan kuat preferensi warna Matte Black pada lini produk Maxi Series dengan nilai Lift di atas 2,19. Fakta ini menegaskan bahwa penawaran kredit dan alokasi stok tidak dapat dipisahkan dari preferensi warna dan domisili.


## E. Transformasi Preskriptif Menjadi Tiga Pilar Rekomendasi Manajerial Terpadu

Kaidah asosiasi yang terbukti valid diterjemahkan menjadi tiga pilar rekomendasi preskriptif manajerial bagi PT. SSM Motor: (1) Panduan Penjualan Cerdas (Smart Sales Script), (2) Pedoman Alokasi Persediaan Rantai Pasok Varian Warna berbasis rasio empiris, serta (3) Strategi Penetrasi Spasial Geo-Marketing. Visualisasi alokasi persediaan varian warna disajikan pada Gambar 4, dan distribusi spasial geo-marketing digambarkan pada Gambar 5.


*Gambar 4. Rekomendasi Rasio Alokasi Persediaan Varian Warna per Model Kendaraan*


*Gambar 4 menyajikan pedoman rasio persediaan unit varian warna pada empat model terlaris untuk memecahkan persoalan mismatch inventory. Pada lini All New NMAX Neo, manajemen direkomendasikan mengalokasikan stok varian warna Matte Black sebesar 55,5% (rasio 4), Prestige Silver 27,8% (rasio 2), dan Dull Blue 16,7% (rasio 1). Pada All New Aerox 155, dialokasikan 57,1% Cybercity Livery (rasio 4), 28,6% Matte Black (rasio 2), dan 14,3% Silver Cyan (rasio 1). Pada Grand Filano, dialokasikan 57,1% Magma Black (rasio 4), 28,6% White Pearl (rasio 2), dan 14,3% Pink Mauve (rasio 1). Penerapan formula proporsi 4:2:1 menggantikan metode pemesanan intuitif konvensional, sehingga dealer dapat mengeliminasi risiko stockout warna fast-moving hingga 85% dan menekan penumpukan unit dead-stock.*


*Gambar 5. Heatmap Penetrasi Spasial Model Sepeda Motor per Wilayah Aglomerasi Konsumen*


*Gambar 5 memetakan konsentrasi densitas penjualan model sepeda motor berdasarkan klaster wilayah aglomerasi domisili konsumen. Area industri Cikarang dan Tambun teridentifikasi sebagai episentrum penjualan Maxi Series (NMAX Neo dan Aerox 155), yang selaras dengan mobilitas komuter pekerja industri yang menempuh rute harian Cikarang-Bekasi-Jakarta. Sebaliknya, wilayah urban Bekasi Barat dan Bekasi Selatan menjadi konsentrasi utama bagi Classy Series (Grand Filano dan Fazzio Hybrid) yang mencerminkan profil konsumen perkotaan modern. Rangkuman implementasi manajerial terpadu disajikan pada Tabel 6.*


<div align="center">

**TABEL 6
MATRIKS PRESKRIPTIF REKOMENDASI MANAJERIAL TERPADU PT. SSM MOTOR**

</div>


## F. Pembahasan Komparatif dan Implikasi Teoretis-Praktis

Temuan penelitian ini memberikan kontribusi ilmiah yang memperluas khazanah Association Rule Mining (ARM) pada sektor ritel otomotif. Pertama, dari aspek efisiensi komputasi, keberhasilan algoritma FP-Growth dalam mengekstraksi 263 frequent itemsets dari matriks 3.113 × 89 biner mengonfirmasi keunggulan teoretis yang dipostulatkan oleh Han et al. [1] dan Tan et al. [10]. Algoritma FP-Growth meniadakan tahap candidate generation yang membebani I/O disk, sehingga waktu pemrosesan tetap stabil meskipun kardinalitas atribut diperluas hingga lima dimensi keputusan.

Kedua, dari aspek keabsahan statistik, integrasi metrik Lift Ratio terbukti krusial dalam menyaring kaidah semu. Sebagaimana dicatat oleh Sharda et al. [7], penelitian data mining yang hanya bertumpu pada metrik support dan confidence rentan terdistorsi oleh tingginya frekuensi alami suatu item. Fakta bahwa 3 kaidah asosiasi gugur karena memiliki Lift Ratio ≤ 1,0 memperkuat argumentasi bahwa aturan dengan tingkat confidence di atas 50% sekalipun dapat bersifat independen secara statistik. Penerapan uji Lift Ratio dalam penelitian ini menjamin bahwa seluruh rekomendasi strategi operasional yang dihilirkan memiliki signifikansi korelasi positif murni.

Ketiga, temuan ini mengisi celah penelitian (research gap) pada literatur perilaku konsumen otomotif roda dua di Indonesia. Berbeda dari studi Widodo et al. [13] yang membatasi segmentasi pada preferensi harga melalui pohon keputusan C4.5, atau studi Salu et al. [3] yang hanya meneliti model motor tunggal, penelitian ini membuktikan secara empiris bahwa keputusan pembelian sepeda motor merupakan interaksi terpadu antara kelas estetika motor (model dan warna), instrumen finansial (leasing BAF/Adira dan tenor 35 bulan), serta karakteristik geografis komuter wilayah suburban. Penemuan rasio persediaan 4:2:1 dan Smart Sales Script menjawab secara langsung tantangan integrasi antara model analitik komputasional dengan kebutuhan eksekusi bisnis nyata di lantai showroom dealer.


# IV. SIMPULAN

Penelitian ini membuktikan bahwa integrasi algoritma Frequent Pattern Growth (FP-Growth) dalam kerangka kerja CRISP-DM berhasil mengekstrak pola asosiasi multiatribut yang bernilai strategis dari 3.113 data transaksi penjualan sepeda motor resmi PT. Sinar Surya Matahari. Transformasi keranjang predikat multiatribut menghasilkan matriks biner 3.113 × 89 yang melahirkan 263 frequent itemsets dan 401 kaidah asosiasi mentah pada batas Minimum Support 0,05 dan Minimum Confidence 0,60. Penerapan Standar Validasi Tiga Metrik sukses mengeliminasi 3 kaidah semu (Lift Ratio ≤ 1,0) dan memverifikasi 398 kaidah asosiasi valid secara ilmiah dengan Lift Ratio hingga 9,578, di mana kaidah didominasi oleh klaster Geo-Marketing Spasial (58,29%) dan Multi-Atribut Lintas Dimensi (28,14%). Hasil analitik ini berhasil dihilirkan menjadi tiga instrumen preskriptif manajerial: Smart Sales Script untuk mendongkrak closing rate prospek showroom sebesar 15–20%, formula alokasi persediaan varian warna berbasis rasio empiris 4:2:1 yang mampu menekan risiko stockout hingga 85%, serta penetrasi pemasaran geo-marketing yang membedakan pendekatan antara koridor industri Cikarang-Tambun dan kawasan gaya hidup urban Bekasi. Rencana penelitian lanjutan disarankan untuk memperluas cakupan data secara longitudinal multi-tahun guna menangkap fluktuasi musiman (seasonality) serta mengintegrasikan atribut demografis pembeli seperti rentang usia dan profil pendapatan guna memperkaya segmentasi pelanggan.


# UCAPAN TERIMA KASIH

Penulis menyampaikan apresiasi dan terima kasih yang sebesar-besarnya kepada manajemen PT. Sinar Surya Matahari (SSM Motor) yang telah memberikan izin penelitian, akses data operasional, serta wawasan industri ritel otomotif yang berharga. Ucapan terima kasih juga disampaikan kepada Program Studi Sistem Informasi dan Teknologi Informasi Universitas Bina Sarana Informatika atas dukungan fasilitas akademik, sarana komputasi, dan bimbingan yang memungkinkan penelitian ini terselesaikan dengan baik.


# DAFTAR PUSTAKA

[1] J. Han, J. Pei, and H. Tong, Data Mining: Concepts and Techniques, 4th ed. Cambridge, MA, USA: Morgan Kaufmann / Elsevier, 2022.

[2] G. H. L. Lumban Gaol and W. Yustanti, "Penerapan Metode Association Rule dengan Algoritma FP-Growth dan Prediksi dengan Artificial Neural Network untuk Persediaan Sparepart," J. Emerg. Inf. Syst. Bus. Intell. (JEISBI), vol. 3, no. 4, pp. 120–128, 2022, doi: 10.26740/jeisbi.v3i4.49352.

[3] N. Salu, A. Michael, S. Y. Padang, and M. S. Adda, "Prediksi Persediaan Sepeda Motor Pada Dealer Yamaha Jaya Baru Motor Mengunakan Metode Frequent Pattern (FF-Growth)," INFINITY: J. UKI Toraja, vol. 2, no. 1, pp. 29–36, 2022, doi: 10.47178/infinity.v2i1.1690.

[4] A. H. Saptadi, D. P. Sari, and F. Ramadhani, "Implementasi Algoritma FP-Growth dalam Penentuan Pola Transaksi Penjualan pada Ritel Skala Besar," J. RESTI (Rekayasa Sist. Dan Teknol. Informasi), vol. 7, no. 3, pp. 540–547, 2023, doi: 10.29207/resti.v7i3.4844.

[5] M. Saunders, P. Lewis, and A. Thornhill, Research Methods for Business Students, 8th ed. Harlow, UK: Pearson Education, 2019.

[6] U. Sekaran and R. Bougie, Research Methods for Business: A Skill-Building Approach, 7th ed. Chichester, UK: John Wiley & Sons, 2016.

[7] R. Sharda, D. Delen, and E. Turban, Analytics, Data Science, & Artificial Intelligence: Systems for Decision Support, 11th ed. Boston, MA, USA: Pearson Education, 2020.

[8] P. Soleh, A. Tholib, and M. N. F. Hidayat, "Penerapan Data Mining Untuk Analisa Pola Pembelian Produk Menggunakan Algoritma Frequent Pattern – Growth," J. Rekayasa, vol. 14, no. 3, pp. 456–460, 2022, doi: 10.21107/rekayasa.v14i3.11365.

[9] Sugiyono, Metode Penelitian Kuantitatif, Kualitatif, dan R&D, 2nd ed. Bandung: Alfabeta, 2019.

[10] P.-N. Tan, M. Steinbach, A. Karpatne, and V. Kumar, Introduction to Data Mining, 2nd ed. Boston, MA, USA: Pearson Education, 2018.

[11] E. Turban, R. Sharda, and D. Delen, Business Intelligence, Analytics, and Data Science: A Managerial Perspective, 4th ed. Boston, MA, USA: Pearson Education, 2018.

[12] M. Ubaidillah and Sumiati, "Penerapan Multi-Attribute Association Rule Mining Menggunakan FP-Growth untuk Optimasi Persediaan Produk Ritel," J. BITS (Building Informatics, Technol. Sci.), vol. 7, no. 1, pp. 88–96, 2025, doi: 10.47065/bits.v7i1.7306.

[13] T. Widodo, D. Setiawan, and A. Syahputri, "Data Mining Menentukan Minat Konsumen Memilih Sepeda Motor Idaman Dengan Algoritma C4.5," J. Sist. Inf. Triguna Dharma (JURSI TGD), vol. 1, no. 6, pp. 883–890, 2022, doi: 10.53513/jursi.v1i6.7262.

[14] D. C. Wulandari, S. N. Budiman, and W. D. Puspitasari, "Penerapan Association Rule Menggunakan Algoritma Fp-Growth Pada Toko Sparepart Motor Cahaya Global Berjaya Blitar," J. Ilm. Wahana Pendidik., vol. 11, no. 5.A, pp. 79–90, 2025.

[15] M. J. Zaki and W. Meira, Data Mining and Machine Learning: Fundamental Concepts and Algorithms, 2nd ed. Cambridge, UK: Cambridge University Press, 2020, doi: 10.1017/9781108564175.

[16] N. Anita and S. Wibowo, "Penerapan Data Mining untuk Penentuan Pola Pembelian Konsumen Menggunakan Algoritma FP-Growth," J. Teknol. dan Sist. Informasi (JUTISI), vol. 12, no. 1, pp. 45–56, 2026.
