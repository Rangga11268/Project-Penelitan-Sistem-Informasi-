import pandas as pd
import numpy as np
import os

def clean_and_prepare_pharmacy_dataset():
    input_path = 'datasets/02_DATASET_CADANGAN_REFERENSI/pharmacy_dataset_csv/DATASET_TRANSAKSI_FARMASI_INDONESIA_CLEAN.csv'
    output_dir = 'datasets/02_DATASET_CADANGAN_REFERENSI/pharmacy_clean_for_training'
    os.makedirs(output_dir, exist_ok=True)
    
    print("1. Loading raw merged pharmacy dataset...")
    df = pd.read_csv(input_path, low_memory=False)
    print(f"   Initial rows: {len(df):,}")
    
    # Clean column names & drop NaN in medicine name or receipt
    print("2. Cleaning missing values and anomalous rows...")
    df = df.dropna(subset=['NO_RESEP', 'NAMA']).copy()
    df['NAMA'] = df['NAMA'].astype(str).str.strip()
    df = df[df['NAMA'] != '']
    df = df[~df['NAMA'].str.lower().isin(['nan', 'null', 'none', '-'])]
    
    # Clean QTY & Price
    df['QTY'] = pd.to_numeric(df['QTY'], errors='coerce').fillna(1.0)
    df = df[df['QTY'] > 0]
    df['HJ'] = pd.to_numeric(df['HJ'], errors='coerce').fillna(0.0)
    df['TOTAL_RP'] = (df['QTY'] * df['HJ']).round(2)
    
    # Format Date
    df['TGL'] = pd.to_datetime(df['TGL'], errors='coerce').dt.strftime('%Y-%m-%d').fillna('2015-01-01')
    
    # Determine Service Type (TIPE_LAYANAN) from NO_RESEP prefix
    def get_service_type(no_resep):
        prefix = str(no_resep)[:2].upper()
        if prefix == 'RJ':
            return 'Rawat Jalan'
        elif prefix == 'RI':
            return 'Rawat Inap'
        elif prefix == 'UM':
            return 'Penjualan Umum / Bebas'
        else:
            return 'Layanan Lainnya'
            
    df['TIPE_LAYANAN'] = df['NO_RESEP'].apply(get_service_type)
    
    # Format Racik status
    df['STATUS_RACIKAN'] = df['RACIK'].apply(lambda x: 'Racikan' if str(x).upper() == 'Y' else 'Non-Racikan')
    
    # Standardize Unit (SATUAN)
    df['SAT_JUAL'] = df['SAT_JUAL'].astype(str).str.strip().str.lower()
    unit_map = {
        'tab': 'Tablet', 'kaps': 'Kapsul', 'amp': 'Ampul', 'vial': 'Vial',
        'btl': 'Botol', 'kalf': 'Kolf/Infus', 'strip': 'Strip', 'tube': 'Tube',
        'pcs': 'Pcs', 'sach': 'Sachet', 'fls': 'Flakon'
    }
    df['SATUAN'] = df['SAT_JUAL'].map(unit_map).fillna(df['SAT_JUAL'].str.capitalize())
    
    # Rename & select readable columns
    df_clean_long = df[[
        'NO_RESEP', 'TGL', 'TIPE_LAYANAN', 'NAMA', 'SATUAN', 
        'QTY', 'HJ', 'TOTAL_RP', 'STATUS_RACIKAN'
    ]].copy()
    
    df_clean_long.columns = [
        'NOMOR_RESEP', 'TANGGAL_TRANSAKSI', 'TIPE_LAYANAN', 'NAMA_OBAT', 
        'SATUAN', 'JUMLAH_QTY', 'HARGA_SATUAN_RP', 'TOTAL_HARGA_RP', 'STATUS_RACIKAN'
    ]
    
    # Deduplicate items inside same receipt (sum QTY & total price)
    df_clean_long = df_clean_long.groupby(
        ['NOMOR_RESEP', 'TANGGAL_TRANSAKSI', 'TIPE_LAYANAN', 'NAMA_OBAT', 'SATUAN', 'STATUS_RACIKAN'],
        as_index=False
    ).agg({'JUMLAH_QTY': 'sum', 'HARGA_SATUAN_RP': 'first', 'TOTAL_HARGA_RP': 'sum'})
    
    file_long = os.path.join(output_dir, '01_DATASET_FARMASI_TRANSAKSI_LENGKAP.csv')
    df_clean_long.to_csv(file_long, index=False, encoding='utf-8')
    print(f"   -> [Saved] Long Transaction Dataset: {len(df_clean_long):,} rows to {file_long}")
    
    # 3. Create Market Basket format (One row per receipt)
    print("3. Building Market Basket Dataset (1 Row = 1 Struk Resep)...")
    basket_grouped = df_clean_long.groupby('NOMOR_RESEP').agg({
        'TANGGAL_TRANSAKSI': 'first',
        'TIPE_LAYANAN': 'first',
        'STATUS_RACIKAN': 'first',
        'TOTAL_HARGA_RP': 'sum',
        'NAMA_OBAT': lambda items: ' | '.join(sorted(list(set(items)))),
        'JUMLAH_QTY': 'count' # distinct item count
    }).reset_index()
    
    basket_grouped.columns = [
        'NOMOR_RESEP', 'TANGGAL_TRANSAKSI', 'TIPE_LAYANAN', 'STATUS_RACIKAN',
        'TOTAL_BIAYA_RESEP_RP', 'DAFTAR_OBAT_KERANJANG', 'JUMLAH_JENIS_OBAT'
    ]
    
    file_basket_all = os.path.join(output_dir, '02_DATASET_FARMASI_MARKET_BASKET_SEMUA.csv')
    basket_grouped.to_csv(file_basket_all, index=False, encoding='utf-8')
    print(f"   -> [Saved] All Basket Dataset: {len(basket_grouped):,} receipts to {file_basket_all}")
    
    # 4. Filter for Multi-Item Receipts (>= 2 items) specifically for Association Training
    print("4. Filtering Multi-Item Baskets (>= 2 items) for FP-Growth Training...")
    basket_train = basket_grouped[basket_grouped['JUMLAH_JENIS_OBAT'] >= 2].copy()
    
    file_train = os.path.join(output_dir, '03_DATASET_FARMASI_TRAIN_FP_GROWTH_MULTI_ITEM.csv')
    basket_train.to_csv(file_train, index=False, encoding='utf-8')
    print(f"   -> [Saved] FP-Growth Training Dataset: {len(basket_train):,} multi-item receipts to {file_train}")
    
    print("\n[SUCCESS] Cleaning and preparation completed successfully!")

if __name__ == '__main__':
    clean_and_prepare_pharmacy_dataset()
