# Description

Can you convert the number 42 (base 10) to binary (base 2)? 

# Hints

Submit your answer in our competition's flag format. For example, if your answer was '11111', you would submit 'picoCTF{11111}' as the flag.

# Solution

- Use [cyberchef](https://gchq.github.io/CyberChef/) to convert the number 42 (base 10) to binary (base 2)
- Or use `bc` tool in linux to convert base 10 to base 2 
  - `echo "obase=2; 42" | bc`

# Flag

 `picoCTF{101010}`