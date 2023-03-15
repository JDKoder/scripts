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

#depends on pathlib to get home directory of user in environment
str_home_path = str(Path.home())
print (f'Path: { str_home_path }')
str_conf_file_path = str_home_path + "/.note"
conf_file_path = Path(str_conf_file_path)

fmode = 'w'

if conf_file_path.is_file():
  fmode = 'a'

fp = open(str_conf_file_path, fmode)
localTime = time.asctime(time.localtime())
print(f'localtime: {localTime}')

"""invocations of note should append to the file as follows
{date time} - {note}note\n
""" 

fp.write(localTime + ' - ' + sys.argv[1] + '\n')
fp.close()




