#!/usr/bin/env python3

import os
import subprocess

sourcedir = "/Video/File/Directory"

for file in os.listdir(sourcedir):
    name = file[:file.rfind(".")]
    subprocess.call(["ffmpeg", "-i", sourcedir+"/"+name+".MP4", sourcedir+"/"+name+".mp3"])