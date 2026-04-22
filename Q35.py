#You have N cars that can seat 5 people each and M cars that can seat 7 people each. Determine the maximum number of people that can travel together in these cars.



t=int(input())
for i in range(t):
    N,M=map(int,input().split())
    print(N*5+M*7)
