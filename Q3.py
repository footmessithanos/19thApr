#Chef is struggling to pass a certain college course. The test has a total of N questions, each question carries 3 marks for a correct answer and 
#−1 for an incorrect answer. Chef is a risk-averse person so he decided to attempt all the questions. It is known that Chef got 
#X questions correct and the rest of them incorrect. For Chef to pass the course he must score at least P marks.
#Will Chef be able to pass the exam or not?






t=int(input())
for i in range(t):
    N,X,P=map(int,input().split())
    a=X*3
    b=(N-X)*(-1)
    c=a+b
    if(c>=P):
        print("PASS")
    else:
        print("FAIL")
