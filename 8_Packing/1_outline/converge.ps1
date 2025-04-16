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

# Process each markdown file
foreach ($file in $markdownFiles) {
    # Add the filename before processing the file content
    $consolidatedContent += ""
    $consolidatedContent += "## File: $($file.Name)"
    $consolidatedContent += ""
    
    # Use UTF-8 encoding for reading files
    $content = Get-Content -Path $file.FullName -Encoding UTF8
    
    # Skip empty files
    if ($content -eq $null -or $content.Length -eq 0) {
        $consolidatedContent += "*Empty file*"
        continue
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

# Create the final output with "# Outline" as the main header
$finalOutput = @("# Outline", "") + $consolidatedContent

# Write the output to the console using UTF-8 encoding
$finalOutput | Out-File -FilePath "$env:TEMP\temp_output.txt" -Encoding UTF8
Get-Content -Path "$env:TEMP\temp_output.txt" -Encoding UTF8 | Write-Output
Remove-Item -Path "$env:TEMP\temp_output.txt"

# Uncomment the following line to write to a file instead
$finalOutput | Out-File -FilePath "C:\projects\SonarQube\8_Packing\1_outline\consolidated_outline.md" -Encoding UTF8