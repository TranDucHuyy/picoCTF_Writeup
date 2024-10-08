# Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings) without running it?

# Hints

[string](https://linux.die.net/man/1/strings)

# Solution

- Type of file is ELF(Executable and Linkable Format), in this exercise we use `strings` command to To extract text strings from a file  

- After that, use `grep` to search flag

# Flag 
`picoCTF{5tRIng5_1T_827aee91}`