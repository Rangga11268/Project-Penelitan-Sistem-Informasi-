import matplotlib.pyplot as plt
import matplotlib.patches as patches
import docx
from docx.shared import Inches
import os

# Pure Black & White Academic Standard with PROMINENT LARGE FONTS
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'

fig, ax = plt.subplots(figsize=(9.2, 14.0), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 15.6)
ax.axis('off')

c_black = '#000000'
c_white = '#FFFFFF'

def draw_terminal(y, text):
    w, h = 4.2, 0.72
    box = patches.FancyBboxPatch(
        (5.0 - w/2, y - h/2), w, h,
        boxstyle="round,pad=0.15,rounding_size=0.35",
        facecolor=c_white, edgecolor=c_black,
        linewidth=1.8, zorder=4
    )
    ax.add_patch(box)
    ax.text(5.0, y, text, ha='center', va='center',
            color=c_black, fontweight='bold', fontsize=14, zorder=5)

def draw_stage(y, stage_num, title, items):
    w, h = 8.5, 1.30
    
    # Outer Process Box
    box = patches.Rectangle(
        (5.0 - w/2, y - h/2), w, h,
        facecolor=c_white, edgecolor=c_black,
        linewidth=1.5, zorder=3
    )
    ax.add_patch(box)
    
    # Stage Title (Large & Bold: 12.5pt)
    header_y = y + h/2 - 0.26
    full_title = f"{stage_num}: {title}"
    ax.text(5.0 - w/2 + 0.30, header_y, full_title,
            ha='left', va='center', color=c_black, fontweight='bold', fontsize=12.2, zorder=5)
    
    # Single Crisp Black Divider Line
    div_y = header_y - 0.18
    ax.plot([5.0 - w/2, 5.0 + w/2], [div_y, div_y],
            color=c_black, linewidth=1.1, zorder=4)
    
    # Bullets (Large & Clear: 10.8pt)
    y1 = div_y - 0.28
    y2 = y1 - 0.32
    ax.text(5.0 - w/2 + 0.35, y1, f"• {items[0]}",
            ha='left', va='center', color=c_black, fontsize=10.6, zorder=5)
    ax.text(5.0 - w/2 + 0.35, y2, f"• {items[1]}",
            ha='left', va='center', color=c_black, fontsize=10.6, zorder=5)

def draw_diamond(y, title, sub):
    w, h = 6.2, 1.35
    pts = [
        [5.0, y + h/2],
        [5.0 + w/2, y],
        [5.0, y - h/2],
        [5.0 - w/2, y]
    ]
    poly = patches.Polygon(pts, closed=True, facecolor=c_white, edgecolor=c_black,
                           linewidth=1.6, zorder=4)
    ax.add_patch(poly)
    ax.text(5.0, y + 0.16, title, ha='center', va='center',
            color=c_black, fontweight='bold', fontsize=12.0, zorder=5)
    ax.text(5.0, y - 0.18, sub, ha='center', va='center',
            color=c_black, fontstyle='italic', fontsize=10.5, zorder=5)

def draw_arrow(y_start, y_end, label=""):
    ax.annotate(
        '', xy=(5.0, y_end), xytext=(5.0, y_start),
        arrowprops=dict(
            arrowstyle='->,head_width=0.34,head_length=0.46',
            color=c_black, lw=1.6
        ),
        zorder=2
    )
    if label:
        ax.text(5.35, (y_start + y_end)/2, label, ha='left', va='center',
                color=c_black, fontweight='bold', fontsize=11.0,
                bbox=dict(boxstyle='square,pad=0.25', facecolor=c_white, edgecolor=c_black, lw=1.0),
                zorder=6)

# 1. Start Node
draw_terminal(14.8, "MULAI")
draw_arrow(14.8 - 0.36, 13.2 + 0.65)

# 2. Stage 1
draw_stage(
    13.2, "Tahap 1", "Pemahaman Bisnis (Business Understanding)",
    [
        "Identifikasi kendala mismatch alokasi stok & penawaran kredit di PT. SSM Motor",
        "Perumusan sasaran analitis data mining 5 dimensi (Model, Warna, Leasing, Tenor, Wilayah)"
    ]
)
draw_arrow(13.2 - 0.65, 11.4 + 0.65)

# 3. Stage 2
draw_stage(
    11.4, "Tahap 2", "Pemahaman Data (Data Understanding)",
    [
        "Ekstraksi basis data operasional Yamaha Dealer Management System (Y-DMS)",
        "Akuisisi & seleksi 3.113 rekaman faktur transaksi sah Q3 (1 Juni - 31 Agustus 2026)"
    ]
)
draw_arrow(11.4 - 0.65, 9.6 + 0.65)

# 4. Stage 3
draw_stage(
    9.6, "Tahap 3", "Persiapan Data (Data Preparation)",
    [
        "Pembersihan data (missing values, faktur retur/batal, anonimisasi privasi NIK)",
        "Transformasi keranjang predikat multi-atribut ke matriks biner (One-Hot Encoding)"
    ]
)
draw_arrow(9.6 - 0.65, 7.8 + 0.65)

# 5. Stage 4
draw_stage(
    7.8, "Tahap 4", "Pemodelan FP-Growth (Modeling)",
    [
        "Pemindaian 2-pass basis data untuk konstruksi Header Table & pohon FP-Tree",
        "Ekstraksi pola frekuensi tinggi rekursif via Conditional Pattern Base tanpa kandidat"
    ]
)
draw_arrow(7.8 - 0.65, 6.0 + 0.65)

# 6. Stage 5
draw_stage(
    6.0, "Tahap 5", "Evaluasi Kaidah Asosiasi (Evaluation)",
    [
        "Kalkulasi Standar Validasi Tiga Metrik: Support, Confidence, dan Lift Ratio",
        "Penyaringan kaidah asosiasi bermakna & eliminasi kaidah semu / redundan"
    ]
)
draw_arrow(6.0 - 0.65, 4.2 + 0.675)

# 7. Decision Rhombus
draw_diamond(4.2, "Validasi Kaidah Asosiasi?", "Apakah Lift Ratio > 1,0 & Lolos Ambang Batas?")

# Forward Branch: "Ya"
draw_arrow(4.2 - 0.675, 2.3 + 0.65, label="Ya (Valid)")

# Feedback Loop Branch: "Tidak"
# Left diamond corner is at x = 5.0 - 3.1 = 1.9, y = 4.2
ax.plot([1.9, 0.45], [4.2, 4.2], color=c_black, lw=1.5, zorder=2)
ax.plot([0.45, 0.45], [4.2, 7.8], color=c_black, lw=1.5, zorder=2)
ax.annotate(
    '', xy=(0.75, 7.8), xytext=(0.45, 7.8),
    arrowprops=dict(
        arrowstyle='->,head_width=0.32,head_length=0.44',
        color=c_black, lw=1.5
    ),
    zorder=2
)
# Large decision feedback tags
ax.text(1.25, 4.50, "Tidak", color=c_black, fontweight='bold', fontsize=11.0,
        bbox=dict(boxstyle='square,pad=0.25', facecolor=c_white, edgecolor=c_black, lw=1.0),
        zorder=6)
ax.text(0.24, 6.0, "Iterasi: Penyesuaian Nilai Ambang Min_Sup & Min_Conf", color=c_black,
        fontsize=10.0, fontstyle='italic', rotation=90, va='center', ha='center',
        bbox=dict(boxstyle='square,pad=0.25', facecolor=c_white, edgecolor=c_black, lw=1.0),
        zorder=6)

# 8. Stage 6
draw_stage(
    2.3, "Tahap 6", "Perumusan Rekomendasi Preskriptif (Deployment)",
    [
        "Penyusunan Smart Sales Script pembiayaan kredit motor bagi pramuniaga counter",
        "Formulasi alokasi stok varian warna antarcabang & paket bundling promosi leasing"
    ]
)
draw_arrow(2.3 - 0.65, 0.8 + 0.36)

# 9. End Node
draw_terminal(0.8, "SELESAI")

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

# Re-embed into both Word documents with proper size
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
            run.add_picture(img_path, width=Inches(5.8))
            p.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
            break
    doc.save(doc_path)

print("Large font B&W flowchart successfully generated and embedded!")
