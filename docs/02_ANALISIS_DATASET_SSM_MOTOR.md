# DOKUMEN ANALISIS DATASET PENELITIAN
## DATA TRANSAKSI PENJUALAN SEPEDA MOTOR & SKEMA KREDIT SSM MOTOR (JUNI – AGUSTUS 2026)

---

## 📌 1. PROFIL DATASET

* **Nama Entitas Bisnis:** PT. SSM Motor (Dealer Resmi Sepeda Motor Yamaha).
* **Unit Operasional:** 
  * `GD.SSM BEKASI`: 2.787 transaksi ($89.5\%$)
  * `SSM MOTOR`: 326 transaksi ($10.5\%$)
* **Total Volume Transaksi:** **3.113 Baris Transaksi Riil**.
* **Rentang Waktu:** 1 Juni 2026 s/d 31 Agustus 2026 (3 Bulan Transaksi / Kuartal III 2026).
* **Lokasi File:** 
  * Excel Rapi: `datasets/01_DATASET_UTAMA_DIGUNAKAN/DATA_TRANSAKSI_SSM_MOTOR_JUN_AGST_2026_RAPI.xlsx`
  * CSV Bersih: `datasets/01_DATASET_UTAMA_DIGUNAKAN/data_transaksi_dealer_jun_agst_2026_clean.csv`

---

## 📊 2. DISTRIBUSI & STATISTIK DATA

### A. Sebaran Transaksi per Bulan
| Bulan | Jumlah Transaksi | Persentase |
| :--- | :---: | :---: |
| **Juni 2026** | 957 | $30.7\%$ |
| **Juli 2026** | 1.131 | $36.3\%$ |
| **Agustus 2026** | 1.025 | $32.9\%$ |
| **Total** | **3.113** | **$100\%$** |

---

### B. Top 10 Model Sepeda Motor Terlaris
| No | Model / Tipe Motor | Jumlah Terjual | Kategori Segmen |
| :-: | :--- | :---: | :--- |
| 1 | **AEROX ALPHA** | 468 | Maxi Sporty |
| 2 | **MIO M3 CW** | 434 | Matic Komuter Entry-Level |
| 3 | **GEAR 125** | 325 | Matic Multi-Guna |
| 4 | **NMAX NEO S** | 252 | Maxi Premium |
| 5 | **GRAND FILANO HYBRID NEO** | 211 | Classy Hybrid |
| 6 | **MX KING 150** | 185 | Moped Sport |
| 7 | **FAZZIO HYBRID NEO** | 142 | Classy Hybrid Youth |
| 8 | **FAZZIO HYBRID** | 117 | Classy Hybrid |
| 9 | **G ULTIMA HYBRID** | 110 | Maxi Hybrid |
| 10 | **G ULTIMA HYBRID SMART** | 96 | Maxi Hybrid Connected |

---

### C. Sebaran Metode Pembayaran & Lembaga Pembiayaan (Leasing)
| Skema Pembayaran / Leasing | Jumlah Transaksi | Keterangan |
| :--- | :---: | :--- |
| **CASH (Tunai)** | **1.969** | Pembayaran lunas langsung |
| **BAF (Bussan Auto Finance)** | **$\pm 750+$** | Leasing utama rekanan Yamaha (Cabang BHL, Jakarta 2, Cikarang, Cempaka Putih, Depok) |
| **ADIRA Finance** | **$\pm 200+$** | Leasing rekanan (Cabang Daan Mogot, Bekasi, Tambun, Kelapa Gading) |
| **OTO & Mandiri Utama Finance** | **$\pm 150+$** | Leasing pelengkap |

---

### D. Sebaran Jangka Waktu Cicilan (Tenor Kredit)
| Durasi Tenor | Jumlah Transaksi | Karakteristik Konsumen |
| :-: | :---: | :--- |
| **0 Bulan (CASH)** | 1.969 | Pembelian tunai |
| **30 Bulan** | 407 | Pilihan tenor favorit konsumen kredit |
| **35 Bulan** | 282 | Tenor cicilan terpanjang dengan angsuran terendah |
| **32 Bulan** | 150 | Tenor menengah-panjang |
| **20 – 23 Bulan** | 105 | Tenor menengah |
| **11 – 17 Bulan** | 88 | Tenor pendek dengan bunga terendah |

---

### E. Sebaran Wilayah Domisili Konsumen
| Wilayah Domisili | Jumlah Konsumen |
| :--- | :---: |
| **Jakarta Selatan** | 526 |
| **Bekasi (Kota & Kabupaten)** | 454 |
| **Jakarta Pusat** | 361 |
| **Jakarta Timur** | 309 |
| **Jakarta Barat** | 282 |

---

## 📖 3. KAMUS DATA (DATA DICTIONARY)

| Nama Kolom | Tipe Data | Deskripsi & Contoh |
| :--- | :--- | :--- |
| `No_Faktur` | Text / String | Nomor faktur penjualan resmi (Contoh: `26FJK0101925`). Berfungsi sebagai **Basket ID**. |
| `No_SPK_Pesanan` | Text / String | Nomor Surat Pesanan Kendaraan dari bagian sales. |
| `Tanggal_Faktur` | Date (DD/MM/YYYY) | Tanggal transaksi faktur disahkan. |
| `Bulan_Transaksi` | Text / String | Periode transaksi (`Juni 2026`, `Juli 2026`, `Agustus 2026`). |
| `Model_Sepeda_Motor` | Text / String | Nama tipe/model sepeda motor yang dibeli konsumen. |
| `Warna_Motor` | Text / String | Varian warna unit motor (Cybercity, Hitam, Putih, Merah, dsb.). |
| `Skema_Pembayaran_Leasing` | Text / String | Metode pembayaran yang dipilih (`CASH`, `BAF`, `ADIRA`, dll.). |
| `Tenor_Kredit_Bulan` | Integer | Jangka waktu angsuran dalam bulan (0 jika Cash). |
| `Uang_Muka_DP_Rp` | Integer (Currency) | Besaran nominal uang muka (DP) yang disetorkan pembeli. |
| `Harga_OTR_Rp` | Integer (Currency) | Harga jual On The Road (OTR) unit kendaraan. |
| `Wilayah_Domisili_Konsumen` | Text / String | Kota/Kabupaten domisili tempat tinggal pembeli pada KTP. |
| `Umur_Konsumen` | Integer | Usia pembeli saat transaksi dilakukan. |
| `Cabang_Dealer` | Text / String | Unit cabang yang melakukan transaksi (`GD.SSM BEKASI` / `SSM MOTOR`). |

---

## 💡 4. CONTOH HASIL ATURAN ASOSIASI (FP-GROWTH RULES)

Dari pengolahan data mentah menggunakan algoritma **FP-Growth**, dihasilkan aturan asosiasi valid:

1. **Aturan Tunai vs Motor Komuter:**
   $$\text{IF } [\text{Wilayah: Bekasi}, \text{Pembayaran: CASH}] \rightarrow \text{THEN } [\text{Motor: MIO M3 CW}] \quad (\text{Confidence: } 66.2\%, \text{Lift: } 4.75)$$
2. **Aturan Wilayah Urban vs Maxi Sport:**
   $$\text{IF } [\text{Wilayah: Jakarta Selatan}, \text{Pembayaran: CASH}] \rightarrow \text{THEN } [\text{Motor: AEROX ALPHA}] \quad (\text{Confidence: } 50.7\%, \text{Lift: } 3.37)$$
3. **Aturan Moped Sport:**
   $$\text{IF } [\text{Motor: MX KING 150}] \rightarrow \text{THEN } [\text{Pembayaran: CASH}] \quad (\text{Confidence: } 100\%, \text{Lift: } 1.58)$$
