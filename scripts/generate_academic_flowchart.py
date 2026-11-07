import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Academic Publication Configuration (IEEE / Springer / JuTISI Standard)
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 9.5
plt.rcParams['mathtext.fontset'] = 'stix'

# Figure setup: Portrait, clean white background, 300 DPI
fig, ax = plt.subplots(figsize=(8.8, 13.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 15.6)
ax.axis('off')

# Journal-grade Palette (High contrast, print-perfect, grayscale-compatible)
c_box_bg    = '#FFFFFF'  # Pure white
c_header_bg = '#F1F5F9'  # Very soft slate for header bar
c_border    = '#1E293B'  # Deep Charcoal / Slate for sharp border
c_text_main = '#0F172A'  # Primary black/slate text
c_text_sub  = '#334155'  # Secondary descriptive text
c_arrow     = '#1E293B'  # Sharp charcoal arrow
c_decision  = '#FAFAFA'  # Crisp off-white for decision rhombus
c_tag_bg    = '#FFFFFF'  # Badge background

def draw_terminal(y, text):
    w, h = 3.8, 0.62
    box = patches.FancyBboxPatch(
        (5.0 - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.18,rounding_size=0.31",
        facecolor='#F8FAFC', edgecolor=c_border,
        linewidth=1.8, zorder=4
    )
    ax.add_patch(box)
    ax.text(5.0, y, text, ha='center', va='center',
            color=c_text_main, fontweight='bold', fontsize=11, zorder=5)

def draw_stage(y, stage_num, title, items):
    w, h = 8.2, 1.22
    
    # Outer Card
    card = patches.FancyBboxPatch(
        (5.0 - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.12,rounding_size=0.12",
        facecolor=c_box_bg, edgecolor=c_border,
        linewidth=1.5, zorder=3
    )
    ax.add_patch(card)
    
    # Header Banner Box inside Card
    h_h = 0.36
    h_box = patches.FancyBboxPatch(
        (5.0 - w/2, y + h/2 - h_h), w, h_h,
        boxstyle="round,pad=0.12,rounding_size=0.12",
        facecolor=c_header_bg, edgecolor=c_border,
        linewidth=1.2, zorder=4
    )
    ax.add_patch(h_box)
    
    # Clip the lower rounded corners of header with a sharp divider
    ax.plot([5.0 - w/2, 5.0 + w/2], [y + h/2 - h_h, y + h/2 - h_h],
            color=c_border, linewidth=1.2, zorder=5)
    
    # Title Text
    full_title = f"{stage_num}: {title}"
    ax.text(5.0 - w/2 + 0.3, y + h/2 - h_h/2, full_title,
            ha='left', va='center', color=c_text_main, fontweight='bold', fontsize=10.0, zorder=6)
    
    # Bullet Items
    y1 = y + h/2 - h_h - 0.24
    y2 = y1 - 0.28
    ax.text(5.0 - w/2 + 0.35, y1, f"• {items[0]}",
            ha='left', va='center', color=c_text_main, fontsize=8.8, zorder=6)
    ax.text(5.0 - w/2 + 0.35, y2, f"• {items[1]}",
            ha='left', va='center', color=c_text_sub, fontsize=8.8, zorder=6)

def draw_rhombus(y, title, sub):
    w, h = 5.2, 1.15
    pts = [
        [5.0, y + h/2],
        [5.0 + w/2, y],
        [5.0, y - h/2],
        [5.0 - w/2, y]
    ]
    poly = patches.Polygon(pts, closed=True, facecolor=c_decision, edgecolor=c_border,
                           linewidth=1.6, zorder=4)
    ax.add_patch(poly)
    ax.text(5.0, y + 0.14, title, ha='center', va='center',
            color=c_text_main, fontweight='bold', fontsize=9.8, zorder=5)
    ax.text(5.0, y - 0.16, sub, ha='center', va='center',
            color=c_text_sub, fontstyle='italic', fontsize=8.6, zorder=5)

def draw_straight_arrow(y_start, y_end, label=""):
    ax.annotate(
        '', xy=(5.0, y_end), xytext=(5.0, y_start),
        arrowprops=dict(
            arrowstyle='->,head_width=0.32,head_length=0.42',
            color=c_arrow, lw=1.5
        ),
        zorder=2
    )
    if label:
        ax.text(5.25, (y_start + y_end)/2, label, ha='left', va='center',
                color=c_text_main, fontweight='bold', fontsize=9,
                bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='#94A3B8', lw=0.8),
                zorder=6)

# 1. Start Node
draw_terminal(14.8, "MULAI")
draw_straight_arrow(14.8 - 0.31, 13.3 + 0.61)

# 2. Stage 1
draw_stage(
    13.3, "Tahap 1", "Pemahaman Bisnis (Business Understanding)",
    [
        "Identifikasi kendala mismatch alokasi stok & penawaran kredit di PT. SSM Motor",
        "Perumusan sasaran analitis data mining 5 dimensi (Model, Warna, Leasing, Tenor, Wilayah)"
    ]
)
draw_straight_arrow(13.3 - 0.61, 11.6 + 0.61)

# 3. Stage 2
draw_stage(
    11.6, "Tahap 2", "Pemahaman Data (Data Understanding)",
    [
        "Ekstraksi basis data operasional Yamaha Dealer Management System (Y-DMS)",
        "Akuisisi & seleksi 3.113 rekaman faktur transaksi sah Q3 (1 Juni - 31 Agustus 2026)"
    ]
)
draw_straight_arrow(11.6 - 0.61, 9.9 + 0.61)

# 4. Stage 3
draw_stage(
    9.9, "Tahap 3", "Persiapan Data (Data Preparation)",
    [
        "Pembersihan data (penanganan missing values, transaksi retur/batal, masking privasi NIK)",
        "Transformasi keranjang predikat multi-atribut ke matriks biner (One-Hot Encoding)"
    ]
)
draw_straight_arrow(9.9 - 0.61, 8.2 + 0.61)

# 5. Stage 4
draw_stage(
    8.2, "Tahap 4", "Pemodelan FP-Growth (Modeling)",
    [
        "Pemindaian 2-pass basis data untuk konstruksi Header Table & pohon FP-Tree",
        "Ekstraksi pola frekuensi tinggi rekursif via Conditional Pattern Base tanpa calon kandidat"
    ]
)
draw_straight_arrow(8.2 - 0.61, 6.5 + 0.61)

# 6. Stage 5
draw_stage(
    6.5, "Tahap 5", "Evaluasi Kaidah Asosiasi (Evaluation)",
    [
        "Kalkulasi Standar Validasi Tiga Metrik: Support, Confidence, dan Lift Ratio",
        "Penyaringan kaidah asosiasi bermakna & eliminasi kaidah semu / redundan"
    ]
)
draw_straight_arrow(6.5 - 0.61, 4.8 + 0.575)

# 7. Decision Rhombus
draw_rhombus(4.8, "Validasi Kaidah Asosiasi?", "Apakah Lift Ratio > 1,0 & Lolos Ambang Batas?")

# Forward Arrow: "Ya"
draw_straight_arrow(4.8 - 0.575, 2.9 + 0.61, label="Ya (Valid)")

# Feedback Loop: "Tidak" (Loop back to Stage 4)
# Route: Left corner (2.4, 4.8) -> left to (0.55, 4.8) -> up to (0.55, 8.2) -> into Stage 4 at (0.9, 8.2)
ax.plot([2.4, 0.55], [4.8, 4.8], color=c_arrow, lw=1.5, zorder=2)
ax.plot([0.55, 0.55], [4.8, 8.2], color=c_arrow, lw=1.5, zorder=2)
ax.annotate(
    '', xy=(0.9, 8.2), xytext=(0.55, 8.2),
    arrowprops=dict(
        arrowstyle='->,head_width=0.32,head_length=0.42',
        color=c_arrow, lw=1.5
    ),
    zorder=2
)
# Labels for feedback branch
ax.text(1.45, 5.0, "Tidak", color='#B91C1C', fontweight='bold', fontsize=8.8,
        bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='#B91C1C', lw=0.8),
        zorder=6)
ax.text(0.35, 6.5, "Iterasi: Penyesuaian Nilai Ambang Min_Sup & Min_Conf", color=c_text_main,
        fontsize=8.2, fontstyle='italic', rotation=90, va='center', ha='center',
        bbox=dict(boxstyle='square,pad=0.2', facecolor='white', edgecolor='#94A3B8', lw=0.8),
        zorder=6)

# 8. Stage 6
draw_stage(
    2.9, "Tahap 6", "Perumusan Rekomendasi Preskriptif (Deployment)",
    [
        "Penyusunan Smart Sales Script pembiayaan kredit motor bagi pramuniaga counter",
        "Formulasi alokasi stok varian warna antarcabang & paket bundling promosi leasing"
    ]
)
draw_straight_arrow(2.9 - 0.61, 1.2 + 0.31)

# 9. End Node
draw_terminal(1.2, "SELESAI")

# Output destinations
paths = [
    r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Gambar_3_1_Bagan_Alir_Penelitian.png",
    r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Penelitian SI\Gambar_3_1_Bagan_Alir_Penelitian.png",
    r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\02_Publikasi_Jurnal_JUTISI\Gambar_3_1_Bagan_Alir_Penelitian.png",
    r"C:\Users\MyBook Hype AMD\.gemini\antigravity\brain\aeafa5f9-baa3-4314-aaf9-c929d8a0a617\Gambar_3_1_Bagan_Alir_Penelitian.png"
]

plt.tight_layout()
for p in paths:
    plt.savefig(p, dpi=300, bbox_inches='tight')
plt.close()

print("Academic-paper standard flowchart successfully generated at all destinations!")
