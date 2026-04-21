#You're given an integer N. Write a program to calculate the sum of all the digits of N.


t=int(input())
for i in range(t):
    N=int(input())
    A=0
    while N>0:
        A+=N%10
        N=N//10
    print(A)
