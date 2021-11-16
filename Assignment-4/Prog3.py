def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    roman = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman_num=""
    while number !=0:
        if num[i] <=number:
            roman_num+=roman[i]
            number= number-num[i]
        else:
            i-=1
    return roman_num
  


number = int(input("Enter the Number : "))
print("Roman value is: ",printRoman(number) )