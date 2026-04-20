#Write a program that first accepts the number of test cases t. For each test case, read an integer num. Check if num is even using the isEven function.
#If num is even, output "Even"; otherwise, output "Odd".




def is_even(num):
    return num%2==0

def main():
    t=int(input())
    for i in range(t):
        num=int(input())
        if is_even(num):
            print("Even")
        else:
            print("Odd")

if __name__ == "__main__":
    main()
