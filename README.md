# video-to-audio
This script takes video files and extracts the audio.

## Setup
The script requires Python 3 and ffmpeg library.

To install Python 3 see https://www.python.org/downloads/

To install FFmpeg view https://ffmpeg.org/download.html

For mp3 conversion please install FFmpeg with the following option --enable-libmp3lame

## Usage
In order to run the file navigate to the file path of the script. The next command depends on your Python configuration. 
If python3 is set as the default Python version the use:
```
python videoToAudio.py
``` 
If a different Python version is set then use:
```
python3 videoToAudio.py
```