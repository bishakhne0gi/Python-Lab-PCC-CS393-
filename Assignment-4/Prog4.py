def is_prime(n):
    for i in range (2,n):
        if(n%i == 0):
            return False
    return True
def twin_prime(lb,ub):
    for i in range(lb,ub-2):
        if(is_prime(i) and is_prime(i+2)):
            print(i," ", i+2)
        i+=2

lb=int(input("Enter the lower bound: "))
ub=int(input("Enter the upper bound: "))
twin_prime(lb,ub)

