#1.10
# print("Bienvenido a la operación exponenciación")
# base=float(input("Digite la base: "))
# exp=float(input("Digite el exponente: "))
# ans=base**exp
# print("%1.2f ^ %1.2f = %1.4f" %(base, exp, ans))
# print("%10.2f ^ %10.2f = %10.4f" %(base, exp, ans))

#2.1
# enter=input("Type a month: ")
# if enter=='December':
#     print("Merry Christmas!")
# else:
#     print("You'll have to wait")
# print("Have a Happy New Year!")

#2.2
# shor=int(input("Enter the shortest side of the triangle: "))
# mid=int(input("Enter the middle side of the triangle: "))
# lon=int(input("Enter the longest side of the triangle: "))
# ans="It is a perfect triangle."
# if shor%3!=0:
#     ans="It is not a perfect triangle."
# if mid%4!=0:
#     ans="It is not a perfect triangle."
# if lon%5!=0:
#     ans="It is not a perfect triangle."
# if shor**2+mid**2!=lon**2:
#     ans="It is not a perfect triangle."
# print(ans)    

# born=input("Are you a born Citizen of the US? ")
# age=input("Are you at least 35 years old? ")
# resi=input("Have you been for 14 years a resident within the US? ")
# president=True
# if born!='yes' or born!='Yes':
#     president=False
# if age!='yes' or age!='Yes':
#     president=False
# if resi!='yes' or resi!='Yes':
#     president=False
# if president==True:
#     print("You are eligible for Office of President of the US")
# else:
#     print("You are not eligible for Office of President of the US")

#BEATIFUL PROGRAMM
# age=int(input("How old are you? "))
# lic=input("Do you have a license? ")
# pare=input("Does your parent have a license? ")
# if (age<=15 and pare=='yes') or lic=='yes':
#     print("You are legal to fish in Minnesota")
# else:
#     print("You are not legal to fish in Minnesota")

#2.7
# shor=float(input("Enter the shortest side of the triangle: "))
# mid=float(input("Enter the middle side of the triangle: "))
# lon=float(input("Enter the longest side of the triangle: "))
# ans="It is a perfect triangle."
# if shor%3!=0:
#     ans="It is not a perfect triangle."
# if mid%4!=0:
#     ans="It is not a perfect triangle."
# if lon%5!=0:
#     ans="It is not a perfect triangle."
# if shor**2+mid**2!=lon**2:
#     ans="It is not a perfect triangle."
# print(ans)    

# 2.12
# sideone = float(input("Please enter length of shortest side of triangle:"))
# sidetwo = float(input("Please enter length of middle side of triangle:"))
# sidethree = float(input("Please enter length of longest side of triangle:"))
# ratio = sideone/3
# msg = "It is a perfect triangle."

# if abs(( ratio - sidetwo / 4) / sidetwo) > 0.001:
#     msg ="It is not a perfect triangle."
# if abs(( ratio - sidethree / 5) / sidethree) > 0.001:
#     msg ="It is not a perfect triangle."
# print(msg)

#TRY AND EXCEPTS TO BEATIFUL PROBLEM
# try:
#     age=int(input("How old are you? "))
# except ValueError:
#     print("You did not enter your age correctly")
#     exit(0)
# lic=input("Do you have a license? ")
# pare=input("Does your parent have a license? ")
# if (age<=15 and pare=='yes') or lic=='yes':
#     print("You are legal to fish in Minnesota")
# else:
#     print("You are not legal to fish in Minnesota")

#try proof
# try: 
#     x=int(input("number 1: "))
#     y=int(input("number 2: "))
# except:
#     print("INVALID")
# print("product: ",x*y)

# 3.2
# s=input("Please enter yes or no: ")
# if len(s)==2:
#     a=s[0].isupper()
#     b=s[1].isupper()
#     c=0
# elif len(s)==3:
#     a=s[0].isupper()
#     b=s[1].isupper()
#     c=s[2].isupper()
# if a==True or b==True or c==True:
#     print("Next time please use all lower case letters")

# frase=input("Enter a phrase: ")
# a=frase.split()
# newString="".join([i[0] for i in a])
# print(newString.upper())

# number=input("Please enter a list of integers (separated numbers): ")
# number_list=number.split()
# contains_even=False
# for i in number_list:
#     x=int(i)
#     if x%2==0:
#         contains_even=True
# if contains_even:
#     print("The list contained an even number")
# else:
#     print("The list did not contain an even number")

# phrase=input("Please make your blog entry for today: ")
# clue_words=["orderly", "shopping", "repeat", "again", "gamble", "bid"]
# word_found=False
# for i in clue_words:
#     if i in phrase:
#         word_found=True
# if word_found:
#     print("You really need to talk to someone about this.")
# else:
#     print("Thanks for updating your blog.")

# s=input("Please enter a list of integers: ")
# lst=s.split()
# count=0
# for i in lst:
#     if int(i)%2==0:
#         count+=1
# print("There were", count ,"even integers in the list.")

# n=int(input("Please enter a number to get its factorial: "))
# multiply=1
# for i in range(1, n+1):
#     multiply=multiply*i
# print("The factorial of",n,"is: ",multiply)

# archivo = open("hola.txt", "r")
# print("----------------------------------------------------------")
# print("A continuación las convers que Hernán tiene con su crush: ")
# for linea in archivo:
#     print(linea.rstrip())
# archivo.close()

# filename = input("Please enter the name of a file: ")
# yourName = input("What is your name? ")
# age = int(input("How old are you? "))
# outfile = open (f"{filename}.txt","w")
# outfile.write("Hello "+ yourName +". How are you?\n")
# outfile.write("Next year you will be "+ str(age+1) \
#                             +" years old!\n")
# outfile.close ()

# frase=input("Enter some phrase: ")
# lista=frase.split()
# i=0
# while True:
#     if i==len(lista):
#         break
#     else: 
#         print(lista[len(lista)-1-i])
#     i+=1
# print("Done.")

# phonebook = open ("addressbook.txt","r")
# numEntries = 0
# eof=False
# while not eof:
#     lastName = phonebook.readline().rstrip()
#     firstName = phonebook.readline().rstrip()
#     street = phonebook.readline().rstrip()
#     citystatezip = phonebook.readline().rstrip()
#     homephone = phonebook.readline().rstrip()
#     mobilephone = phonebook.readline().rstrip()
#     print(lastName)
#     print(firstName)
#     print(street)
#     print(citystatezip)
#     print(homephone)
#     print(mobilephone)
#     if lastName=="":
#         eof=True
#     else:
#         numEntries = numEntries + 1
# print("You have", numEntries ,"entries in your address book.")

