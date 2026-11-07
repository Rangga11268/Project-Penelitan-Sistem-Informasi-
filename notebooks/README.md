# Notebook Analisis Kaidah Asosiasi FP-Growth (PT. SSM Motor)

Folder ini berisi berkas Jupyter Notebook komputasi penambangan data riil untuk **Bab IV (Hasil dan Pembahasan)** penelitian.

---

## 📁 Berkas di Folder Ini
1. **`01_ANALISIS_FP_GROWTH_PT_SSM_MOTOR.ipynb`**  
   Notebook utama terintegrasi yang mencakup tahapan CRISP-DM:
   * **Bagian 1 (Sub-bab 4.1): Data Understanding** — Eksplorasi univariat 3.113 transaksi, distribusi model motor, varian warna, leasing, tenor, dan wilayah domisili.
   * **Bagian 2 (Sub-bab 4.2): Data Preparation** — Pembersihan data, verifikasi keunikan faktur, eliminasi identitas pribadi (anonimisasi privasi), transformasi keranjang predikat multiatribut `{Atribut=Nilai}`, dan pembentukan matriks insidensi biner (3.113 baris $\times$ 87 kolom predikat).
   * **Bagian 3 (Sub-bab 4.3): Modeling Algoritma FP-Growth** — Pembangkitan F-List ($min\_sup = 0{,}02$), konstruksi pohon FP-Tree dan *Header Table*, serta ekstraksi rekursif *Conditional Pattern Base* (259 *frequent itemsets*).
   * **Bagian 4 (Sub-bab 4.4): Evaluation & Association Rules** — Pembentukan aturan asosiasi, filter metrik ($Confidence \ge 0{,}50$ dan $Lift > 1{,}0$), menghasilkan 396 kaidah valid, dan ekspor 15 kaidah terbaik.
2. **`top_15_association_rules_ssm_motor.csv`**  
   Daftar 15 kaidah asosiasi terkuat yang telah diformat dalam bentuk persentase Support, Confidence, dan nilai Lift Ratio untuk kebutuhan Tabel 4.5 naskah Bab IV.
3. **`visualisasi_4_1_univariat.png`**  
   Grafik komposit 4-in-1 untuk visualisasi Gambar 4.1 dan 4.2 pada Sub-bab 4.1.
4. **`visualisasi_4_4_scatter_rules.png`**  
   Grafik sebaran (*scatter plot*) hubungan Support vs Confidence dengan gradasi warna Lift Ratio untuk Gambar 4.4 pada Sub-bab 4.4.

---

## 🚀 Cara Menjalankan Notebook
1. Pastikan virtual environment `.venv` di direktori root sudah terpasang.
2. Buka notebook di VS Code:  
   Pilih kernel: **`Python (Penelitian SI .venv)`** atau `.venv/Scripts/python.exe`.
3. Notebook sudah memiliki output lengkap (*pre-rendered*). Untuk menjalankan ulang seluruh sel dari awal, klik tombol **Run All** di toolbar VS Code.
