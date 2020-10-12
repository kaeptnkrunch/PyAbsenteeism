# Greeting
Write-Host "Fehlzeitquoten Rechner von Stephan Langenau"

# Date
$datum = Get-Date 
Write-Host "Today we have $datum"

# Break
Write-Host "`n"

# Input
$Input1 = Read-Host "Enter your current days of absence"
$Input2 = Read-Host "Enter your current working days"

# calculation
$quote = ($Input1 / $Input2) * 100 

# Break
Write-Host "`n"

# Result
Write-Host "Deine aktuelle Fehlzeitquote am $datum ist $quote"