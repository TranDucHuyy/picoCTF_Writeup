# Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `b60940ca`

Additional details will be available after launching your challenge instance.

# Hints

- Finding a cheatsheet for bash would be really helpful!

# Solution

- After connect to `ssh ctf-player@venus.picoctf.net -p 50440`, use `ls` to check list
- We have part 1 of the flag in `1of3.flag.txt`
- In the `instructions-to-2of3.txt`, follow the prompt and move to `/` and we will take next part of the flag
- Finally we wind find the part 3 in the path `/home/ctf-player`

# Flag
`picoCTF{xxsh_0ut_0f_\/\/4t3r_c1754242}`