def is_prime(n):
    for i in range (2,n):
        if(n%i == 0):
            return False
    return True
def is_Pallindrome(n):
    temp=n
    num=0
    while (n!=0):
        d=n%10
        num=num*10+d
        n=n//10
    if(num==temp):
        return True
    else:
        return False

lb=int(input("Enter the lower bound: "))
ub=int(input("Enter the upper bound: "))
for i in range (lb,ub):
    if(is_prime(i) and is_Pallindrome(i)):
        print(i," ")
