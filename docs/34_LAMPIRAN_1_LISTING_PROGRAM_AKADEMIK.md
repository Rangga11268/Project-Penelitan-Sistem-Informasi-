# LAMPIRAN 1: LISTING KODE PROGRAM PENGUJIAN DAN PEMODELAN FP-GROWTH

> **Format Standar Proposal Skripsi / Riset Akademik (UBSI)**:
> - Kertas: A4 (21,0 cm × 29,7 cm)
> - Margin: Kiri = 4,0 cm (Penjilidan), Atas = 3,0 cm, Kanan = 3,0 cm, Bawah = 3,0 cm
> - Font Teks: Times New Roman 12 pt, Spasi 1.5, First Line Indent 1,0 cm, Justified
> - Font Kode: Courier New 8,5 pt, Spasi 1.0, Penomoran Baris 2 Digit, Border Netral Hitam Tipis

---

Listing program di bawah ini merupakan implementasi komputasional penambangan data (*data mining*) menggunakan algoritma *Frequent Pattern Growth* (FP-Growth) yang dieksekusi menggunakan bahasa pemrograman Python 3.10 pada lingkungan Jupyter Notebook. Pengujian dilakukan terhadap 3.113 data faktur transaksi penjualan fisik resmi dari sistem enterprise *Yamaha Dealer Management System* (Y-DMS) PT. Sinar Surya Matahari untuk periode 1 Juni hingga 31 Agustus 2026. Kode program mencakup enam fase metodologi CRISP-DM yang meliputi inisialisasi pustaka, analisis statistik univariat lima dimensi keputusan, transformasi keranjang predikat multiatribut biner (3.113 baris × 89 kolom) guna mengatasi kendala *empty itemsets*, ekstraksi *frequent itemsets* berbasis struktur pohon FP-Tree, pembentukan kaidah asosiasi serta penyaringan Standar Validasi Tiga Metrik (*Support*, *Confidence*, *Lift Ratio*), hingga simulasi preskriptif manajerial dealer. Seluruh berkas kode sumber dan dataset penelitian juga terdokumentasi secara terbuka pada repositori GitHub resmi penelitian.

### Tabel L1.1 Spesifikasi Teknis Lingkungan Komputasi dan Repositori Riset

| Komponen Sistem | Spesifikasi Operasional |
| :--- | :--- |
| **Bahasa Pemrograman** | Python 3.10.12 (64-bit environment) |
| **Pustaka Utama (Libraries)** | Pandas 2.2.2, NumPy 1.26.4, MLxtend 0.23.1, Matplotlib 3.8.4, Seaborn 0.13.2 |
| **Basis Data Penelitian** | 3.113 Faktur Transaksi Penjualan Bersih (Sensus Y-DMS PT. SSM Motor) |
| **Representasi Matriks** | Keranjang Predikat Multiatribut Biner (3.113 Baris × 89 Kolom Fitur) |
| **Spesifikasi Perangkat Keras** | AMD Ryzen 5 Processor, 16 GB DDR4 RAM, 512 GB NVMe SSD, Windows 11 OS |
| **Tautan Repositori GitHub** | [https://github.com/Rangga11268/Project-Penelitan-Sistem-Informasi-.git](https://github.com/Rangga11268/Project-Penelitan-Sistem-Informasi-.git) |

---

### Listing L.1 Import Pustaka dan Inisialisasi Lingkungan Komputasi
*Listing L.1 memuat pustaka-pustaka utama yang digunakan dalam proses komputasi data mining, antara lain Pandas dan NumPy untuk pemrosesan larik dan struktur data tabular, Matplotlib dan Seaborn untuk perancangan visualisasi grafik analitis, serta pustaka MLxtend (TransactionEncoder, fpgrowth, dan association_rules) sebagai pustaka inti implementasi algoritma FP-Growth.*

```python
# ==========================================
# 0. IMPORT PUSTAKA UTAMA
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Pustaka Association Rule Mining
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

# Pengaturan visualisasi grafik
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
```

---

### Listing L.2 Pemuatan Basis Data Transaksi Penjualan Y-DMS dan Verifikasi Dimensi
*Listing L.2 mengeksekusi pembacaan berkas dataset faktur penjualan PT. Sinar Surya Matahari dari sistem enterprise Yamaha Dealer Management System (Y-DMS) yang memuat 3.113 baris transaksi valid selama periode kuartal ketiga (1 Juni – 31 Agustus 2026), dilanjutkan dengan verifikasi kelengkapan atribut dan penanganan nilai kosong (missing values).*

```python
# ==========================================
# 4.1.1 MEMUAT DATASET TRANSAKSI Y-DMS
# ==========================================
data_path = 'data/Transaksi_Penjualan_Yamaha_SSM_Motor_Clean.csv'
df_raw = pd.read_csv(data_path)

print(f"Total Baris Transaksi : {df_raw.shape[0]} baris")
print(f"Total Kolom Atribut   : {df_raw.shape[1]} kolom")
print(f"Jumlah Nilai Kosong   : {df_raw.isnull().sum().sum()}")
```

---

### Listing L.3 Eksplorasi Statistik Deskriptif dan Profil Univariat Lima Dimensi
*Listing L.3 melakukan perhitungan distribusi frekuensi univariat pada lima dimensi keputusan konsumen: peringkat 10 model sepeda motor terlaris, sebaran 22 varian warna bodi, proporsi lembaga pembiayaan tunai versus kredit, sebaran durasi tenor cicilan, serta distribusi spasial wilayah domisili pembeli.*

```python
# ==========================================
# 4.1.2 EKSPLORASI STATISTIK UNIVARIAT 5 DIMENSI
# ==========================================
print("=== 1. TOP 10 MODEL SEPEDA MOTOR (NAMA_BRG) ===")
s_model = df_raw['NAMA_BRG'].value_counts()
pct_model = df_raw['NAMA_BRG'].value_counts(normalize=True) * 100
df_m = pd.DataFrame({'Frekuensi (Unit)': s_model, 'Proporsi (%)': pct_model})
print(df_m.head(10).round(2))

print("\n=== 2. SEBARAN METODE PEMBAYARAN (CASH VS KREDIT) ===")
s_pay = df_raw['NAMA_LEASING'].value_counts()
pct_pay = df_raw['NAMA_LEASING'].value_counts(normalize=True) * 100
df_p = pd.DataFrame({'Frekuensi (Unit)': s_pay, 'Proporsi (%)': pct_pay})
print(df_p.round(2))

print("\n=== 3. TOP 5 VARIAN WARNA TERPOPULER ===")
s_clr = df_raw['WARNA'].value_counts()
pct_clr = df_raw['WARNA'].value_counts(normalize=True) * 100
df_c = pd.DataFrame({'Frekuensi (Unit)': s_clr, 'Proporsi (%)': pct_clr})
print(df_c.head(5).round(2))

print("\n=== 4. SEBARAN DURASI TENOR KREDIT ===")
s_tnr = df_raw['TENOR'].value_counts()
pct_tnr = df_raw['TENOR'].value_counts(normalize=True) * 100
df_t = pd.DataFrame({'Frekuensi (Unit)': s_tnr, 'Proporsi (%)': pct_tnr})
print(df_t.round(2))

print("\n=== 5. TOP 5 WILAYAH DOMISILI KONSUMEN ===")
s_wil = df_raw['KOTA_KAB'].value_counts()
pct_wil = df_raw['KOTA_KAB'].value_counts(normalize=True) * 100
df_w = pd.DataFrame({'Frekuensi (Unit)': s_wil, 'Proporsi (%)': pct_wil})
print(df_w.head(5).round(2))
```

---

### Listing L.4 Pembersihan Data dan Rekayasa Keranjang Predikat Multiatribut
*Listing L.4 merekayasa transaksi fisik sepeda motor tunggal menjadi representasi keranjang predikat multiatribut berformat pasangan logika Atribut=Nilai guna mengatasi kendala empty itemsets pada analisis keranjang pasar konvensional, sehingga algoritma FP-Growth dapat menemukan keterkaitan lintas-dimensi.*

```python
# ==========================================
# 4.2.1 PEMBENTUKAN FITUR STANDAR (DF_CLEAN)
# ==========================================
df_clean = pd.DataFrame()
df_clean['NO_FAKTUR'] = df_raw['NO_FAKTUR']
df_clean['Model'] = "Model=" + df_raw['NAMA_BRG'].astype(str).str.strip()
df_clean['Warna'] = "Warna=" + df_raw['WARNA'].astype(str).str.strip()
df_clean['Leasing'] = "Leasing=" + df_raw['NAMA_LEASING'].astype(str).str.strip()
df_clean['Tenor'] = "Tenor=" + df_raw['TENOR'].astype(str).str.strip() + " Bulan"
df_clean['Wilayah'] = "Wilayah=" + df_raw['KOTA_KAB'].astype(str).str.strip()

# ==========================================
# 4.2.2 TRANSFORMASI KERANJANG PREDIKAT MULTIATRIBUT
# ==========================================
basket_transactions = []
for _, row in df_clean.iterrows():
    basket = [
        row['Model'],
        row['Warna'],
        row['Leasing'],
        row['Tenor'],
        row['Wilayah']
    ]
    basket_transactions.append(basket)

print("Jumlah Keranjang Transaksi :", len(basket_transactions))
print("Contoh Sampel Keranjang #1 :", basket_transactions[0])
```

---

### Listing L.5 Pembentukan Matriks Insidensi Biner (One-Hot Encoding 3.113 × 89)
*Listing L.5 mengonversi daftar keranjang predikat ke dalam matriks insidensi biner berdimensi 3.113 baris kali 89 kolom fitur menggunakan modul TransactionEncoder. Seluruh nilai True/False kemudian diubah menjadi representasi integer numerik 1 dan 0 sebagai input terstandarisasi bagi algoritma penambangan pola.*

```python
# ==========================================
# 4.2.3 PEMBENTUKAN MATRIKS INSIDENSI BINER
# ==========================================
te = TransactionEncoder()
te_ary = te.fit(basket_transactions).transform(basket_transactions)
df_binary = pd.DataFrame(te_ary, columns=te.columns_).astype(int)

print(f"Dimensi Matriks Biner: {df_binary.shape[0]} Baris × {df_binary.shape[1]} Kolom")
print("Contoh Cuplikan Matriks:")
print(df_binary.iloc[:3, :5])
```

---

### Listing L.6 Konstruksi FP-Tree dan Ekstraksi Frequent Itemsets (FP-Growth)
*Listing L.6 mengeksekusi algoritma Frequent Pattern Growth (FP-Growth) pada matriks insidensi biner dengan parameter ambang batas Minimum Support = 2,0% (0,02). Prosedur ini membangun struktur pohon frekuensi FP-Tree di memori kerja dan mengekstrak seluruh kombinasi item berfrekuensi tinggi tanpa pembentukan kandidat.*

```python
# ==========================================
# 4.3.1 EKSTRAKSI FREQUENT ITEMSETS (FP-GROWTH)
# ==========================================
min_sup = 0.02 # Ambang batas Minimum Support 2%

# Eksekusi algoritma FP-Growth pada matriks biner
frequent_itemsets = fpgrowth(df_binary, min_support=min_sup, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False).reset_index(drop=True)

print(f"Total Frequent Itemsets Terbentuk (Min Sup >= {min_sup}): {len(frequent_itemsets)}")
print("Distribusi Berdasarkan Panjang Itemset:")
print(frequent_itemsets['length'].value_counts())
print("\nTop 5 Frequent Itemsets Tertinggi:")
print(frequent_itemsets.head(5))
```

---

### Listing L.7 Pembangkitan Kaidah Asosiasi dan Perhitungan Nilai Tri-Metrik
*Listing L.7 membangkitkan kaidah asosiasi (association rules) dari kumpulan frequent itemsets berdasarkan ambang batas Minimum Confidence = 50,0% (0,50). Setiap aturan yang terbentuk dihitung secara simultan nilai Support, Confidence, dan Lift Ratio-nya.*

```python
# ==========================================
# 4.4.1 PEMBANGKITAN KAIDAH ASOSIASI & FILTER TRI-METRIK
# ==========================================
min_conf = 0.50 # Ambang batas Minimum Confidence 50%

# Pembangkitan kaidah asosiasi dari frequent itemsets
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_conf)

print(f"Total Kaidah Asosiasi Awal (Confidence >= {min_conf}): {len(rules)}")
print("Ringkasan Statistik Metrik Kaidah Asosiasi:")
print(rules[['support', 'confidence', 'lift']].describe().round(4))
```

---

### Listing L.8 Uji Dependensi Statistik dan Eliminasi Kaidah Semu (Lift Ratio ≤ 1,0)
*Listing L.8 menerapkan prosedur validasi ilmiah untuk mengeliminasi aturan asosiasi yang memiliki nilai Lift Ratio <= 1,0 (kaidah semu atau berkorelasi negatif), sehingga hanya kaidah dengan Lift Ratio > 1,0 (interdependensi positif murni) yang lolos ke tahap perumusan strategi bisnis.*

```python
# ==========================================
# 4.4.2 ELIMINASI KAIDAH SEMU & SELEKSI KAIDAH EMAS
# ==========================================
# Filter hanya kaidah dengan Lift Ratio > 1.0 (korelasi positif murni)
valid_rules = rules[rules['lift'] > 1.0].copy()
spurious_rules = rules[rules['lift'] <= 1.0].copy()

print(f"Jumlah Kaidah Valid (Lift > 1.0)     : {len(valid_rules)} kaidah ({len(valid_rules)/len(rules)*100:.2f}%)")
print(f"Jumlah Kaidah Semu Tereliminasi      : {len(spurious_rules)} kaidah")

# Urutkan berdasarkan kekuatan Lift Ratio tertinggi
valid_rules = valid_rules.sort_values(by='lift', ascending=False).reset_index(drop=True)

# Format kolom keterbacaan
valid_rules['antecedents_str'] = valid_rules['antecedents'].apply(lambda x: ', '.join(list(x)))
valid_rules['consequents_str'] = valid_rules['consequents'].apply(lambda x: ', '.join(list(x)))

print("\nTop 10 Kaidah Asosiasi Emas (Golden Rules):")
for idx, r in valid_rules.head(10).iterrows():
    print(f"[{idx+1}] IF {r['antecedents_str']} THEN {r['consequents_str']} "
          f"(Sup: {r['support']*100:.2f}%, Conf: {r['confidence']*100:.2f}%, Lift: {r['lift']:.3f})")
```

---

### Listing L.9 Klasifikasi dan Pemetaan Klaster Manajerial Kaidah Asosiasi
*Listing L.9 mengelompokkan kaidah asosiasi valid ke dalam empat klaster operasional dealer: (1) Klaster Spasial Geo-Marketing, (2) Klaster Finansial Lembaga Pembiayaan, (3) Klaster Multiatribut Lintas Dimensi, dan (4) Klaster Estetika Warna-Model Kendaraan.*

```python
# ==========================================
# 4.4.3 KATEGORISASI KLASTER MANAJERIAL
# ==========================================
def classify_rule(row):
    ant = ' '.join(list(row['antecedents']))
    con = ' '.join(list(row['consequents']))
    rule_str = ant + " " + con
    
    has_wilayah = 'Wilayah=' in rule_str
    has_leasing = 'Leasing=' in rule_str or 'Tenor=' in rule_str
    has_model = 'Model=' in rule_str
    has_warna = 'Warna=' in rule_str
    
    if has_wilayah and (has_model or has_leasing or has_warna):
        return "Geo-Marketing Spasial"
    elif has_leasing and (has_model or has_warna):
        return "Finansial & Kredit"
    elif has_model and has_warna and not has_leasing and not has_wilayah:
        return "Warna & Model Kendaraan"
    else:
        return "Multi-Atribut Lintas Dimensi"

valid_rules['Cluster'] = valid_rules.apply(classify_rule, axis=1)

print("Distribusi Kaidah Asosiasi per Klaster:")
print(valid_rules['Cluster'].value_counts())
print("\nProporsi (%) per Klaster:")
print((valid_rules['Cluster'].value_counts(normalize=True)*100).round(2))
```

---

### Listing L.10 Simulasi Hilirisasi Rekomendasi Preskriptif Dealer (Alokasi Stok & Sales Script)
*Listing L.10 menghitung probabilitas bersyarat P(Warna | Model) untuk memformulasikan rasio alokasi stok proporsional antargudang 4:2:1 (Matte Black : Prestige Silver : Magma Black), memetakan matriks penawaran pramuniaga (Smart Sales Script), serta menyusun strategi penetrasi pasar regional Jabodetabek.*

```python
# ==========================================
# 4.5.1 SIMULASI ALOKASI PERSEDIAAN VARIAN WARNA
# ==========================================
top_models = ['All New NMAX 155', 'All New Aerox 155', 'Grand Filano Hybrid', 'Fazzio Hybrid']

for m in top_models:
    sub = df_raw[df_raw['NAMA_BRG'] == m]
    tot = len(sub)
    print(f"\nModel: {m} (Total Sensus: {tot} Unit)")
    clr_vc = sub['WARNA'].value_counts()
    for clr, cnt in clr_vc.head(3).items():
        prob = (cnt / tot) * 100
        print(f"  - Warna {clr:<18}: {cnt:>4} unit ({prob:>5.1f}%)")

# ==========================================
# 4.5.2 SIMULASI SMART SALES SCRIPT MATRIX
# ==========================================
print("\n=== MATRIKS SMART SALES SCRIPT (MODEL VS PEMBIAYAAN) ===")
ct_sales = pd.crosstab(df_raw['NAMA_BRG'], df_raw['NAMA_LEASING'], normalize='index') * 100
print(ct_sales.loc[top_models].round(2))

print("\n[INFO] Seluruh proses pemodelan dan pengujian komputasi FP-Growth berhasil dieksekusi secara optimal.")
```
