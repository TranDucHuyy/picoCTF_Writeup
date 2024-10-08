# Description

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/14/level2.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/14/level2.flag.txt.enc) in the same directory too.

# Hints

- To view the file in the webshell, do: `$ nano level1.py`
- To exit `nano`, press Ctrl and x and follow the on-screen prompts.
- The `str_xor` function does not need to be reverse engineered for this challenge.

# Solution

- After run code by `python3 level2.py`, we need enter the password to find the flag
- Read source code, we need decrypt `chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)` to take the password
- Just print the result 
> ![alt text](/Beginner%20picoMini%202022/image/image2.png)
# Flag
`picoCTF{tr45h_51ng1ng_9701e681}`