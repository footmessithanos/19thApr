#Write a program in the IDE which does the followingmAccepts the count of test cases - t - in the 1st line First line of each test case consists of a string 
#S You need to perform the following operation Create a variable X which contains the string S concatenated with the string S
#Output X for each test case



t = int(input())
for i in range(t):
    S=input()
    X=S+S 
    print(X)
