#You are given an array A of size N and an element X, Your task is to find whether the array A contains the element X or not.



N,X=map(int,input().split())
A=list(map(int,input().split()))
if X in A:
    print("YES")
else: 
    print("NO")
