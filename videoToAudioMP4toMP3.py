#!/usr/bin/env python3

import os
import subprocess

sourceDir = "/Video/File/Directory"

#Choose the file formats below. See https://ffmpeg.org/ffmpeg.html for supported file types.
videoFormat = ".mp4" 
audioFormat = ".mp3"


for file in os.listdir(sourceDir):
    name = file[:file.rfind(".")]
    subprocess.call(["ffmpeg", "-i", sourceDir+"/"+name+".MP4", sourceDir+"/"+name+".mp3"])sourceDir+"/"+name+videoFormat, sourceDir+"/"+name+audioFormat])