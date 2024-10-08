# Description

Unzip this archive and find the flag. [Download zip file](https://artifacts.picoctf.net/c/505/big-zip-files.zip)

# Hints

Can grep be instructed to look at every file in a directory and its subdirectories?

# Solution

-  Normally, we use the command line `grep -i` to search text in the file, but in this exercise we need find at all folder after unzip
-  Use `unzip -p big-zip-files.zip | grep -i "picoCTF"` (-p: This option allows unzip to extract the contents of the files in the zip to standard output (stdout) without archiving them to a file)

# Flag
`picoCTF{gr3p_15_m4g1c_ef8790dc}`