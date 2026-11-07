import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil

# Matplotlib configuration for publication-grade layout
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9.0

# Dimensions
fig, ax = plt.subplots(figsize=(9.2, 13.8), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 15.5)
ax.axis('off')

# Professional Academic Palette
c_navy      = '#0F172A'  # Deep Slate Navy for terminal & headers
c_border    = '#2563EB'  # Royal Tech Blue for borders
c_bg_card   = '#F8FAFC'  # Clean white/slate background
c_diamond   = '#FEF3C7'  # Warm amber/cream for decision diamond
c_diamond_b = '#D97706'  # Amber border
c_text_dark = '#0F172A'  # Primary text
c_text_sub  = '#334155'  # Subtext
c_arrow     = '#1E40AF'  # Solid blue arrow
c_arrow_red = '#DC2626'  # Red feedback arrow for "Tidak"
c_arrow_grn = '#16A34A'  # Green arrow for "Ya"

# Stage Elements Layout
# Y-positions:
# 14.7 : Mulai
# 13.2 : Tahap 1
# 11.5 : Tahap 2
# 9.8  : Tahap 3
# 8.1  : Tahap 4
# 6.4  : Tahap 5
# 4.7  : Decision Diamond (Lift > 1.0?)
# 2.8  : Tahap 6
# 1.2  : Selesai

def draw_capsule(y, text):
    w, h = 4.2, 0.65
    box = patches.FancyBboxPatch(
        (5.0 - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.2,rounding_size=0.32",
        facecolor=c_navy, edgecolor=c_navy,
        linewidth=2, zorder=4
    )
    ax.add_patch(box)
    ax.text(5.0, y, text, ha='center', va='center',
            color='white', fontweight='bold', fontsize=11, zorder=5)

def draw_process(y, stage_num, title, items, is_focal=False):
    w, h = 8.0, 1.2
    edge_col = '#1D4ED8' if not is_focal else '#2563EB'
    bg_col = '#F1F5F9' if is_focal else c_bg_card
    
    box = patches.FancyBboxPatch(
        (5.0 - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.15,rounding_size=0.15",
        facecolor=bg_col, edgecolor=edge_col,
        linewidth=1.8, zorder=3
    )
    ax.add_patch(box)
    
    # Title / Stage banner
    header_y = y + h/2 - 0.28
    full_title = f"{stage_num}: {title}"
    ax.text(5.0 - w/2 + 0.35, header_y, full_title,
            ha='left', va='center', color=c_navy, fontweight='bold', fontsize=9.8, zorder=4)
    
    # Divider line
    ax.plot([5.0 - w/2 + 0.3, 5.0 + w/2 - 0.3], [header_y - 0.16, header_y - 0.16],
            color='#CBD5E1', linewidth=1.1, zorder=4)
    
    # Content rows
    y1 = header_y - 0.40
    y2 = header_y - 0.67
    ax.text(5.0 - w/2 + 0.45, y1, f"• {items[0]}",
            ha='left', va='center', color=c_text_dark, fontsize=8.6, zorder=4)
    ax.text(5.0 - w/2 + 0.45, y2, f"• {items[1]}",
            ha='left', va='center', color=c_text_sub, fontsize=8.6, zorder=4)

def draw_diamond(y, title, sub):
    w, h = 5.2, 1.15
    pts = [
        [5.0, y + h/2],
        [5.0 + w/2, y],
        [5.0, y - h/2],
        [5.0 - w/2, y]
    ]
    poly = patches.Polygon(pts, closed=True, facecolor=c_diamond, edgecolor=c_diamond_b,
                           linewidth=2.0, zorder=4)
    ax.add_patch(poly)
    ax.text(5.0, y + 0.14, title, ha='center', va='center',
            color='#78350F', fontweight='bold', fontsize=9.6, zorder=5)
    ax.text(5.0, y - 0.16, sub, ha='center', va='center',
            color='#92400E', fontsize=8.4, zorder=5)

def draw_arrow(y_start, y_end, label="", label_col='#0F172A', color=c_arrow):
    ax.annotate(
        '', xy=(5.0, y_end), xytext=(5.0, y_start),
        arrowprops=dict(
            arrowstyle='->,head_width=0.35,head_length=0.45',
            color=color, lw=2.0
        ),
        zorder=3
    )
    if label:
        ax.text(5.25, (y_start + y_end)/2, label, ha='left', va='center',
                color=label_col, fontweight='bold', fontsize=9,
                bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='none'),
                zorder=6)

# 1. Mulai
draw_capsule(14.7, "MULAI")
draw_arrow(14.7 - 0.32, 13.2 + 0.6)

# 2. Tahap 1
draw_process(
    13.2, "Tahap 1", "Pemahaman Bisnis (Business Understanding)",
    [
        "Identifikasi kendala mismatch alokasi stok & penawaran kredit di PT. SSM Motor",
        "Perumusan sasaran analitis data mining 5 dimensi (Model, Warna, Leasing, Tenor, Wilayah)"
    ]
)
draw_arrow(13.2 - 0.6, 11.5 + 0.6)

# 3. Tahap 2
draw_process(
    11.5, "Tahap 2", "Pemahaman Data (Data Understanding)",
    [
        "Ekstraksi basis data operasional Yamaha Dealer Management System (Y-DMS)",
        "Akuisisi & seleksi 3.113 rekaman faktur transaksi sah Q3 (1 Juni - 31 Agustus 2026)"
    ]
)
draw_arrow(11.5 - 0.6, 9.8 + 0.6)

# 4. Tahap 3
draw_process(
    9.8, "Tahap 3", "Persiapan Data (Data Preparation)",
    [
        "Data cleaning (penanganan missing values, transaksi retur/batal, masking privasi NIK)",
        "Transformasi keranjang predikat multi-atribut ke representasi biner (One-Hot Encoding)"
    ]
)
draw_arrow(9.8 - 0.6, 8.1 + 0.6)

# 5. Tahap 4
draw_process(
    8.1, "Tahap 4", "Pemodelan FP-Growth (Modeling)",
    [
        "Pemindaian 2-pass basis data untuk konstruksi Header Table & pohon FP-Tree",
        "Ekstraksi pola frekuensi tinggi rekursif via Conditional Pattern Base tanpa calon kandidat",
    ],
    is_focal=True
)
draw_arrow(8.1 - 0.6, 6.4 + 0.6)

# 6. Tahap 5
draw_process(
    6.4, "Tahap 5", "Evaluasi Kaidah Asosiasi (Evaluation)",
    [
        "Kalkulasi Standar Validasi Tiga Metrik: Support, Confidence, dan Lift Ratio",
        "Penyaringan kaidah asosiasi bermakna & eliminasi kaidah semu / redundan"
    ]
)
draw_arrow(6.4 - 0.6, 4.7 + 0.575)

# 7. Decision Diamond (Kaidah Valid?)
draw_diamond(4.7, "Validasi Kaidah Asosiasi?", "Lift Ratio > 1,0 & Lolos Ambang Batas?")

# Arrow "Ya" from Diamond to Tahap 6
draw_arrow(4.7 - 0.575, 2.9 + 0.65, label="Ya (Valid)", label_col=c_arrow_grn, color=c_arrow_grn)

# Arrow "Tidak" (Feedback Loop) from Diamond to Tahap 4
# Path: from left diamond (x=2.4, y=4.7) -> left to x=0.5 -> up to y=8.1 -> right to Tahap 4 (x=1.0)
ax.plot([2.4, 0.6], [4.7, 4.7], color=c_arrow_red, lw=1.8, zorder=3)
ax.plot([0.6, 0.6], [4.7, 8.1], color=c_arrow_red, lw=1.8, zorder=3)
ax.annotate(
    '', xy=(1.0, 8.1), xytext=(0.6, 8.1),
    arrowprops=dict(
        arrowstyle='->,head_width=0.35,head_length=0.45',
        color=c_arrow_red, lw=1.8
    ),
    zorder=3
)
ax.text(1.5, 4.9, "Tidak", color=c_arrow_red, fontweight='bold', fontsize=8.5,
        bbox=dict(boxstyle='square,pad=0.15', facecolor='white', edgecolor='none'), zorder=6)
ax.text(0.35, 6.4, "Iterasi: Penyesuaian Min_Sup & Min_Conf", color=c_arrow_red,
        fontsize=8.0, rotation=90, va='center', ha='center',
        bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='#FECACA'), zorder=6)

# 8. Tahap 6
draw_process(
    2.9, "Tahap 6", "Perumusan Rekomendasi Preskriptif (Deployment)",
    [
        "Penyusunan Smart Sales Script pembiayaan kredit motor bagi pramuniaga counter",
        "Formulasi alokasi stok varian warna antarcabang & paket bundling promosi leasing"
    ]
)
draw_arrow(2.9 - 0.65, 1.2 + 0.32)

# 9. Selesai
draw_capsule(1.2, "SELESAI")

# Output paths
out1 = r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Gambar_3_1_Bagan_Alir_Penelitian.png"
out2 = r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Penelitian SI\Gambar_3_1_Bagan_Alir_Penelitian.png"
out3 = r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\02_Publikasi_Jurnal_JUTISI\Gambar_3_1_Bagan_Alir_Penelitian.png"

# Brain artifact directory
artifact_dir = r"C:\Users\MyBook Hype AMD\.gemini\antigravity\brain\aeafa5f9-baa3-4314-aaf9-c929d8a0a617"
out_artifact = os.path.join(artifact_dir, "Gambar_3_1_Bagan_Alir_Penelitian.png")

plt.tight_layout()
plt.savefig(out1, dpi=300, bbox_inches='tight')
plt.savefig(out2, dpi=300, bbox_inches='tight')
plt.savefig(out3, dpi=300, bbox_inches='tight')
plt.savefig(out_artifact, dpi=300, bbox_inches='tight')
plt.close()

print(f"Bagan Alir berhasil digenerate di:\n1. {out1}\n2. {out2}\n3. {out_artifact}")
