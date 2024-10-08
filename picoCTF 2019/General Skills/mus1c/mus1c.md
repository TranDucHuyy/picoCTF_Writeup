# Description

I wrote you a [song](https://jupiter.challenges.picoctf.org/static/c594d8d915de0129d92b4c41e25a2313/lyrics.txt). Put it in the picoCTF{} flag format.

# Hints

Do you think you can master rockstar?

# Solution

- Decode by [rockstar-py](https://web.archive.org/web/20190101232934/https://github.com/yanorestes/rockstar-py)   
- After we install rockstar-py, we need run the conversion by  `rockstar-py lyrics.txt --output output.py` to compile code in `lyrics.txt`

- Access to [rockstar online](https://codewithrockstar.com/online) to decode in file `lyrics.txt`

- Then we use `python3` to decode by function `chr()`
![alt text](/image/1.png)

# Flag
`picoCTF{rrrocknrn0113r}`