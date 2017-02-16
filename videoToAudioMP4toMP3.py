#!/usr/bin/env python3

import os
import subprocess

sourcedirsourceDir = "/Video/File/Directory"


for file in os.listdir(sourcedir):os.listdir(sourceDir):
    name = file[:file.rfind(".")]
    subprocess.call(["ffmpeg", "-i", sourcedir+"/"+name+".MP4", sourcedir+"/"+name+".mp3"])sourceDir+"/"+name+".MP4", sourceDir+"/"+name+".mp3"])