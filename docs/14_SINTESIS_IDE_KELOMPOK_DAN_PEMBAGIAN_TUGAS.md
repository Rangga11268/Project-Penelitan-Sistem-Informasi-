# SINTESIS IDE RISET DAN STRUKTUR PEMBAGIAN TUGAS KELOMPOK 1
## MATA KULIAH: PENELITIAN SISTEM INFORMASI (SEMESTER 5 UBSI)

**Dosen Pengampu:** Syifa Nur Rakhmah, M.Kom.  
**Kelompok 1:**
- Darell Rangga Putra R. (19241009)
- Megi Refkiansyah (19240488)
- Wahyu Rizky (19240493)

**Objek Riset:** PT. Sinar Surya Matahari (Dealer Resmi Sepeda Motor Yamaha)  
**Dataset Utama:** 3.113 Data Transaksi Penjualan Riil (Juni – Agustus 2026)  
**Target Luaran:** Publikasi Artikel Jurnal Terakreditasi SINTA (SINTA 2–4)

---

## 1. SINTESIS KONTRIBUSI & KESEPAKATAN IDE 3 ANGGOTA

Ketiga anggota Kelompok 1 telah menyumbangkan draf perumusan judul, *research gap*, dan *novelty* yang saling melengkapi:

| Anggota | Intisari Usulan & Kekuatan Konseptual | Dokumen Terkait |
| :--- | :--- | :--- |
| **Darell Rangga Putra R.** | Merumuskan judul standar *Compound Title* (Ken Hyland & James Hartley), memetakan metodologi *Multi-Attribute Association Rule Mining* berbasis FP-Growth, dan membangun evaluasi Tri-Metrik (*Support*, *Confidence*, $\text{Lift Ratio} > 1.0$). | `docs/05_BUKTI_NOVELTY_DAN_RESEARCH_GAP.md`<br>`docs/12_BAB_1_PENDAHULUAN_TUGAS_BU_SYIFA.md`<br>`docs/13_ANALISIS_AKADEMIK_JUDUL_DAN_NOVELTY_HYLAND.md` |
| **Megi Refkiansyah** | Menyusun 3 opsi judul komprehensif dalam bentuk PDF lengkap dengan latar belakang, tinjauan pustaka, komparasi Apriori vs FP-Growth, preferensi varian warna (22 warna), serta strategi alokasi stok multi-gudang (Bekasi vs Jakarta). | `docs/3_Judul_Penelitian_Association_Rule_SSM_Motor.pdf` |
| **Wahyu Rizky** | Merumuskan 3 opsi judul dan *research gap* tajam yang menyoroti kelemahan *candidate generation* Apriori, eksplorasi variabel estetika varian warna motor dengan skema tenor pembiayaan, serta analisis spasial konsumen Jabodetabek. | Catatan Riset WAG & Formulasi Judul Multivariat |

---

## 2. FORMULASI JUDUL FINAL KESEPAKATAN BERSAMA

Dari integrasi ide Darell, Megi, dan Wahyu, disepakati satu judul final yang paling representatif dan berdaya saing tinggi:

> **"Multi-Attribute Association Rule Mining Menggunakan Algoritma FP-Growth: Analisis Pola Pembelian dan Preferensi Pembiayaan Konsumen Sepeda Motor"**  
> *(Studi Kasus: PT. Sinar Surya Matahari)*
>
> **Padanan Bahasa Inggris (IEEE / Scopus Standard):**  
> *"Multi-Attribute Association Rule Mining Using FP-Growth Algorithm: Uncovering Motorcycle Purchasing Patterns and Consumer Financing Preferences"*

---

## 3. PEMBAGIAN TUGAS 6 KOMPONEN UTAMA PENDAHULUAN (BAB 1)

Sesuai dengan 6 komponen baku pendahuluan yang diinstruksikan oleh Ibu Syifa Nur Rakhmah, M.Kom.:

| No | Komponen Pendahuluan | Penanggung Jawab Utama | Rincian Isi & Fokus Pengerjaan |
| :-: | :--- | :--- | :--- |
| 1 | **Latar Belakang (Background)** | **Megi Refkiansyah** | Gambaran umum industri otomotif roda dua nasional, peran dealer resmi Yamaha, profil 3.113 transaksi PT. Sinar Surya Matahari, dan pentingnya integrasi data transaksi produk fisik dengan skema pembiayaan. |
| 2 | **Tinjauan Pustaka Singkat (Literature Review)** | **Wahyu Rizky** | Telaah kritis 6–10 artikel jurnal SINTA 1–4 terbitan 2021–2025 (Saptadi 2023, Rahman 2025, Soleh 2022, Hafizh 2023, dll.) terkait metode Association Rule Mining. |
| 3 | **Rumusan Masalah & Celah Penelitian (Research Gap)** | **Wahyu Rizky** | Identifikasi defisit literatur: sebagian besar paper ARM otomotif hanya meneliti sparepart bengkel mikro, menggunakan analisis bivariat parsial, atau mengabaikan korelasi produk fisik bernilai tinggi dengan lembaga pembiayaan. |
| 4 | **Kebaruan (Novelty) & Solusi** | **Darell Rangga Putra R.** | Penjelasan proposisi nilai orisinal: integrasi simultan 5 dimensi (*Model + Warna + Leasing BAF/Adira/OTO + Tenor + Domisili*) menggunakan *FP-Tree Predicate Basket* tanpa aturan semu (*spurious rules*). |
| 5 | **Ruang Lingkup (Scope)** | **Megi Refkiansyah** | Batasan variabel penelitian (44 model motor, varian warna dominan, lembaga multifinance, tenor 11–35 bln), lokasi geografis konsumen Jabodetabek, dan periode waktu transaksi (Juni–Agustus 2026). |
| 6 | **Tujuan Penelitian (Research Objective)** | **Darell Rangga Putra R.** | Pernyataan sasaran algoritmik (menghasilkan aturan asosiasi valid dengan $\text{Lift Ratio} > 1.0$) dan sasaran terapan manajerial (*Smart Sales Script* dan panduan alokasi stok unit). |

---

## 4. PEMBAGIAN TUGAS TEKNIS & PENGOLAHAN DATA

| Tahapan Teknis | Penanggung Jawab | Deskripsi Output |
| :--- | :--- | :--- |
| **Data Preprocessing & Encoding** | **Megi Refkiansyah** | • Pembersihan data mentah Excel (3.113 baris).<br>• Standarisasi teks leasing dan tipe motor.<br>• Pembentukan tabel biner *One-Hot Encoding*. |
| **Algoritma & Pemodelan Data Mining** | **Darell Rangga Putra R.** | • Implementasi FP-Growth di Python (`mlxtend`) / RapidMiner.<br>• Pengujian ambang batas Min Support, Min Confidence, dan Lift Ratio.<br>• Pembuatan visualisasi *Association Network Graph*. |
| **Penyusunan Naskah & Analisis Bisnis** | **Wahyu Rizky** | • Integrasi draf BAB 1–5 laporan penelitian.<br>• Menerjemahkan aturan asosiasi menjadi rekomendasi bisnis nyata.<br>• Manajemen referensi Mendeley (.ris / APA 7th). |

---

## 5. STRUKTUR ARSIP DOKUMEN DALAM REPOSITORI

Seluruh arsip pendukung penelitian tersimpan rapi pada folder `docs/`:
1. `docs/05_BUKTI_NOVELTY_DAN_RESEARCH_GAP.md` — Matriks komparasi empiris jurnal SINTA (2021–2026).
2. `docs/11_BEDAH_3_JUDUL_FINAL_SSM_MOTOR.md` — Bedah mendalam 3 alternatif sudut pandang judul.
3. `docs/12_BAB_1_PENDAHULUAN_TUGAS_BU_SYIFA.md` — Naskah BAB 1 lengkap sesuai format UBSI.
4. `docs/13_ANALISIS_AKADEMIK_JUDUL_DAN_NOVELTY_HYLAND.md` — Landasan teoretis Academic Writing Hyland & Hartley.
5. `docs/14_SINTESIS_IDE_KELOMPOK_DAN_PEMBAGIAN_TUGAS.md` — Dokumen pembagian tugas dan sintesis ide tim.
6. `docs/3_Judul_Penelitian_Association_Rule_SSM_Motor.pdf` — Dokumen proposal 3 judul dari Megi.
7. `docs/BAB_1_PENDAHULUAN_KELOMPOK_1_UBSI.pdf` — File PDF siap cetak / siap kumpul BAB 1.
8. `docs/DAFTAR_REFERENSI_MENDELEY.ris` — File ekspor sitasi Mendeley untuk 11 artikel jurnal SINTA.
