$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

function Get-GarudaDocInfo($docId) {
    $url = "https://garuda.kemdiktisaintek.go.id/documents/detail/$docId"
    $resp = Invoke-WebRequest -Uri $url -UserAgent $ua -UseBasicParsing -TimeoutSec 15
    $html = $resp.Content
    
    $jName = if ($html -match '<div style="margin: 30px">\s*<xmp>(.*?)</xmp>') { $Matches[1].Trim() } else { "N/A" }
    $vol = if ($html -match '<hr>\s*<xmp>(.*?)</xmp>') { $Matches[1].Trim() } else { "N/A" }
    $title = if ($html -match '<h3 class="ui header">\s*<xmp>(.*?)</xmp>\s*</h3>') { $Matches[1].Trim() } else { "N/A" }
    $authors = [regex]::Matches($html, '<a href="/author/view/\d+"><xmp>(.*?)</xmp></a>') | ForEach-Object { $_.Groups[1].Value }
    $download = if ($html -match 'href="([^"]+)"[^>]*>\s*<div class="header"\s*>Download Original</div>') { $Matches[1] } else { "N/A" }
    
    $jId = if ($html -match '/journal/view/(\d+)') { $Matches[1] } else { $null }
    $sinta = "Unknown"
    if ($jId) {
        $jHtml = (Invoke-WebRequest -Uri "https://garuda.kemdiktisaintek.go.id/journal/view/$jId" -UserAgent $ua -UseBasicParsing -TimeoutSec 15).Content
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
        Status = $resp.StatusCode
        Url = $url
    }
}

function Search-Garuda($q) {
    $encoded = [System.Uri]::EscapeDataString($q)
    $url = "https://garuda.kemdiktisaintek.go.id/documents?q=$encoded"
    $html = (Invoke-WebRequest -Uri $url -UserAgent $ua -UseBasicParsing -TimeoutSec 15).Content
    $matches = [regex]::Matches($html, '<a class="title-article" href="/documents/detail/(\d+)">\s*([\s\S]*?)\s*</a>')
    $matches | ForEach-Object {
        [PSCustomObject]@{
            DocId = $_.Groups[1].Value
            Title = ($_.Groups[2].Value -replace '\s+', ' ').Trim()
        }
    }
}
