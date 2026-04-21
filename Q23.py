#Chef has X 5 rupee coins and Y 10 rupee coins. Chef goes to a shop to buy chocolates for Chefina where each chocolate costs 
#Z rupees. Find the maximum number of chocolates that Chef can buy for Chefina.


t=int(input())
for i in range(t):
    X,Y,Z=map(int,input().split())
    A=X*5+Y*10
    print(A//Z)
