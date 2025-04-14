# Define the directory path
$outlinePath = "C:\projects\SonarQube\8_Packing\1_outline\"

# Get all markdown files in the directory
$markdownFiles = Get-ChildItem -Path $outlinePath -Filter "*.md" -File

# Sort files logically for version numbers
$markdownFiles = $markdownFiles | Sort-Object -Property {
    # Extract version number from filename
    if ($_.BaseName -match '(\d+)\.(\d+)\.?(\d*)') {
        # Convert to numeric arrays for proper numeric sorting
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        # If third segment exists, use it, otherwise default to 0
        $patch = if ($matches[3]) { [int]$matches[3] } else { 0 }
        
        # Create a sortable string with padded numbers
        return "{0:D10}.{1:D10}.{2:D10}" -f $major, $minor, $patch
    }
    elseif ($_.BaseName -match '(\d+)\.(\d+)') {
        # Handle cases with just major.minor
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        
        # Create a sortable string with padded numbers
        return "{0:D10}.{1:D10}.{2:D10}" -f $major, $minor, 0
    }
    else {
        # Default case for non-version filenames
        return $_.BaseName
    }
}

# Initialize variables
$consolidatedContent = @()
$mainHeader = ""

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
    
    # Add all content from the file
    foreach ($line in $content) {
        $consolidatedContent += $line
    }
    
    # Add a separator between files
    $consolidatedContent += ""
    $consolidatedContent += "---"
    $consolidatedContent += ""
}

# Create the final output with the main header on one line at the top
$finalOutput = @("# $mainHeader", "") + $consolidatedContent

# Write the output to the console
$finalOutput | Out-String | Write-Output

# Uncomment the following line to write to a file instead
$finalOutput | Out-File -FilePath "C:\projects\SonarQube\8_Packing\1_outline\consolidated_outline.md" -Encoding utf8