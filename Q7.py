#Write a program to find the factorial value of any number entered by the user.





t=int(input())
for i in range(t):
    N=int(input())
    a=1
    for i in range(1,N+1):
        a=a*i
    print(a)
