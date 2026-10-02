$ids = @("3087354", "3165017", "4408461", "3073417", "5624943")

function Verify-Doc($docId) {
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
    
    # Test download link
    $dlStatus = "Untested"
    if ($download -ne "N/A") {
        $head = curl.exe -s -L -I -m 5 $download
        if ($head -match 'HTTP/\S+\s+(\d+)') {
            $dlStatus = $Matches[1]
        }
    }
    
    [PSCustomObject]@{
        DocId = $docId
        Title = $title
        Journal = $jName
        Volume = $vol
        Authors = ($authors -join ', ')
        Download = $download
        DL_Status = $dlStatus
        Sinta = $sinta
        Garuda_Url = $url
    }
}

foreach ($id in $ids) {
    Verify-Doc $id | Format-List
}
