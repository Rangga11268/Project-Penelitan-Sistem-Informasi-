import pandas as pd
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import re
import os

def clean_excel_text(val):
    if pd.isna(val) or val is None:
        return ""
    # Remove control characters not allowed by Excel XML
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', str(val))

def generate_formatted_excel():
    csv_long_path = 'datasets/02_DATASET_CADANGAN_REFERENSI/pharmacy_clean_for_training/01_DATASET_FARMASI_TRANSAKSI_LENGKAP.csv'
    csv_basket_path = 'datasets/02_DATASET_CADANGAN_REFERENSI/pharmacy_clean_for_training/03_DATASET_FARMASI_TRAIN_FP_GROWTH_MULTI_ITEM.csv'
    
    excel_out_path = 'datasets/02_DATASET_CADANGAN_REFERENSI/DATASET_FARMASI_INDONESIA_RAPI_DAN_MUDAH_DIBACA.xlsx'
    
    print("1. Membaca data CSV yang sudah dibersihkan...")
    df_long = pd.read_csv(csv_long_path, low_memory=False)
    df_basket = pd.read_csv(csv_basket_path, low_memory=False)
    
    # Bersihkan karakter anomali dari string
    for col in df_long.select_dtypes(include='object').columns:
        df_long[col] = df_long[col].apply(clean_excel_text)
        
    for col in df_basket.select_dtypes(include='object').columns:
        df_basket[col] = df_basket[col].apply(clean_excel_text)
    
    # 1. Sheet Ringkasan Statistik
    print("2. Menyusun Sheet Ringkasan Statistik & Top Obat...")
    top_meds = df_long['NAMA_OBAT'].value_counts().reset_index()
    top_meds.columns = ['NAMA_OBAT', 'TOTAL_DITEBUS']
    top_meds['PERSENTASE_KETERSEDIAAN'] = ((top_meds['TOTAL_DITEBUS'] / len(df_basket)) * 100).round(2).astype(str) + '%'
    
    stats_data = [
        ["Nama Dataset", "Retail Sales Dataset of a Pharmacy in Indonesia (Mendeley Data DOI: 10.17632/2ym7v78wtd.1)"],
        ["Peneliti Asal", "Dr. Rendra Gustriansyah (Lisensi Terbuka CC BY 4.0)"],
        ["Total Detail Transaksi Obat", f"{len(df_long):,} baris transaksi"],
        ["Total Struk Resep (Semua)", f"{df_long['NOMOR_RESEP'].nunique():,} resep unik"],
        ["Total Resep Multi-Item (>= 2 Obat)", f"{len(df_basket):,} keranjang resep"],
        ["Total Varian Obat Unik", f"{df_long['NAMA_OBAT'].nunique():,} jenis obat"],
        ["Rata-rata Obat per Resep", f"{(len(df_long)/df_long['NOMOR_RESEP'].nunique()):.2f} obat per resep"],
        ["Jenis Layanan Pasien", "Rawat Jalan (RJ), Rawat Inap (RI), Penjualan Umum Bebas (UM)"],
        ["Metode Data Mining Cocok", "Association Rule Mining (FP-Growth / Apriori / Market Basket Analysis)"]
    ]
    df_stats = pd.DataFrame(stats_data, columns=["Indikator Metadata", "Keterangan"])
    
    # 2. Master Obat Katalog
    df_catalog = df_long.groupby(['NAMA_OBAT', 'SATUAN'], as_index=False).agg({
        'HARGA_SATUAN_RP': 'first',
        'JUMLAH_QTY': 'sum',
        'NOMOR_RESEP': 'nunique'
    }).rename(columns={
        'HARGA_SATUAN_RP': 'HARGA_SATUAN_RP',
        'JUMLAH_QTY': 'TOTAL_QTY_TERJUAL',
        'NOMOR_RESEP': 'TOTAL_RESEP_MENGANDUNG_OBAT'
    }).sort_values(by='TOTAL_RESEP_MENGANDUNG_OBAT', ascending=False)
    
    # Ambil sampel representatif rapi (5.000 resep & 10.000 baris item) agar Excel enteng dibuka di semua laptop
    df_basket_sample = df_basket.head(5000).copy()
    df_long_sample = df_long.head(10000).copy()
    
    print("3. Menulis ke Excel Workbook (.xlsx)...")
    with pd.ExcelWriter(excel_out_path, engine='openpyxl') as writer:
        df_stats.to_excel(writer, sheet_name='Ringkasan_Dataset', index=False)
        top_meds.head(50).to_excel(writer, sheet_name='Top_50_Obat_Terlaris', index=False)
        df_basket_sample.to_excel(writer, sheet_name='Keranjang_Resep_Multi_Item', index=False)
        df_long_sample.to_excel(writer, sheet_name='Detail_Transaksi_Obat', index=False)
        df_catalog.head(1000).to_excel(writer, sheet_name='Katalog_Master_Obat', index=False)
        
    print("4. Menerapkan gaya visual (Header biru, border, auto-width, format angka)...")
    wb = openpyxl.load_workbook(excel_out_path)
    
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        ws.views.sheetView[0].showGridLines = True
        
        # Style Header (Row 1)
        for cell in ws[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            
        # Style data rows
        for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
            for cell in row:
                cell.border = thin_border
                cell.font = Font(name="Calibri", size=10)
                
                # Alignments & formats
                col_header = str(ws.cell(row=1, column=cell.column).value)
                if isinstance(cell.value, (int, float)):
                    if "HARGA" in col_header or "BIAYA" in col_header or "RP" in col_header:
                        cell.number_format = '#,##0'
                        cell.alignment = Alignment(horizontal="right", vertical="center")
                    else:
                        cell.alignment = Alignment(horizontal="right", vertical="center")
                else:
                    cell.alignment = Alignment(horizontal="left", vertical="center")

        # Auto-adjust column widths
        for col in ws.columns:
            max_len = 0
            col_letter = get_column_letter(col[0].column)
            for cell in col:
                val = str(cell.value or '')
                if len(val) > max_len:
                    max_len = len(val)
            ws.column_dimensions[col_letter].width = min(max(max_len + 4, 12), 65)
            
    wb.save(excel_out_path)
    print(f"-> [SELESAI] File Excel Berhasil Disimpan: {excel_out_path}")

if __name__ == '__main__':
    generate_formatted_excel()
