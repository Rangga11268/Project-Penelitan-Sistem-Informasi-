import matplotlib.pyplot as plt
import matplotlib.patches as patches
import docx
from docx.shared import Inches
import os

# Pure Black & White Academic Standard (100% Line Art, No Gray, No Tint)
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 9.5
plt.rcParams['mathtext.fontset'] = 'stix'

fig, ax = plt.subplots(figsize=(8.8, 13.5), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 15.6)
ax.axis('off')

# 100% Pure Black and White
c_black = '#000000'
c_white = '#FFFFFF'

def draw_terminal(y, text):
    w, h = 3.6, 0.58
    box = patches.FancyBboxPatch(
        (5.0 - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.15,rounding_size=0.29",
        facecolor=c_white, edgecolor=c_black,
        linewidth=1.4, zorder=4
    )
    ax.add_patch(box)
    ax.text(5.0, y, text, ha='center', va='center',
            color=c_black, fontweight='bold', fontsize=10.5, zorder=5)

def draw_stage(y, stage_num, title, items):
    w, h = 8.2, 1.20
    
    # Outer Process Box (Pure White with Solid Black Border)
    box = patches.Rectangle(
        (5.0 - w/2, y - h/2), w, h,
        facecolor=c_white, edgecolor=c_black,
        linewidth=1.2, zorder=3
    )
    ax.add_patch(box)
    
    # Stage Title Text (Bold Black)
    header_y = y + h/2 - 0.22
    full_title = f"{stage_num}: {title}"
    ax.text(5.0 - w/2 + 0.28, header_y, full_title,
            ha='left', va='center', color=c_black, fontweight='bold', fontsize=9.8, zorder=5)
    
    # Single Crisp Black Divider Line
    div_y = header_y - 0.16
    ax.plot([5.0 - w/2, 5.0 + w/2], [div_y, div_y],
            color=c_black, linewidth=0.9, zorder=4)
    
    # Bullet Items (Pure Black Text)
    y1 = div_y - 0.25
    y2 = y1 - 0.28
    ax.text(5.0 - w/2 + 0.35, y1, f"• {items[0]}",
            ha='left', va='center', color=c_black, fontsize=8.8, zorder=5)
    ax.text(5.0 - w/2 + 0.35, y2, f"• {items[1]}",
            ha='left', va='center', color=c_black, fontsize=8.8, zorder=5)

def draw_diamond(y, title, sub):
    w, h = 5.2, 1.15
    pts = [
        [5.0, y + h/2],
        [5.0 + w/2, y],
        [5.0, y - h/2],
        [5.0 - w/2, y]
    ]
    poly = patches.Polygon(pts, closed=True, facecolor=c_white, edgecolor=c_black,
                           linewidth=1.2, zorder=4)
    ax.add_patch(poly)
    ax.text(5.0, y + 0.14, title, ha='center', va='center',
            color=c_black, fontweight='bold', fontsize=9.6, zorder=5)
    ax.text(5.0, y - 0.16, sub, ha='center', va='center',
            color=c_black, fontstyle='italic', fontsize=8.5, zorder=5)

def draw_arrow(y_start, y_end, label=""):
    ax.annotate(
        '', xy=(5.0, y_end), xytext=(5.0, y_start),
        arrowprops=dict(
            arrowstyle='->,head_width=0.28,head_length=0.38',
            color=c_black, lw=1.2
        ),
        zorder=2
    )
    if label:
        ax.text(5.25, (y_start + y_end)/2, label, ha='left', va='center',
                color=c_black, fontweight='bold', fontsize=8.8,
                bbox=dict(boxstyle='square,pad=0.2', facecolor=c_white, edgecolor=c_black, lw=0.8),
                zorder=6)

# 1. Start Node
draw_terminal(14.8, "MULAI")
draw_arrow(14.8 - 0.29, 13.3 + 0.60)

# 2. Stage 1
draw_stage(
    13.3, "Tahap 1", "Pemahaman Bisnis (Business Understanding)",
    [
        "Identifikasi kendala mismatch alokasi stok & penawaran kredit di PT. SSM Motor",
        "Perumusan sasaran analitis data mining 5 dimensi (Model, Warna, Leasing, Tenor, Wilayah)"
    ]
)
draw_arrow(13.3 - 0.60, 11.6 + 0.60)

# 3. Stage 2
draw_stage(
    11.6, "Tahap 2", "Pemahaman Data (Data Understanding)",
    [
        "Ekstraksi basis data operasional Yamaha Dealer Management System (Y-DMS)",
        "Akuisisi & seleksi 3.113 rekaman faktur transaksi sah Q3 (1 Juni - 31 Agustus 2026)"
    ]
)
draw_arrow(11.6 - 0.60, 9.9 + 0.60)

# 4. Stage 3
draw_stage(
    9.9, "Tahap 3", "Persiapan Data (Data Preparation)",
    [
        "Pembersihan data (penanganan missing values, transaksi retur/batal, masking privasi NIK)",
        "Transformasi keranjang predikat multi-atribut ke matriks biner (One-Hot Encoding)"
    ]
)
draw_arrow(9.9 - 0.60, 8.2 + 0.60)

# 5. Stage 4
draw_stage(
    8.2, "Tahap 4", "Pemodelan FP-Growth (Modeling)",
    [
        "Pemindaian 2-pass basis data untuk konstruksi Header Table & pohon FP-Tree",
        "Ekstraksi pola frekuensi tinggi rekursif via Conditional Pattern Base tanpa calon kandidat"
    ]
)
draw_arrow(8.2 - 0.60, 6.5 + 0.60)

# 6. Stage 5
draw_stage(
    6.5, "Tahap 5", "Evaluasi Kaidah Asosiasi (Evaluation)",
    [
        "Kalkulasi Standar Validasi Tiga Metrik: Support, Confidence, dan Lift Ratio",
        "Penyaringan kaidah asosiasi bermakna & eliminasi kaidah semu / redundan"
    ]
)
draw_arrow(6.5 - 0.60, 4.8 + 0.575)

# 7. Decision Rhombus
draw_diamond(4.8, "Validasi Kaidah Asosiasi?", "Apakah Lift Ratio > 1,0 & Lolos Ambang Batas?")

# Forward Branch: "Ya"
draw_arrow(4.8 - 0.575, 2.9 + 0.60, label="Ya (Valid)")

# Feedback Loop Branch: "Tidak"
# Orthogonal path: Left corner (2.4, 4.8) -> left to (0.55, 4.8) -> up to (0.55, 8.2) -> into Stage 4 at (0.9, 8.2)
ax.plot([2.4, 0.55], [4.8, 4.8], color=c_black, lw=1.2, zorder=2)
ax.plot([0.55, 0.55], [4.8, 8.2], color=c_black, lw=1.2, zorder=2)
ax.annotate(
    '', xy=(0.9, 8.2), xytext=(0.55, 8.2),
    arrowprops=dict(
        arrowstyle='->,head_width=0.28,head_length=0.38',
        color=c_black, lw=1.2
    ),
    zorder=2
)
# Pure black-and-white tags
ax.text(1.45, 5.02, "Tidak", color=c_black, fontweight='bold', fontsize=8.8,
        bbox=dict(boxstyle='square,pad=0.2', facecolor=c_white, edgecolor=c_black, lw=0.8),
        zorder=6)
ax.text(0.35, 6.5, "Iterasi: Penyesuaian Nilai Ambang Min_Sup & Min_Conf", color=c_black,
        fontsize=8.2, fontstyle='italic', rotation=90, va='center', ha='center',
        bbox=dict(boxstyle='square,pad=0.2', facecolor=c_white, edgecolor=c_black, lw=0.8),
        zorder=6)

# 8. Stage 6
draw_stage(
    2.9, "Tahap 6", "Perumusan Rekomendasi Preskriptif (Deployment)",
    [
        "Penyusunan Smart Sales Script pembiayaan kredit motor bagi pramuniaga counter",
        "Formulasi alokasi stok varian warna antarcabang & paket bundling promosi leasing"
    ]
)
draw_arrow(2.9 - 0.60, 1.2 + 0.29)

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

# Re-embed into both Word documents
img_path = paths[0]
for doc_path in [
    r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1.docx',
    r'D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1 - Final_Revisi.docx'
]:
    doc = docx.Document(doc_path)
    for i, p in enumerate(doc.paragraphs):
        if len(p._element.xpath('.//a:blip')) > 0 and 160 < i < 185:
            p.clear()
            run = p.add_run()
            run.add_picture(img_path, width=Inches(5.6))
            p.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
            break
    doc.save(doc_path)

print("100% Pure Black and White Flowchart successfully generated and embedded!")
