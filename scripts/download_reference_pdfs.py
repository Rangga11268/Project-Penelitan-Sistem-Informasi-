import os
import urllib.request
import urllib.parse
import re
import ssl

# Disable SSL verification for OJS with self-signed certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8'
}

PAPERS = [
    {
        "id": "01_Widodo_2022_C45_Yamaha",
        "landing": "https://ojs.trigunadharma.ac.id/index.php/jursi/article/view/7262",
        "title": "Widodo (2022) - C4.5 Sepeda Motor Yamaha (JURSI TGD SINTA 4)"
    },
    {
        "id": "02_Soleh_2022_FPGrowth_Sparepart",
        "landing": "https://journal.trunojoyo.ac.id/rekayasa/article/view/11365",
        "title": "Soleh (2022) - FP-Growth Suku Cadang (Rekayasa UTM SINTA 3)"
    },
    {
        "id": "03_Subakti_2022_Apriori_OliMotor",
        "landing": "http://ejournal.polbeng.ac.id/index.php/ISI/article/view/2684",
        "title": "Subakti (2022) - Apriori Oli Motor (Inovtek Polbeng SINTA 3)"
    },
    {
        "id": "04_Rahmatullah_2022_Apriori_YamahaKotabumi",
        "landing": "http://journal.dcckotabumi.ac.id/index.php/jik/article/view/393",
        "title": "Rahmatullah (2022) - Apriori Sparepart Yamaha (JIK SINTA 4)"
    },
    {
        "id": "05_Rahman_2025_Apriori_vs_FPGrowth_CRISPDM",
        "landing": "https://jurnal.itg.ac.id/index.php/algoritma/article/view/2303",
        "title": "Rahman (2025) - Apriori vs FP-Growth CRISP-DM (Jurnal Algoritma SINTA 4)"
    },
    {
        "id": "06_Rachmawati_2024_Apriori_vs_FPGrowth",
        "landing": "https://ejournal.stmik-sumedang.ac.id/index.php/resistor/article/view/1527",
        "title": "Rachmawati (2024) - Komparasi Apriori & FP-Growth (RESISTOR SINTA 3)"
    },
    {
        "id": "07_Saptadi_2023_RESTI_MarketBasket",
        "landing": "https://jurnal.iaii.or.id/index.php/RESTI/article/view/4844",
        "title": "Saptadi (2023) - Association Data Mining (Jurnal RESTI SINTA 2)"
    },
    {
        "id": "08_Muharam_2025_JITET_FPGrowth",
        "landing": "https://jurnal.fmipa.unila.ac.id/jitet/article/view/5935",
        "title": "Muharam (2025) - FP-Growth Rekomendasi POS (JITET SINTA 3)"
    },
    {
        "id": "09_Hidayat_2023_JTEKSIS_FPGrowth",
        "landing": "https://jurnal.unidha.ac.id/index.php/jteksis/article/view/847",
        "title": "Hidayat (2023) - FP-Growth Transaksi Penjualan (JTEKSIS SINTA 3)"
    },
    {
        "id": "10_Pratama_2024_Generation_FPGrowth",
        "landing": "https://ojs.unik-kediri.ac.id/index.php/gj/article/view/22994",
        "title": "Pratama (2024) - FP-Growth Barang Terpopuler (Generation SINTA 4)"
    }
]

def find_pdf_url_from_landing(landing_url):
    try:
        req = urllib.request.Request(landing_url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Look for citation_pdf_url meta tag (standard OJS)
            m = re.search(r'<meta\s+name=["\']citation_pdf_url["\']\s+content=["\']([^"\']+)["\']', html, re.IGNORECASE)
            if m:
                return m.group(1)
                
            # Look for standard OJS download link
            m2 = re.search(r'href=["\']([^"\']+/article/download/[^"\']+)["\']', html, re.IGNORECASE)
            if m2:
                link = m2.group(1)
                if link.startswith('/'):
                    parsed = urllib.parse.urlparse(landing_url)
                    link = f"{parsed.scheme}://{parsed.netloc}{link}"
                return link
                
            # Look for /view/ -> /download/ replacement pattern in OJS
            if '/article/view/' in landing_url:
                parts = landing_url.split('/article/view/')
                # Match article ID
                art_id = parts[1].split('/')[0].split('?')[0]
                # Look for galley ID in HTML
                m3 = re.search(rf'article/view/{art_id}/(\d+)', html)
                if m3:
                    galley_id = m3.group(1)
                    return f"{parts[0]}/article/download/{art_id}/{galley_id}"
                else:
                    return f"{parts[0]}/article/download/{art_id}"
    except Exception as e:
        print(f"  [WARN] Failed to scrape landing page {landing_url}: {e}")
    return None

def download_all_pdfs():
    out_dir = os.path.abspath(os.path.join("docs", "REFERENSI_JURNAL_PDF"))
    os.makedirs(out_dir, exist_ok=True)
    print(f"Target Directory: {out_dir}\n")
    
    success_count = 0
    for p in PAPERS:
        filename = f"{p['id']}.pdf"
        target_path = os.path.join(out_dir, filename)
        print(f"Processing: {p['title']} ...")
        
        pdf_url = find_pdf_url_from_landing(p['landing'])
        if not pdf_url:
            print(f"  [ERROR] Could not find direct PDF link for {p['landing']}")
            continue
            
        print(f"  Found PDF URL: {pdf_url}")
        try:
            req = urllib.request.Request(pdf_url, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=25) as response:
                content = response.read()
                # Check if it's actually a PDF (starts with %PDF) or HTML redirection
                if content.startswith(b'%PDF'):
                    with open(target_path, 'wb') as f:
                        f.write(content)
                    print(f"  [SUCCESS] Downloaded: {filename} ({len(content):,} bytes)")
                    success_count += 1
                else:
                    # Might be an intermediate OJS view/download wrapper page
                    html_wrapper = content.decode('utf-8', errors='ignore')
                    m_embed = re.search(r'<iframe\s+[^>]*src=["\']([^"\']+)["\']', html_wrapper, re.IGNORECASE) or \
                              re.search(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', html_wrapper, re.IGNORECASE) or \
                              re.search(r'class=["\']download["\']\s+href=["\']([^"\']+)["\']', html_wrapper, re.IGNORECASE)
                    if m_embed:
                        direct_url = m_embed.group(1)
                        if direct_url.startswith('/'):
                            parsed = urllib.parse.urlparse(pdf_url)
                            direct_url = f"{parsed.scheme}://{parsed.netloc}{direct_url}"
                        print(f"  Following embedded iframe/button PDF URL: {direct_url}")
                        req2 = urllib.request.Request(direct_url, headers=HEADERS)
                        with urllib.request.urlopen(req2, context=ctx, timeout=25) as resp2:
                            pdf_data = resp2.read()
                            with open(target_path, 'wb') as f2:
                                f2.write(pdf_data)
                            print(f"  [SUCCESS] Downloaded: {filename} ({len(pdf_data):,} bytes)")
                            success_count += 1
                    else:
                        print(f"  [WARN] Response was not a direct PDF (received {len(content)} bytes of HTML). Saved as fallback.")
        except Exception as e:
            print(f"  [ERROR] Download failed: {e}")

    print(f"\n==========================================")
    print(f"Completed! Successfully downloaded {success_count}/{len(PAPERS)} PDF files.")
    print(f"Files saved in: {out_dir}")

if __name__ == '__main__':
    download_all_pdfs()
