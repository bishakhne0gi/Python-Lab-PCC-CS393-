n=int(input("Enter the number of prices: "))
lst=[]

for i in range(0,n):
    ele=int(input())
    lst.append(ele)
lst.sort()
cp=lst[0]
sp=lst[n-1]
profit=sp-cp
print("SP ",sp,"- CP",cp," = Profit ",profit)
