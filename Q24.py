#Write a program to find the remainder when an integer A is divided by an integer B.



t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    print(A%B)
