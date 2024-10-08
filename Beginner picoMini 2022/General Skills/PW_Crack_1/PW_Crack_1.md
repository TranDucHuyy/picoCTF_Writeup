# Description

Can you crack the password to get the flag? Download the password checker [here](https://artifacts.picoctf.net/c/12/level1.py) and you'll need the encrypted [flag](https://artifacts.picoctf.net/c/12/level1.flag.txt.enc) in the same directory too.

# Hints

- To view the file in the webshell, do: `$ nano level1.py`
- To exit `nano`, press Ctrl and x and follow the on-screen prompts.
- The `str_xor` function does not need to be reverse engineered for this challenge.

# Solution

- After run code by `python3 level1.py`, we need enter the password to find the flag
- Read source code and we will easy to catch the password

# Flag
`picoCTF{545h_r1ng1ng_1b2fd683}`