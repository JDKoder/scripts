#new version
"""
NAME note.py - single line note taker written in python
SYNOPSIS
  note.py [message]
DESCRIPTION:
  If no arguments are given, this assumes the message which should be wrapped in double-quotes is written to the .note file in the user's home directory specified by the systems python implementation of pathlib.Path.Path.home().

"""

from pathlib import Path
import sys
import time
import os

LINE_NUM_SEPARATOR = ']'
NOTE_CONFIG_FILE = ".note"

#depends on pathlib to get home directory of user in environment
str_home_path = str(Path.home())
print (f'Path: { str_home_path }')
str_conf_file_path = str_home_path + "/" + NOTE_CONFIG_FILE
conf_file_path = Path(str_conf_file_path)

fmode = 'w'
nextint = 0

if conf_file_path.is_file():
  fmode = 'a'

last_line = ""
#read last line from file in binary mode to avoid looping through each line.
with open(str_conf_file_path, 'rb') as f:
    try:  # catch OSError in case of a one line file 
      f.seek(-2, os.SEEK_END)
      while f.read(1) != b'\n':
          f.seek(-2, os.SEEK_CUR)
      last_line = f.readline().decode()
    except OSError:
      f.seek(0)
    finally:
      f.close()

#print(f'last line {last_line}')
close_line_number = last_line.find(LINE_NUM_SEPARATOR)
#print(f'close index {close_line_number}')
last_note_int = last_line[1:close_line_number]
#print(f'last note int {last_note_int}')
fp = open(str_conf_file_path, fmode)

localTime = time.asctime(time.localtime())
print(f'localtime: {localTime}')

try:
    last_note_int = str(int(last_note_int) + 1)
except ValueError:
    print(f'value at beginning of last line was not an integer: {last_note_int}')
    last_note_int = "0"

#invocations of note should append to the file as follows
#[nextint][{date time}] - {note}note\n
 

#TODO build a message decorating based on subcommands and option arguments

fp.write('[' + last_note_int + ']' + localTime + ' - ' + sys.argv[1] + '\n')
fp.close()




