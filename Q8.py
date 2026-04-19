#Chef has just started Programming, he is in first year of Engineering. Chef is reading about Relational Operators.
#Relational Operators are operators which check relationship between two values. Given two numerical values A and B you need to help chef 
#in finding the relationship between them that is,
#First one is greater than second or, First one is less than second or, First and second one are equal.




t=int(input())
for i in range(t):
    A,B=map(int,input().split())
    if A>B:
        print('>')
    elif A<B:
        print('<')
    else:
        print('=')
