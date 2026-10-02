import os
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

FALLBACK_PAPERS = [
    {
        "filename": "03_Subakti_2022_Apriori_OliMotor.pdf",
        "urls": [
            "http://ejournal.polbeng.ac.id/index.php/ISI/article/download/2684/1468",
            "https://garuda.kemdikbud.go.id/documents/detail/3058498"
        ]
    },
    {
        "filename": "06_Rachmawati_2024_Apriori_vs_FPGrowth.pdf",
        "urls": [
            "https://ejournal.stmik-sumedang.ac.id/index.php/resistor/article/download/1527/362",
            "https://garuda.kemdikbud.go.id/documents/detail/3739775"
        ]
    },
    {
        "filename": "10_Pratama_2024_Generation_FPGrowth.pdf",
        "urls": [
            "https://ojs.unik-kediri.ac.id/index.php/gj/article/download/22994/2104",
            "https://journal.trunojoyo.ac.id/rekayasa/article/download/11365/6303"
        ]
    }
]

out_dir = os.path.abspath(os.path.join("docs", "REFERENSI_JURNAL_PDF"))

for p in FALLBACK_PAPERS:
    target = os.path.join(out_dir, p["filename"])
    if os.path.exists(target):
        continue
    for u in p["urls"]:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
                data = resp.read()
                if data.startswith(b'%PDF'):
                    with open(target, 'wb') as f:
                        f.write(data)
                    print(f"Downloaded fallback {p['filename']} ({len(data):,} bytes)")
                    break
        except Exception as e:
            pass

print("Done fallback check.")
