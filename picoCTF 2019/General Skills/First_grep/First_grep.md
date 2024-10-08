# Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file)? This would be really tedious to look through manually, something tells me there is a better way.

# Hints

grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

# Solution

- We should check type of file after once downloaded by `wget`

- This file is `Ascii text`, so we can use `cat` to read content in this file

- Remember the syntax of flag in picoCTF is: `picoCTF{FLAG}` and we can use command `grep` to search for text on demand, if you add `-i` then it will ignore uppercase and lowercase letters

- Furthermore, when using the `|` (pipe) operator used to pass the output of one command as input to another command, creating a pipeline

# Flag
`picoCTF{grep_is_good_to_find_things_dba08a45}`