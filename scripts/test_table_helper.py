import docx
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import re

foreign_terms = [
    r'\bMaxi Series\b', r'\bClassy\b', r'\bMatic 125\b', r'\bSport\b', r'\bMoped\b',
    r'\bMatte Black\b', r'\bMetallic Red\b', r'\bPrestige Silver\b', r'\bDull Blue\b',
    r'\bCyan\b', r'\bWhite\b', r'\bCash\b', r'\bNon-Kredit\b', r'\bMulti-Attribute Predicate Basket\b',
    r'\bleasing\b', r'\bOne-Hot Encoding\b', r'\bone-hot encoding\b', r'\bFP-Growth\b'
]
combined_regex = re.compile(r'(' + '|'.join(foreign_terms) + r')', re.IGNORECASE)

def add_formatted_text(p, text, font_name='Times New Roman', font_size_pt=9):
    parts = combined_regex.split(text)
    for part in parts:
        if not part: continue
        r = p.add_run(part)
        r.font.name = font_name
        r.font.size = Pt(font_size_pt)
        if combined_regex.fullmatch(part):
            r.font.italic = True

def create_academic_table(doc, headers, data, col_widths, font_size_pt=9, font_name='Times New Roman'):
    table = doc.add_table(rows=len(data) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Table borders
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:bottom w:val="single" w:sz="8" w:space="0" w:color="000000"/>\n'
        f'  <w:insideH w:val="none"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)
    
    def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>\n'
            f'  <w:top w:w="{top}" w:type="dxa"/>\n'
            f'  <w:bottom w:w="{bottom}" w:type="dxa"/>\n'
            f'  <w:left w:w="{left}" w:type="dxa"/>\n'
            f'  <w:right w:w="{right}" w:type="dxa"/>\n'
            f'</w:tcMar>'
        )
        tcPr.append(tcMar)
        
    header_row = table.rows[0]
    trPr = header_row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    
    for i, title in enumerate(headers):
        cell = header_row.cells[i]
        cell.width = Inches(col_widths[i])
        set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
        tcPr = cell._tc.get_or_add_tcPr()
        tcPr.append(parse_xml(f'<w:tcBorders {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/></w:tcBorders>'))
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(title)
        r.font.name = font_name
        r.font.size = Pt(font_size_pt)
        r.font.bold = True

    for row_idx, row_data in enumerate(data):
        row = table.rows[row_idx + 1]
        for col_idx, cell_value in enumerate(row_data):
            cell = row.cells[col_idx]
            cell.width = Inches(col_widths[col_idx])
            set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            if len(headers) == 4 and col_idx in [1, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            elif len(headers) == 3 and col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_text(p, cell_value, font_name=font_name, font_size_pt=font_size_pt)

    return table

doc = docx.Document()
headers1 = ['Atribut', 'Tipe Data', 'Jumlah Varian', 'Keterangan dan Contoh Nilai']
data1 = [
    ['Model Motor', 'Kategorikal', '44 Model', 'Lini produk Yamaha pada segmen Maxi Series, Classy, Matic 125, Sport, dan Moped (contoh: Aerox 155 Cyber City, NMAX Connected, Grand Filano, Fazzio Neo, Gear 125).'],
    ['Varian Warna', 'Kategorikal', '22 Warna', 'Pilihan estetika warna eksterior dari pabrikan (contoh: Matte Black, Metallic Red, Prestige Silver, Dull Blue, White).'],
    ['Lembaga Pembiayaan', 'Kategorikal', '4 Kategori', 'Skema pembelian tunai (Cash) dan fasilitas pembiayaan kredit melalui mitra resmi (BAF, Adira Finance, OTO Multiartha).'],
    ['Tenor Angsuran', 'Diskret', '5 Opsi', 'Jangka waktu cicilan yang disepakati konsumen (11 Bulan, 23 Bulan, 30 Bulan, 35 Bulan, Non-Kredit).'],
    ['Wilayah Domisili', 'Kategorikal', '10 Area', 'Wilayah tempat tinggal konsumen di kawasan aglomerasi Jabodetabek (Kota Bekasi, Kab. Bekasi, Jakarta Timur, Jakarta Selatan, Depok, Bogor, Tangerang, dll.).']
]
col_widths1 = [1.3, 1.0, 1.0, 3.2]
t1 = create_academic_table(doc, headers1, data1, col_widths1)

doc.save('test_table_output.docx')
print("Successfully generated test table output!")
