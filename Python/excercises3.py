#1
# prime_list=[]
# counter=0
# for num in range(2,1000):
#     prime = True
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False
#             counter+=1
#     if prime:
#        prime_list.append(num)
# print("You have",counter,"prime numbers between 1 and 1000: ")
# print(prime_list)

#2
# out=True
# while out:
#     print(" 1) Look up a person by last name.\n 2) Add a person to the address book.\n 3) Quit.")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         search = input("Please enter the last name to look up: ")
#         phonebook = open("addressbook.txt", "r")
#         found = False
#         while not found:
#             name = phonebook.readline().rstrip()
#             street = phonebook.readline().rstrip()
#             citystatezip = phonebook.readline().rstrip()
#             homephone = phonebook.readline().rstrip()
#             mobilephone = phonebook.readline().rstrip()
#             if name == "":
#                 print("Person not found in the addressbook.")
#                 exit(0)
#             if search in name:
#                 found = True
#         print(name)
#         print(street)
#         print(citystatezip)
#         print("home:", homephone)
#         print("mobile:", mobilephone)
#     elif choice==2:
#         name=input("Enter the name and lastname: ")
#         street=input("Enter the street: ")
#         citystatezip=input("Enter the city: ")
#         homephone=input("Enter the homephone: ")
#         mobilephone=input("Enter the mobilephone: ")
#         filename=open("addressbook.txt", "w")
#         filename.write(f"{name}\n")
#         filename.write(f"{street}\n")
#         filename.write(f"{citystatezip}\n")
#         filename.write(f"{homephone}\n")
#         filename.write(f"{mobilephone}\n")
#         filename.close()
#     elif choice==3:
#         print("Done.")
#         out=False

#3
# numbers_list=input("Please enter a list of numbers: ")
# numbers_list=numbers_list.split()
# count, suma=0, 0
# for i in numbers_list:
#     suma+=float(i)
#     count+=1
# print("There were",count,"numbers in the list.")
# print("The average of the numbers was", round((suma/count),2))

# 4
# numbers_list=input("Please enter a list of numbers: ")
# numbers_list=numbers_list.split()
# final_numbers=""
# for i in numbers_list:
#     if float(i)>0 and float(i)<100:
#         final_numbers+=str(float(i))+" "
# print("The numbers between 0 and 100 are:", final_numbers)

# 5
# lista=input("Enter whatever: ")
# lista=lista.split()
# lista_reversed=[]
# for i in range(len(lista)):
#     lista_reversed.append(lista[len(lista)-1-i])
# print(lista_reversed)

# 7
# lista=input("Enter whatever: ")
# lista=lista.split()
# lista.reverse()
# print(lista)

# 9
# print("Enter a list of integers terminated by a -1.")
# first=float(input("Please enter the first integer and press enter: "))
# lista=[first]
# if lista[0]==-1:
#     print("No integer entered.")
#     exit(0)
# else:
#     i=1
#     while True:
#         value=float(input("Please enter another integer: "))
#         lista.append(value)
#         if lista[i]==-1:
#             lista.pop()
#             break
#         i+=1
# final_list=""
# for i in lista:
#     final_list+=str(int(i))+" "
# print("The list of integers is", final_list)

# 10
# print("This program computes your GPA.\n"
#     "Please enter your completed courses.\n"
#     "Terminate your entry by entering 0 credits.")
# credit=[]
# grade=[]
# while True:
#     value_C=int(input("Credits? "))
#     if value_C!=0:
#         credit.append(value_C)
#         value_G=input("Grade? ")
#         if value_G=="A":
#             grade.append(4)
#         elif value_G=="A-":
#             grade.append(3.7)
#         elif value_G=="B+":
#             grade.append(3.3)
#         elif value_G=="B":
#             grade.append(3)
#         elif value_G=="B-":
#             grade.append(2.7)
#         elif value_G=="C+":
#             grade.append(2.3)
#         elif value_G=="C":
#             grade.append(2)
#         elif value_G=="C-":
#             grade.append(1.7)
#         elif value_G=="D+":
#             grade.append(1.3)
#         elif value_G=="D":
#             grade.append(1)
#         elif value_G=="D-":
#             grade.append(0.7)
#         elif value_G=="F":
#             grade.append(0)
#     else:
#         break
# i, gpa, total_credits=0, 0, 0
# for i in credit:
#     total_credits+=int(i)
# for i in range(len(grade)):
#     gpa+=credit[i]*grade[i]
# print("Your GPA is: ", gpa/total_credits)

# 11 (TOUGHEST SO FAR)
n=int(input("Enter a number: "))
remainders=[]
if n>=0:
    whole=0
else: 
    whole=1
while True:
    a=int(n/2)
    b=int(n%2)
    remainders.append(b)
    if a==0 or len(remainders)==64:
        break
    n=a
final_list=[]
final_conver=""
if whole==0:
    for i in range(len(remainders)):
        final_list.append(remainders[len(remainders)-1-i])
        final_conver+=str(int(final_list[i]))
    print(final_conver)
elif whole==1:
    for i in range(len(remainders)):
        if remainders[i]==0:
            remainders[i]=1
        elif remainders[i]==1:
            remainders[i]=0
    a=len(remainders)
    for i in range(a):
        final_list.append(remainders[a-1-i])
    if final_list[a-1]==0:
        final_list[a-1]=1
    else:
        i=0
        last=1
        while last==1:
            last=final_list[len(final_list)-1-i]     #cicle that goes through the array and replaces by 0 when 1 is found
            if last==1:                              #making this till finding 0 as next-left value and printing result 
                final_list[len(final_list)-1-i]=0
            elif last==0:
                final_list[len(final_list)-1-i]=1
            i+=1
    for i in range(a):
        final_conver+=str(int(final_list[i]))
    print(final_conver)

