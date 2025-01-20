import os
import ffmpeg

def convert_videos_to_webp(input_folder, output_folder):
    # Validate input folder
    if not os.path.exists(input_folder) or not os.path.isdir(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist or is not a directory.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get list of video files in the input folder
    video_files = [
        f for f in os.listdir(input_folder) 
        if f.endswith(('.mp4', '.avi', '.mov', '.mkv', '.webm'))
    ]

    if not video_files:
        print(f"No video files found in '{input_folder}'.")
        return

    # Convert each video to WebP
    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(output_folder, os.path.splitext(video_file)[0] + '.webp')

        # Run ffmpeg command. Refer to the ffmpeg documentation for more information on the options used here.
        ffmpeg.input(input_path).output(
            output_path,
            vcodec='libwebp',   # Video codec for WebP
            loop=0, # How many times to loop the animation (0 for infinite loop)
            lossless=1, # Determine whether to use lossless compression. 0 is lossy, 1 is lossless
            crf=0,  # Adjust balance between quality and size. 0 is best quality, 100 is smallest file size
            preset='default', # Preset for the encoding process. 'default' is a good balance between speed and quality
            pix_fmt='yuv420p',  # Pixel format. Alternatives are 'yuv444p' and 'yuv422p'
            qscale=5    # Quality scale. 0 is best quality, 100 is worst quality
        ).run(overwrite_output=True)

        print(f'Conversion of {video_file} to WebP completed')

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    convert_videos_to_webp(input_folder, output_folder)
