# scripts
These are utility scripts.  

note_1.py:

depends on path (pip3 install Path)

the note.py script is a python3 script that appends to a rolling file with the first argument passed on the command line

to run:
python3 note.py "foo bar baz"

This will output the path to the USER_HOME directory where the .note file that keeps track of these files will reside.
The time the note was taken and append to the .note file.
The file will now contain a line like the following.
[0][Wed Mar 15 17:01:29 2023] - foo bar baz

output format:
[note enumeration][local date time of note] - first argument

On unix like systems, I like to keep an open terminal following the note file so I can see these updates in real time:
tail -f ~/.note

