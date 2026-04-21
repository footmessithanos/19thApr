#Chef has scored A,B, and C marks in 3 different subjects respectively. Chef will fail if the average score of any two subjects is less than 
#35. Determine whether Chef will pass or fail.


t=int(input())
for i in range(t):
    A,B,C=map(int,input().split())
    if (A+B)/2<35 or (B+C)/2<35 or (A+C)/2<35:
        print("FAIL")
    else:
        print("PASS")
