# def implode(lista):
#     result=""
#     for c in lista: 
#         result=result+c
#     return result
# t=input("Enter the characters separed by one space: ")
# print("The list obtained is: ", implode(t.split()))

#This code does NOT work since "len" function is called to be used as a variable. 
# def lenght(L):
#     len=1
#     for i in range(len(L)):
#         len = len +1
#     return len
# print(lenght([1, 2, 3]))

# def reverseInPlace(lst):
#     for i in range(len(lst)//2):
#         tmp = lst[i]
#         lst[i] = lst[ len(lst)-1-i]
#         lst[len(lst)-1-i]=tmp
# s = input("Please enter a sentence:")
# lst = s.split()
# reverseInPlace(lst)
# print("The sentence backwards is:",end="")
# for word in lst:
#     print (word ,end="")
# print()

#DIVING ELEMENTS FROM LIST
# def evenlyDivides(y, x):
#     return y % x==0
# def evenlyDividesElements(lst, n):
#     global do_divide
#     for i in lst:
#         if evenlyDivides(n, int(i)):
#             do_divide.append(int(i))          
# do_divide=[]
# a=input("Enter a list of numbers: ")
# lst=a.split()
# n=int(input("Enter the divider number: "))
# evenlyDividesElements(lst, n)
# print(do_divide)

#MORE ABOUT DIVIDING

# FACTORIAL
# def factorial(n):
#     if n==0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# REVERSING A STRIG EASILY
# def reverse(s):
#     if s=="":
#         return ""
#     return reverse(s[1:]) + s[0]
# print(reverse("Hello"))

# FIBONACCI
# def Fibonacci(n):
#     if n==0 or n==1:
#         return 1
#     return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(25))

# def evenlyDivides(y, x):
#     return y % x==0
# def evenlyDividesElements(lst, n):
#     do_divide=[]
#     for i in lst:
#         if evenlyDivides(n, int(i)):
#             do_divide.append(int(i)) 
#     divisors=" ".join([str(i) for i in do_divide]) 
#     return divisors
# a=input("Enter a list of numbers: ") 
# lst=a.split()
# for i in lst:
#     print(i, "is evenly divisible by ", evenlyDividesElements(lst, int(i)))

import matplotlib.pyplot as plt
import numpy as np

x = [10*i for i in range(0, 7)]
y = 