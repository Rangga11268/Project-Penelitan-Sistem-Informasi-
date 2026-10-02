function Get-GarudaDocInfo($docId) {
    $url = "https://garuda.kemdiktisaintek.go.id/documents/detail/$docId"
    $html = (curl.exe -s -L $url) -join "`n"
    
    $jName = if ($html -match '<div style="margin: 30px">\s*<xmp>(.*?)</xmp>') { $Matches[1].Trim() } else { "N/A" }
    $vol = if ($html -match '<hr>\s*<xmp>(.*?)</xmp>') { $Matches[1].Trim() } else { "N/A" }
    $title = if ($html -match '<h3 class="ui header">\s*<xmp>(.*?)</xmp>\s*</h3>') { $Matches[1].Trim() } else { "N/A" }
    $authors = [regex]::Matches($html, '<a href="/author/view/\d+"><xmp>(.*?)</xmp></a>') | ForEach-Object { $_.Groups[1].Value }
    $download = if ($html -match 'href="([^"]+)"[^>]*>\s*<div class="header"\s*>Download Original</div>') { $Matches[1] } else { "N/A" }
    
    $jId = if ($html -match '/journal/view/(\d+)') { $Matches[1] } else { $null }
    $sinta = "Unknown"
    if ($jId) {
        $jHtml = (curl.exe -s -L "https://garuda.kemdiktisaintek.go.id/journal/view/$jId") -join "`n"
        if ($jHtml -match 'sinta-(\d)') { $sinta = "SINTA " + $Matches[1] }
        elseif ($jHtml -match 'S(\d)') { $sinta = "SINTA " + $Matches[1] }
    }
    
    [PSCustomObject]@{
        DocId = $docId
        Title = $title
        Journal = $jName
        Volume = $vol
        Authors = ($authors -join ', ')
        Download = $download
        Sinta = $sinta
        Url = $url
    }
}

Write-Output "=== 3. RACHMAWATI ET AL (4408461) ==="
Get-GarudaDocInfo "4408461" | Format-List

Write-Output "=== 5. MUHARAM ET AL (5624943) ==="
Get-GarudaDocInfo "5624943" | Format-List
