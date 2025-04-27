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
unique_scene_number=1

# Create the base directory if it doesn't exist
mkdir -p "$creation_path"
echo "📁 Base directory created at: $creation_path"

echo "🚀 Starting production artifact creation..."

# Create Main Intro with Video
main_intro_dir="$creation_path/1_Main_Intro"
mkdir -p "$main_intro_dir"
echo "📁 Created Main Intro directory at: $main_intro_dir"

# Create Main Intro Video
main_intro_video_dir="$main_intro_dir/Video_1"
mkdir -p "$main_intro_video_dir"
((video_count++))
echo "📁 Created Main Intro Video directory at: $main_intro_video_dir"

# Create scenes for Main Intro Video
for ((scene=1; scene<=4; scene++)); do
    scene_dir="$main_intro_video_dir/Scene_$unique_scene_number"
    mkdir -p "$scene_dir"
    
    # Create Show file
    show_file="$scene_dir/1_Show.json"
    {
        echo "{"
        echo "  \"title\": \"Show\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $unique_scene_number,"
        echo "  \"edittingStyle\": \"Show the goal at the beginning of the scene\","
        echo "  \"notes\": {"
        echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
        echo "  }"
        echo "}"
    } > "$show_file"
    echo "📝 Created Show file at: $show_file"
    
    # Create Tell file
    tell_file="$scene_dir/2_Tell.json"
    {
        echo "{"
        echo "  \"title\": \"Tell\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $unique_scene_number,"
        echo "  \"edittingStyle\": \"Show lower thirds at the timing of the scene and check the audio and match it\","
        echo "  \"notes\": {"
        echo "    \"data\": \"backlog\""
        echo "  }"
        echo "}"
    } > "$tell_file"
    echo "📝 Created Tell file at: $tell_file"
    
    # Create Do file
    do_file="$scene_dir/3_Do.json"
    {
        echo "{"
        echo "  \"title\": \"Do\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $unique_scene_number,"
        echo "  \"edittingStyle\": \"The action part of the video it comes in the aroll and video capture, time it with the audio\","
        echo "  \"notes\": {"
        echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
        echo "  }"
        echo "}"
    } > "$do_file"
    echo "📝 Created Do file at: $do_file"
    
    ((scene_count++))
    ((unique_scene_number++))
    echo "📁 Created scene directory at: $scene_dir"
done

# Loop through each learning objective
for ((lo=1; lo<=4; lo++)); do
    lo_dir="$creation_path/2_LO_$lo"
    mkdir -p "$lo_dir"
    ((lo_count++))
    echo "📁 Created LO directory at: $lo_dir"

    # Create Intro file with Hook and Objective sections
    intro_file="$lo_dir/Intro.json"
    mkdir -p "$(dirname "$intro_file")"
    {
        echo "{"
        echo "  \"hook\": {"
        echo "    \"status\": {"
        echo "      \"data\": \"backlog\""
        echo "    }"
        echo "  },"
        echo "  \"objective\": {"
        echo "    \"status\": {"
        echo "      \"data\": \"backlog\""
        echo "    }"
        echo "  },"
        echo "  \"edittingStyle\": \"Create engaging hook and clear learning objectives\","
        echo "  \"notes\": {"
        echo "    \"data\": \"backlog\""
        echo "  }"
        echo "}"
    } > "$intro_file"
    ((intro_count++))
    echo "📝 Created Intro file at: $intro_file"

    # Determine number of videos for this LO
    if [ "$lo" -eq 2 ]; then
        num_videos=6
    else
        num_videos=3
    fi

    # Create Videos directory and files
    for ((video=1; video<=num_videos; video++)); do
        video_dir="$lo_dir/Video_$video"
        mkdir -p "$video_dir"
        ((video_count++))
        echo "📁 Created Video directory at: $video_dir"

        # Create scenes for each video
        for ((scene=1; scene<=5; scene++)); do
            scene_dir="$video_dir/Scene_$unique_scene_number"
            mkdir -p "$scene_dir"
            
            # Create Show file
            show_file="$scene_dir/1_Show.json"
            {
                echo "{"
                echo "  \"title\": \"Show\","
                echo "  \"status\": {"
                echo "    \"data\": \"backlog\""
                echo "  },"
                echo "  \"sceneNumber\": $unique_scene_number,"
                echo "  \"edittingStyle\": \"Show the goal at the beginning of the scene\","
                echo "  \"notes\": {"
                echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
                echo "  }"
                echo "}"
            } > "$show_file"
            echo "📝 Created Show file at: $show_file"
            
            # Create Tell file
            tell_file="$scene_dir/2_Tell.json"
            {
                echo "{"
                echo "  \"title\": \"Tell\","
                echo "  \"status\": {"
                echo "    \"data\": \"backlog\""
                echo "  },"
                echo "  \"sceneNumber\": $unique_scene_number,"
                echo "  \"edittingStyle\": \"Show lower thirds at the timing of the scene and check the audio and match it\","
                echo "  \"notes\": {"
                echo "    \"data\": \"backlog\""
                echo "  }"
                echo "}"
            } > "$tell_file"
            echo "📝 Created Tell file at: $tell_file"
            
            # Create Do file
            do_file="$scene_dir/3_Do.json"
            {
                echo "{"
                echo "  \"title\": \"Do\","
                echo "  \"status\": {"
                echo "    \"data\": \"backlog\""
                echo "  },"
                echo "  \"sceneNumber\": $unique_scene_number,"
                echo "  \"edittingStyle\": \"The action part of the video it comes in the aroll and video capture, time it with the audio\","
                echo "  \"notes\": {"
                echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
                echo "  }"
                echo "}"
            } > "$do_file"
            echo "📝 Created Do file at: $do_file"
            
            ((scene_count++))
            ((unique_scene_number++))
            echo "📁 Created scene directory at: $scene_dir"
        done
    done

    # Create Hands-On Learning file
    hol_file="$lo_dir/Hands_On_Learning.json"
    mkdir -p "$(dirname "$hol_file")"
    {
        echo "{"
        echo "  \"subject\": {"
        echo "    \"status\": {"
        echo "      \"data\": \"backlog\""
        echo "    }"
        echo "  },"
        echo "  \"edittingStyle\": \"Create practical exercises and demonstrations\","
        echo "  \"notes\": {"
        echo "    \"data\": \"backlog\""
        echo "  }"
        echo "}"
    } > "$hol_file"
    ((hol_count++))
    echo "📝 Created Hands-On Learning file at: $hol_file"

    # Create In-Video Questions file
    ivq_file="$lo_dir/In_Video_Questions.json"
    mkdir -p "$(dirname "$ivq_file")"
    {
        echo "{"
        echo "  \"subject\": {"
        echo "    \"status\": {"
        echo "      \"data\": \"backlog\""
        echo "    }"
        echo "  },"
        echo "  \"edittingStyle\": \"Create engaging questions to test understanding\","
        echo "  \"notes\": {"
        echo "    \"data\": \"backlog\""
        echo "  }"
        echo "}"
    } > "$ivq_file"
    ((ivq_count++))
    echo "📝 Created In-Video Questions file at: $ivq_file"
done

# Create Course Closure with Video
closure_dir="$creation_path/3_Course_Closure"
mkdir -p "$closure_dir"
echo "📁 Created Course Closure directory at: $closure_dir"

# Create Closure Video
closure_video_dir="$closure_dir/Video_1"
mkdir -p "$closure_video_dir"
((video_count++))
echo "📁 Created Closure Video directory at: $closure_video_dir"

# Create scenes for Closure Video
for ((scene=1; scene<=4; scene++)); do
    scene_dir="$closure_video_dir/Scene_$unique_scene_number"
    mkdir -p "$scene_dir"
    
    # Create Show file
    show_file="$scene_dir/1_Show.json"
    {
        echo "{"
        echo "  \"title\": \"Show\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $unique_scene_number,"
        echo "  \"edittingStyle\": \"Show the goal at the beginning of the scene\","
        echo "  \"notes\": {"
        echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
        echo "  }"
        echo "}"
    } > "$show_file"
    echo "📝 Created Show file at: $show_file"
    
    # Create Tell file
    tell_file="$scene_dir/2_Tell.json"
    {
        echo "{"
        echo "  \"title\": \"Tell\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $unique_scene_number,"
        echo "  \"edittingStyle\": \"Show lower thirds at the timing of the scene and check the audio and match it\","
        echo "  \"notes\": {"
        echo "    \"data\": \"backlog\""
        echo "  }"
        echo "}"
    } > "$tell_file"
    echo "📝 Created Tell file at: $tell_file"
    
    # Create Do file
    do_file="$scene_dir/3_Do.json"
    {
        echo "{"
        echo "  \"title\": \"Do\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $unique_scene_number,"
        echo "  \"edittingStyle\": \"The action part of the video it comes in the aroll and video capture, time it with the audio\","
        echo "  \"notes\": {"
        echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
        echo "  }"
        echo "}"
    } > "$do_file"
    echo "📝 Created Do file at: $do_file"
    
    ((scene_count++))
    ((unique_scene_number++))
    echo "📁 Created scene directory at: $scene_dir"
done

# Create Extra Scenes folder
extra_dir="$creation_path/4_Extra"
mkdir -p "$extra_dir"
echo "📁 Created Extra Scenes directory at: $extra_dir"

# Create Extra Scenes (84-100)
for ((scene=84; scene<=100; scene++)); do
    scene_dir="$extra_dir/Scene_$scene"
    mkdir -p "$scene_dir"
    
    # Create Show file
    show_file="$scene_dir/1_Show.json"
    {
        echo "{"
        echo "  \"title\": \"Show\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $scene,"
        echo "  \"edittingStyle\": \"Show the goal at the beginning of the scene\","
        echo "  \"notes\": {"
        echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
        echo "  }"
        echo "}"
    } > "$show_file"
    echo "📝 Created Show file at: $show_file"
    
    # Create Tell file
    tell_file="$scene_dir/2_Tell.json"
    {
        echo "{"
        echo "  \"title\": \"Tell\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $scene,"
        echo "  \"edittingStyle\": \"Show lower thirds at the timing of the scene and check the audio and match it\","
        echo "  \"notes\": {"
        echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
        echo "  }"
        echo "}"
    } > "$tell_file"
    echo "📝 Created Tell file at: $tell_file"
    
    # Create Do file
    do_file="$scene_dir/3_Do.json"
    {
        echo "{"
        echo "  \"title\": \"Do\","
        echo "  \"status\": {"
        echo "    \"data\": \"backlog\""
        echo "  },"
        echo "  \"sceneNumber\": $scene,"
        echo "  \"edittingStyle\": \"The action part of the video it comes in the aroll and video capture, time it with the audio\","
        echo "  \"notes\": {"
        echo "    \"data\": \"Use original authentic content while getting inspired from the producers file. Do not use it directly.\""
        echo "  }"
        echo "}"
    } > "$do_file"
    echo "📝 Created Do file at: $do_file"
    
    ((scene_count++))
    echo "📁 Created extra scene directory at: $scene_dir"
done

echo "✅ Production artifact creation complete!"

# Verification step
echo "🔍 Verifying created files..."
expected_files=$((scene_count * 3 + intro_count + hol_count + ivq_count))
actual_files=$(find "$creation_path" -type f -name "*.json" | wc -l)

if [ "$actual_files" -eq "$expected_files" ]; then
    echo "✅ Verification successful! All $expected_files files were created."
else
    echo "❌ Verification failed! Expected $expected_files files but found $actual_files files."
    echo "Please check the following paths for missing files:"
    find "$creation_path" -type d
fi

echo "📊 Creation Summary:"
echo "   Learning Objectives created: $lo_count"
echo "   Videos created: $video_count (Including Main Intro and Closure videos)"
echo "   Scenes created: $scene_count"
echo "   - Main Course Scenes: 1-$((unique_scene_number-1))"
echo "   - Extra Scenes: 84-100"
echo "   Scene parts created: $((scene_count * 3)) (1_Show, 2_Tell, 3_Do)"
echo "   Intro files created: $intro_count"
echo "   Hands-On Learning files created: $hol_count"
echo "   In-Video Questions files created: $ivq_count"
echo "   Total files created: $((scene_count * 3 + intro_count + hol_count + ivq_count))"
echo "   Total directories created: $((lo_count + video_count + scene_count + 3))"
echo ""
echo "📂 Full directory structure:"
find "$creation_path" -type d | sort
