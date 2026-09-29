import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
import time
import os

def run_pharmacy_fp_growth_training():
    data_path = 'datasets/02_DATASET_CADANGAN_REFERENSI/pharmacy_clean_for_training/03_DATASET_FARMASI_TRAIN_FP_GROWTH_MULTI_ITEM.csv'
    results_dir = 'datasets/02_DATASET_CADANGAN_REFERENSI/pharmacy_training_results'
    os.makedirs(results_dir, exist_ok=True)
    
    print("=================================================================")
    print("   TRAINING FP-GROWTH ASSOCIATION RULE MINING (PHARMACY DATA)    ")
    print("=================================================================")
    
    print("\n1. Membaca dataset keranjang transaksi farmasi...")
    df = pd.read_csv(data_path)
    print(f"   Total Transaksi Multi-Item: {len(df):,} resep.")
    
    # Parse items list per transaction
    transactions = [items.split(' | ') for items in df['DAFTAR_OBAT_KERANJANG']]
    
    print("\n2. Melakukan One-Hot Encoding (TransactionEncoder)...")
    start_time = time.time()
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
    encoding_time = time.time() - start_time
    print(f"   Dimensi Matriks: {df_encoded.shape[0]:,} transaksi x {df_encoded.shape[1]:,} jenis obat unik.")
    print(f"   Waktu Encoding: {encoding_time:.2f} detik.")
    
    # Run FP-Growth
    min_support = 0.005 # 0.5% (muncul minimal di ~622 resep)
    print(f"\n3. Menjalankan Algoritma FP-Growth (Minimum Support = {min_support*100}%)...")
    fpg_start = time.time()
    frequent_itemsets = fpgrowth(df_encoded, min_support=min_support, use_colnames=True)
    fpg_time = time.time() - fpg_start
    print(f"   Ditemukan {len(frequent_itemsets):,} Frequent Itemset.")
    print(f"   Waktu Komputasi FP-Growth: {fpg_time:.2f} detik.")
    
    # Generate Association Rules
    min_confidence = 0.15 # 15%
    print(f"\n4. Membangun Association Rules (Minimum Confidence = {min_confidence*100}%)...")
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    rules['antecedents_str'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
    rules['consequents_str'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))
    
    # Filter rules with lift > 1.0 (valid positive correlation)
    strong_rules = rules[rules['lift'] > 1.0].sort_values(by='lift', ascending=False).reset_index(drop=True)
    print(f"   Dihasilkan {len(strong_rules):,} Aturan Asosiasi Kuat (Lift Ratio > 1.0).")
    
    # Save results to CSV
    rules_out = os.path.join(results_dir, 'HASIL_ASSOCIATION_RULES_FARMASI_FP_GROWTH.csv')
    strong_rules.to_csv(rules_out, index=False, encoding='utf-8')
    print(f"\n-> Hasil Aturan Lengkap Disimpan di: {rules_out}")
    
    # Display Top 15 Rules
    print("\n" + "="*85)
    print("                TOP 15 ATURAN ASOSIASI KOMBINASI OBAT TERBAIK (LIFT TERTINGGI)")
    print("="*85)
    
    top15 = strong_rules[['antecedents_str', 'consequents_str', 'support', 'confidence', 'lift']].head(15)
    for idx, row in top15.iterrows():
        print(f"Rule #{idx+1:02d}:")
        print(f"   JIKA PASIEN MENEBUS : [{row['antecedents_str']}]")
        print(f"   MAKA JUGA MENEBUS   : [{row['consequents_str']}]")
        print(f"   Support: {row['support']*100:.2f}% | Confidence: {row['confidence']*100:.2f}% | Lift Ratio: {row['lift']:.2f}")
        print("-" * 85)
        
    print("\n[SUCCESS] Pelatihan Model Asosiasi Berhasil dengan Kualitas Sangat Tinggi!")

if __name__ == '__main__':
    run_pharmacy_fp_growth_training()
