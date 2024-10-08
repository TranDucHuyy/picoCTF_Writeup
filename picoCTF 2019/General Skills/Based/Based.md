# Description

To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29221`.

# Hints

- I hear python can convert things
- It might help to have multiple win-dows open.

# Solution
After using `nc` to connect `jupiter.challenges.picoctf.org` at port `29221`, we have:

- Method 1: Use [cyberchef](https://gchq.github.io/CyberChef/)

- Method 2: Code python to decode
  - If we want convert binary to ascii, use [binary_to_ascii.py](/General_skills/Based/bina_to_ascii.py)
  - If we want convert binary to ascii, use [heximal_to_ascii.py](/General_skills/Based/hexi_to_ascii.py)
  - If we want convert binary to ascii, use [octal_to_ascii.py](/General_skills/Based/octal_to_ascii.py)

# Flag
 `picoCTF{learning_about_converting_values_00a975ff}`