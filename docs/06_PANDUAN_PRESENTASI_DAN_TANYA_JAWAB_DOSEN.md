# PANDUAN PRESENTASI & SIMULASI TANYA JAWAB PENGUJI (DOSEN)
## MATA KULIAH PENELITIAN SISTEM INFORMASI

**Topik:** Multi-Attribute Association Rule Mining (FP-Growth) pada Transaksi Dealer SSM Motor  
**Tim Peneliti (Kelompok 1):** Darell Rangga Putra R. (19241009), Megi Refkiansyah (19240488), Wahyu Rizky (19240493)

---

## 🎯 DAFTAR PERTANYAAN KRITIS DOSEN & JAWABAN TELAK ILMIAH

---

### ❓ PERTANYAAN 1:
> *"Untuk apa sih kita mencari keterkaitan antara tipe motor dengan lembaga leasing dan tenor 35 bulan? Kan bisa saja leasing BAF memang prosesnya lebih cepat di luar sana, dampaknya apa bagi dealer?"*

#### 💡 Jawaban Telak:
> *"Izin menjawab Ibu,*
> 
> *Pertanyaan yang sangat bagus, Bu. Hubungan antara tipe motor, leasing, dan tenor ini memiliki **3 dampak finansial dan operasional nyata** bagi dealer:*
> 
> 1. **Mencegah 'Lost Sales' Akibat *Price Shock*:** Motor matik premium (Aerox/NMAX) memiliki harga OTR tinggi (Rp 30–40 jutaan). Jika sales langsung menawarkan tunai atau cicilan jangka pendek (11 bulan) yang angsurannya Rp 2–3 juta/bulan, konsumen sering kali kaget dan membatalkan pembelian. Dengan data empiris yang membuktikan bahwa $85\%$ pembeli tipe ini mengambil **tenor 35 bulan via BAF**, sales langsung menyodorkan brosur cicilan paling ringan (Rp 1 jutaan/bulan) sejak detik pertama. Ini menaikkan *closing rate* transaksi.
> 
> 2. **Optimalisasi Kecepatan *Approval* Kredit:** BAF adalah *captive finance* resmi Yamaha dengan matriks *credit scoring* khusus motor Yamaha. Jika sales salah memasukkan aplikasi ke leasing non-rekanan utama, proses survei memakan waktu 3–5 hari dan berisiko ditolak (*reject*). Mengetahui pola asosiasi ini membuat sales langsung mengarahkan ke BAF sehingga *approval* selesai dalam hitungan jam dan unit motor bisa langsung dikirim (*SLA efisien*).
> 
> 3. **Pendapatan Komisi Dealer (*Refund Leasing*):** Dealer mendapatkan margin ganda pada penjualan kredit, yaitu margin unit dan insentif (*refund rate*) dari pihak leasing. Mengetahui motor mana yang paling laris via kredit tenor panjang memungkinkan dealer bernegosiasi program subsidi DP bersama BAF secara tepat sasaran.*
> 
> *Jadi kesimpulannya Bu, penelitian ini membangun **Sistem Pendukung Keputusan (Decision Support)** agar penawaran sales berbasis data objektif, bukan tebak-tebakan."*

---

### ❓ PERTANYAAN 2:
> *"Kenapa menggunakan istilah 'Multi-Attribute Association Rule Mining'? Kenapa bukan Market Basket Analysis biasa?"*

#### 💡 Jawaban Telak:
> *"Izin Ibu, dalam literatur baku data mining (*Han, Kamber & Pei*), Market Basket Analysis klasik hanya menghitung kombinasi item tunggal sejenis (seperti barang belanjaan supermarket: roti + selai).
> 
> Sedangkan pada transaksi pembelian kendaraan bermotor, konsumen membeli 1 unit kendaraan tetapi secara simultan membuat **kumpulan keputusan multi-dimensi** (Tipe Motor + Skema Leasing + Durasi Tenor + Wilayah Domisili). Kumpulan atribut inilah yang kita bentuk menjadi keranjang biner (*One-Hot Encoding*). Istilah ilmiah yang tepat untuk kasus ini adalah **Multi-Attribute Association Rule Mining**."*

---

### ❓ PERTANYAAN 3:
> *"Kenapa memilih algoritma FP-Growth dibanding Apriori?"*

#### 💡 Jawaban Telak:
> *"Izin Ibu, ada 2 alasan teknis utama:*
> 1. **Efisiensi Waktu & Memori Tanpa *Candidate Generation*:** Algoritma Apriori harus memindai (*scan*) database berulang kali untuk setiap kombinasi kandidat itemset ($C_k$), yang sangat lambat pada ribuan transaksi. Sedangkan **FP-Growth** hanya memindai database **2 kali saja** dan memampatkan data ke dalam struktur pohon **FP-Tree**.
> 2. **Kinerja pada Pola Multi-Atribut:** FP-Growth menggunakan pendekatan *Divide and Conquer* (melalui *Conditional Pattern Base*), sehingga proses pencarian pola kombinasi frekuensi tinggi menjadi jauh lebih cepat dan stabil."*

---

### ❓ PERTANYAAN 4:
> *"Bagaimana Anda membuktikan bahwa aturan asosiasi yang dihasilkan benar-benar valid dan bukan kebetulan?"*

#### 💡 Jawaban Telak:
> *"Izin Ibu, kami memvalidasinya menggunakan metrik statistik **Lift Ratio**.
> 
> Nilai Lift mengukur kekuatan keterkaitan antar-item dibanding jika keduanya terjadi secara acak independen. Syarat aturan valid secara ilmiah adalah **$\text{Lift} > 1.0$**.
> 
> Pada eksperimen data riil 3.113 transaksi SSM Motor kami, seluruh aturan yang lolos memiliki nilai **Lift Ratio antara 1.58 hingga 4.76**, yang membuktikan adanya korelasi positif yang sangat kuat antar-atribut transaksi."*

---

### ❓ PERTANYAAN 5:
> *"Apa novelty / kebaruan penelitian ini dibanding penelitian di Google Scholar?"*

#### 💡 Jawaban Telak:
> *"Izin Ibu, setelah kami meninjau Google Scholar dan portal SINTA:*
> * Mayoritas penelitian kredit motor hanya memakai metode SPK Kelayakan (seperti SAW, TOPSIS, SMART) untuk menilai nasabah diterima/ditolak.
> * Penelitian yang menerapkan **FP-Growth pada Multi-Atribut Transaksi Penjualan Motor (Tipe + Leasing + Tenor + Wilayah)** berbasis data transaksi riil kuartal 2026 **belum pernah ada yang meneliti (0 hasil serupa di Google Scholar)**.
> * Penelitian ini orisinal dan memiliki kebaruan dalam mengintegrasikan pola data mining transaksi dengan strategi pembiayaan otomotif."*

---

## ⚡ RINGKASAN CHEAT-SHEET PRESENTASI (3 POIN KUNCI)

1. **Objek & Data:** PT. SSM Motor (Dealer Resmi Yamaha), 3.113 transaksi riil (Juni – Agustus 2026).
2. **Metode:** Algoritma **FP-Growth** pada keranjang multi-atribut dengan evaluasi **Support, Confidence, dan Lift Ratio**.
3. **Manfaat:** Panduan taktik sales counter, strategi promosi subsidi DP bersama leasing (BAF/Adira), dan optimasi alokasi stok gudang.
