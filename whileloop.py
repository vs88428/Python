# print number from 1 to 100

# i=1
# while i<=100:
#     print(i)
#     i +=1
# print("Loop Ended")

# Print number from 100 to 1

# i=100
# while i>=1:
#     print(i)
#     i -= 1
   
 #print multiplication number of an numner n

# n = int(input("Enter the table you want:"))

# i = 1
# while i<=10:
#     print(n*i)
#     i += 1

# print the elements of the list using loop

# list = [1,4,9,16,25,36,49,64,81,100]

# i=0
# while i< len(list):
#     print(list[i])
#     i += 1

# Search for a number x in the list

# tup = (1,2,3,4,5,6,7,8,8,9,10)

# x = int(input("Enter the number to find:"))   

# i = 0
# while i < len(tup):
#     if(tup[i] == x):
#         print("found at",i)
#     else:
#         print("Finding")
#     i +=1         

# Using break and continue
#for odd number print
# i = 1
# while i<10:
#     if(i%2 == 0):
#         i +=1
#         continue #skip
#     print(i)
#     i +=1

# using for loop

# Print the element using loop

# list = [1,2,3,4,5,6,7,8,9,10]

# for val in list:
#     print(val)

# # finding a number in the tuple

# tup = (1,2,3,4,5,6,7,78,78,56,45,)

# x = int(input("Write the number to find:"))
# ind = 0
# for val in tup:
#     if(val == x):
#         print("x is found",ind)
#     ind +=1

# Using Range

# for i in range(5): #range(stop)
#     print(i)

# for i in range(1,5):  #range(start,stop)
#     print(i)

#Print even number using range

# for i in range(2,100,2):
#     print(i)

# Print the table of number n using for ans range

n = int(input("Enter the number:"))
for i in range(1,10):
    print(n*i)
