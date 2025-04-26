#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
creation_path="$SCRIPT_DIR/kanban"

# Initialize counters
lo_count=0
video_count=0
scene_count=0
intro_count=0
hol_count=0
ivq_count=0

# Create the base directory if it doesn't exist
mkdir -p "$creation_path"
echo "📁 Base directory created at: $creation_path"

echo "🚀 Starting production artifact creation..."

# Loop through each learning objective
for ((lo=1; lo<=3; lo++)); do
    lo_dir="$creation_path/LO_$lo"
    mkdir -p "$lo_dir"
    ((lo_count++))
    echo "📁 Created LO directory at: $lo_dir"

    # Create Intro file with Hook and Objective sections
    intro_file="$lo_dir/Intro.md"
    mkdir -p "$(dirname "$intro_file")"
    {
        echo "# Hook"
        echo "## Status"
        echo "### Data"
        echo ""
        echo "# Objective"
        echo "## Status"
        echo "### Data"
    } > "$intro_file"
    ((intro_count++))
    echo "📝 Created Intro file at: $intro_file"

    # Create Videos directory and files
    for ((video=1; video<=3; video++)); do
        video_dir="$lo_dir/Video_$video"
        mkdir -p "$video_dir"
        ((video_count++))
        echo "📁 Created Video directory at: $video_dir"

        # Create scenes for each video
        for ((scene=1; scene<=5; scene++)); do
            scene_file="$video_dir/Scene_$scene.md"
            mkdir -p "$(dirname "$scene_file")"
            {
                echo "# Subject"
                echo "## Status"
                echo "### Data"
            } > "$scene_file"
            ((scene_count++))
            echo "📝 Created scene file at: $scene_file"
        done
    done

    # Create Hands-On Learning file
    hol_file="$lo_dir/Hands_On_Learning.md"
    mkdir -p "$(dirname "$hol_file")"
    {
        echo "# Subject"
        echo "## Status"
        echo "### Data"
    } > "$hol_file"
    ((hol_count++))
    echo "📝 Created Hands-On Learning file at: $hol_file"

    # Create In-Video Questions file
    ivq_file="$lo_dir/In_Video_Questions.md"
    mkdir -p "$(dirname "$ivq_file")"
    {
        echo "# Subject"
        echo "## Status"
        echo "### Data"
    } > "$ivq_file"
    ((ivq_count++))
    echo "📝 Created In-Video Questions file at: $ivq_file"
done

echo "✅ Production artifact creation complete!"

# Verification step
echo "🔍 Verifying created files..."
expected_files=$((scene_count + intro_count + hol_count + ivq_count))
actual_files=$(find "$creation_path" -type f -name "*.md" | wc -l)

if [ "$actual_files" -eq "$expected_files" ]; then
    echo "✅ Verification successful! All $expected_files files were created."
else
    echo "❌ Verification failed! Expected $expected_files files but found $actual_files files."
    echo "Please check the following paths for missing files:"
    find "$creation_path" -type d
fi

echo "📊 Creation Summary:"
echo "   Learning Objectives created: $lo_count"
echo "   Videos created: $video_count"
echo "   Scenes created: $scene_count"
echo "   Intro files created: $intro_count"
echo "   Hands-On Learning files created: $hol_count"
echo "   In-Video Questions files created: $ivq_count"
echo "   Total files created: $((scene_count + intro_count + hol_count + ivq_count))"
echo "   Total directories created: $((lo_count + video_count))"
echo ""
echo "📂 Full directory structure:"
find "$creation_path" -type d | sort
