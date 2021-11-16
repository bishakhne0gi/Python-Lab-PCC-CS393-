def freq(str):
    max_count=1
    count=1
    n=len(str)
    for i in range(0,n-1):
        if(str[i]==str[i+1]):
            count+=1
            max_count=max(max_count,count)
        else:
            count=1
    print("It is a ",max_count," neighbour")   
str=input("Enter the string: ")
freq(str)