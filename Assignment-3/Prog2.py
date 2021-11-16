ls=[]
n=int(input("Enter number of elements: "))
sum=0
for i in range(0,n):
     ele=int(input())
     ls.append(ele)
for i in range(0,n):
    sum+=ls[i]
print(sum)
