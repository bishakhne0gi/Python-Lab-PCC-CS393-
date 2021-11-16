n=int(input("Enter the number to be inserted: "))
lst=[]
n_lst=[]
m=int(input("Enter the number of elements: "))

for i in range(0,m):
    ele=int(input())
    lst.append(ele)

print(lst)

def inerstion():
    count =0
    while(count<=m):
        lst.insert(count,n)
        print(lst)
        count+=1
        lst.remove(n)

inerstion()


