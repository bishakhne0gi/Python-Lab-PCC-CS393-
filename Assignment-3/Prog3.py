ls=[]
n=int(input("Enter number of elements: "))
prod=1
for i in range(0,n):
     ele=int(input())
     ls.append(ele)
for i in range(0,n):
    prod*=ls[i]
print(prod)