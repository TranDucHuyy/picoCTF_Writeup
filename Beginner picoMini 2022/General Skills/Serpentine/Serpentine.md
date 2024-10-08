# Description

Find the flag in the Python script! [Download Python script](https://artifacts.picoctf.net/c/36/serpentine.py)

# Hints

- Try running the script and see what happens
- In the webshell, try examining the script with a text editor like `nano`
- To exit `nano`, press Ctrl and x and follow the on-screen prompts.
- The `str_xor` function does not need to be reverse engineered for this challenge.

# Solution

- When we run the code, it will display a dashboard with three options
> ![alt text](/Beginner%20picoMini%202022/image/image1.png)

- We need choose option 2 to take the flag, but it will display notification `Oops! I must have misplaced the print_flag function! Check my source code!`

- To solve this problem , we need call the function `flag_enc` in source code to decrypt and take the flag
# Flag
`picoCTF{7h3_r04d_l355_7r4v3l3d_aa2340b2}`