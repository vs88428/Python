# grade print

marks = int(input("Enter the marks obtained by you:"))

if(marks>=90):
    grade = "A"
elif(marks>=80 and marks<90):
     grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
     grade = "D"

print("Result is declared, Grade ->", grade)      

# #use of nesting

age = 24

if(age>=18):
     if(age>=80):
          print("can't drive")
     else:
          print("can drive")
else:
     print("can't drive")

# # print whether number written is odd or even

num = int(input("Enter the number:"))

if(num%2 == 0):
     print("Number is even")
else:
     print("Number is odd")   

# Greatest of three number 

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the seconf number:"))
num3 = int(input("Enter the third number:"))

if(num1>num2 and num1>num3):
     print("Num1 is greatest",num1)
elif(num2>num3):
     print("Num2 is greatest", num2)
else:
     print("Num3 is greatest",num3) 

# # multiple of 7 check


a =int(input("Enter number:"))

if(a%7 == 0):
     print("It is multiple")
else:
     print("Not a multiple")     


# Greatest of four number
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
d = int(input("Enter forth number:"))

if(a>b and a>c and a>d):
    print("1st no. is largest")
elif(b>c and b>d):
    print("2nd no. is largest")
elif(c>d):
    print("3rd no. is largest")
else:
    print("4th no. is largest")