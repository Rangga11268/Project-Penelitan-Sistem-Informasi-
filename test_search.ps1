function Check-Query($q) {
    $encoded = [System.Uri]::EscapeDataString($q)
    $url = "https://garuda.kemdiktisaintek.go.id/documents?q=$encoded"
    $html = (curl.exe -s -L $url) -join "`n"
    $matches = [regex]::Matches($html, '<a class="title-article" href="/documents/detail/(\d+)">\s*([\s\S]*?)\s*</a>')
    Write-Output "=== QUERY: $q (Found: $($matches.Count)) ==="
    $matches | Select-Object -First 5 | ForEach-Object {
        $did = $_.Groups[1].Value
        $t = ($_.Groups[2].Value -replace '\s+', ' ').Trim()
        Write-Output "[$did] $t"
    }
}

Check-Query "pola penjualan pupuk"
Check-Query "Rachmawati pupuk"
Check-Query "Perbandingan Algoritma Apriori dan Algoritma FP Growth dalam Menentukan Pola Penjualan Pupuk"
Check-Query "Piknik Cafe"
Check-Query "Muharam"
Check-Query "JSINBIS Market Basket"
Check-Query "Ramadhan Sensuse"
