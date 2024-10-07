# marks = {}

# x=int(input("enter the physics marks:",  ))
# marks.update({"physics": x})
# y=int(input("enter the chemistry marks:",  ))
# marks.update({"chemistry": y})
# z=int(input("enter the maths marks:",  ))
# marks.update({"maths": z})
# print(marks)

# values ={
#     ("float",9.0),
#     ("int",9)
# }
# print(values)

# list = []
# movie1=input("enter the movie name:",)
# movie2=input("enter the movie name:",)
# movie3=input("enter the movie name:",)
# list.append(movie2)
# list.append(movie1)
# list.append(movie3)
# print(list)

# list2 = [1,2,3,4,]
# list2 = [1,2,1]
# list2=["ma'am"]
# copy_list2=list2.copy()
# copy_list2.reverse()
# print(copy_list2)
# if(list2 == copy_list2):
#     print("The list element is Palindrome")
# else:
#     print("Not a Palindrome")

# tup =("C","D","A","A","B","B","A")
# print(tup.count("A"))

# list =["C","D","A","A","B","B","A"]
# list.sort()
# print(list)

# #Example of for loop 
# numbers = [20,1,3,4,7,2,9,1,6,4,8,5]
# to_tal = 0
# for i in numbers:
#     to_tal += i
#     print("the steps to add :",to_tal)
# print("the total sum is :",to_tal)

def fact(n):
    if(n == 0 or n==1):
        # print("The factorial of 0 and 1 is: 1")
        return 1
    elif n<0:
        print("Factorial can not defined for negative integers")
        return None
    else:
        return n*fact(n-1)

print(fact(3))
  
# def factorial(a):
#     if a==1:
#         return 1
#     else:
#         return a*factorial(a-1)
    
# print(factorial(5))