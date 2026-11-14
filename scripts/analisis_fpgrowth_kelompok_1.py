"""
========================================================================================
PROYEK AKHIR RISET METODE PENELITIAN SISTEM INFORMASI
IMPLEMENTASI ALGORITMA FP-GROWTH MULTI-ATTRIBUTE PREDICATE BASKET TRANSFORMATION
Studi Kasus: PT. Sinar Surya Matahari (Yamaha Dealer Management System / Y-DMS)
Tim Peneliti : Darell Rangga Putra Rachman, Megi Refkiansyah, Wahyu Rizky Khoirudin
Program Studi: Sistem Informasi, Universitas Bina Sarana Informatika
Repositori   : https://github.com/Rangga11268/Project-Penelitan-Sistem-Informasi-.git
========================================================================================
"""

# --- CELL 1 ---
# ==========================================
# 0. IMPORT PUSTAKA UTAMA
# ==========================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Pustaka Association Rule Mining
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Konfigurasi Tampilan Grafik & Visualisasi
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300

# Deteksi path dataset secara dinamis
possible_dataset_paths = [
    os.path.join('..', 'datasets', '01_DATASET_UTAMA_DIGUNAKAN', 'data_transaksi_dealer_jun_agst_2026_clean.csv'),
    os.path.join('datasets', '01_DATASET_UTAMA_DIGUNAKAN', 'data_transaksi_dealer_jun_agst_2026_clean.csv'),
    r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Penelitian SI\datasets\01_DATASET_UTAMA_DIGUNAKAN\data_transaksi_dealer_jun_agst_2026_clean.csv'
]
data_path = next((p for p in possible_dataset_paths if os.path.exists(p)), possible_dataset_paths[0])
print(f"Dataset terdeteksi di: {data_path}")


# --- CELL 3 ---
# ==========================================
# 4.1.1 MEMUAT DATASET TRANSAKSI Y-DMS
# ==========================================
df_raw = pd.read_csv(data_path)

print(f"Total Baris Transaksi : {df_raw.shape[0]} baris")
print(f"Total Kolom Awal      : {df_raw.shape[1]} kolom")
print("\n5 Baris Pertama Data Mentah Y-DMS:")
display(df_raw.head())


# --- CELL 4 ---
# ==========================================
# 4.1.2 EKSPLORASI STATISTIK UNIVARIAT 5 DIMENSI
# ==========================================
print("=== 1. TOP 10 MODEL SEPEDA MOTOR (NAMA_BRG) ===")
s_model = df_raw['NAMA_BRG'].value_counts()
display(pd.DataFrame({'Frekuensi': s_model.head(10), 'Persentase (%)': (s_model.head(10)/len(df_raw)*100).round(2)}))

print("\n=== 2. TOP 10 VARIAN WARNA UNIT (WARNA) ===")
s_warna = df_raw['WARNA'].value_counts()
display(pd.DataFrame({'Frekuensi': s_warna.head(10), 'Persentase (%)': (s_warna.head(10)/len(df_raw)*100).round(2)}))

print("\n=== 3. LEMBAGA PEMBIAYAAN / SKEMA PEMBAYARAN ===")
def group_leasing(val):
    if pd.isna(val) or str(val).strip().upper() in ['CASH', 'TUNAI', 'NON LEASING', 'NAN']: return 'CASH'
    val = str(val).upper()
    if 'BAF' in val: return 'BAF'
    if 'ADIRA' in val or 'ADR' in val: return 'ADIRA'
    if 'OTO' in val: return 'OTO'
    if 'MUF' in val or 'MANDIRI' in val: return 'MANDIRI_UTAMA_FINANCE'
    if 'WOM' in val: return 'WOM'
    return 'LAINNYA'
s_lease = df_raw['NMLEASE'].apply(group_leasing).value_counts()
display(pd.DataFrame({'Frekuensi': s_lease, 'Persentase (%)': (s_lease/len(df_raw)*100).round(2)}))

print("\n=== 4. TENOR ANGSURAN PEMBIAYAAN ===")
def group_tenor(val):
    try: t = int(float(val))
    except: return '0_BULAN_CASH'
    if t == 0: return '0_BULAN_CASH'
    elif 1 <= t <= 17: return '11-17_BULAN'
    elif 18 <= t <= 23: return '20-23_BULAN'
    elif 24 <= t <= 32: return '30-32_BULAN'
    elif t >= 33: return '35_BULAN'
    return 'LAINNYA'
s_tenor = df_raw['JK_WAKTU'].apply(group_tenor).value_counts()
display(pd.DataFrame({'Frekuensi': s_tenor, 'Persentase (%)': (s_tenor/len(df_raw)*100).round(2)}))

print("\n=== 5. TOP 10 WILAYAH DOMISILI KONSUMEN ===")
def group_kota(val):
    if pd.isna(val): return 'WILAYAH_LAIN'
    val = str(val).upper().strip()
    if 'BEKASI' in val:
        if 'KAB' in val: return 'KABUPATEN_BEKASI'
        return 'KOTA_BEKASI'
    if 'JAKARTA TIMUR' in val: return 'JAKARTA_TIMUR'
    if 'JAKARTA SELATAN' in val: return 'JAKARTA_SELATAN'
    if 'JAKARTA BARAT' in val: return 'JAKARTA_BARAT'
    if 'JAKARTA PUSAT' in val: return 'JAKARTA_PUSAT'
    if 'JAKARTA UTARA' in val: return 'JAKARTA_UTARA'
    if 'JAKARTA' in val: return 'DKI_JAKARTA_LAIN'
    if 'DEPOK' in val: return 'KOTA_DEPOK'
    if 'BOGOR' in val: return 'BOGOR'
    if 'TANGERANG' in val: return 'TANGERANG'
    return 'WILAYAH_LAIN'
s_kota = df_raw['KOTA'].apply(group_kota).value_counts()
display(pd.DataFrame({'Frekuensi': s_kota.head(10), 'Persentase (%)': (s_kota.head(10)/len(df_raw)*100).round(2)}))


# --- CELL 7 ---
# ==========================================
# 4.2.1 PEMBENTUKAN FITUR STANDAR (DF_CLEAN)
# ==========================================
df_clean = pd.DataFrame()
df_clean['NO_FAKTUR'] = df_raw['NO_FAKTUR'].astype(str).str.strip()
df_clean['Model'] = df_raw['NAMA_BRG'].astype(str).str.upper().str.strip()
df_clean['Warna'] = df_raw['WARNA'].astype(str).str.upper().str.strip()
df_clean['Leasing'] = df_raw['NMLEASE'].apply(group_leasing)
df_clean['Tenor'] = df_raw['JK_WAKTU'].apply(group_tenor)
df_clean['Wilayah'] = df_raw['KOTA'].apply(group_kota)

print("5 Sampel Data Transaksi Setelah Standarisasi (df_clean):")
display(df_clean.head())


# --- CELL 8 ---
# ==========================================
# 4.2.2 TRANSFORMASI KERANJANG PREDIKAT MULTIATRIBUT
# ==========================================
basket_transactions = []
for _, row in df_clean.iterrows():
    basket_items = [
        f"Model={row['Model']}",
        f"Warna={row['Warna']}",
        f"Leasing={row['Leasing']}",
        f"Tenor={row['Tenor']}",
        f"Wilayah={row['Wilayah']}"
    ]
    basket_transactions.append(basket_items)

print(f"Total Keranjang Transaksi Multiatribut Terbentuk: {len(basket_transactions)}")
print("\n5 Sampel Keranjang Predikat Multiatribut Pertama:")
for idx, b in enumerate(basket_transactions[:5], 1):
    print(f"Faktur {idx} ({df_clean['NO_FAKTUR'].iloc[idx-1]}): {b}")


# --- CELL 9 ---
# ==========================================
# 4.2.3 PEMBENTUKAN MATRIKS INSIDENSI BINER (ONE-HOT ENCODING)
# ==========================================
te = TransactionEncoder()
te_ary = te.fit(basket_transactions).transform(basket_transactions)
df_binary = pd.DataFrame(te_ary, columns=te.columns_)

print(f"Dimensi Matriks Biner Akhir: {df_binary.shape[0]} Baris x {df_binary.shape[1]} Kolom Predikat")
print("\nCuplikan 5 Baris Pertama Matriks Insidensi Biner (10 Kolom Predikat):")
display(df_binary.iloc[:5, :10].astype(int))


# --- CELL 11 ---
# ==========================================
# 4.3.1 EKSTRAKSI FREQUENT ITEMSETS (FP-GROWTH)
# ==========================================
# Ambang batas Minimum Support = 2% (0.02)
min_sup = 0.02

# Eksekusi algoritma FP-Growth pada matriks biner
frequent_itemsets = fpgrowth(df_binary, min_support=min_sup, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets = frequent_itemsets.sort_values(by='support', ascending=False).reset_index(drop=True)

print(f"Total Frequent Itemsets yang Lolos Ambang Batas (Min Support {min_sup*100}%): {len(frequent_itemsets)}")
print("\nDistribusi Panjang Pola Frekuensi Tinggi (k-itemset):")
display(frequent_itemsets['length'].value_counts().sort_index().rename('Jumlah Pola'))

print("\nTop 15 Frequent Itemsets Tertinggi Berdasarkan Support:")
display(frequent_itemsets.head(15))


# --- CELL 13 ---
# ==========================================
# 4.4.1 PEMBENTUKAN KAIDAH ASOSIASI & FILTER TRI-METRIK
# ==========================================
# Ambang batas Minimum Confidence = 50% (0.50)
min_conf = 0.50

# Pembangkitan kaidah asosiasi
raw_rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=min_conf)

# Standar Validasi Tri-Metrik: Hanya pertahankan kaidah dengan Lift Ratio > 1.0 (korelasi positif nyata)
valid_rules = raw_rules[raw_rules['lift'] > 1.0].sort_values(by='lift', ascending=False).reset_index(drop=True)

print(f"Total Kaidah Asosiasi Mentah Terbentuk (Confidence >= {min_conf*100}%): {len(raw_rules)}")
print(f"Total Kaidah Lolos Validasi Ilmiah (Lift Ratio > 1.0)               : {len(valid_rules)}")
print(f"Total Kaidah Gugur / Non-Korelasi (Lift Ratio <= 1.0)              : {len(raw_rules) - len(valid_rules)}")


# --- CELL 15 ---
# ==========================================
# 4.4.3 KATEGORISASI KLASTER MANAJERIAL KAIDAH ASOSIASI
# ==========================================
def classify_rule(row):
    ant = ' '.join(list(row['antecedents']))
    con = ' '.join(list(row['consequents']))
    all_str = ant + ' ' + con
    has_model = 'Model=' in all_str
    has_finance = ('Leasing=' in all_str) or ('Tenor=' in all_str)
    has_warna = 'Warna=' in all_str
    has_wilayah = 'Wilayah=' in all_str
    
    if has_model and has_finance and not has_warna and not has_wilayah:
        return 'Klaster Finansial & Pembiayaan'
    elif has_model and has_warna and not has_finance:
        return 'Klaster Persediaan & Warna'
    elif has_wilayah:
        return 'Klaster Geo-Marketing Spasial'
    elif has_finance and has_warna:
        return 'Klaster Multi-Atribut Kompleks'
    return 'Klaster Umum'

valid_rules['klaster'] = valid_rules.apply(classify_rule, axis=1)

print("Distribusi Jumlah Kaidah Asosiasi Berdasarkan Klaster Manajerial:")
display(valid_rules['klaster'].value_counts().rename('Jumlah Kaidah'))


# --- CELL 16 ---
# ==========================================
# 4.4.4 REKAPITULASI TOP 20 KAIDAH ASOSIASI TERKUAT (LIFT TERTINGGI)
# ==========================================
top_20_rules = valid_rules[['antecedents', 'consequents', 'support', 'confidence', 'lift', 'klaster']].head(20).copy()
top_20_rules['Antecedents (X)'] = top_20_rules['antecedents'].apply(lambda x: ', '.join(list(x)))
top_20_rules['Consequents (Y)'] = top_20_rules['consequents'].apply(lambda x: ', '.join(list(x)))
top_20_rules['Support (%)'] = (top_20_rules['support'] * 100).round(2).astype(str) + '%'
top_20_rules['Confidence (%)'] = (top_20_rules['confidence'] * 100).round(2).astype(str) + '%'
top_20_rules['Lift Ratio'] = top_20_rules['lift'].round(3)

display_top_20 = top_20_rules[['Antecedents (X)', 'Consequents (Y)', 'Support (%)', 'Confidence (%)', 'Lift Ratio', 'klaster']]
print("=== TABEL 4.11: TOP 20 KAIDAH ASOSIASI TERKUAT VALIDASI TRI-METRIK ===")
display(display_top_20)

# Ekspor ke file CSV untuk Bab IV
csv_rules_path = 'top_20_association_rules_evaluasi.csv'
display_top_20.to_csv(csv_rules_path, index=False)
print(f"File CSV Kaidah Evaluasi berhasil disimpan di: {csv_rules_path}")


# --- CELL 18 ---
# ==========================================
# 4.5.1 SIMULASI REKOMENDASI MANAJEMEN PERSEDIAAN (INVENTORY ALLOCATION)
# ==========================================
# Ekstraksi probabilitas bersyarat P(Warna | Model) untuk model terlaris
top_models = ['AEROX ALPHA', 'MIO M3 CW', 'GEAR 125', 'NMAX NEO S', 'FAZZIO HYBRID']
inventory_allocation = []

for m in top_models:
    sub = df_clean[df_clean['Model'] == m]
    warna_counts = sub['Warna'].value_counts()
    for w, count in warna_counts.head(3).items():
        ratio = count / len(sub) * 100
        inventory_allocation.append({
            'Model Sepeda Motor': m,
            'Varian Warna': w,
            'Frekuensi Terjual': count,
            'Rasio Alokasi Rekomendasi (%)': round(ratio, 2),
            'Status Pengadaan Gudang': 'Prioritas Utama (Fast-Moving)' if ratio >= 30 else 'Penyeimbang Stok'
        })

df_inventory_rec = pd.DataFrame(inventory_allocation)
print("=== TABEL 4.12: MATRIKS SIMULASI REKOMENDASI ALOKASI PENGADAAN PERSEDIAAN GUDANG ===")
display(df_inventory_rec)

# Visualisasi Alokasi Warna per Model dengan Palet Warna Riil Sepeda Motor
warna_inventory_palette = {
    'HITAM': '#212121',        # Hitam Pekat Glossy / Matte
    'BIRU': '#1565C0',         # Biru Khas Yamaha Racing
    'MERAH': '#C62828',        # Merah Sporty
    'PUTIH': '#ECEFF1',        # Putih Pearl / Mutiara
    'ABU PINK': '#F48FB1',     # Pastel Rose / Abu Pink (Fazzio Hybrid)
    'HITAM MERAH': '#880E4F',  # Varian Two-Tone Hitam Aksen Merah
    'BIRU PUTIH': '#4FC3F7',   # Varian Two-Tone Biru Putih Pastel
    'PERAK HIJAU': '#80CBC4',  # Mint Green / Perak Hijau (Mio M3)
    'HIJAU PERAK': '#AED581'   # Sage Silver / Hijau Perak (Gear 125)
}

plt.figure(figsize=(14, 6.5))
bar_plot = sns.barplot(
    data=df_inventory_rec, 
    x='Model Sepeda Motor', 
    y='Rasio Alokasi Rekomendasi (%)', 
    hue='Varian Warna', 
    palette=warna_inventory_palette, 
    edgecolor='black', 
    linewidth=0.8
)
plt.title('Rekomendasi Rasio Alokasi Persediaan Varian Warna per Model Motor (Mitigasi Dead Stock)', fontsize=13, fontweight='bold')
plt.ylabel('Rasio Alokasi Pengadaan (%)', fontsize=11)
plt.xlabel('Model Sepeda Motor', fontsize=11)
plt.ylim(0, 105)

# Menambahkan label persentase di atas setiap batang
for p in bar_plot.patches:
    height = p.get_height()
    if not np.isnan(height) and height > 0:
        bar_plot.annotate(f'{height:.1f}%',
                          (p.get_x() + p.get_width() / 2., height + 1.5),
                          ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.legend(title='Varian Warna (Warna Riil)', bbox_to_anchor=(1.02, 1), loc='upper left', frameon=True, edgecolor='black')
plt.tight_layout()
plt.savefig('visualisasi_4_5_alokasi_persediaan.png', dpi=300)
plt.show()
print("Grafik Persediaan 4.5 berhasil disimpan: visualisasi_4_5_alokasi_persediaan.png")


# --- CELL 19 ---
# ==========================================
# 4.5.2 SIMULASI STRATEGI PENJUALAN TERPADU (SMART SALES SCRIPT MATRIX)
# ==========================================
# Menghubungkan Model Terlaris dengan Preferensi Pembiayaan Tertinggi
sales_script_data = []

for m in top_models:
    sub = df_clean[df_clean['Model'] == m]
    top_lease = sub['Leasing'].value_counts().index[0]
    top_lease_pct = (sub['Leasing'].value_counts().iloc[0] / len(sub)) * 100
    
    # Ambil tenor terpopuler jika kredit, atau cash
    sub_credit = sub[sub['Leasing'] != 'CASH']
    if len(sub_credit) > 0:
        top_tenor = sub_credit['Tenor'].value_counts().index[0]
        top_tenor_pct = (sub_credit['Tenor'].value_counts().iloc[0] / len(sub_credit)) * 100
    else:
        top_tenor = '0_BULAN_CASH'
        top_tenor_pct = 100.0
        
    sales_script_data.append({
        'Model Diminati Konsumen': m,
        'Skema / Leasing Utama': f"{top_lease} ({top_lease_pct:.1f}%)",
        'Rekomendasi Tenor Cicilan': f"{top_tenor} ({top_tenor_pct:.1f}% kredit)",
        'Rekomendasi Bundling / Action Script': f"Tawarkan promo uang muka rendah BAF tenor 30-35 bulan & bonus aksesoris resmi." if top_lease == 'BAF' else "Berikan opsi diskon tunai langsung atau asuransi gratis."
    })

df_sales_script = pd.DataFrame(sales_script_data)
print("=== TABEL 4.13: SMART SALES SCRIPT & PROMOTIONAL BUNDLING MATRIX ===")
display(df_sales_script)
df_sales_script.to_csv('matriks_smart_sales_script.csv', index=False)


# --- CELL 20 ---
# ==========================================
# 4.5.3 SIMULASI STRATEGI PEMASARAN SPASIAL (GEO-MARKETING STRATEGY)
# ==========================================
# Proporsi Penjualan Model Terlaris di 2 Koridor Utama: Bekasi Raya vs DKI Jakarta Raya
def simplify_region(kota):
    if 'BEKASI' in kota: return 'Kawasan Bekasi Raya'
    elif 'JAKARTA' in kota: return 'Kawasan DKI Jakarta Raya'
    elif 'TANGERANG' in kota: return 'Kawasan Tangerang'
    return 'Kawasan Lain'

df_clean['Region_Cluster'] = df_clean['Wilayah'].apply(simplify_region)

geo_matrix = pd.crosstab(df_clean['Model'], df_clean['Region_Cluster'], normalize='index') * 100
geo_matrix_top = geo_matrix.loc[top_models].round(2)

print("=== TABEL 4.14: MATRIKS DISTRIBUSI MODEL BERBASIS KAWASAN KONSUMEN (GEO-MARKETING %) ===")
display(geo_matrix_top)

# Visualisasi Heatmap Geo-Marketing
plt.figure(figsize=(10, 5))
sns.heatmap(geo_matrix_top, annot=True, fmt='.1f', cmap='YlGnBu', cbar_kws={'label': 'Proporsi Penjualan per Model (%)'}, linewidths=0.5)
plt.title('Matriks Penetrasi Model Kendaraan Berdasarkan Wilayah Konsumen (Geo-Marketing Heatmap)', fontsize=12, fontweight='bold')
plt.xlabel('Kawasan Aglomerasi')
plt.ylabel('Model Sepeda Motor')
plt.tight_layout()
plt.savefig('visualisasi_4_5_geo_marketing.png', dpi=300)
plt.show()
print("Grafik Geo-Marketing 4.5 berhasil disimpan: visualisasi_4_5_geo_marketing.png")

