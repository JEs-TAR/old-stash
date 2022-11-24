#factorial function

n = input("Hey! enter the number you wanna find the factorial for: ")

while n.isdigit()==False:
    n = int(input("Hey! enter the number you wanna find the factorial for: "))
    n=int(n)


def findin():
    global n
    ans=1
    for j in range(1,n+1):
        ans=ans*j
    print(f'The factorial is {ans}')    


findin()

