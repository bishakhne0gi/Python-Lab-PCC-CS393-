def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
str=input("Enter the string: ")
n_str=str
if(n_str== reverse(str)):
    print("Is Pallindrome")
else:
    print("Not Pallindrome")