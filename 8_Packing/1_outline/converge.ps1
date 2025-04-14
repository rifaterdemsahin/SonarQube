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
        $paddedParts = $versionParts | ForEach-Object { [int]$_ }
        return [string]::Join('.', $paddedParts)
    }
    return $filename
}

# Initialize variables
$consolidatedContent = @()
$seenHeaders = @{}
$mainHeader = ""
$inWriteOutputSection = $false

# Process each markdown file
foreach ($file in $markdownFiles) {
    # Add the filename before processing the file content
    $consolidatedContent += ""
    $consolidatedContent += "## File: $($file.Name)"
    $consolidatedContent += ""
    
    $content = Get-Content -Path $file.FullName
    
    # Skip empty files
    if ($content -eq $null -or $content.Length -eq 0) {
        $consolidatedContent += "*Empty file*"
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
    $skipContent = $false
    
    foreach ($line in $content) {
        # Skip empty lines at the beginning
        if ($consolidatedContent.Count -eq 0 -and [string]::IsNullOrWhiteSpace($line)) {
            continue
        }
        
        # Handle level 1 headers (# headers) - just include the header line, not content
        if ($line -match '^#\s(.+)') {
            $skipContent = $true  # Start skipping content
            # We don't add the level 1 header to the output as we'll use it as the main title
            continue
        }
        
        # Check for "## Write Output" section
        if ($line -match '^##\s+Write\s+Output') {
            $inWriteOutputSection = $true
            $skipContent = $false  # Stop skipping content for this section
            
            # Add this header if we haven't seen it before
            $headerKey = "2-write output"
            if (-not $seenHeaders.ContainsKey($headerKey)) {
                $seenHeaders[$headerKey] = $true
                $consolidatedContent += $line
            }
            continue
        }
        
        # Start of a new section (any level 2+ header)
        if ($line -match '^(#{2,6})\s(.+)' -and $line -notmatch '^##\s+Write\s+Output') {
            $skipContent = $false  # Stop skipping content for other sections
            $inWriteOutputSection = $false
            
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
        elseif (-not $skipContent -and $inWriteOutputSection -and -not [string]::IsNullOrWhiteSpace($line)) {
            $consolidatedContent += $line
        }
    }
    
    # Add a separator between files
    $consolidatedContent += ""
    $consolidatedContent += "---"
    $consolidatedContent += ""
    
    # Reset flags for the next file
    $inWriteOutputSection = $false
    $skipContent = $false
}

# Create the final output with just the main header on one line
$finalOutput = @("# $mainHeader", "") + $consolidatedContent

# Write the output to the console
$finalOutput | Out-String | Write-Output

# Uncomment the following line to write to a file instead
# $finalOutput | Out-File -FilePath "C:\projects\SonarQube\8_Packing\consolidated_outline.md" -Encoding utf8