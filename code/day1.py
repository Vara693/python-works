# import sys
# from math import pi
# import datetime
# print(sys.version)
# print(sys.version_info)

# now = datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))



# # circle area calculator
# r = int(input("enter radius of circle: "))
# area = pi*pow(r,2)
# print("area of circle is ",area)


# reverse Full Name
# str = input("enter first name: ")
# str1 = input("enter last name: ")
# print("Hello! ", str1, str)

#list/tuple generator
# seq = input("enter some comma separated values: ")
# list = seq.split(",")
# tuple = tuple(list)
# print(list)
# print(tuple)

#file extension printer
# filename = input('enter the file name with extension: ')
# fetx = filename.split('.')
# print('the extension of the file you entered is: ', repr(fetx[1]))

#First and Last Colors
# color_list = ["Red","Green","White" ,"Black"]
# print("the first color is: ", color_list[0])
# print("the last color is: ", color_list[3])


#Exam Schedule Formatter
# exam_st_date = (11, 12, 2014)
# print("the exams are from: %s/%i/%i" %exam_st_date)


#Number Expansion Calculator
# n = int(input("enter a number: "))
# n1 = int("%s%s" %(n,n))
# n2 = int("%s%s%s" %(n,n,n))
# sum = n+n1+n2
# print(sum)

# n = input("Enter an integer: ")
# result = int(n) + int(n*2) + int(n*3)
# print("Result:", result)


#Function Documentation Printer
# print(sorted.__doc__)
# print(len.__doc__)
# print(print.__doc__)
# print(input.__doc__)


#Monthly Calendar Display
# import calendar
# m = int(input("enter the month: "))
# y = int(input("enter the year: "))
# print(calendar.month(y,m))


#Days Between Dates
# from datetime import date
# f1 = date(2025,1,18)
# f2 = date(2025,6,22)

# pro = f2-f1
# print(pro.days)


#Sphere Volume Calculator
# from math import pi
# r = float(input("enter radius of the sphere: "))
# volume = 4/3*pi*pow(r,3)
# print("volume of the sphere is ", volume)


#Difference from 17
# n = int(input("enter your number: "))
# if(n>=17):
#     print(n-17)
# else:
#     print(2*abs(n-17))


#Number Range Tester
# n = float(input("enter your number: "))
# if(n>100 and n<=1000):
#     print("true")
# elif(n<100):
#     print("less than given range")
# else:
#     print("false")


#Triple Sum Calculator
# a = int(input("enter a number: "))
# b = int(input("enter a number: "))
# c = int(input("enter a number: "))

# if(a==b and b==c):
#     print(3*3*a)
# else:
#     print(a+b+c)


#Prefix "Is" String Modifier
# def pulse(str):
#     if len(str)>=2 and str[:2]=="Is":
#         return str
#     else:
#         return "Is"+str
# print(pulse("array"))
# print(pulse("Isbinary"))
# print(pulse("Isheavy"))


#String Copy Generator
# str = input("enter your string: ")
# n = int(input("enter the number of copies you want: "))
# if(n>=1):
#     for i in range(0,n):
#         print(str)
# else:
#     print("ERROR!!!")


# Even or Odd Checker
# n = int(input("enter a number: "))
# if n%2==0:
#     print("EVEN")
# else:
#     print("ODD")


#Count 4 in List
# count = 0
# list = [1,3,4,7,4,8,4]
# for i in list:
#     if i==4:
#         count = count + 1
# print(count)


#String Prefix Copies
# str = input("enter your string: ")
# n = int(input("enter the number of copies you want: "))
# if(len(str)>=2):
#     for i in range(0,n):
#         print(str[:2])
# else:
#     for i in range(0,n):
#      print(str)
   

#Hiatogram
# list = [5,4,2,8]
# def histo(list):
#     for i in list:
#         print("*"*i)
# histo(list)


#List to String Concatenator
# list = [1,2,3,4,5]
# tuple = tuple(list)
# print("%i%i%i%i%i" %tuple)


#Even Numbers Until 237
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# for i in numbers:
#     if i%2==0 and i<237:
#         print(i)


#Unique Colors Finder
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# diff = color_list_1-color_list_2
# print(diff)


#Triangle Area Calculator
# b=float(input("enter base of the triangle: "))
# h=float(input("enter height of the triangle: "))
# area= 1/2*h*b
# print(area)


#GCD Calculator
# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# while b>0:
#     r = a%b
#     a = b
#     b = r
# gcd = a
# print(gcd)


#LCM Calculator
# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# m = max(a,b)
# while(True):
#     if m%a==0 and m%b==0:
#         break
#     m+=1
# print(f"the lcm of {a} and {b} is {m}")


#Triple Sum with Equality Rule
# def addition(a,b,c):
#     if a==b or b==c or a==c:
#         return 0
#     else:
#         return a+b+c
# print(addition(1,2,3))
# print(addition(1,2,2))
# print(addition(2,2,2))


#Conditional Sum to 20
# def sam(a,b):
#     sum2 = a+b
#     if sum2>15 and sum2<20:
#         return 20
#     else:
#         return a+b
# print(sam(1,2))
# print(sam(10,8))


#Equality or 5 Rule Checker
# def sam(a,b):
#     # sum2 = a+b
#     if a==b or a+b==5 or a-b==5:
#         return True
#     else:
#         return False
# print(sam(1,2))
# print(sam(10,5))
# print(sam(2,3))
# print(sam(5,5))


#Add Integers Validator
# # Define a function 'add_numbers' that takes two arguments: a and b.
# def add_numbers(a, b):
#     # Check if both 'a' and 'b' are integers using the 'isinstance' function.
#     if not (isinstance(a, int) and isinstance(b, int)):
#         # If either 'a' or 'b' is not an integer, return an error message.
#         return "Inputs must be integers!"
#     # If both 'a' and 'b' are integers, return their sum.
#     return a + b

# # Test the 'add_numbers' function with various input values and print the results.
# print(add_numbers(10, 20))     # Valid: Both inputs are integers, and it returns the sum.
# print(add_numbers(10, 20.23))  # Invalid: One of the inputs is a float, so it returns an error message.
# print(add_numbers('5', 6))     # Invalid: One of the inputs is a string, so it returns an error message.
# print(add_numbers('5', '6'))   # Invalid: Both inputs are strings, so it returns an error message.


#Personal Info Formatter
# student = {
# "name": "Varadraj",
# "age": 19,
# "address": "moblinching"

# }
# print(student["name"])
# print(student["age"])
# print(student['address'])


#Expression Solver
# def solve(a,b):
#     sol = pow(a+b,2)
#     return sol
# print(solve(4,5))


#Future Value Calculator
# def famu(amt,int,years):
#     famt = amt*((1 + (0.01*int))**years)
#     return famt
# print(famu(10000,3.5,7))


#Distance Between Points
# def dis(a,b,c,d):
#     distance = pow((c-a)**2 + (d-b)**2,0.5)
#     return distance
# print(dis(4,1,8,4))


# Import the 'platform' and 'os' modules.
# import platform
# import os

# # Print the name of the operating system based on the 'os.name' attribute.
# # 'os.name' provides the name of the operating system dependent module imported.
# print("Name of the operating system:", os.name)

# # Print the name of the OS system using the 'platform.system()' function.
# # 'platform.system()' returns the name of the operating system, such as 'Windows', 'Linux', or 'Darwin' (macOS).
# print("\nName of the OS system:", platform.system())

# # Print the version of the operating system using the 'platform.release()' function.
# # 'platform.release()' returns the version or release of the operating system.
# print("\nVersion of the operating system:", platform.release())

# # Import the os.path module to work with file and directory paths.
# import os.path

# # Check if 'main.txt' is a file and print the result.
# print(os.path.isfile('main.txt'))

# # Check if 'main.py' is a file and print the result.
# print(os.path.isfile('main.py'))


#shell mode detector
# import struct
# print(struct.calcsize("P") * 8)


#Printing the closest
# n = int(input("Enter 1st number:  "))
# m = int(input("Enter 2nd number:  "))
# close = []
# for i in range(n-m,m+n):
#     if i%m == 0:
#         close.append(i)
# a = abs(close[0])/abs(m)
# b = abs(n)/abs(m)
# c = abs(close[1])/abs(m)

# d = b/a
# e = c/b
# if d>e:
#     print(close[1])
# elif e>d:
#     print(close[0])
# else:
#     print(m)

    
#dice problem
# face = int(input("Enter the face number: "))
# oface = 7 - face
# print(f"the number on the oppo side of {face} is {oface}")


#Arithmetic Progression
# def ap(a1,a2,n):
#     term = a1 + (n-1)*(a2-a1)
#     return term
# print(ap(2,3,4))


#sum of digits of a number
#1. string method
# n = int(input("enter a number: "))
# br = str(n)
# sum = 0
# for i in br:
#     ch = int(i)
#     sum += ch
# print(sum)


#Reverse the number
# n = int(input("Enter a number: "))
# ogstr = str(n)
# revstr = ''.join(reversed(ogstr))
# num = int(revstr)
# print(num)


#Prime tester
# n = int(input("Enter a number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("Not a prime number")
#     else: 
#         print("prime")


# #Given two positive numbers x and y, check if y is a power of x or not.
# x = int(input("Enter an integr: "))
# y = int(input("Enter the power of the integer: "))

# pow = x


#Given two positive integers a and b, the task is to find the GCD of the two numbers.
# x = int(input("enter 1st number: "))
# y = int(input("enter 2nd number: "))
# while y>0:
#     r = x%y
#     x = y
#     y  = r
# print(x)


#Given two positive integers a and b. Find the Least Common Multiple (LCM) of a and b.
# x = int(input("enter 1st number: "))
# y = int(input("enter 2nd number: "))
# m = max(x,y)
# while True:
#     if m%x ==0 and m%y ==0:
#         break
#     m+=1
# print(m)


#A number is a perfect number if it is equal to the sum of its proper divisors, that is, the sum of its positive divisors excluding the number itself. Find whether a given positive integer n is perfect or not.
# def perfect_no(n):
#     list = []
#     sum = 0
#     for i in range(1,n-1):
#         if n%i == 0:
#             list.append(i)
#     for l in range(0,len(list)):
#         sum += list[l]
#     if sum == n:
#         return True
#     else:
#         return False
    
# print(perfect_no(15))


#Given two integer arrays a[] and b[] containing two integers each representing the numerator and denominator of a fraction respectively. The task is to find the sum of the two fractions and return the numerator and denominator of the result.
# def dowry(a,b):
#     m = max(a[1],b[1])
#     while True:
#         if m%a[1] == 0 and m%b[1] == 0:
#             break
#         m+=1
#     a = [a[0],m]
#     b = [b[0],m]
#     sum = [a[0]+b[0],m]
#     list = []
#     while sum[1]>0:
#         r  = sum[0]%sum[1]
#         sum[0] = sum[1]
#         sum[1] = r
#         list.append(sum[0])

#     alpha = (a[0]+b[0])/list[-1]
#     omega = m/list[-1]
#     result = [int(alpha),int(omega)]
#     return result

# a = [1,2]
# b = [3,4]
# print(dowry(a,b))




    


        
      








