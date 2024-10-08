# Description

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm) has extraordinarily helpful information...

# Hints

- This program will only work in the webshell or another Linux computer.
- To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/cfea736820f329083dab9558c3932ada/warm`
- Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm
- -h and --help are the most common arguments to give to programs to get more information from them!
- Not every program implements help features like -h and --help.

# Solution

- For the first, we need check type of file by `file warm`
- It is ELF file, try use `./warm` to run this program 
- System had suggest for us use `-h` and we will find the flag

# Flag
`picoCTF{b1scu1ts_4nd_gr4vy_30e77291}`