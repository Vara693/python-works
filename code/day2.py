#Loops with else   
# for i in range(6):
#     print(i)
#     if i==6:
#         break
# else:
#     print("Sorry no i")


#Exception Handling
# try:
#     a = int(input("Enter a number: "))
#     for i in range(1,11):
#         print(f"{a}x{i}={a*i}")
# except:
#     print("Entered element is not a integer.")


#Use of finally
#1. no finally
# def funk():
#     try:
#         l = [1,2,3,4,5]
#         i = int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("An error occured!!")
#         return 0
#     print("I am getting excecuted anyway")
# print(funk())

# #2. with finally
# def funk():
#     try:
#         l = [1,2,3,4,5]
#         i = int(input("Enter the index: "))
#         print(l[i])
#         return 1
#     except:
#         print("An error occured!!")
#         return 0
#     finally:
#         print("I am getting excecuted anyway")
# print(funk())


#ValueError
# a = int(input("Enter a value between 5 and 9: "))
# if(a<5 or a>9):
#     raise ValueError("ERROR!!!!")

# str = input("Enter a string:")
# if str == 'quit':
#     print("Success")
# else:
#     raise ValueError("ERROR!!!!")


#Short if else statement
# a = 4000
# b = 4000
# print("A") if a>b else print("poke") if a==b else print("B")


#Enumerate
#1. normal
# marks = [56,78,99,34,56,25,70]
# index = 0
# for i in marks:
#     print(i)
#     if(index==2):
#         print("AS always Varadraj")
#     index+=1

# #2. using
# for i,mark in enumerate(marks):
#     print(f'{i+1}.)',mark)
#     if(i==2):
#         print("AS always Varadraj")



# #File I/O
# f = open('myfile.txt','r')
# test = f.read()
# print(test) 
# f.close()



# #Lambda function
# def hen(x):
#     return x*2
# def jack(gx,value):
#     return 10+gx(value)

# funk = lambda x:x*2
# cube = lambda x:pow(x,3)
# lambda x,y,z:(x+y+z)/3
# print(hen(5))
# print(funk(5))
# print(cube(5))
# print(jack(lambda x:x**2,2))


# #map,filter and reduce
# #1.MAP
# # def cube(x):
# #     return x*x*x
# l = (1,4,5,2,3,7)
# poke = tuple(map(lambda x:x**3,l))
# print(poke)

# #2. FILTER
# newl = list(filter(lambda x: x>3, l))
# print(newl)

# #3. REDUCE
# from functools import reduce
# fibre = reduce(lambda x,y:  x+y,l)
# print(fibre)


# # Diff in 'is' and '=='
# # a = (1,2,3)
# # b = (1,2,3)
# # print(a is b) #compares exact location of object in memory
# # print(a==b) #compares values


# #Armstrong number
# num = int(input())
# string = str(num)
# power = len(string)
# total = 0
# for i in string:
#     total += int(i)**power
# if total == num:
#     print("The entered number is a Armstrong number")
# else:
#     print('No')


# #Given a positive integer n ( 1 <= n <= 1015). Find the largest prime factor of a number. 
# num = int(input())
# prime = []
# prime2 = []
# if num == 1:
#     print("Not possible")
# elif num <=0:
#     print("Enter a +ve number.")
# else:
#     for i in range(3,num,2):
#         if num%i==0:
#             prime.append(i)

# for j in prime:
#     for k in (3,j+1):
#         if j%k != 0:
#             prime2.append(j)

# print(max(prime2))


#pointers in python
# a = [1,2,3,4]
# b=a
# print(id(a), id(b))



# #Josephus Problem  -- Not Solved
# num = int(input("Enter the number of peoplr: "))
# k = int(input("The number to skip: "))
# circle = []*num
# i =0
# while(i!=num):
#     for j in circle:
#         if(j==k):
#             circle.remove(i)



# #Euler's Totient Function
# num = int(input("Enter the number: "))
# for  i in range(1, num):
#     if num%i !=0:
#         print(i) 



#Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target
# def win(elements, target):
#     n =len(elements)
#     for i in range(n):
#         for j in range(i+1, n+1):
#             if sum(elements[i:j]) == target:
#                 return i, j-1
            

# print(win([1,2,3,4,5,6,7,8,9], 15))


#You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
def win(elements):
    n =len(elements)
    sums = []
    for i in range(n):
        for j in range(i+1, n+1):
            add = sum(elements[i:j])
            sums.append(add)

    return max(sums)

print(win([5, 4, 1, 7, 8]))
















