#Write a program to obtain a number N and increment its value by 1, if the number is divisible by 4 otherwise decrement its value by 1.

N=int(input())
if(N%4==0):
    print(N+1)
else:
    print(N-1)
