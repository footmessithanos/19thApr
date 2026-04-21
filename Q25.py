#Chef has started working at the candy store. The store has 100 chocolates in total.
#Chef’s daily goal is to sell X chocolates. For each chocolate sold, he will get 1 rupee. However, if Chef exceeds his daily goal, he gets 
#2 rupees per chocolate for each extra chocolate. If Chef sells Y chocolates in a day, find the total amount he made.



t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    if(X>=Y):
        print(Y)
    else:
        A=Y-X
        print(A*2+X)
