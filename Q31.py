#Chef is given two integers A and C such that A≤C. Chef wants to find whether there exists any integer B such that A,B, and C are in arithmetic progression.
#For each test case, output −1 if there exists no integer B such that A, B, and C are in arithmetic progression. Else then output the value of B.




t=int(input())
for i in range(t):
    A,C=map(int,input().split())
    if (A+C)%2==0:
        print((A+C)//2)
    else:
        print(-1)

