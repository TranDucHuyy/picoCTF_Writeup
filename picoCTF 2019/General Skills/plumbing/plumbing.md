# Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 7480`.

# Hints

- Remember the flag format is picoCTF{XXXX}
- What's a pipe? No not that kind of pipe... This [kind](http://www.linfo.org/pipes.html)

# Solution

- After connect to server, we can see a lot of content divided into many lines, can not search flag in each line
- So we can combine the pipe `|` with `grep` to search for specific text within the output of a command. The pipe `|` takes the output of one command and passes it as input to another command

# Flag 
`picoCTF{digital_plumb3r_06e9d954}`