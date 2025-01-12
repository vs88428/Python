#  three movies name and store in list
list = []
a = input("Enter the first movie name:")
b = input("Enter the second movie name:")
c = input("Enter the third movie name:")

list.append(a) #we can use list.append(input)
list.append(a)
list.append(a)
print(list)

# To check if list have a palindrome , use copy and reverse it to check

list=[1,2,3,2,1]
 

copy1=list.copy()
copy1.reverse()

if(copy1 == list):
    print("Palindrome")
else:
    print("Not a Palindrome")
        
# count the number of grades in tuple

tup=("A","A","B","C")

print(tup.count("A"))
