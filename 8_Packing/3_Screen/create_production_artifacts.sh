#!/bin/bash

# Number of sections to create
NUM_SECTIONS=1

echo "🚀 Starting production artifact creation..."

# Loop through each section
for ((section=1; section<=NUM_SECTIONS; section++)); do
    section_id="1.$section"
    section_dir="Section_$section_id"
    mkdir -p "$section_dir"
    echo "📁 Created section directory: $section_dir"

    # Loop through each learning objective
    for ((lo=1; lo<=3; lo++)); do
        lo_dir="$section_dir/LO_$lo"
        mkdir -p "$lo_dir"
        echo "🎯 Created LO directory: $lo_dir"

        # Loop through each video
        for ((video=1; video<=3; video++)); do
            video_dir="$lo_dir/Video_$video"
            mkdir -p "$video_dir"
            echo "🎬 Created Video directory: $video_dir"

            # Loop through each scene
            for ((scene=1; scene<=5; scene++)); do
                scene_file="$video_dir/Scene_$scene.md"
                {
                    echo "# Subject"
                    echo "## Status"
                    echo "### Data"
                } > "$scene_file"
                echo "📝 Created scene file: $scene_file"
            done
        done

        # Create Hands-On Learning file
        {
            echo "# Subject"
            echo "## Status"
            echo "### Data"
        } > "$lo_dir/Hands_On_Learning.md"
        echo "🤲 Created Hands-On Learning file: $lo_dir/Hands_On_Learning.md"

        # Create In-Video Questions file
        {
            echo "# Subject"
            echo "## Status"
            echo "### Data"
        } > "$lo_dir/In_Video_Questions.md"
        echo "❓ Created In-Video Questions file: $lo_dir/In_Video_Questions.md"
    done
done

echo "✅ Production artifact creation complete!"
