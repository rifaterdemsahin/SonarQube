# Define the directory path
$outlinePath = "C:\projects\SonarQube\8_Packing\1_outline\"

# Get all markdown files in the directory
$markdownFiles = Get-ChildItem -Path $outlinePath -Filter "*.md" -File

# Sort files logically for version numbers
$markdownFiles = $markdownFiles | Sort-Object -Property {
    # Extract numbers from the filename and pad them with zeros for proper sorting
    $filename = $_.BaseName
    
    if ($filename -match '([\d\.]+)') {
        $versionParts = $matches[1] -split '\.'
        $paddedParts = $versionParts | ForEach-Object { [int]$_.PadLeft(10, '0') }
        $sortableVersion = $paddedParts -join '.'
        return $sortableVersion
    }
    return $filename
}

# Initialize variables
$consolidatedContent = @()
$seenHeaders = @{}
$mainHeader = ""

# Process each markdown file
foreach ($file in $markdownFiles) {
    $content = Get-Content -Path $file.FullName
    
    # Skip empty files
    if ($content -eq $null -or $content.Length -eq 0) {
        continue
    }
    
    # Find the main header (first # header) if not already set
    if ([string]::IsNullOrEmpty($mainHeader)) {
        foreach ($line in $content) {
            if ($line -match '^#\s(.+)') {
                $mainHeader = $matches[1].Trim()
                break
            }
        }
    }
    
    # Process each line in the file
    foreach ($line in $content) {
        # Skip empty lines at the beginning
        if ($consolidatedContent.Count -eq 0 -and [string]::IsNullOrWhiteSpace($line)) {
            continue
        }
        
        # Process headers (## or lower)
        if ($line -match '^(#{2,6})\s(.+)') {
            $headerLevel = $matches[1].Length
            $headerText = $matches[2].Trim()
            
            # Check if we've seen this header before (case insensitive)
            $headerKey = "$headerLevel-$($headerText.ToLower())"
            
            if (-not $seenHeaders.ContainsKey($headerKey)) {
                $seenHeaders[$headerKey] = $true
                $consolidatedContent += $line
            }
        }
        # Process non-header content
        elseif (-not [string]::IsNullOrWhiteSpace($line)) {
            $consolidatedContent += $line
        }
    }
    
    # Add a separator between files
    $consolidatedContent += ""
    $consolidatedContent += "---"
    $consolidatedContent += ""
}

# Create the final output with the main header
$finalOutput = @("# $mainHeader", "") + $consolidatedContent

# Write the output to the console
$finalOutput | Out-String | Write-Output

# Uncomment the following line to write to a file instead
# $finalOutput | Out-File -FilePath "C:\projects\SonarQube\8_Packing\consolidated_outline.md" -Encoding utf8