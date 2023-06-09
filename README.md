# scripts
These are utility scripts.  

note_1.py:
---------------------
_depends on path (`pip3 install Path`)_

the note.py script is a python3 script that appends to a rolling file with the first argument passed on the command line

to run:
`python3 note.py "foo bar baz"`

This will output the path to the USER_HOME directory where the .note file that keeps track of these files will reside.
The time the note was taken and append to the .note file.
The file will now contain a line like the following.
[0][Wed Mar 15 17:01:29 2023] - foo bar baz

output format:
`[note enumeration][local date time of note] - first argument`

On unix like systems, I like to keep an open terminal following the note file so I can see these updates in real time:
tail -f ~/.note

dbranch.sh:
------------------------
_Depends on git & find_

This shell script is for determining the differing files between 2 github branches.  It uses _find_ to take snapshots of all the files recursively in the current directory. You may specify the end of the file names to search for.

Example:  If you are only interested in the java files that differ between 2 branches the following call with tell where the files are relative the current directory.

to run:
`dbranches mybranch myotherbranch .java`

Also provides other smaller one line utilities:
`currentBranch`: outputs the name of the current github branch
This can also be passed into the dbranches function
`dbranches mybranch $(currentBranch)`

artifacts:
running dbranches leaves artifacts of the run for review.  These can be cleaned up simply by running `dbranchCleanup`
