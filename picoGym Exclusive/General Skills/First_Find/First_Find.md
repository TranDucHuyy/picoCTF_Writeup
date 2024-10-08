# Description

Unzip this archive and find the file named 'uber-secret.txt'. [Download zip file](https://artifacts.picoctf.net/c/501/files.zip)


# Hints

None

# Solution

-  Use `unzip -p big-zip-files.zip | grep -i "picoCTF"` (-p: This option allows unzip to extract the contents of the files in the zip to standard output (stdout) without archiving them to a file)

# Flag
`picoCTF{f1nd_15_f457_ab443fd1}`