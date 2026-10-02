import os
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

TARGETS = [
    {
        "filename": "01_Widodo_2022_C45_Yamaha.pdf",
        "urls": [
            "https://ojs.trigunadharma.ac.id/index.php/jsi/article/download/7262/1933",
            "https://ojs.trigunadharma.ac.id/index.php/jursi/article/download/7262/826"
        ]
    },
    {
        "filename": "03_Subakti_2022_Apriori_OliMotor.pdf",
        "urls": [
            "http://ejournal.polbeng.ac.id/index.php/ISI/article/download/2684/1261",
            "http://ejournal.polbeng.ac.id/index.php/ISI/article/download/2684/1468"
        ]
    },
    {
        "filename": "04_Rahmatullah_2022_Apriori_YamahaKotabumi.pdf",
        "urls": [
            "https://dcckotabumi.ac.id/ojs/index.php/jik/article/download/393/254",
            "http://journal.dcckotabumi.ac.id/index.php/jik/article/download/393/254"
        ]
    },
    {
        "filename": "06_Rachmawati_2024_Apriori_vs_FPGrowth.pdf",
        "urls": [
            "https://ejournal.instiki.ac.id/index.php/jurnalresistor/article/download/1527/490",
            "https://ejournal.stmik-sumedang.ac.id/index.php/resistor/article/download/1527/362"
        ]
    },
    {
        "filename": "08_Muharam_2025_JITET_FPGrowth.pdf",
        "urls": [
            "https://journal.eng.unila.ac.id/index.php/jitet/article/download/5935/2368",
            "https://jurnal.fmipa.unila.ac.id/jitet/article/download/5935/2368"
        ]
    }
]

out_dir = os.path.abspath(os.path.join("docs", "REFERENSI_JURNAL_PDF"))
os.makedirs(out_dir, exist_ok=True)

for t in TARGETS:
    dest = os.path.join(out_dir, t["filename"])
    if os.path.exists(dest):
        print(f"Already exists: {t['filename']}")
        continue
    for u in t["urls"]:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                data = resp.read()
                if data.startswith(b'%PDF'):
                    with open(dest, 'wb') as f:
                        f.write(data)
                    print(f"[SUCCESS] Downloaded: {t['filename']} ({len(data):,} bytes)")
                    break
                else:
                    # check if there's html wrapper
                    text = data.decode('utf-8', errors='ignore')
                    import re
                    m = re.search(r'href=["\']([^"\']+\.pdf[^"\']*)["\']', text) or re.search(r'src=["\']([^"\']+\.pdf[^"\']*)["\']', text)
                    if m:
                        pdf_link = m.group(1)
                        req2 = urllib.request.Request(pdf_link, headers=HEADERS)
                        with urllib.request.urlopen(req2, context=ctx, timeout=15) as resp2:
                            pdf_bytes = resp2.read()
                            with open(dest, 'wb') as f:
                                f.write(pdf_bytes)
                            print(f"[SUCCESS] Downloaded via wrapper: {t['filename']} ({len(pdf_bytes):,} bytes)")
                            break
        except Exception as e:
            print(f"  Attempt {u} failed: {e}")

print("\nFinished downloading target PDFs.")
