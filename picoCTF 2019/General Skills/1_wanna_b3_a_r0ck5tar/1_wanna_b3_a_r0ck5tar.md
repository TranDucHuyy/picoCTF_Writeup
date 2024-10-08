# Description

I wrote you another [song](https://jupiter.challenges.picoctf.org/static/b99c57e4274172bf3c93534b6d59632d/lyrics.txt). Put the flag in the picoCTF{} flag format

# Hints

(None)

# Solution

- But in this exercise, when we use [rockstar online](https://codewithrockstar.com/online) to decode, its not working
![alt text](/image/2.png)

- So we can try compile by [rockstar -py](https://web.archive.org/web/20190101232934/https://github.com/yanorestes/rockstar-py)
  - cmd: `rockstar -py -i lyrics.txt -o output.py`
![alt text](/image/3.png)

- We need analyzing [ouput.txt](/General_skills/1_wanna_b3_a_r0ck5tar/output.py) 
  - Tommy = 66, Music = 79, Jamming = 78, Tommy = 74, `They are dazzled audiences`, Rock = 86, Tommy = 73
  - That's all values number we need decrypt to find flag, but we are missing one value number in `They are dazzled audiences` and we need solve that
  - Go to back `lyrics.txt`, we can see the logic of code. All words with `is, are` will be equivalent operation `=`, so the value we need find is `dazzled audiences`
  - I've read all code rockstar in `lyrics.txt` and i found Their rule is the number of characters after the "=" operator, meaning that each character will be equivalent to 1 value
  - So `dazzled audiences` is 79
  - We have [66, 79, 78, 74, 79, 86, 73] and use `chr()` function in python3 to decode ascii like [mus1c](/General_skills/mus1c/mus1c.md)

# Flag
`picoCTF{BONJOVI}`