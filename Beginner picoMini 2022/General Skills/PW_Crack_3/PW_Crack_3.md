# Description

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/18/level3.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/18/level3.flag.txt.enc) and the [hash](https://artifacts.picoctf.net/c/18/level3.hash.bin) in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

# Hints

- To view the level3.hash.bin file in the webshell, do: `$ bvi level3.hash.bin`
- To exit `bvi` type `:q` and press enter
- The `str_xor` function does not need to be reverse engineered for this challenge.

# Solution

- After run code by `python3 level2.py`, we need enter the password to find the flag
- Read source code, we need decrypt `chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)` to take the password
- Just print the result 
> ![alt text](/Beginner%20picoMini%202022/image/image2.png)


# Flag
`picoCTF{tr45h_51ng1ng_9701e681}`