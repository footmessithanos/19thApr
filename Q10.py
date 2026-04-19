#Alice and Bob are playing a game. Each player rolls a standard six-sided die three times. The score of a player is calculated as the sum of the two
#highest rolls. The player with the higher score wins. If both players have the same score, the game ends in a tie.
#Determine the winner of the game or if it is a tie.




t=int(input())
for i in range(t):
    A1,A2,A3,B1,B2,B3=map(int,input().split())
    A=A1+A2+A3-min(A1,A2,A3)
    B=B1+B2+B3-min(B1,B2,B3)
    if(A>B):
        print("Alice")
    elif(B>A):
        print("Bob")
    else:
        print("Tie")
