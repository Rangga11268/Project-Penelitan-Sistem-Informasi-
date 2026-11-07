# BAB IV: HASIL DAN PEMBAHASAN
*(Kerangka Kerja CRISP-DM — Multi-Attribute Association Rule Mining Algoritma FP-Growth pada PT. Sinar Surya Matahari)*

---

## 4.1 Profil Objek dan Statistik Deskriptif Data (*Data Understanding*)

Tahap pemahaman data (*data understanding*) dalam kerangka kerja *Cross-Industry Standard Process for Data Mining* (CRISP-DM) bertujuan untuk mengidentifikasi karakteristik intrinsik, memverifikasi kualitas dan integritas data, serta mengekstraksi wawasan awal dari himpunan data empiris sebelum tahapan penyiapan (*data preparation*) dan pemodelan (*modeling*) algoritma dijalankan (Sharda et al., 2020). Pada sub-bab ini, dipaparkan gambaran umum basis data transaksi operasional *Yamaha Dealer Management System* (Y-DMS) milik PT. Sinar Surya Matahari (SSM Motor) serta analisis distribusi frekuensi univariat pada lima dimensi utama keputusan pembelian unit kendaraan roda dua (Tan et al., 2018).

---

### 4.1.1 Gambaran Umum Data Transaksi Y-DMS PT. SSM Motor

Data empiris yang dianalisis dalam penelitian ini bersumber langsung dari sistem informasi terpadu *Yamaha Dealer Management System* (Y-DMS) milik PT. Sinar Surya Matahari (SSM Motor), yaitu dealer resmi sepeda motor Yamaha yang beroperasi melayani kawasan aglomerasi Jabodetabek dengan basis pergudangan dan distribusi utama berlokasi di Kota Bekasi. Basis data yang diekstraksi merekam aktivitas transaksi faktur penjualan unit kendaraan selama periode operasional 1 Juni 2026 hingga 31 Agustus 2026 (Kuartal III). 

Populasi data mentah yang diekstraksi mencakup **3.113 rekaman faktur penjualan tunggal** (*single-item retail invoices*). Sebagaimana diidentifikasi dalam studi Salu et al. (2022), transaksi penjualan unit sepeda motor pada dealer resmi memiliki karakteristik operasional yang sangat berbeda dengan transaksi keranjang belanja ritel barang konsumen harian: setiap nomor faktur transaksi (`NO_FAKTUR`) hanya mencatat pembelian **1 unit sepeda motor** beserta atribut spesifikasi teknis kendaraan dan fasilitas pembiayaan yang menyertainya.

Setiap baris transaksi pada basis data Y-DMS memuat 12 atribut operasional yang merepresentasikan entitas administratif, teknis kendaraan, finansial pembiayaan, hingga profil sosio-demografis konsumen. Tabel 4.1 menyajikan metadata skema atribut mentah yang terdapat dalam pangkalan data Y-DMS PT. SSM Motor.

<br>

**Tabel 4.1 Metadata Skema Atribut Data Transaksi Penjualan Y-DMS PT. SSM Motor**

| No | Nama Atribut | Tipe Data | Contoh Nilai Riil | Deskripsi dan Relevansi Bisnis |
| :-: | :--- | :--- | :--- | :--- |
| 1 | `TG_FAKTUR` | Date / String | 2026-06-02 | Tanggal penerbitan faktur penjualan resmi dari sistem dealer kepada konsumen. |
| 2 | `NO_FAKTUR` | Varchar (Kunci) | 0126/B/FAK/000001 | Nomor unik identifikasi faktur transaksi penjualan unit motor (berfungsi sebagai *Basket ID*). |
| 3 | `NO_PESAN` | Varchar | 0126/B/SPK/000001 | Nomor Surat Pemesanan Kendaraan (SPK) yang menjadi rujukan awal pemesanan unit. |
| 4 | `NAMA_BRG` | Varchar (Kategorikal) | AEROX ALPHA | Tipe dan model spesifik unit sepeda motor yang dibeli konsumen (mencakup 44 model). |
| 5 | `WARNA` | Varchar (Kategorikal) | HITAM | Varian warna estetika unit motor yang dipilih konsumen (mencakup 22 varian warna). |
| 6 | `NMLEASE` | Varchar (Kategorikal) | BAF BHL | Identitas skema pembayaran: transaksi tunai (`CASH`) atau nama lembaga pembiayaan/*leasing* kredit. |
| 7 | `JK_WAKTU` | Integer (Numerik) | 35 | Jangka waktu (tenor) cicilan kredit dalam satuan bulan (bernilai 0 untuk transaksi tunai/*cash*). |
| 8 | `NILAI_UMK` | Float / Moneter | 3.500.000 | Besaran uang muka (*Down Payment* / DP) yang disetorkan konsumen dalam skema kredit (Rp). |
| 9 | `NILAI_JUAL` | Float / Moneter | 28.750.000 | Nilai harga jual *On The Road* (OTR) unit sepeda motor yang tercantum pada faktur transaksi (Rp). |
| 10 | `KOTA` | Varchar (Kategorikal) | BEKASI, KOTA. | Wilayah administratif kota atau kabupaten tempat tinggal domisili konsumen pemohon faktur. |
| 11 | `UMUR` | Integer (Numerik) | 28 | Usia konsumen pembeli unit sepeda motor saat transaksi diterbitkan (tahun). |
| 12 | `NM_CABANG` | Varchar (Kategorikal) | GD.SSM BEKASI | Identitas entitas titik distribusi operasional dealer tempat unit diproses dan diserahterimakan. |

*Sumber: Pangkalan Data Y-DMS PT. Sinar Surya Matahari (2026)*

<br>

Berdasarkan struktur pada Tabel 4.1, atribut operasional yang bersifat administratif dan moneter kontinu (`TG_FAKTUR`, `NO_PESAN`, `NILAI_UMK`, `NILAI_JUAL`, dan `UMUR`) tidak ditambang secara langsung sebagai predikat biner asosiasi, melainkan dialokasikan sebagai parameter verifikasi keabsahan data dan pembagian segmen. Sementara itu, lima atribut inti keputusan konsumen, yaitu **Model Unit Motor (`NAMA_BRG`)**, **Varian Warna (`WARNA`)**, **Lembaga Pembiayaan (`NMLEASE`)**, **Tenor Angsuran (`JK_WAKTU`)**, dan **Wilayah Domisili Konsumen (`KOTA`)** ditetapkan sebagai variabel fokus dalam pembentukan keranjang predikat multiatribut (*multi-attribute predicate basket*) pada tahapan penyiapan data (Ubaidillah & Sumiati, 2025).

---

### 4.1.2 Distribusi Frekuensi Univariat

Analisis distribusi frekuensi univariat dilakukan untuk membedah sebaran proporsi kemunculan masing-masing nilai variabel secara tunggal pada 3.113 transaksi. Tahapan ini sangat esensial untuk memetakan konsentrasi pangsa pasar (*market share*), mendeteksi potensi ketimpangan sebaran data (*data skewness*), serta memberikan landasan teoretis bagi penetapan nilai ambang batas dukungan minimum (*minimum support threshold*) pada tahap pemodelan algoritma FP-Growth (Sharda et al., 2020; Tan et al., 2018).

#### 1. Distribusi Frekuensi Model Sepeda Motor (`NAMA_BRG`)
Dari total populasi 3.113 transaksi penjualan, teridentifikasi sebanyak **44 model sepeda motor unik** yang dipasarkan oleh dealer. Sebaran penjualan memperlihatkan bahwa preferensi pasar sangat terkonsentrasi pada lini skuter matik, terutama pada kategori *Maxi Series* dan *Matic 125 cc Standard*. Tabel 4.2 menyajikan sebaran frekuensi dan persentase untuk 10 model sepeda motor dengan volume penjualan tertinggi di PT. SSM Motor.

<br>

**Tabel 4.2 Distribusi Frekuensi 10 Model Sepeda Motor Terlaris pada PT. SSM Motor**

| Peringkat | Model Sepeda Motor (`NAMA_BRG`) | Frekuensi (Faktur) | Persentase Populasi (%) | Kategori Segmen Pasar |
| :-: | :--- | :-: | :-: | :--- |
| 1 | AEROX ALPHA | 468 | 15,03% | *Maxi Series* (*Sporty Matic*) |
| 2 | MIO M3 CW | 434 | 13,94% | *Standard Matic 125 cc* (*Entry Level*) |
| 3 | GEAR 125 | 325 | 10,44% | *Standard Matic 125 cc* (*Utility Matic*) |
| 4 | NMAX NEO S | 252 | 8,10% | *Maxi Series* (*Comfort Matic*) |
| 5 | GRAND FILANO HYBRID NEO | 211 | 6,78% | *Classy Yamaha* (*Retro Hybrid*) |
| 6 | MX KING 150 | 185 | 5,94% | *Moped Sport 150 cc* (*Underbone*) |
| 7 | FAZZIO HYBRID NEO | 142 | 4,56% | *Classy Yamaha* (*Youth Hybrid*) |
| 8 | FAZZIO HYBRID | 117 | 3,76% | *Classy Yamaha* (*Standard Hybrid*) |
| 9 | G ULTIMA HYBRID | 110 | 3,53% | *Classy Yamaha* (*Premium Hybrid*) |
| 10 | G ULTIMA HYBRID SMART | 96 | 3,08% | *Classy Yamaha* (*Smart Key Hybrid*) |
| - | 34 Model Lainnya (Agregat) | 773 | 24,83% | *Sport*, *Moped*, & *Maxi Series* Lain |
| **Total** | **44 Model Motor Unik** | **3.113** | **100,00%** | **Populasi Transaksi Bersih** |

*Sumber: Pengolahan Data Transaksi Y-DMS PT. SSM Motor (2026)*

<br>

Tabel 4.2 memperlihatkan fenomena bisnis yang krusial: sepuluh model terlaris menguasai **75,17% (2.340 unit)** dari keseluruhan perputaran transaksi dealer. Model **AEROX ALPHA** menempati posisi teratas dengan 468 transaksi (15,03%), disusul oleh **MIO M3 CW** dengan 434 transaksi (13,94%), dan **GEAR 125** sebanyak 325 transaksi (10,44%). Tingginya permintaan Aerox Alpha mengindikasikan kuatnya penetrasi pasar pada kelompok konsumen usia muda dan pekerja urban komuter yang mendambakan performa mesin 155 cc dengan desain agresif. 

Di sisi lain, bertahannya Mio M3 CW dan Gear 125 pada tiga besar membuktikan bahwa segmen matik *entry-level* dengan efisiensi bahan bakar tinggi dan keterjangkauan harga tetap menjadi tulang punggung volume (*volume driver*) dealer. Selain itu, penetrasi segmen *Classy Hybrid* (Grand Filano dan Fazzio) yang secara kumulatif menyumbang 18,68% transaksi mengindikasikan adanya pergeseran minat konsumen komuter perkotaan menuju teknologi mesin ramah lingkungan (*Blue Core Hybrid*) dengan estetika gaya klasik modern. Sebagaimana dicatat oleh Salu et al. (2022), dominasi lini matik pada jaringan penjualan Yamaha menuntut pengelolaan persediaan yang responsif agar varian cepat laku tidak mengalami kekosongan stok (*stockout*).

---

#### 2. Distribusi Frekuensi Varian Warna Unit (`WARNA`)
Dealer PT. SSM Motor mencatat sebanyak **22 varian warna estetika**. Preferensi warna kendaraan merefleksikan selera visual konsumen yang berpengaruh langsung terhadap perputaran stok di gudang (*inventory turnover*). Tabel 4.3 memaparkan distribusi frekuensi 10 varian warna unit terpopuler.

<br>

**Tabel 4.3 Distribusi Frekuensi 10 Varian Warna Unit Terpopuler pada PT. SSM Motor**

| No | Varian Warna Unit (`WARNA`) | Frekuensi (Unit) | Persentase (%) | Karakteristik Estetika Pasar |
| :-: | :--- | :-: | :-: | :--- |
| 1 | HITAM | 1.317 | 42,31% | Netral / Maskulin (*Matte & Glossy Black*) |
| 2 | BIRU | 349 | 11,21% | Warna Ikonik Yamaha (*Racing Blue / Cyan*) |
| 3 | MERAH | 203 | 6,52% | Berani / Elegan (*Metallic & Matte Red*) |
| 4 | PUTIH | 201 | 6,46% | Netral Bersih (*Pearl White*) |
| 5 | ABU-ABU | 171 | 5,49% | Modern Kontemporer (*Elixir & Matte Grey*) |
| 6 | UNGU MUDA | 138 | 4,43% | Trendi / Pastel (*Mauve / Lilac Fazzio Series*) |
| 7 | PERAK HIJAU | 109 | 3,50% | *Dual-Tone* Estetik (*Greenish Silver*) |
| 8 | PERAK | 108 | 3,47% | Futuristik (*Prestige Silver*) |
| 9 | HIJAU | 92 | 2,96% | Natural / Vintage (*Tuscan Green*) |
| 10 | HIJAU PERAK | 73 | 2,35% | Kombinasi Khusus *Sport/Classy* |
| - | 12 Varian Warna Lainnya | 352 | 11,31% | Cyan, Kuning, Emas, Jingga, Dll. |
| **Total** | **22 Varian Warna** | **3.113** | **100,00%** | **Total Transaksi** |

*Sumber: Pengolahan Data Transaksi Y-DMS PT. SSM Motor (2026)*

<br>

Data pada Tabel 4.3 menunjukkan dominasi mutlak warna **HITAM** yang menyerap **42,31% (1.317 unit)** dari total transaksi. Warna hitam dipilih secara luas lintas model—mulai dari skutik *entry-level* hingga *Maxi Series*—karena dianggap berkarakter netral, memiliki nilai depresiasi harga jual kembali yang relatif stabil, serta lebih mudah dalam perawatan visual. Varian **BIRU** menempati posisi kedua sebesar 11,21% sebagai warna identitas balap resmi (*racing identity*) Yamaha. 

Varian warna pastel dan *dual-tone* seperti Ungu Muda (4,43%) dan Perak Hijau (3,50%) terkonsentrasi kuat pada lini skutik *Classy Yamaha* (Fazzio dan Grand Filano), mencerminkan segmentasi pasar khusus wanita dan generasi muda perkotaan yang memprioritaskan ekspresi gaya personal.

---

#### 3. Distribusi Frekuensi Lembaga Pembiayaan / Skema Pembayaran (`NMLEASE`)
Skema transaksi pembelian unit di dealer PT. SSM Motor terbagi menjadi dua skema utama, yaitu transaksi tunai (*cash*) dan transaksi kredit melalui lembaga pembiayaan non-bank (*multifinance/leasing*). Sebanyak 40 kode pembiayaan *leasing* terdaftar dalam sistem Y-DMS yang kemudian dikelompokkan ke dalam korporasi pembiayaan induknya. Tabel 4.4 memaparkan proporsi pangsa pasar lembaga pembiayaan.

<br>

**Tabel 4.4 Distribusi Skema Pembayaran dan Lembaga Pembiayaan Konsumen**

| No | Lembaga Pembiayaan / Skema (`NMLEASE`) | Frekuensi (Faktur) | Persentase Total Transaksi (%) | Pangsa Pasar Kredit (%) |
| :-: | :--- | :-: | :-: | :-: |
| 1 | **CASH (Pembelian Tunai)** | **1.969** | **63,25%** | *-* |
| 2 | PT. Bussan Auto Finance (BAF) | 844 | 27,11% | 73,78% |
| 3 | PT. Adira Dinamika Multi Finance (Adira) | 269 | 8,64% | 23,51% |
| 4 | PT. OTO Multiartha (OTO) | 21 | 0,67% | 1,84% |
| 5 | PT. Mandiri Utama Finance (MUF) | 7 | 0,22% | 0,61% |
| 6 | PT. Wahana Ottomitra Multiartha (WOM) | 3 | 0,10% | 0,26% |
| **Subtotal** | **Skema Kredit (*Multifinance*)** | **1.144** | **36,75%** | **100,00%** |
| **Total** | **Populasi Transaksi** | **3.113** | **100,00%** | *-* |

*Sumber: Pengolahan Data Transaksi Y-DMS PT. SSM Motor (2026)*

<br>

Berdasarkan Tabel 4.4, transaksi pembelian secara **Tunai (*CASH*)** mencatatkan proporsi mayoritas sebesar **63,25% (1.969 unit)**, sementara skema **Kredit** mencakup **36,75% (1.144 unit)**. Dominasi skema tunai pada dealer PT. SSM Motor dipengaruhi oleh tingginya volume pasokan unit grosir dan korporasi dari fasilitas Gudang SSM Bekasi kepada jaringan sub-dealer maupun pembeli perorangan dengan daya beli memadai. 

Pada segmen pembiayaan kredit (1.144 transaksi), **PT. Bussan Auto Finance (BAF)** menguasai pangsa pasar secara masif sebesar **73,78% (844 transaksi)**, disusul oleh **Adira Finance** sebesar **23,51% (269 transaksi)**. Dominasi BAF yang begitu mutlak terjadi karena BAF merupakan mitra pembiayaan resmi eksklusif (*captive finance company*) bagi pabrikan Yamaha, sehingga menawarkan program promosi terintegrasi, proses persetujuan berkas yang lebih cepat, serta batas uang muka (*down payment*) yang sangat kompetitif di tingkat dealer. Integrasi atribut fasilitas pembiayaan ini sejalan dengan kerangka analitik keputusan terpadu yang digariskan oleh Sharda et al. (2020) dan Widodo et al. (2022).

---

#### 4. Distribusi Frekuensi Tenor Angsuran Pembiayaan (`JK_WAKTU`)
Tenor angsuran merefleksikan komitmen durasi cicilan bulanan yang diambil oleh konsumen pembiayaan kredit. Jangka waktu kredit dicatat dalam satuan bulan, di mana nilai 0 merepresentasikan transaksi non-kredit (tunai). Tabel 4.5 menyajikan rekapitulasi distribusi jangka waktu pembiayaan pada PT. SSM Motor.

<br>

**Tabel 4.5 Distribusi Frekuensi Jangka Waktu (Tenor) Angsuran Konsumen**

| No | Kelompok Jangka Waktu (`JK_WAKTU`) | Frekuensi (Faktur) | Persentase Total Populasi (%) | Proporsi Transaksi Kredit (%) |
| :-: | :--- | :-: | :-: | :-: |
| 1 | 0 Bulan (Pembelian Tunai / *Cash*) | 1.969 | 63,25% | - |
| 2 | Tenor 30–32 Bulan (Jangka Panjang) | 627 | 20,14% | 54,81% |
| 3 | Tenor 35 Bulan (Jangka Maksimal) | 324 | 10,41% | 28,32% |
| 4 | Tenor 20–23 Bulan (Jangka Menengah) | 123 | 3,95% | 10,75% |
| 5 | Tenor 11–17 Bulan (Jangka Pendek) | 70 | 2,25% | 6,12% |
| **Total** | **Populasi Transaksi** | **3.113** | **100,00%** | **100,00%** |

*Sumber: Pengolahan Data Transaksi Y-DMS PT. SSM Motor (2026)*

<br>

Sebagaimana dipaparkan pada Tabel 4.5, di antara konsumen yang memilih opsi pembiayaan kredit (1.144 konsumen), mayoritas mutlak mengonsentrasikan pilihan pada tenor jangka panjang. Kelompok tenor **30–32 bulan** menduduki urutan pertama dengan 627 transaksi (**54,81%** dari total kredit), diikuti tenor **35 bulan** sebanyak 324 transaksi (**28,32%** dari total kredit). Secara kumulatif, sebanyak **83,13% debitur dealer memilih tenor angsuran 30 hingga 35 bulan**. 

Kecenderungan ini mengindikasikan bahwa konsumen otomotif roda dua sangat sensitif terhadap besaran nominal angsuran per bulan (*monthly installment affordability*). Konsumen bersedia menanggung beban akumulasi margin pembiayaan yang lebih panjang demi memperoleh cicilan bulanan yang paling terjangkau bagi arus kas rumah tangga mereka.

---

#### 5. Distribusi Frekuensi Wilayah Domisili Konsumen (`KOTA`)
Dealer PT. SSM Motor memiliki jangkauan distribusi yang melayani konsumen di seluruh wilayah aglomerasi megapolitan Jabodetabek. Analisis geografis terhadap alamat domisili pemohon faktur pada Tabel 4.6 memetakan kantong-kantong konsentrasi pasar utama dealer.

<br>

**Tabel 4.6 Distribusi Frekuensi Wilayah Domisili Konsumen pada PT. SSM Motor**

| No | Wilayah Administratif Konsumen (`KOTA`) | Frekuensi (Faktur) | Persentase Populasi (%) | Klaster Wilayah Aglomerasi |
| :-: | :--- | :-: | :-: | :--- |
| 1 | JAKARTA SELATAN | 546 | 17,54% | DKI Jakarta Raya |
| 2 | KOTA BEKASI | 493 | 15,84% | Bekasi Raya (Pusat Dealer) |
| 3 | JAKARTA PUSAT | 420 | 13,49% | DKI Jakarta Raya |
| 4 | JAKARTA BARAT | 373 | 11,98% | DKI Jakarta Raya |
| 5 | JAKARTA TIMUR | 345 | 11,08% | DKI Jakarta Raya |
| 6 | KABUPATEN BEKASI | 322 | 10,34% | Bekasi Raya (Pusat Dealer) |
| 7 | DKI JAKARTA LAINNYA | 220 | 7,07% | DKI Jakarta Raya |
| 8 | TANGERANG (Kota/Kab/Tangsel) | 193 | 6,20% | Banten / Bodetabek |
| 9 | JAKARTA UTARA | 108 | 3,47% | DKI Jakarta Raya |
| 10 | BOGOR (Kota & Kabupaten) | 33 | 1,06% | Jawa Barat / Bodetabek |
| 11 | KOTA DEPOK | 28 | 0,90% | Jawa Barat / Bodetabek |
| 12 | WILAYAH LAIN / LUAR JABODETABEK | 32 | 1,03% | Domisili Khusus |
| **Total** | **12 Klaster Wilayah Administratif** | **3.113** | **100,00%** | **Total Transaksi Bersih** |

*Sumber: Pengolahan Data Transaksi Y-DMS PT. SSM Motor (2026)*

<br>

Berdasarkan Tabel 4.6, wilayah pembeli terbagi ke dalam dua kutub episentrum utama: **Kawasan DKI Jakarta Raya** yang secara kumulatif mencakup **64,63% (2.012 transaksi)**, dan **Kawasan Bekasi Raya (Kota & Kabupaten Bekasi)** yang menyerap **26,18% (815 transaksi)**. Wilayah Jakarta Selatan menempati peringkat pertama tunggal dengan 546 transaksi (17,54%), disusul oleh Kota Bekasi dengan 493 transaksi (15,84%) dan Jakarta Pusat sebanyak 420 transaksi (13,49%). 

Besarnya porsi konsumen dari wilayah DKI Jakarta yang membeli unit di PT. SSM Motor (yang berpusat di Bekasi) menunjukkan daya tarik kompetitif dealer dalam hal ketersediaan alokasi unit (*stock readiness*), varian warna yang lengkap, serta kecepatan pengurusan dokumen faktur dan STNK dibanding dealer ritel lokal lainnya.

---

### 4.1.3 Visualisasi Statistik Deskriptif

Untuk memberikan pemahaman visual yang menyeluruh dan intuitif mengenai sebaran statistik univariat yang telah dianalisis, Gambar 4.1 menampilkan grafik visualisasi komposit empat dimensi keputusan pembelian konsumen di PT. SSM Motor.

<br>

![Gambar 4.1 Visualisasi Statistik Deskriptif Distribusi Univariat Transaksi PT. SSM Motor](assets/img/visualisasi_4_1_univariat.png)

*Gambar 4.1 Visualisasi Statistik Deskriptif Distribusi Univariat Transaksi Penjualan PT. SSM Motor: (a) Grafik Batang 10 Model Terlaris, (b) Grafik Batang 10 Varian Warna Dominan, (c) Diagram Lingkaran Pangsa Pasar Skema Pembayaran, dan (d) Diagram Batang Proporsi Durasi Tenor Kredit.*

<br>

Gambar 4.1 secara grafis mengonfirmasi keterpusatan pola belanja konsumen pada lini produk tertentu. Pada Gambar 4.1(a), tampak jurang volume yang nyata antara kelompok tiga besar (Aerox Alpha, Mio M3 CW, Gear 125) dengan model-model lainnya. Gambar 4.1(b) menonjolkan dominasi warna hitam yang melampaui 40% total unit. Gambar 4.1(c) memperlihatkan rasio 63:37 antara transaksi tunai dan pembiayaan kredit, di mana BAF menguasai hampir tiga perempat dari seluruh transaksi kredit. Terakhir, Gambar 4.1(d) menegaskan preferensi ekstrem konsumen kredit pada durasi cicilan 30–35 bulan.

Karakteristik sebaran univariat ini membuktikan bahwa meskipun pilihan model dan opsi transaksi sangat beragam, perilaku pembelian konsumen di lapangan memperlihatkan kecenderungan berkelompok (*clustering tendency*) pada atribut-atribut spesifik (Tan et al., 2018). Namun, analisis frekuensi satu dimensi ini belum mampu menjawab keterikatan implisit antar-variabel: *apakah pembeli model Aerox Alpha selalu memilih warna hitam? Apakah pembeli Fazzio Hybrid cenderung memilih leasing BAF dengan tenor panjang? Atau apakah konsumen tunai memiliki preferensi model yang berbeda dibanding konsumen kredit?* 

Sebagaimana ditegaskan oleh Han et al. (2022) dan Zaki & Meira (2020), keterikatan tersembunyi lintas-dimensi tersebut hanya dapat diungkap melalui komputasi *Frequent Pattern Mining*. Oleh karena itu, tahapan berikutnya memerlukan perancangan struktur pohon *FP-Tree* pada *Multi-Attribute Association Rule Mining* guna mengekstraksi kaidah implikasi secara efisien tanpa pembentukan kandidat kombinasi yang berlebihan.
