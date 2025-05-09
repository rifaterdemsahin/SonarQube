#!/bin/bash

# Create necessary directories
mkdir -p scenes
mkdir -p metadata

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Check if PyYAML is installed
if ! python3 -c "import yaml" &> /dev/null; then
    echo "Installing PyYAML..."
    pip3 install pyyaml
fi

# Process all YAML files in the metadata directory
echo "Processing scene metadata files..."
for file in metadata/scene*.yaml; do
    if [ -f "$file" ]; then
        echo "Generating markdown for $file..."
        python3 generate-scene-md.py "$file"
    fi
done

# Check if any files were generated
if [ -z "$(ls -A scenes/)" ]; then
    echo "Warning: No markdown files were generated."
    echo "Please ensure you have YAML files in the metadata/ directory."
    exit 1
fi

echo "Scene generation complete!"
echo "Generated files are in the scenes/ directory." 