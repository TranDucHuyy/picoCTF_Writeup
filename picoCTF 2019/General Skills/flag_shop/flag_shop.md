# Description

There's a flag shop selling stuff, can you buy a flag? [Source](https://jupiter.challenges.picoctf.org/static/64e724ad327f83ad833d9c6baa072b1f/store.c). Connect with `nc jupiter.challenges.picoctf.org 4906`.

# Hints

Two's compliment can do some weird things when numbers get really big!

# Solution

- In the first option we will see the balance in the wallet is 1100
- In the second option, a flag has a value of 1337 and because the balance is not enough, it cannot be purchased. However, there is also a section "Defintely not the flag Flag", when we enter here we will see the price of the fake flag is 900, if we buy, the balance will be 200 more but we will not receive anything.
- Now let's look at the received source code, in the option to buy fake flag, we can see that total_cost is being declared as an int variable (-2,147,483,648 to 2,147,483,647). Assuming we use overflow on the flag count, let's do some basic math:
![alt text](/image/4.png)
> 123,313,231 * 900 = 110,981,907,900 (overflow), the system will keep the low 32-bit part of this number
> 
> 110,981,907,900≡110,981,907,900−(2^32)×N
> 
> Here, we find the value of NN, such that the remainder of the subtraction fits into the range of the 32-bit integer: 110,981,907,900÷(2^32)=25.85
> 
> 110,981,907,900−107,374,182,400=3,607,725,500 (still overflow)
> 
- The system will continue to repeat this process until the final result does not exceed the limit of the value of the int initialized variable. And in this case we will get the answer as −687,241,796

- And now when we check our wallet we will get 687,241,796. Then buy flag for 1337
  
# Flag
`picoCTF{m0n3y_bag5_9c5fac9b}`
