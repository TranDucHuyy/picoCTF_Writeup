# Description

Python scripts are invoked kind of like programs in the Terminal... Can you run this [Python script](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py) using [this password](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/pw.txt) to get [the flag](https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/flag.txt.en)?

# Hints

- Get the Python script accessible in your shell by entering the following command in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/b351a89e0bc6745b00716849105f87c6/ende.py`
- `$ man python`

# Solution

- In the source code `ende.py`, the author has left us a hint on how to use encrypt and decrypt in python using `-e` or `-d`

- In this post we need to use `-d` to run the source code and enter the available password to find the flag

# Flag
`picoCTF{4p0110_1n_7h3_h0us3_67c6cc96}`