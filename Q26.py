#Given A,B, and C as the sides of a triangle, find whether the triangle is scalene.



t=int(input())
for i in range(t):
    A,B,C=map(int,input().split())
    if A!=B and B!=C and A!=C:
        print("YES")
    else:
        print("NO")
