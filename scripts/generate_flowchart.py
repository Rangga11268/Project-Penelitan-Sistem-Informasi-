import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Set font and figure settings
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9.5

fig, ax = plt.subplots(figsize=(8.5, 11), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Color palette (Academic Navy & Modern Clean)
c_start_end = '#1E3A8A'      # Deep Navy
c_stage_box = '#F8FAFC'      # Off white / light slate
c_border    = '#3B82F6'      # Tech Blue border
c_highlight = '#0284C7'      # Vibrant Sky Blue
c_text_dark = '#0F172A'      # Dark Slate for text
c_text_sub  = '#475569'      # Slate for subtext
c_arrow     = '#2563EB'      # Blue arrow

# Stages data
stages = [
    {
        "y": 13.0, "h": 0.65, "w": 4.0,
        "type": "terminal",
        "title": "Mulai",
        "desc": ""
    },
    {
        "y": 11.4, "h": 1.1, "w": 7.8,
        "type": "process",
        "stage_num": "Tahap 1: Pemahaman Bisnis (Business Understanding)",
        "items": [
            "- Identifikasi masalah penawaran kredit & ketidakseimbangan stok di PT. SSM",
            "- Perumusan sasaran: Pola multi-atribut (model, warna, leasing, tenor, wilayah)"
        ]
    },
    {
        "y": 9.6, "h": 1.1, "w": 7.8,
        "type": "process",
        "stage_num": "Tahap 2: Pemahaman Data (Data Understanding)",
        "items": [
            "- Ekstraksi data sekunder dari Yamaha Dealer Management System (Y-DMS)",
            "- Akuisisi 3.113 data faktur penjualan unit motor baru (Juni - Agustus 2026)"
        ]
    },
    {
        "y": 7.8, "h": 1.1, "w": 7.8,
        "type": "process",
        "stage_num": "Tahap 3: Persiapan Data (Data Preparation)",
        "items": [
            "- Pembersihan data (penanganan missing values & verifikasi faktur valid)",
            "- Anonimisasi data privasi konsumen & transformasi biner (One-Hot Encoding)"
        ]
    },
    {
        "y": 6.0, "h": 1.1, "w": 7.8,
        "type": "process",
        "stage_num": "Tahap 4: Pemodelan Data Mining (Modeling FP-Growth)",
        "items": [
            "- Peringkasan basis data ke struktur pohon FP-Tree di memori (2 scan)",
            "- Penambangan rekursif Conditional Pattern Base tanpa pembangkitan kandidat"
        ]
    },
    {
        "y": 4.2, "h": 1.1, "w": 7.8,
        "type": "process",
        "stage_num": "Tahap 5: Evaluasi Kaidah Asosiasi (Evaluation)",
        "items": [
            "- Pengujian Standar Validasi Tiga Metrik: Support, Confidence, dan Lift Ratio",
            "- Seleksi aturan valid dengan Lift Ratio > 1,0 (korelasi positif nyata)"
        ]
    },
    {
        "y": 2.4, "h": 1.1, "w": 7.8,
        "type": "process",
        "stage_num": "Tahap 6: Perumusan Rekomendasi Preskriptif (Deployment)",
        "items": [
            "- Perumusan strategi bundling produk-pembiayaan (Motor + DP/Tenor Leasing)",
            "- Optimalisasi alokasi stok warna/varian per cabang dealer Jabodetabek"
        ]
    },
    {
        "y": 0.9, "h": 0.65, "w": 4.0,
        "type": "terminal",
        "title": "Selesai",
        "desc": ""
    }
]

# Draw boxes and connectors
for i, stage in enumerate(stages):
    x_center = 5.0
    y_center = stage["y"]
    w = stage["w"]
    h = stage["h"]
    
    if stage["type"] == "terminal":
        # Rounded capsule
        box = patches.FancyBboxPatch(
            (x_center - w/2, y_center - h/2), w, h,
            boxstyle="round,pad=0.2,rounding_size=0.3",
            facecolor=c_start_end, edgecolor=c_start_end,
            linewidth=2, zorder=3
        )
        ax.add_patch(box)
        ax.text(x_center, y_center, stage["title"], ha='center', va='center',
                color='white', fontweight='bold', fontsize=11, zorder=4)
    else:
        # Process card
        box = patches.FancyBboxPatch(
            (x_center - w/2, y_center - h/2), w, h,
            boxstyle="round,pad=0.15,rounding_size=0.15",
            facecolor=c_stage_box, edgecolor=c_border,
            linewidth=1.8, zorder=3
        )
        ax.add_patch(box)
        
        # Header banner inside card
        header_y = y_center + h/2 - 0.28
        ax.text(x_center - w/2 + 0.35, header_y, stage["stage_num"],
                ha='left', va='center', color=c_start_end, fontweight='bold', fontsize=10, zorder=4)
        
        # Horizontal subtle divider line
        ax.plot([x_center - w/2 + 0.3, x_center + w/2 - 0.3], [header_y - 0.16, header_y - 0.16],
                color='#CBD5E1', linewidth=1, zorder=4)
        
        # Content bullet points
        line_y1 = header_y - 0.38
        line_y2 = header_y - 0.62
        ax.text(x_center - w/2 + 0.45, line_y1, stage["items"][0],
                ha='left', va='center', color=c_text_dark, fontsize=8.5, zorder=4)
        ax.text(x_center - w/2 + 0.45, line_y2, stage["items"][1],
                ha='left', va='center', color=c_text_dark, fontsize=8.5, zorder=4)
        
    # Draw arrow to next stage
    if i < len(stages) - 1:
        next_stage = stages[i+1]
        arrow_start_y = y_center - h/2
        arrow_end_y = next_stage["y"] + next_stage["h"]/2
        ax.annotate(
            '', xy=(5.0, arrow_end_y), xytext=(5.0, arrow_start_y),
            arrowprops=dict(
                arrowstyle='->,head_width=0.35,head_length=0.45',
                color=c_arrow, lw=2.0
            ),
            zorder=2
        )

# Save the figure to both locations
out_dir1 = r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR"
out_dir2 = r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\02_Publikasi_Jurnal_JUTISI"

out_path1 = os.path.join(out_dir1, "bagan_alir_penelitian.png")
out_path2 = os.path.join(out_dir2, "bagan_alir_penelitian.png")

plt.tight_layout()
plt.savefig(out_path1, dpi=300, bbox_inches='tight')
plt.savefig(out_path2, dpi=300, bbox_inches='tight')
plt.close()

print(f"Flowchart successfully generated at:\n1. {out_path1}\n2. {out_path2}")
