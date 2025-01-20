# Video to WebP Converter

This Python script converts video files from a specified input folder into WebP format, saving the converted files in a specified output folder. 
The script uses `ffmpeg` via the `ffmpeg-python` library to perform the conversion, allowing you to manage video quality and encoding settings.

## Features

- Supports various video formats: `.mp4`, `.avi`, `.mov`, `.mkv`, `.webm`
- Converts videos to WebP format with adjustable quality settings
- Uses `ffmpeg` for reliable and efficient video processing
- Automatically creates the output folder if it does not exist
- Customizable encoding parameters for better quality control

## Note on Empty Directories

This project includes empty `input` and `output` directories tracked using `.gitkeep` files to ensure they are present in the repository. You can safely delete them.

## Requirements

- Python 3.6 or higher
- `ffmpeg` installed on your system
- `ffmpeg-python` package installed

## Installation

1. **Install `ffmpeg`:**

   Make sure `ffmpeg` is installed on your system and is accessible from the command line. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html) and follow the installation instructions for your operating system.

2. **Install the `ffmpeg-python` package:**

   You can install the required Python package using `pip`:

   ```bash
   pip install ffmpeg-python
