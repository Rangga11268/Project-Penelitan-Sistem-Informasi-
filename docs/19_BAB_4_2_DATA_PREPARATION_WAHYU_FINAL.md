# BAB IV: HASIL DAN PEMBAHASAN
*(Kerangka Kerja CRISP-DM — Multi-Attribute Association Rule Mining Algoritma FP-Growth pada PT. Sinar Surya Matahari)*

---

## 4.2 Hasil Pra-Pemrosesan dan Transformasi Data (*Data Preparation*)

Tahap penyiapan data (*data preparation*) merupakan fase rekayasa data mentah (*raw data*) menjadi bentuk representasi tabular dan biner terstruktur yang siap diproses secara komputasi oleh algoritma *Frequent Pattern Growth* (*FP-Growth*) (Sharda et al., 2020). Dalam siklus penambangan data (*data mining*), tahapan ini menyerap porsi terbesar dari keseluruhan upaya analitis karena kualitas keterikatan aturan asosiasi (*association rules*) yang dihasilkan sangat bergantung pada kebersihan, konsistensi, dan ketepatan pemodelan representasi data masukan (*input data*) (Han et al., 2022). 

Pada tahapan ini, data transaksi operasional *Yamaha Dealer Management System* (Y-DMS) PT. Sinar Surya Matahari (SSM Motor) sebanyak 3.113 rekaman transaksi faktur penjualan unit motor diproses melalui empat prosedur sistematis: pembersihan data (*data cleaning*) dan penegakan etika privasi data konsumen (*consumer data privacy*), standarisasi dan reduksi dimensi fitur (*feature reduction*), transformasi keranjang predikat multiatribut (*multi-attribute predicate basket*), serta pembentukan matriks insidensi biner (*binary incidence matrix*) melalui pengodean *one-hot encoding*.

---

### 4.2.1 Hasil Pembersihan (*Data Cleaning*) dan Anonimisasi Privasi Data

Prosedur pembersihan data (*data cleaning*) diawali dengan melakukan verifikasi integritas struktural terhadap basis data transaksi hasil ekstraksi Y-DMS. Penarikan sampel sensus menerapkan kriteria inklusi dan eksklusi yang ketat guna memastikan keabsahan data empiris (Sekaran & Bougie, 2016; Sugiyono, 2019). Tiga prosedur utama yang diterapkan meliputi:
1. **Verifikasi Keunikan Nomor Faktur:** Seluruh baris transaksi dipastikan memiliki identitas nomor faktur (`NO_FAKTUR`) yang unik dan valid. Tidak ditemukan adanya rekaman transaksi faktur ganda (*duplicate invoice records*) dalam pangkalan data.
2. **Penanganan Transaksi Batal dan Derau (*Noise*):** Sistem Y-DMS secara operasional dapat mencatat pengajuan yang kemudian dibatalkan oleh pihak pembeli (*canceled transactions*), penolakan pengajuan kredit oleh komite pembiayaan *leasing* (*rejected credit applications*), transaksi retur unit fisik, maupun layanan servis bengkel berkala dan pembelian suku cadang murni. Seluruh entitas non-penjualan unit fisik ini dieliminasi secara menyeluruh, sehingga data yang tersaring murni merepresentasikan transaksi unit motor baru yang sah (*closed & completed transactions*).
3. **Pemeriksaan Nilai Kosong (*Missing Values*):** Pemeriksaan integritas data terhadap atribut analisis inti membuktikan tidak adanya nilai kosong (*null/missing values*). Seluruh transaksi telah memuat kelengkapan data spesifikasi unit fisik, lembaga pembiayaan, durasi angsuran, dan alamat domisili.

Sebagai bentuk kepatuhan penuh terhadap etika penelitian sains data dan perlindungan privasi data konsumen (*consumer data privacy*), seluruh atribut identitas personal langsung dieliminasi secara permanen melalui teknik anonimisasi data (*data anonymization*). Atribut pengenal langsung seperti Nomor Induk Kependudukan (NIK), nama lengkap konsumen, nomor kontak telepon seluler, alamat jalan spesifik (RT/RW), nomor rangka kendaraan (*chassis number*), serta nomor mesin dihapus dari struktur data analisis. Rekapitulasi hasil prosedur pembersihan data disajikan pada Tabel 4.7.

<br>

**Tabel 4.7 Rekapitulasi Tahapan Pembersihan Data (*Data Cleaning*) dan Anonimisasi Privasi**

| Tahapan Prosedur Pembersihan | Parameter Operasional yang Diterapkan | Jumlah Rekaman Awal | Jumlah Rekaman Tereliminasi | Jumlah Bersih Akhir | Status Validasi |
| :--- | :--- | :-: | :-: | :-: | :---: |
| Filter Kategori Transaksi | Eliminasi servis berkala, retur unit, dan penjualan suku cadang bengkel. | Populasi Sistem | Variatif | 3.113 | Lolos Inklusi |
| Verifikasi Keabsahan Faktur | Pengecekan status faktur selesai (*closed*) dan eliminasi transaksi batal (*canceled/rejected*). | 3.113 | 0 | 3.113 | Lolos Inklusi |
| Penanganan Nilai Kosong (*Missing Values*) | Verifikasi kelengkapan nilai pada atribut Model, Warna, *Leasing*, Tenor, dan Kota. | 3.113 | 0 | 3.113 | Lengkap 100% |
| Anonimisasi Privasi Data (*Data Privacy*) | Penghapusan NIK, nama pembeli, nomor telepon, nomor rangka mesin (*chassis*), dan nomor mesin. | 12 Atribut Mentah | 7 Atribut Sensitif | 5 Atribut Inti | Teranonimisasi |
| **Total Populasi Bersih Masukan (*Input*)** | **Sensus Transaksi Penjualan Fisik Unit Motor Baru Y-DMS (Kuartal III 2026)** | **3.113** | **0** | **3.113** | **Siap Olah** |

*Sumber: Hasil Pengolahan Pra-Pemrosesan Data Y-DMS PT. SSM Motor (2026)*

---

### 4.2.2 Standarisasi dan Reduksi Fitur Keputusan Pembelian

Basis data mentah Y-DMS memuat 12 atribut operasional yang mencakup data administratif dan moneter kontinu (seperti `TG_FAKTUR`, `NO_PESAN`, `NILAI_UMK`, `NILAI_JUAL`, dan `UMUR`). Sebagaimana digariskan dalam kerangka analitik keputusan (Sharda et al., 2020), fitur administratif dan moneter kontinu direduksi karena tidak relevan secara langsung terhadap pembentukan keranjang predikat kategorikal diskret. 

Proses seleksi fitur menyisakan **5 dimensi keputusan pembelian inti** yang distandarisasikan format nilainya:
1. **Model Sepeda Motor (`NAMA_BRG`):** Format teks nama model motor diseragamkan ke huruf kapital baku (*uppercase standardization*), mencakup 44 model resmi Yamaha (misalnya `FAZZIO HYBRID`, `ALL NEW AEROX 155`, `NMAX NEO S`, `MIO M3 CW`, dan `GEAR 125`).
2. **Varian Warna Bodi (`WARNA`):** Penyeragaman nama varian estetika warna bodi kendaraan pabrikan ke bentuk baku sebanyak 22 varian warna (misalnya `HITAM`, `BIRU`, `ABU PINK`, `HIJAU MUDA`, dan `MERAH`).
3. **Lembaga Pembiayaan (`NMLEASE`):** Variasi penulisan 40 kantor cabang *leasing* rekanan pada pangkalan data dikelompokkan ke dalam korporasi pembiayaan induknya, yaitu `BAF` (PT. Bussan Auto Finance), `ADIRA` (PT. Adira Dinamika Multi Finance), `OTO` (PT. OTO Multiartha), `MANDIRI_UTAMA_FINANCE` (PT. Mandiri Utama Finance), `WOM` (PT. Wahana Ottomitra Multiartha), serta `CASH` untuk transaksi tunai tanpa fasilitas pembiayaan.
4. **Tenor Angsuran Kredit (`JK_WAKTU`):** Nilai jangka waktu cicilan numerik diklasifikasikan ke dalam 5 interval durasi logis bisnis: `0_BULAN_CASH` (transaksi non-kredit), `11-17_BULAN` (tenor pendek), `20-23_BULAN` (tenor menengah), `30-32_BULAN` (tenor panjang), dan `35_BULAN` (tenor maksimal).
5. **Wilayah Domisili Konsumen (`KOTA`):** Cakupan alamat domisili pemohon faktur distandarisasi ke dalam 12 entitas kota/kabupaten aglomerasi Jabodetabek (seperti `JAKARTA_TIMUR`, `JAKARTA_SELATAN`, `JAKARTA_PUSAT`, `JAKARTA_BARAT`, `JAKARTA_UTARA`, `KOTA_BEKASI`, `KABUPATEN_BEKASI`, `TANGERANG`, `BOGOR`, dan `KOTA_DEPOK`).

Tabel 4.8 menampilkan cuplikan lima rekaman transaksi pertama setelah tahapan standarisasi dan reduksi fitur (*clean features dataset*).

<br>

**Tabel 4.8 Cuplikan Sampel Data Transaksi Setelah Standarisasi dan Reduksi Fitur**

| No | Nomor Faktur (`NO_FAKTUR`) | Model Motor | Varian Warna | Lembaga Pembiayaan (*Leasing*) | Interval Tenor Kredit | Wilayah Domisili |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| 1 | `26FJK0101925` | FAZZIO HYBRID | ABU PINK | BAF | 30–32 Bulan | JAKARTA TIMUR |
| 2 | `26FJK0101926` | ALL NEW AEROX 155 | HITAM | BAF | 20–23 Bulan | JAKARTA TIMUR |
| 3 | `26FJK0101927` | FAZZIO HYBRID NEO | HIJAU MUDA | ADIRA | 20–23 Bulan | KOTA BEKASI |
| 4 | `26FJK0101928` | FREEGO 125 | MERAH | CASH | 0 Bulan (*Cash*) | JAKARTA SELATAN |
| 5 | `26FJK0101929` | FREEGO 125 | MERAH | BAF | 35 Bulan | JAKARTA UTARA |

*Sumber: Hasil Standarisasi Fitur Transaksi Y-DMS PT. SSM Motor (2026)*

---

### 4.2.3 Hasil Transformasi Keranjang Predikat Multiatribut (*Data Transformation*)

Karakteristik transaksi ritel sepeda motor bersifat faktur tunggal (*single-item retail*), di mana setiap transaksi hanya mencatat pembelian satu unit sepeda motor fisik (Salu et al., 2022). Karakteristik ini membuat data tidak dapat diproses secara langsung menggunakan algoritma penambangan keranjang belanja tradisional (*market basket analysis* biasa), karena tidak ada kombinasi produk fisik antarmotor yang dibeli bersamaan dalam satu struk faktur.

Guna mengatasi kendala struktural tersebut, penelitian ini menerapkan teknik **Transformasi Keranjang Predikat Multiatribut** (*Multi-Attribute Predicate Basket Transformation*) (Tan et al., 2018; Ubaidillah & Sumiati, 2025). Setiap rekaman faktur relasional dikonversi menjadi sebuah himpunan predikat berpasangan yang merefleksikan format relasional `{Atribut=Nilai}`. Melalui teknik ini, seluruh atribut keputusan pembelian diperlakukan sebagai item-item predikat unik (*predicate items*) yang berada di dalam satu keranjang transaksi konseptual yang sama (*conceptual transaction basket*).

Secara formal, setiap transaksi faktur ke-$i$ ($\text{TRX}_i$) ditransformasikan ke dalam bentuk himpunan predikat multiatribut sesuai Persamaan (4.1):

$$\text{TRX}_i = \Big\{ \text{Model} = m_i, \; \text{Warna} = w_i, \; \text{Leasing} = l_i, \; \text{Tenor} = t_i, \; \text{Wilayah} = k_i \Big\} \tag{4.1}$$

di mana $m_i$ merupakan nilai model sepeda motor, $w_i$ adalah varian warna, $l_i$ merepresentasikan lembaga pembiayaan (*leasing*), $t_i$ adalah durasi tenor angsuran, dan $k_i$ adalah wilayah domisili konsumen pada transaksi ke-$i$. Sebagai ilustrasi konkret, faktur pertama dengan nomor `26FJK0101925` ditransformasikan menjadi:

$$\text{TRX}_1 = \Big\{ \text{Model}=\text{FAZZIO HYBRID}, \; \text{Warna}=\text{ABU PINK}, \; \text{Leasing}=\text{BAF}, \; \text{Tenor}=\text{30–32 Bulan}, \; \text{Wilayah}=\text{JAKARTA TIMUR} \Big\}$$

Tabel 4.9 memaparkan cuplikan hasil transformasi lima transaksi pertama menjadi format daftar keranjang transaksi multiatribut (*basket transactions*).

<br>

**Tabel 4.9 Cuplikan Sampel Transformasi Data Menjadi Keranjang Transaksi Multiatribut**

| No | Nomor Faktur | Himpunan Item Predikat dalam Keranjang Transaksi (*Basket Items*) |
| :-: | :---: | :--- |
| 1 | `26FJK0101925` | `{'Model=FAZZIO HYBRID', 'Warna=ABU PINK', 'Leasing=BAF', 'Tenor=30-32 Bulan', 'Wilayah=JAKARTA TIMUR'}` |
| 2 | `26FJK0101926` | `{'Model=ALL NEW AEROX 155', 'Warna=HITAM', 'Leasing=BAF', 'Tenor=20-23 Bulan', 'Wilayah=JAKARTA TIMUR'}` |
| 3 | `26FJK0101927` | `{'Model=FAZZIO HYBRID NEO', 'Warna=HIJAU MUDA', 'Leasing=ADIRA', 'Tenor=20-23 Bulan', 'Wilayah=KOTA BEKASI'}` |
| 4 | `26FJK0101928` | `{'Model=FREEGO 125', 'Warna=MERAH', 'Leasing=CASH', 'Tenor=0 Bulan (Cash)', 'Wilayah=JAKARTA SELATAN'}` |
| 5 | `26FJK0101929` | `{'Model=FREEGO 125', 'Warna=MERAH', 'Leasing=BAF', 'Tenor=35 Bulan', 'Wilayah=JAKARTA UTARA'}` |

*Sumber: Hasil Transformasi Keranjang Multiatribut Y-DMS PT. SSM Motor (2026)*

<br>

Penerapan keranjang predikat multiatribut ini menjamin bahwa algoritma FP-Growth dapat mengekstraksi keterikatan asosiatif lintas-domain secara objektif—seperti mengungkap keterkaitan preferensi model motor tertentu dengan skema *leasing* dan durasi tenor kredit—tanpa menimbulkan bias ataupun menghasilkan kaidah semu (*spurious rules*) (Ubaidillah & Sumiati, 2025).

---

### 4.2.4 Pembentukan Matriks Insidensi Biner (*Binary Incidence Matrix*)

Langkah penutup pada tahap penyiapan data adalah mengonversi daftar keranjang transaksi (*basket transactions*) ke dalam struktur **Matriks Insidensi Biner** (*Binary Incidence Matrix*) melalui proses pengodean biner *one-hot encoding* (Han et al., 2022; Zaki & Meira, 2020). Algoritma FP-Growth membutuhkan representasi data berformat biner sebagai masukan (*input*) dasar untuk mengidentifikasi keberadaan (*presence*) atau ketiadaan (*absence*) suatu item dalam basis data transaksi.

Pada matriks biner ini, setiap baris mewakili satu transaksi penjualan tunggal ($N$), sedangkan setiap kolom mewakili satu predikat biner unik ($M$) dari keseluruhan kombinasi pasangan `Atribut=Nilai` yang hadir dalam populasi data. Secara matematis, elemen matriks biner $B_{ij}$ didefinisikan sebagai:

$$B_{ij} = \begin{cases} 1, & \text{jika predikat } j \text{ hadir dalam transaksi } i \; (\textit{presence}) \\ 0, & \text{jika predikat } j \text{ tidak hadir dalam transaksi } i \; (\textit{absence}) \end{cases}$$

Berdasarkan hasil komputasi pengodean biner terhadap 3.113 rekaman transaksi empiris PT. SSM Motor, diperoleh dimensi matriks biner akhir sebagai berikut:
* **Jumlah Baris Transaksi ($N$):** **3.113 baris transaksi faktur bersih**.
* **Jumlah Kolom Predikat ($M$):** **87 kolom predikat biner unik**, yang terdiri dari:
  * 44 predikat model motor (`Model=AEROX ALPHA`, `Model=MIO M3 CW`, `Model=GEAR 125`, dll.)
  * 22 predikat varian warna (`Warna=HITAM`, `Warna=BIRU`, `Warna=MERAH`, dll.)
  * 6 predikat lembaga pembiayaan (`Leasing=CASH`, `Leasing=BAF`, `Leasing=ADIRA`, dll.)
  * 5 predikat interval tenor kredit (`Tenor=0 Bulan (Cash)`, `Tenor=30-32 Bulan`, `Tenor=35 Bulan`, dll.)
  * 12 predikat wilayah domisili konsumen (`Wilayah=KOTA BEKASI`, `Wilayah=JAKARTA SELATAN`, dll.)

Tabel 4.10 menyajikan cuplikan struktur matriks insidensi biner berdimensi $3.113 \times 87$ yang dihasilkan dari tahap persiapan data (*data preparation*).

<br>

**Tabel 4.10 Cuplikan Matriks Insidensi Biner Transaksi Penjualan (*Binary Incidence Matrix* $3.113 \times 87$)**

| Nomor Faktur | Model=FAZZIO HYBRID | Model=ALL NEW AEROX 155 | Warna=HITAM | Warna=ABU PINK | Leasing=BAF | Leasing=CASH | Tenor=30–32 Bulan | Tenor=0 Bulan | Wilayah=JAKARTA TIMUR | ... | Wilayah=KOTA BEKASI |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `26FJK0101925` | **1** | 0 | 0 | **1** | **1** | 0 | **1** | 0 | **1** | ... | 0 |
| `26FJK0101926` | 0 | **1** | **1** | 0 | **1** | 0 | 0 | 0 | **1** | ... | 0 |
| `26FJK0101927` | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ... | **1** |
| `26FJK0101928` | 0 | 0 | 0 | 0 | 0 | **1** | 0 | **1** | 0 | ... | 0 |
| `26FJK0101929` | 0 | 0 | 0 | 0 | **1** | 0 | 0 | 0 | 0 | ... | 0 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| **Status Masukan (*Input*)** | **Kolom 1** | **Kolom 2** | **Kolom 3** | **Kolom 4** | **Kolom 5** | **Kolom 6** | **Kolom 7** | **Kolom 8** | **Kolom 9** | ... | **Kolom 87** |

*Sumber: Hasil Pengodean One-Hot Encoding Matriks Biner PT. SSM Motor (2026)*

<br>

Matriks insidensi biner berdimensi $3.113 \times 87$ ini merupakan representasi data terstandarisasi akhir yang langsung menjadi masukan (*input*) komputasi memori utama bagi algoritma FP-Growth pada tahap pemodelan (*modeling*) berikutnya, yaitu untuk pemindaian basis data pertama (*first-pass scan*) dalam pembentukan struktur urutan frekuensi *F-List* dan konstruksi pohon terkompresi *FP-Tree*.
