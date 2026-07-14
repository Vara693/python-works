#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# if __name__ == '__main__':
#     records = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name,score])
    
#     scores  = sorted(set([
#         grade for name,grade in records
#     ]))
#     second_lowest = scores[1]
    
#     results = sorted([
#         name for name,grade in records if grade == second_lowest
#     ])
#     for name in results:
#         print(name)


##Using split
# n = int(input())
# student_marks = {}
# for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores

# print(name)
# print(scores)


##hash
# from builtins import hash
# n = int(input())
# ele = input().split()
# t = tuple(map(float,ele))
# print(hash(t))


##TextAllignment
# width = 20
# print('HackerRank'.center(width,'-'))



##HackerRank logo
#Replace all ______ with rjust, ljust or center. 

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



##print 2nd highest
# if __name__== '__main__':
#     n = input().split()
#     raft = set(map(int,n))
#     rough = list(raft)
#     maxi = max(rough)
#     rough.remove(maxi)
#     smax = max(rough)
#     print(smax)



##Factorial and Trailing zeros
# def trail(num):
#     count = 0
#     while num >= 5:
#         num //= 5
#         count += num
#     return count
#     print(f"The number of trailing zeros in factorial {num} are {count}")

# n = int(input("Entaer a number: "))
# if n<0:
#     print("The entered integer can't have a factorial")
# if n==0 or n==1:
#     print(f"The factorial of {n} is 1")
# if n>0 :
#     fac = 1
#     for i in range(0,n):
#         fac = fac*(n-i)
#     print(f"The factorial of {n} is {fac}")
    
# print(trail(n))



##append and print nested list
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     list = []
#     for i in range(0,x+1):
#         for j in range(0,y+1):
#             for k in range(0,z+1):
#                 if i + j+ k!=n:
#                     list.append([i,j,k])
#print(list)
    



    
##print 2nd highest 
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     poke = list(arr)
#     m = max(poke)
#     sm = max([x for x in poke if x!=m], default = None)
#     print(sm)

            

# #armstrong Number
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


# #Pallindrome number
# num = int(input())
# string  = str(num)
# rev_str = ''.join(reversed(string))
# if int(string) == int(rev_str):
#     print("the entered number is a pallindrome number")
# else:
#     print('No')


# #digit root
# def digit_root(n):
#     while n>=10:
#         print(f'Current: {n}')
#         n = sum(int(d) for d in str(n))
#     print(f"Digit root: {n}")
#     return n
# digit_root(890)


# #square root
# from math import sqrt
# num = int(input())
# root = sqrt(num)
# print(root)


# #Having 3 divisors
# def divisors(n):
#     count = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             count +=1
#     return count

# def three_divisors(n):
#     for i in range(1,n+1):
#         if divisors(i)==3:
#             print(i, end = ' ')

# three_divisors(49)


# #divisle by 11
# def divide(n):
#     even = 0
#     odd = 0
#     for i in n[:len(n):2]:
#         even+=int(i)
#     for i in n[1:len(n):2]:
#         odd+=int(i)
#     return (odd - even)%11 ==0


# num = input()
# if int(num)%11==0:
#     print('True')
# else:
#     print('False')

# print('true') if divide(num) else print('flase')


#kth digit
# def kth(a,b,k):
#     power = pow(a,b)
#     stpower = str(power)
#     if k<=len(stpower):
#         print(int(stpower[k-1]))
#     else:
#         print("No such value was found")

# kth(11,3,4)


# #collecions: counter
# from collections import Counter
# string = 'angela'
# nr = Counter(string)
# print(nr)
# for i in nr:
#     if nr[i] == 1:
#         print(i)


# #Given two integers a and b(b != 0), the task is to return the fraction a/b in string format. 
# # If the fractional part is repeating, enclose the repeating part in parentheses.
# def divide(a,b):
#     div = a/b
#     num = (str(div)).split('.')
#     bfdec = num[0]
#     sfdec = num[1]
#     hash_set = set(sfdec)
#     print(bfdec,hash_set)

# divide(10,2)



#Given three integers x, n, and M, compute (xn) % M (remainder when x raised to the power n is divided by M).
# n = list(map(int, input().split(' ')))
# result = (n[0]**n[1]) % n[2]
# print(result)


#Power Set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}. If S has n elements in it then P(s) will have 2n elements
ter = {'a', 'b', 'c'}
power_ter = []
poke = []
power_ter.append({})
power_ter.append(ter)
for i in ter:
    power_ter.append({i})

for i in ter:
    for j in ter:
        if i!=j:
            poke.append((i,j))


set(poke)
list(poke)
power_ter.append(poke)
print((power_ter))











    

    








