$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $docPath = Join-Path (Get-Location) "NabiMuhammad.docx"
    $htmlPath = Join-Path (Get-Location) "exported.html"
    $doc = $word.Documents.Open($docPath)
    $doc.SaveAs2($htmlPath, 8) # 8 is wdFormatHTML
    $doc.Close()
    Write-Host "Export successful"
} catch {
    Write-Host "Error: $_"
} finally {
    $word.Quit()
}
