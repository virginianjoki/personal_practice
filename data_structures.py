# fruits = ["watemelon" , "grapes" , "lemon"]
# fruits.append("apple")
# fruits.pop()
# print(fruits[-2:-1])  

# # #dictionaries
# #dict :  variable ={"k1": "v1" , }
# harry_potter = {"title" : "the wicked" , "author" : "J.K Rowling" , "genre" : "fiction" }
# # print(harry_potter["author"])

# import random
# # random_number ={1, 2, 2 , 3  ,4 ,5 , 6 , 7, 8  ,10}
# # print(random_number)

# # import.def_functions

# # Generate a list of random numbers between 1 and 10
# random_numbers = [random.randint(1, 10) for _ in range(10)]

# # Convert the list to a set to remove duplicates
# unique_numbers = set(random_numbers)

# # Display the random numbers and the unique numbers
# print(f"Random numbers: {random_numbers}")
# print(f"Unique numbers: {unique_numbers}")

import calculator
number1 = 10
number2 = 5
result = calculator.add(number1,number2)
print(f"the sum of {number1}and {number2} is {result}")