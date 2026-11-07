import docx
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def update_sub_a(doc_path):
    doc = docx.Document(doc_path)
    
    idx_a = None
    idx_b = None
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if t == "A. Pendekatan dan Desain Penelitian":
            idx_a = i
        if t == "B. Bagan Alir Tahapan Penelitian":
            idx_b = i
            break
            
    if idx_a is None or idx_b is None:
        print(f"Could not find A and B in {doc_path}")
        return False
        
    print(f"Found A at {idx_a}, B at {idx_b} in {doc_path}")
    
    paras_to_remove = [doc.paragraphs[k] for k in range(idx_a + 1, idx_b)]
    for p in paras_to_remove:
        p._element.getparent().remove(p._element)
        
    p_b = None
    for p in doc.paragraphs:
        if p.text.strip() == "B. Bagan Alir Tahapan Penelitian":
            p_b = p
            break
            
    texts = [
        (
            "Penelitian ini dirancang sebagai penelitian terapan (applied research) dengan menggunakan "
            "pendekatan kuantitatif komputasional (computational data-driven research) berbasis penambangan "
            "data (data mining) (Sugiyono, 2019; Tan et al., 2018). Pendekatan kuantitatif dipilih karena seluruh "
            "proses analisis berpijak pada data empiris faktual berskala besar yang diukur secara matematis melalui "
            "metrik frekuensi kemunculan bersama (co-occurrence) dan korelasi statistik antaratribut keputusan pembelian "
            "(Sekaran & Bougie, 2016). Melalui pendekatan kuantitatif berbasis komputasi ini, pola keterkaitan perilaku "
            "konsumen yang laten dan tidak kasat mata pada rekaman operasional harian dapat diidentifikasi secara objektif, "
            "terukur, dan terbebas dari bias subjektivitas pengamat."
        ),
        (
            "Berbeda dengan penelitian kuantitatif konvensional yang bertumpu pada pengujian hipotesis deduktif dengan "
            "asumsi variabel terikat tunggal, desain penelitian ini mengadopsi paradigma Association Rule Mining (ARM) "
            "yang bersifat induktif-eksploratif (Han et al., 2022). Paradigma ini bertujuan menemukan keteraturan pola "
            "kombinasi atribut yang sering muncul secara simultan (frequent itemsets) di dalam keranjang transaksi tanpa "
            "memerlukan penetapan variabel dependen dan independen di awal. Karakteristik ini sangat relevan untuk "
            "membedah kompleksitas transaksi dealer sepeda motor yang melibatkan lima dimensi keputusan sekaligus: "
            "model kendaraan, varian warna estetika, skema metode pembayaran, durasi tenor kredit, dan wilayah domisili konsumen."
        ),
        (
            "Guna memandu seluruh rangkaian aktivitas penelitian agar terstruktur dan memiliki ketelitian metodologis yang "
            "tinggi, penelitian ini mengimplementasikan kerangka kerja standar industri Cross-Industry Standard Process for "
            "Data Mining (CRISP-DM) (Sharda et al., 2020; Turban et al., 2018). Kerangka kerja CRISP-DM menyediakan metodologi "
            "yang komprehensif melalui enam fase terintegrasi: Pemahaman Bisnis (Business Understanding), Pemahaman Data "
            "(Data Understanding), Persiapan Data (Data Preparation), Pemodelan (Modeling), Evaluasi (Evaluation), dan "
            "Penyebaran (Deployment). Keunggulan fundamental CRISP-DM terletak pada sifatnya yang berdaur ulang dan iteratif "
            "(iterative feedback loop), yang memungkinkan penyempurnaan parameter pemodelan komputasi algoritma FP-Growth "
            "secara berulang hingga menghasilkan kaidah asosiasi yang selaras dengan kebutuhan strategis dealer PT. Sinar Surya "
            "Matahari (SSM Motor). Penerapan kerangka ini memastikan penelitian memiliki dasar saintifik yang kokoh, transparan, "
            "serta memenuhi kaidah keterulangan (replicability) dalam domain penambangan data otomotif."
        )
    ]
    
    for t in texts:
        new_p = p_b.insert_paragraph_before()
        new_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        new_p.paragraph_format.line_spacing = 1.5
        new_p.paragraph_format.space_before = Pt(0)
        new_p.paragraph_format.space_after = Pt(6)
        new_p.paragraph_format.first_line_indent = Inches(0.4)
        run = new_p.add_run(t)
        run.font.name = "Times New Roman"
        run.font.size = Pt(12)
        
    doc.save(doc_path)
    print(f"Successfully updated Sub-Bab A in {doc_path}")
    return True

if __name__ == "__main__":
    doc2 = r"D:\MATERI SLIDE\MATERI SMT 5\TUGAS SMT 5\Tugas Penelitian SI\099_PROYEK_AKHIR\Penelitian SI - Kelompok 1.docx"
    update_sub_a(doc2)
