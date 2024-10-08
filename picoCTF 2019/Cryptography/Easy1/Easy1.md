# Description

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help `UFJKXQZQUNB` with the key of `SOLVECRYPTO`. Can you use this [table](https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt) to solve it?. 

# Hints

- Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
- Please use all caps for the message.

# Solution

- This is the text encrypted using Vigenere type, to decrypt we need to apply to the alphabet
- 
```
cipher text: UFJKXQZQUNB
Key: SOLVECRYPTO
```

- U at position 20 - S at position 18 = 2 is letter C, continue with other letters

# Flag  
`picoCTF{CRYPTOISFUN}`