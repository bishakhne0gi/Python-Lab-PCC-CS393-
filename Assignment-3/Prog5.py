def check(str):
    n=len(str)
    up,low=0,0
    for i in range(0,n):
        if(str[i].isupper()):
            up+=1
        elif(str[i].islower()):
            low+=1
    print(up," ", low)

str=input("Enter the string: ")
check(str)
        