#Given a list ofN integers, representing height of mountains. Find the height of the tallest mountain.




t=int(input())
for i in range(t):
    N=int(input())
    A=list(map(int,input().split()))
    C=max(A)
    print(C)
