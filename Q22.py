#Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.



t=int(input())
for i in range(t):
    N=list(map(int,input().split()))
    N.sort()
    print(N[1])
