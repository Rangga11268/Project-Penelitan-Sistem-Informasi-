import re
import csv
import os

def parse_sql_dump(sql_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    print(f"Reading SQL file: {sql_file}...")
    
    # We will read line-by-line or chunk-by-chunk to be fast and memory efficient
    table_files = {}
    table_counts = {}
    
    # Open files for appending
    def get_csv_writer(table_name, columns):
        if table_name not in table_files:
            csv_path = os.path.join(output_dir, f"{table_name}.csv")
            f = open(csv_path, 'w', newline='', encoding='utf-8')
            writer = csv.writer(f)
            writer.writerow(columns)
            table_files[table_name] = (f, writer)
            table_counts[table_name] = 0
        return table_files[table_name][1]

    # Regex patterns
    insert_pattern = re.compile(r"INSERT INTO `(\w+)` \((.*?)\) VALUES\s*(.*)", re.IGNORECASE)
    row_pattern = re.compile(r"\(((?:'[^']*'|[^,)]+)(?:,\s*(?:'[^']*'|[^,)]+))*)\)")

    print("Extracting SQL statements into CSV...")
    with open(sql_file, 'r', encoding='utf-8', errors='ignore') as sf:
        buffer = []
        in_insert = False
        current_table = None
        current_cols = None
        
        for line in sf:
            if 'INSERT INTO' in line:
                m = insert_pattern.search(line)
                if m:
                    in_insert = True
                    current_table = m.group(1)
                    cols_raw = m.group(2)
                    current_cols = [c.strip().strip('`') for c in cols_raw.split(',')]
                    remainder = m.group(3)
                    buffer = [remainder]
                    if remainder.strip().endswith(';'):
                        in_insert = False
                        # process buffer
                        full_val_str = ''.join(buffer)
                        writer = get_csv_writer(current_table, current_cols)
                        for rm in row_pattern.finditer(full_val_str):
                            row_items = list(csv.reader([rm.group(1)], quotechar="'", skipinitialspace=True))[0]
                            writer.writerow(row_items)
                            table_counts[current_table] += 1
                        buffer = []
                continue
                
            if in_insert:
                buffer.append(line)
                if line.strip().endswith(';'):
                    in_insert = False
                    full_val_str = ''.join(buffer)
                    writer = get_csv_writer(current_table, current_cols)
                    for rm in row_pattern.finditer(full_val_str):
                        row_items = list(csv.reader([rm.group(1)], quotechar="'", skipinitialspace=True))[0]
                        writer.writerow(row_items)
                        table_counts[current_table] += 1
                    buffer = []

    # Close all files
    for tname, (f, _) in table_files.items():
        f.close()
        print(f"-> Table '{tname}': {table_counts[tname]:,} total rows exported.")

    # Create a joined clean transaction table with medicine names
    print("\nCreating joined pharmacy transaction dataset (NO_RESEP + NAMA_OBAT)...")
    create_joined_dataset(output_dir)

def create_joined_dataset(output_dir):
    import pandas as pd
    
    prod_path = os.path.join(output_dir, "ms_product.csv")
    det_path = os.path.join(output_dir, "det_sales.csv")
    sales_path = os.path.join(output_dir, "ms_sales.csv")
    
    if os.path.exists(prod_path) and os.path.exists(det_path):
        df_prod = pd.read_csv(prod_path, dtype=str)
        df_det = pd.read_csv(det_path, dtype=str)
        
        # Merge det_sales with ms_product to get medicine names
        df_merged = df_det.merge(df_prod[['KD_OBAT', 'NAMA', 'SAT_JUAL']], on='KD_OBAT', how='left')
        
        if os.path.exists(sales_path):
            df_sales = pd.read_csv(sales_path, dtype=str)
            df_merged = df_merged.merge(df_sales[['NO_RESEP', 'TGL', 'RACIK']], on='NO_RESEP', how='left')
            
        out_joined = os.path.join(output_dir, "DATASET_TRANSAKSI_FARMASI_INDONESIA_CLEAN.csv")
        df_merged.to_csv(out_joined, index=False, encoding='utf-8')
        print(f"-> Saved clean joined dataset with {len(df_merged):,} rows to: {out_joined}")

if __name__ == '__main__':
    sql_path = 'datasets/02_DATASET_CADANGAN_REFERENSI/2ym7v78wtd-1/extracted/sales.sql'
    out_dir = 'datasets/02_DATASET_CADANGAN_REFERENSI/pharmacy_dataset_csv'
    parse_sql_dump(sql_path, out_dir)
