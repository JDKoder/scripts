from pathlib import Path
import sys
import time
import os

LINE_NUM_SEPARATOR = ']'
NOTE_CONFIG_FILE = ".note"
REPLACEMENT_CONFIG_FILE = ".note_tmp"
enumerator = 0

#depends on pathlib to get home directory of user in environment
str_home_path = str(Path.home())

fp = open(str_home_path + "/" + NOTE_CONFIG_FILE, 'r')
#start at the beginning of the file
fp.seek(0)
#read each line prepending it with the next integer
content_buffer = ""
for line in fp:
    fp.readline()
    content_buffer += "[" + str(enumerator) + "]" + line
    enumerator += 1
fp.close()

new_file = open(str_home_path + "/" + REPLACEMENT_CONFIG_FILE, "w")
new_file.write(content_buffer)
new_file.close()