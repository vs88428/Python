# Wap to find the sum of first n natural numbers

# n = int(input("write the value of n:"))

# sum = 0

# for i in range(1,n+1):
#     sum +=i

# print(sum)

#same using while:

# n=5
# sum=0
# i=1
# while i<=n:
#     sum +=i
#     i +=1
# print(sum)  


# Factorial of first n natural numbers

n = int(input("Enter the factorial you want:"))

fact =1
for i in range(1,n+1):
    fact *= i

print("Factorial is",fact)
      