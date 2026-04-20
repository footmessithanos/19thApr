#Write a program to calculate the simple interest for a given principal amount, rate of interest, and time period using a function.




def calculate_simple_interest(P, T, R):
    return P*T*R/100
    

def main():
    P, T, R = map(int, input().split())
    result=calculate_simple_interest(P,T,R)
    print(result)


main()
