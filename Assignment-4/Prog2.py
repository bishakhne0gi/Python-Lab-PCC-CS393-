s = input("Enter the string: ")

variable = True
while variable and s != "":
    variable = False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            variable = True
            s = s[:(i)] + s[(i+2):]
            break

if s == "":
    print('Empty String')
else:
    print(s)