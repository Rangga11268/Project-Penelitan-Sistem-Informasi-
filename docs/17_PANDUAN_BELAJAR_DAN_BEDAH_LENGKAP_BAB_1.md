# PANDUAN BELAJAR & BEDAH LENGKAP PROPOSAL BAB 1 (MASTER STUDY GUIDE)
**Mata Kuliah:** Penelitian Sistem Informasi (Semester 5 UBSI)  
**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Tim Peneliti (Kelompok 1):** Darell Rangga Putra R. (19241009), Megi Refkiansyah (19240488), Wahyu Rizky (19240493)  
**Objek Riset:** PT. Sinar Surya Matahari (Dealer Resmi Sepeda Motor Yamaha, 3.113 Data Faktur Riil)  

---

## 🎯 PETA JALUR BELAJAR (UNTUK KITA ANGGOTA KELOMPOK)

Buku panduan ini ditulis khusus dengan **bahasa manusia yang super detail, gamblang, runtut, dan kaya analogi** agar kita bertiga (Darell, Megi, Wahyu) paham 100% luar dalam mengenai:
1. Apa arti setiap kalimat di judul penelitian kita.
2. Apa sebenarnya yang kita kerjakan dan buat apa hasil riset ini bagi bisnis dealer.
3. Apa itu Multi-Atribut dan kenapa di dealer motor wajib pakai Multi-Atribut.
4. **Bedah Sangat Mendalam Setiap Sub-Bab (1.1 s.d. 1.6)**: Apa artinya, apa rincian detail isi di dalamnya, kenapa ditulis begitu, analoginya apa, dan bagaimana cara menjelaskannya ke Bu Syifa.
5. Bedah 3 Celah Riset (Gap) vs 3 Kebaruan (Novelty).
6. Tabel Simetris 1:1 Rumusan Masalah vs Tujuan Penelitian.
7. Skrip jawaban 5 pertanyaan maut dosen dan pembagian tugas tim.

---

# MODUL 1: BEDAH JUDUL KATA PER KATA (DENGAN ANALOGI SANTAI)

**Judul Lengkap Penelitian Kita:**  
> *"Multi-Attribute Association Rule Mining Menggunakan Algoritma FP-Growth: Analisis Pola Pembelian dan Preferensi Pembiayaan Konsumen Sepeda Motor (Studi Kasus: PT. Sinar Surya Matahari)"*

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               BEDAH ANATOMI JUDUL PENELITIAN KELOMPOK 1                                │
├──────────────────────────┬─────────────────────────────────────────────────────────────────────────────┤
│ 1. Multi-Attribute       │ Menggabungkan 5 kolom data berbeda (Model, Warna, Leasing,                  │
│                          │ Tenor, Wilayah) secara simultan dalam satu kali proses penambangan pola.    │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 2. Association Rule      │ Teknik data mining untuk mencari pola aturan sebab-akibat kebiasaan:        │
│    Mining (ARM)          │ "JIKA konsumen beli motor X warna Y, MAKA mereka cenderung pilih leasing Z".│
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 3. Algoritma FP-Growth   │ Metode cerdas berbasis pohon (FP-Tree) yang memadatkan ribuan data transaksi│
│                          │ hanya dengan 2 kali scan database tanpa membuat jutaan calon kombinasi lag. │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 4. Preferensi Pembiayaan │ Kebiasaan konsumen dalam memilih cara pembayaran (CASH tunai atau Kredit via│
│                          │ BAF, Adira, OTO) dan durasi mencicil (11, 23, 30, hingga 35 bulan).         │
├──────────────────────────┼─────────────────────────────────────────────────────────────────────────────┤
│ 5. PT. Sinar Surya       │ Tempat riset empiris nyata: Dealer Resmi Yamaha 3S di Jabodetabek dengan    │
│    Matahari (SSM Motor)  │ 3.113 data faktur transaksi riil periode aktif Juni–Agustus 2026.           │
└──────────────────────────┴─────────────────────────────────────────────────────────────────────────────┘
```

* **Analogi Beli Baju Pengantin untuk Multi-Attribute:**  
  Saat menyewa baju pengantin, kita tidak cuma memilih ukuran baju (M atau L). Kita wajib mencocokkan warna kebaya, bahan kain, tanggal sewa, dan budget rias pengantin secara bersamaan! Multi-atribut pada motor persis seperti itu: Tipe Motor + Warna + Leasing + Tenor + Wilayah.
* **Analogi Warung Bakso untuk Association Rules:**  
  JIKA orang memesan *Bakso Urat Pedas* MAKA 90% kemungkinan besar pasti memesan *Es Teh Manis*.
* **Analogi Lemari Baju untuk FP-Growth:**  
  Apriori itu seperti orang malas yang membongkar seluruh isi lemari berkali-kali untuk mencari pasangan baju dan celana. FP-Growth itu seperti orang rapi yang langsung menggantung baju per kategori di lemari (*FP-Tree*), sehingga mencari pasangan pakaian cuma butuh 2 kali lirik!

---

# MODUL 2: APA ITU "MULTI-ATRIBUT" & KENAPA WAJIB DI DEALER MOTOR?

### 1. Apa Sebenarnya "Atribut" Itu?
Dalam tabel database nota transaksi, **Atribut** adalah **nama kolom / karakteristik data** yang dicatat.  
Pada data faktur dealer PT. SSM Motor, terdapat 5 Atribut Kunci:
1. **Atribut 1 (Model Sepeda Motor):** Aerox 155, NMAX 155, Fazzio, Grand Filano, Mio M3, Gear 125, R15 Connected.
2. **Atribut 2 (Varian Warna Unit):** Matte Black, Cyan, Metallic Red, Prestige Silver, White, Dull Blue.
3. **Atribut 3 (Lembaga Pembiayaan / Cara Bayar):** Tunai (*CASH*) atau Kredit Multifinance (*BAF, Adira Finance, OTO Multiartha*).
4. **Atribut 4 (Durasi Tenor Angsuran):** 11 Bulan, 23 Bulan, 30 Bulan, 35 Bulan (atau *Non-Tenor* jika CASH).
5. **Atribut 5 (Wilayah Domisili Konsumen):** Jakarta Timur, Jakarta Selatan, Jakarta Utara, Kota Bekasi, Kab. Bekasi, Depok, Tangerang, Bogor.

### 2. Apa Itu "Multi-Atribut"?
**Multi-Atribut** artinya kita menambang pola hubungan yang **menggabungkan 5 kolom informasi berbeda di atas secara bersamaan dalam satu transaksi**, bukan cuma melihat satu kolom nama barang saja.

### 3. Kenapa Beli Motor WAJIB Pakai Multi-Atribut? (Kenapa Beda dari Minimarket?)
* **Di Minimarket (Single-Atribut Klasik):**  
  Satu struk belanjaan isinya **BANYAK barang fisik sekaligus** `{Roti Tawar, Selai Cokelat, Susu UHT, Kopi}`. Polanya mencari keterkaitan antar-barang (*Jika beli Roti $\rightarrow$ Beli Selai*).
* **Di Dealer Sepeda Motor (Multi-Atribut):**  
  **Satu faktur penjualan fisiknya HANYA MEMUAT 1 UNIT MOTOR!**  
  Tidak ada konsumen perorangan yang membeli `{NMAX + Aerox + Mio}` sekaligus dalam satu nota transaksi harian.  
  * ❌ *Masalah Fatal:* Jika kita memaksakan cara minimarket biasa, algoritma FP-Growth akan **mati / nol hasil (0 rules)** karena tidak ada kombinasi produk fisik.  
  * ✅ *Solusi Cerdas Multi-Atribut Kita:* Kita mentransformasikan 1 baris faktur motor menjadi **1 keranjang predikat berisi 5 atribut keputusan lengkap**:  
    $$\mathbf{Keranjang} = \{\text{Model Motor, Varian Warna, Lembaga Leasing, Tenor Angsuran, Wilayah Domisili}\}$$

### 4. Analogi Santai: "Paket Nasi Padang Komplit"
> *"Di rumah makan Padang, orang tidak cuma beli 'Nasi' doang.  
> Anda memesan satu paket keputusan utuh:  
> `[Lauk: Rendang] + [Sayur: Nangka] + [Sambal: Ijo] + [Bayar: QRIS] + [Makan: Bungkus]`.*  
>  
> *Nah, multi-atribut di dealer motor persis seperti itu!  
> Pembeli motor tidak cuma beli motor doang, tapi satu paket keputusan:  
> `[Model: Aerox] + [Warna: Cyan] + [Leasing: BAF] + [Tenor: 35 Bln] + [Wilayah: Bekasi]`!"*

---

# 📖 MODUL 3: BEDAH MENDALAM SETIAP SUB-BAB (1.1 SAMPAI 1.6) — RINCIAN DETAIL & BAHAS APA

Berikut adalah bedah tuntas yang sangat detail mengenai **apa arti sub-bab itu, kenapa wajib ada di karya ilmiah, apa saja yang dibahas secara gamblang di dalamnya, dan bagaimana cara kita memahaminya**:

---

## 📌 1.1 LATAR BELAKANG (BACKGROUND)

### A. Apa Artinya Sub-Bab Ini & Kenapa Wajib Ada?
Latar Belakang adalah pondasi utama proposal. Tujuannya adalah membuktikan kepada dosen bahwa **kita meneliti masalah nyata di industri, ada data riil yang bisa diolah, dan ada urgensi bisnis yang mendesak untuk diselesaikan dengan metode Sistem Informasi (Data Mining)**.

### B. Rincian Sangat Detail: Apa Saja yang Dibahas di Dalamnya?
Di naskah proposal BAB 1 kita, Sub-bab 1.1 mengalir dalam 5 alur cerita logis (*Piramida Terbalik / Funnel Structure*):
1. **Konteks Makro Industri Otomotif & Perilaku Kredit Nasional:**
   - Sepeda motor adalah moda transportasi primer masyarakat Indonesia.
   - Fakta penting industri: Lebih dari **75% transaksi pembelian sepeda motor di Indonesia dilakukan melalui skema kredit (mencicil)** lewat lembaga pembiayaan (*multifinance*), bukan tunai keras (*CASH*).
2. **Profil Objek Riset & Ketersediaan Dataset Empiris:**
   - Objek riset kita adalah **PT. Sinar Surya Matahari (SSM Motor)**, dealer resmi Yamaha (3S: *Sales, Service, Sparepart*) di wilayah Jabodetabek.
   - Perusahaan memiliki aset data masif berupa **3.113 catatan faktur transaksi penjualan riil** sepanjang triwulan operasional aktif (Juni s.d. Agustus 2026).
   - Data ini tersimpan rapi di sistem *Dealer Management System* (DMS), mencakup 5 informasi: tipe motor, varian warna, lembaga pembiayaan, tenor angsuran, dan lokasi pembeli.
3. **Tiga Masalah Bisnis Nyata di Lapangan (Kenapa Dealer Mengalami Kerugian?):**
   - **Masalah 1 — *Price Shock* dan Kehilangan Penjualan (*Lost Sales*):**  
     Pramuniaga (*sales counter*) sering kali tidak memiliki panduan data saat melayani calon pembeli. Misalnya ada anak muda datang tertarik membeli Yamaha Aerox 155, sales malah menyodorkan simulasi cicilan pendek (11 bulan) dengan angsuran Rp 2,5 juta/bulan. Konsumen kaget melihat cicilan terlalu mahal (*price shock*), merasa tidak sanggup, lalu mundur dan batal beli (*lost sales*), atau pindah ke dealer kompetitor. Padahal kalau sales langsung menyodorkan paket cicilan 35 bulan via BAF (Rp 1,1 juta/bulan), transaksi langsung *closing*!
   - **Masalah 2 — Ketidaksesuaian Pemilihan Lembaga Pembiayaan (*Leasing Mismatch*):**  
     Sales counter sering salah mengajukan berkas kredit konsumen ke lembaga leasing yang tidak cocok dengan profil motornya. Akibatnya proses verifikasi berbelit-belit, survei lama, dan berujung penolakan kredit (*credit rejection*).
   - **Masalah 3 — Ketidakseimbangan Distribusi Persediaan Gudang (*Inventory Imbalance*):**  
     Manajemen dealer sering salah membagi kuota pengiriman stok warna motor antargudang cabang. Contoh nyata: Varian warna *Cyan* dan *Matte Black* sangat laris di wilayah Kota Bekasi dan Kab. Bekasi, tetapi manajemen justru mengirim stok warna tersebut ke gudang Jakarta Selatan. Akibatnya di Jakarta motornya menumpuk mangkrak (*overstock* / biaya simpan membengkak), sementara di cabang Bekasi dealer kehabisan stok sehingga pembeli kecewa (*lost sales*).
4. **Kelemahan Operasional Saat Ini:**
   - Tumpukan 3.113 data faktur tersebut selama ini **hanya mengendap sebagai arsip nota transaksi mati** dan cuma digunakan untuk laporan pembukuan akuntansi bulanan biasa tanpa pernah diolah (*untapped data asset*).
5. **Solusi Ilmiah yang Diajukan:**
   - Menerapkan metode *Data Mining* khususnya teknik *Association Rule Mining* menggunakan algoritma **FP-Growth Multi-Atribut** untuk membongkar keterkaitan tersembunyi antara tipe motor, warna, leasing, tenor, dan wilayah menjadi wawasan bisnis cerdas.

* **Analogi Latar Belakang:**  
  *Seperti seorang dokter spesialis yang punya lemari arsip berisi 3.113 rekam medis pasien. Kalau rekam medis itu cuma ditumpuk, dokter tidak tahu pola penyakit pasiennya. Tapi kalau diolah dengan data mining, dokter langsung tahu: pasien dengan gejala pusing + meriang + batuk paling cepat sembuh kalau dikasih obat kombinasi A + B!*

---

## 📌 1.2 TINJAUAN PUSTAKA SINGKAT (LITERATURE REVIEW)

### A. Apa Artinya Sub-Bab Ini & Kenapa Wajib Ada?
Tinjauan Pustaka Singkat adalah bukti ilmiah bahwa **penelitian kita berakar dari buku teks babon internasional (*Gold Standard Textbooks*) dan didukung oleh telaah jurnal-jurnal ilmiah nasional terakreditasi SINTA dalam 5 tahun terakhir (2021–2026)**. Ini membuktikan kita paham konsep teori yang kita gunakan.

### B. Rincian Sangat Detail: Apa Saja yang Dibahas di Dalamnya?
Di naskah proposal, Sub-bab 1.2 dipecah menjadi 5 landasan teori yang sangat solid:
1. **1.2.1 Konsep Dasar Data Mining & Association Rule Mining (ARM):**
   - Data mining adalah tahapan inti dalam kerangka *Knowledge Discovery in Databases* (KDD) yang meliputi: Pembersihan Data (*Cleaning*) $\rightarrow$ Integrasi $\rightarrow$ Transformasi $\rightarrow$ *Data Mining* $\rightarrow$ Evaluasi Pola $\rightarrow$ Visualisasi Pengetahuan (Han, Pei, & Tong, 2022).
   - Aturan asosiasi dirumuskan dalam bentuk implikasi matematis:  
     $$X \Rightarrow Y$$  
     di mana $X$ adalah *Antecedent* (kondisi pemicu) dan $Y$ adalah *Consequent* (hasil keterikatan).
2. **1.2.2 Standar Evaluasi Tiga Metrik (Support, Confidence, dan Lift Ratio):**
   - **Support (Frekuensi):** Mengukur seberapa sering kombinasi atribut itu muncul bersama-sama dari seluruh 3.113 transaksi:  
     $$\text{Support}(X \Rightarrow Y) = \frac{\text{Jumlah Transaksi Mengandung } X \text{ dan } Y}{\text{Total Transaksi (3.113)}}$$
   - **Confidence (Kepastian / Kekuatan Aturan):** Mengukur seberapa yakin jika konsumen memilih atribut $X$, mereka pasti memilih atribut $Y$:  
     $$\text{Confidence}(X \Rightarrow Y) = \frac{\text{Support}(X \cup Y)}{\text{Support}(X)}$$
   - **Lift Ratio (Uji Korelasi Positif Murni / Kunci Mutlak):**  
     $$\text{Lift}(X \Rightarrow Y) = \frac{\text{Confidence}(X \Rightarrow Y)}{\text{Support}(Y)}$$  
     *Interpretasi Lift:*
     * $\text{Lift} > 1{,}0$: **Korelasi Positif Murni.** Menandakan pemilihan motor dan skema kredit tersebut memang saling mengikat kuat secara ilmiah.
     * $\text{Lift} = 1{,}0$: Independen (tidak ada hubungan apa-apa).
     * $\text{Lift} < 1{,}0$: Korelasi Negatif (saling tolak-menolak).
3. **1.2.3 Algoritma FP-Growth & Mekanisme Struktur Data FP-Tree:**
   - Dibandingkan algoritma Apriori yang lambat karena harus bolak-balik membaca database dan membangkitkan jutaan kombinasi kandidat (*candidate generation*), algoritma **FP-Growth** bekerja dengan cara memadatkan seluruh transaksi ke dalam memori komputer berupa struktur pohon berakar (*Frequent Pattern Tree / FP-Tree*).
   - FP-Growth hanya membutuhkan **2 kali pemindaian database (*2-pass scan*)**, lalu mengekstraksi kaidah asosiasi secara rekursif melalui *Conditional Pattern Base* (CPB), sehingga eksekusinya super cepat dan hemat memori (Zaki & Meira, 2020).
4. **1.2.4 Multi-Attribute Decision Support System (DSS) pada Barang Bernilai Tinggi:**
   - Sepeda motor adalah barang bernilai tinggi (*high-involvement durable goods*), sehingga keputusan pembelian konsumen selalu melibatkan pertimbangan harga dan angsuran bulanan.
   - Pola asosiasi multi-atribut yang dihasilkan tidak cuma dibiarkan jadi angka, melainkan diintegrasikan langsung menjadi Sistem Pendukung Keputusan (*Decision Support System*) untuk operasional dealer (Sharda, Delen, & Turban, 2020).
5. **1.2.5 Sintesis Penelitian Empiris Terdahulu (15 Jurnal SINTA 2021–2026):**
   - Kita menelaah 15 artikel jurnal SINTA terkini dan membuktikan bahwa:
     * Riset asosiasi terdahulu di dealer otomotif mayoritas cuma meneliti sparepart murah (Soleh et al., 2022; Anita & Wibowo, 2026; Ismarmiaty & Rismayati, 2023).
     * Riset kredit motor di perbankan cuma meneliti prediksi orang macet pakai C4.5 secara defensif (Widodo et al., 2022).
     * Belum pernah ada yang meneliti transaksi unit motor baru 5 dimensi multi-atribut.

---

## 📌 1.3 CELAH PENELITIAN (RESEARCH GAP) & RUMUSAN MASALAH

### A. Apa Artinya Sub-Bab Ini & Kenapa Wajib Ada?
Sub-bab ini adalah jantung metodologis proposal. Tujuannya adalah **menunjukkan kelemahan/kesenjangan pada penelitian-penelitian terdahulu (*Research Gap*)**, lalu merumuskan **4 pertanyaan kunci ilmiah (*Rumusan Masalah*)** yang akan dijawab tuntas oleh eksperimen kita.

### B. Rincian Sangat Detail: Apa Saja yang Dibahas di Dalamnya?

#### 1.3.1 Tiga Celah Riset Utama (Research Gap):
1. **Domain Gap (Kesenjangan Ranah Objek):**  
   Lebih dari 90% publikasi data mining di bidang otomotif hanya meneliti penjualan suku cadang murah bengkel (oli, busi, kampas rem seharga Rp 20.000 – Rp 50.000). Barang-barang ini bersifat murah dan dibeli secara spontan/rutin (*low-involvement goods*). Menemukan pola *"orang beli oli bareng kampas rem"* adalah hal biasa (*common sense*). Belum pernah ada riset SINTA yang meneliti transaksi penjualan **unit fisik sepeda motor baru bernilai puluhan juta rupiah (*high-involvement goods*)**.
2. **Product-Finance Integration Gap (Kesenjangan Finansial Produk):**  
   Di jurnal perbankan dan multifinance, variabel kredit selalu diteliti terpisah menggunakan algoritma klasifikasi (C4.5 atau Naive Bayes) untuk memprediksi orang gagal bayar (*credit scoring*). Pendekatan ini bersifat **defensif** (cuma nyaring boleh pinjam atau tidak) dan **buta jenis motor** (tidak peduli motor apa yang dibeli). Belum ada riset yang menyatukan karakteristik motor fisik dengan pilihan leasing dan tenor secara komersial-ofensif (jualan).
3. **Multi-Attribute Structure Gap (Kesenjangan Struktur Data):**  
   Riset asosiasi ritel di SINTA mayoritas hanya memakai data 1 dimensi (barang A $\rightarrow$ barang B). Pada dealer motor, 1 nota cuma beli 1 motor, sehingga metode 1 dimensi pasti gagal. Diperlukan struktur keranjang predikat 5 dimensi terindeks.

#### 1.3.2 Empat Butir Rumusan Masalah (Alur Eksperimen Sistematis):
1. **RM 1 (Transformasi Data):** Bagaimana mentransformasikan data faktur transaksi penjualan tunggal (*single-unit sales*) pada PT. Sinar Surya Matahari menjadi format keranjang transaksi multi-atribut (*multi-attribute predicate basket*) tanpa menimbulkan kaidah asosiasi semu (*spurious/trivial rules*)?
2. **RM 2 (Ekstraksi FP-Growth):** Bagaimana mengimplementasikan algoritma *Frequent Pattern Growth* (FP-Growth) untuk mengekstraksi kaidah asosiasi tersembunyi yang menghubungkan karakteristik model sepeda motor, varian warna, lembaga pembiayaan (*leasing*), tenor angsuran, dan wilayah domisili konsumen?
3. **RM 3 (Validasi Tri-Metrik):** Bagaimana menguji validitas dan signifikansi korelasi kaidah asosiasi yang terbentuk menggunakan standar evaluasi tiga metrik (*Support*, *Confidence*, dan *Lift Ratio* > 1,0)?
4. **RM 4 (Hilirisasi Bisnis Terapan):** Bagaimana merumuskan rekomendasi strategi bisnis preskriptif (*Smart Sales Script*, alokasi persediaan varian warna berbasis wilayah, dan program bundling promosi pembiayaan) berdasarkan kaidah asosiasi yang terbukti valid?

---

## 📌 1.4 KEBARUAN (NOVELTY) & SOLUSI YANG DITAWARKAN

### A. Apa Artinya Sub-Bab Ini & Kenapa Wajib Ada?
Sub-bab ini adalah etalase orisinalitas riset kita. Tujuannya adalah menjawab pertanyaan dosen: **"Apa kontribusi baru yang kelompok kalian berikan bagi ilmu Sistem Informasi dan bagi dunia usaha dealer motor?"**

### B. Rincian Sangat Detail: Apa Saja yang Dibahas di Dalamnya?

#### 1.4.1 Tiga Pilar Kebaruan Ilmiah (Scientific Novelty):
1. **Pilar 1 — Kebaruan Integrasi Domain (*Cross-Domain Product-Finance Bridge*):**  
   Menjadi penelitian pelopor di Indonesia yang menjembatani karakteristik fisik barang bernilai tinggi (Model Motor & Varian Warna) secara langsung dengan struktur pembiayaan komersial konsumen (Leasing CASH/BAF/Adira/OTO dan Tenor 11–35 bulan).
2. **Pilar 2 — Kebaruan Metodologis (*Multi-Attribute Predicate Basket Transformation*):**  
   Merancang teknik pra-pemrosesan data faktur tunggal menjadi format keranjang 5 atribut biner terindeks:
   $$T_k = \langle \text{Model}, \text{Warna}, \text{Leasing}, \text{Tenor}, \text{Domisili} \rangle$$
   Teknik ini memastikan pohon *FP-Tree* bekerja efisien tanpa lonjakan cabang berlebih (*combinatorial branching explosion*) dan otomatis memblokir aturan mustahil seperti `{Mio M3} -> {Yamaha NMAX}`.
3. **Pilar 3 — Kebaruan Preskriptif-Manajerial (*Actionable Business Intelligence*):**  
   Kaidah asosiasi yang dihasilkan tidak berhenti sebagai grafik di atas kertas, tetapi ditransformasikan langsung menjadi 3 produk manajerial terapan:
   - **Smart Sales Script:** Contekan bagi pramuniaga *counter* untuk langsung menyodorkan paket cicilan yang paling berpeluang disetujui leasing (*closing rate* tinggi).
   - **Optimasi Alokasi Stok Gudang:** Pedoman distribusi unit motor warna tertentu berdasarkan wilayah (Bekasi vs Jakarta) guna mencegah *lost sales* dan *overstock*.
   - **Joint Multifinance Bundling Program:** Dasar pengajuan subsidi DP bersama leasing mitra (BAF/Adira).

#### 1.4.2 Solusi yang Ditawarkan:
Menerapkan algoritma **FP-Growth** dengan panduan kerangka kerja standar industri **CRISP-DM** (6 fase: *Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment*) yang divalidasi secara ketat dengan kriteria mutlak **Lift Ratio > 1,0**.

---

## 📌 1.5 RUANG LINGKUP PENELITIAN (SCOPE & LIMITATIONS)

### A. Apa Artinya Sub-Bab Ini & Kenapa Wajib Ada?
Ruang Lingkup adalah **"Benteng Pertahanan Akademik"**. Tujuannya adalah mengunci batas penelitian agar dosen penguji tidak melenceng menanyakan hal-hal di luar batasan data yang kita miliki.

### B. Rincian Sangat Detail: 5 Pagar Batasan Penelitian:
1. **Pagar 1 — Batasan Objek Penelitian:** Dealer Resmi Sepeda Motor Yamaha PT. Sinar Surya Matahari (SSM Motor) dengan area pasar di Jabodetabek.
2. **Pagar 2 — Batasan Sumber & Volume Data:** Menggunakan **3.113 catatan faktur transaksi riil** penjualan unit baru (*single-unit sales*) yang ditarik dari database *Dealer Management System* (DMS) perusahaan.
3. **Pagar 3 — Batasan Periode Waktu:** Rekam jejak transaksi triwulan operasional aktif selama 3 bulan penuh, yaitu **Juni hingga Agustus 2026**.
4. **Pagar 4 — Batasan Variabel Analisis (5 Atribut Kunci):** Dibatasi hanya pada 5 variabel: (1) Model Motor, (2) Varian Warna, (3) Metode/Lembaga Pembiayaan, (4) Durasi Tenor Cicilan, dan (5) Wilayah Domisili Konsumen.
5. **Pagar 5 — Batasan Metode & Metrik:** Dibatasi menggunakan algoritma FP-Growth berbasis FP-Tree dengan kriteria kelulusan aturan wajib memiliki nilai **Lift Ratio > 1,0**.

* **Analogi Ruang Lingkup:**  
  *Seperti memasang pagar di sekeliling lapangan sepak bola. Wasit dan penonton tidak boleh minta kita main bola di luar garis lapangan yang sudah kita pasang!*

---

## 📌 1.6 TUJUAN PENELITIAN (RESEARCH OBJECTIVES)

### A. Apa Artinya Sub-Bab Ini & Kenapa Wajib Ada?
Tujuan Penelitian adalah **pernyataan sasaran operasional yang 100% Simetris (Isomorfis 1:1) menjawab 4 butir Rumusan Masalah di sub-bab 1.3**.

### B. Rincian Sangat Detail: 4 Sasaran Operasional Penelitian:
1. **Tujuan 1 (Menjawab RM 1):** Mengonstruksi skema transformasi data faktur transaksi penjualan tunggal (*single-unit sales*) PT. Sinar Surya Matahari ke dalam format representasi keranjang transaksi multi-atribut (*multi-attribute predicate basket*) terstruktur guna mengeliminasi potensi terbentuknya kaidah asosiasi semu (*spurious rules*).
2. **Tujuan 2 (Menjawab RM 2):** Mengimplementasikan algoritma *Frequent Pattern Growth* (FP-Growth) berbasis struktur *FP-Tree* untuk mengekstraksi *frequent itemsets* dan kaidah asosiasi yang memetakan keterkaitan tersembunyi antara karakteristik model sepeda motor, varian warna, lembaga pembiayaan (*leasing*), tenor angsuran, dan wilayah domisili konsumen dari 3.113 data transaksi empiris.
3. **Tujuan 3 (Menjawab RM 3):** Menguji validitas empiris dan kekuatan keterikatan kaidah asosiasi yang terbentuk menggunakan standar evaluasi tiga metrik (*Support*, *Confidence*, dan *Lift Ratio* > 1,0) guna memastikan signifikansi korelasi dependensi antaratribut.
4. **Tujuan 4 (Menjawab RM 4):** Merumuskan rekomendasi strategi bisnis preskriptif bagi manajemen PT. Sinar Surya Matahari berupa panduan pramuniaga cerdas (*Smart Sales Script*), optimasi alokasi persediaan varian warna berbasis wilayah cabang, serta formulasi paket *bundling* promosi pembiayaan bersama lembaga rekanan.

---

# MODUL 4: TABEL MATRIKS 3 GAP VS 3 NOVELTY KELOMPOK 1

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        MATRIKS KOMPARASI: RESEARCH GAP VS SCIENTIFIC NOVELTY                           │
├──────────────────────────┬──────────────────────────────────────────┬──────────────────────────────────┤
│ Dimensi Celah Riset      │ Kelemahan Fatal Riset Terdahulu (SINTA)  │ Kebaruan & Solusi Kelompok 1     │
├──────────────────────────┼──────────────────────────────────────────┼──────────────────────────────────┤
│ 1. Domain Gap            │ 90%+ riset SINTA cuma neliti sparepart   │ Meneliti transaksi UNIT MOTOR    │
│    (Kesenjangan Objek)   │ bengkel murah (busi/oli Rp 20.000).      │ BARU puluhan juta rupiah         │
│                          │ Barang low-involvement beli spontan.     │ (high-involvement durable goods).│
├──────────────────────────┼──────────────────────────────────────────┼──────────────────────────────────┤
│ 2. Product-Finance Gap   │ Riset multifinance/bank selalu pakai     │ Menghubungkan tipe motor fisik   │
│    (Kesenjangan Finansial│ C4.5 cuma untuk prediksi kredit macet.   │ langsung dengan leasing & tenor  │
│     Produk)              │ Bersifat defensif & buta tipe motor.     │ secara komersial-ofensif.        │
├──────────────────────────┼──────────────────────────────────────────┼──────────────────────────────────┤
│ 3. Multi-Attribute Gap   │ Riset minimarket cuma 1 dimensi produk   │ Merancang keranjang 5 atribut    │
│    (Kesenjangan Struktur │ (Barang A -> Barang B). Kalau dipakai    │ biner terindeks ke FP-Tree       │
│     Data)                │ di motor, FP-Growth mati (0 rules).      │ bebas aturan salah.              │
└──────────────────────────┴──────────────────────────────────────────┴──────────────────────────────────┘
```

---

# MODUL 5: SKRIP JAWABAN MENGHADAPI 5 PERTANYAAN MAUT BU SYIFA

#### ❓ Q1: "Kenapa kalian memilih FP-Growth, bukan Apriori atau C4.5 / Naive Bayes?"
> **Jawaban Mantap:** *"Izin Bu Syifa. Dibanding Apriori, FP-Growth jauh lebih efisien karena hanya 2 kali scan database dan memadatkan data ke struktur FP-Tree tanpa membuat jutaan kandidat kombinasi yang bikin komputer lag. Dibanding C4.5 yang cuma klasifikasi satu label kredit macet, FP-Growth bisa mencari pola hubungan multi-arah (tipe motor × warna × leasing × tenor) secara bersamaan."*

#### ❓ Q2: "Di mana letak NOVELTY (Kebaruan) riset kalian? Apa kalian bikin rumus baru?"
> **Jawaban Mantap:** *"Izin Bu, sesuai kaidah metodologi penelitian Sistem Informasi (Dr. Romi Satria Wahono), kebaruan penelitian S1 terletak pada representasi data, integrasi domain, dan kegunaan bisnis. Kebaruan kami ada 3: (1) Meneliti unit motor baru puluhan juta rupiah, bukan sparepart receh Rp 20.000; (2) Memadukan fisik motor langsung dengan preferensi leasing dan tenornya; (3) Format keranjang 5 dimensi yang hasilnya diwujudkan jadi Smart Sales Script terapan."*

#### ❓ Q3: "Apa maksud transformasi Multi-Attribute Predicate Basket pada Rumusan Masalah 1?"
> **Jawaban Mantap:** *"Izin Bu. Di dealer motor, 1 nota faktur hanya mencatat pembelian 1 unit motor. Kalau dimasukkan mentah ke FP-Growth, algoritmanya mati karena tidak ada pasangan barang. Jadi kami ubah 1 faktur menjadi 1 keranjang berisi 5 data lengkap: {Model, Warna, Leasing, Tenor, Wilayah}. Dengan cara ini, FP-Tree bisa menambang pola perilaku tanpa menghasilkan aturan aneh seperti {Mio} -> {NMAX}."*

#### ❓ Q4: "Kenapa harus pakai Lift Ratio > 1.0? Berapa batas Support dan Confidence-nya?"
> **Jawaban Mantap:** *"Izin Bu. Support hanya mengukur seberapa sering muncul (kami pasang 1%–3% agar motor premium seperti NMAX tidak hilang), dan Confidence hanya kepastian searah (kami pasang ≥50%). Kuncinya ada pada Lift Ratio > 1.0 yang membuktikan secara matematis bahwa hubungannya adalah korelasi positif nyata dan bukan kebetulan acak (aturan temuan kami memiliki Lift 1.58 hingga 4.76)."*

#### ❓ Q5: "Sebagai mahasiswa Sistem Informasi, apa manfaat nyata hasil riset ini bagi dealer?"
> **Jawaban Mantap:** *"Izin Bu, hasil data mining kami tidak berhenti di tabel angka, tapi diubah jadi 3 alat bisnis nyata: (1) Smart Sales Script: contekan sales showroom agar tahu simulasi cicilan mana yang paling gampang disetujui leasing; (2) Alokasi Stok Gudang: membagi stok warna motor per cabang (Bekasi vs Jakarta) agar tidak ada motor mangkrak; (3) Promo Bundling: dasar nego diskon DP bersama leasing mitra."*

---

# MODUL 6: PEMBAGIAN PERAN & TANGGUNG JAWAB KELOMPOK 1

| Anggota Tim | Fokus Penguasaan Materi (Bila Ditanya Dosen) | Tanggung Jawab Dokumen Bab 1 |
| :--- | :--- | :--- |
| **Megi Refkiansyah**<br/>*(NIM: 19240488)* | • Latar Belakang Masalah Dealer PT. SSM Motor.<br/>• Teori KDD, FP-Growth vs Apriori, Struktur FP-Tree.<br/>• Tinjauan Pustaka Buku Babon & Jurnal SINTA 2021–2026. | Menguasai **Sub-bab 1.1 (Latar Belakang)** dan **Sub-bab 1.2 (Tinjauan Pustaka)**. |
| **Darell Rangga Putra R.**<br/>*(NIM: 19241009)* | • Formulasi 4 Butir Rumusan Masalah & 3 Celah Riset (Gap).<br/>• 3 Pilar Kebaruan Ilmiah (Novelty) & Solusi CRISP-DM.<br/>• Konsep Multi-Attribute Predicate Basket Transformation. | Menguasai **Sub-bab 1.3 (Rumusan Masalah & Gap)** dan **Sub-bab 1.4 (Novelty & Solusi)**. |
| **Wahyu Rizky**<br/>*(NIM: 19240493)* | • Batasan 5 Parameter Ruang Lingkup Penelitian.<br/>• 4 Butir Tujuan Penelitian Simetris (SMART Objectives).<br/>• Karakteristik 3.113 Data Faktur DMS & Validasi Tri-Metrik. | Menguasai **Sub-bab 1.5 (Ruang Lingkup)** dan **Sub-bab 1.6 (Tujuan Penelitian)**. |
