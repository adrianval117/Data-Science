# 1)
# x=float(input("Enter a number: "))
# y=float(input("Enter a second number: "))
# print("1) Add two numbers")
# print("2) Substract two numbers")
# print("3) Multiply two numbers")
# print("4) Divide two numbers")
# choice=int(input("Enter your choice: "))
# print("The answer is: ", end="")
# if choice==1:
#     print(x+y)
# elif choice==2:
#     print(x-y)
# elif choice==3:
#     print(x*y)
# elif choice==4:
#     print(x/y)
# else:
#     print("You did not enter a valid choice.")

# 2
# try:
#     percentage=float(input(\
#         "Please enter your percentage achieved in the class: "))
# except:
#     print("You did not enter a valid percentage.")
#     exit(0)
# ans=""
# if percentage>=93.99:
#     ans='A'
# elif percentage>=90 and percentage<93.33:
#     ans='A-'
# elif percentage>=86.67 and percentage<90:
#     ans='B+'
# elif percentage>=83.33 and percentage<86.67:
#     ans='B'
# elif percentage>=80 and percentage<83.33:
#     ans='B-'
# elif percentage>=76.67 and percentage<80:
#     ans='C+'
# elif percentage>=73.33 and percentage<76.67:
#     ans='C'
# elif percentage>=70 and percentage<73.33:
#     ans='C-'
# elif percentage>=66.67 and percentage<70:
#     ans='D+'
# elif percentage>=63.33 and percentage<66.63:
#     ans='D'
# elif percentage>=63.33 and percentage<66.63:
#     ans='D-'
# elif percentage>=60 and percentage<66.63:
#     ans='F'
# else:
#     ans='0'
# print("You earned an",ans,"in the class.")

# 3 Cms to Yard(s), foot(feet) and inches.
# cms=float(input("How many centimeters do you want to convert? "))
# inches=cms/2.54
# yards=int(inches/36)
# inches=inches-(yards*36)
# feet=int(inches/12)
# inches=inches-(feet*12)
# if yards==0 and feet==0 and inches==0:
#     print("There's no given data here")
# if yards==0:
#     if feet==0:
#         print("This is  %1.6f inches"%(inches))
#     elif feet==1:
#         print("This is 1 foot, %1.6f inches"%(inches))
#     elif feet>1:
#         print("This is",feet,"feet, %1.6f inches"%(inches))
# elif yards==1:
#     if feet==0:
#         print("This is 1 yard, %1.6f "%(inches))
#     elif feet==1:
#         print("This is 1 yard, 1 foot, %1.6f "%(inches))
#     elif feet>1:
#         print("This is 1 yard,",feet,"feet, %1.6f "%(inches))
# elif yards>1:
#     if feet==0:
#         print("This is",yards,"yards, %1.6f inches"%(inches))
#     elif feet==1:
#         print("This is",yards,"yards, 1 foot, %1.6f inches"%(inches))
#     elif feet>1:
#         print("This is",yards,"yards,",feet,"feet, %1.6f inches"%(inches))

# 4 too large and do not care about it

# 5
# try:
#     number=int(input("Please enter an integer less than 50: "))
# except ValueError:
#     print("Your enter is not valid.")
#     exit(0)
# if number%3==0 or number%5==0 or number%7==0 or number%11==0 or number%13==0 or\
#     number%7==0 or number%11==0 or number%13 or number%17==0 or number%19==0 or\
#     number%23==0 or number%29==0 or number%31 or number%37==0 or number%41==0 or\
#     number%43==0 or number%47==0:
#     print(number, "is prime")

#6 no


# 7
# binary = input("Please enter a 16-bit binary number: ")
# ans=0
# if int(binary[0])==1:
#     if len(binary)==16:
#         a = int(binary[0])*2**15
#         b = int(binary[1])*2**14
#         c = int(binary[2])*2**13
#         d = int(binary[3])*2**12
#         e = int(binary[4])*2**11
#         f = int(binary[5])*2**10
#         g = int(binary[6])*2**9
#         h = int(binary[7])*2**8
#         i = int(binary[8])*2**7
#         j = int(binary[9])*2**6
#         k = int(binary[10])*2**5
#         l = int(binary[11])*2**4
#         m = int(binary[12])*2**3
#         n = int(binary[13])*2**2
#         ñ = int(binary[14])*2**1
#         o = int(binary[15])*2**0
#     ans=int(a+b+c+e+d+f+g+h)
#     print("The base 10 equivalent of the binary number "+binary+" is: -"+str(ans))
# elif int(binary[0])==0:
#     if len(binary)==16:
#         a = int(binary[0])*2**15
#         b = int(binary[1])*2**14
#         c=int(binary[2])*2**13
#         d=int(binary[3])*2**12
#         e=int(binary[4])*2**11
#         f=int(binary[5])*2**10
#         g=int(binary[6])*2**9
#         h=int(binary[7])*2**8
#         i=int(binary[8])*2**7
#         j=int(binary[9])*2**6
#         k=int(binary[10])*2**5
#         l=int(binary[11])*2**4 
#         m=int(binary[12])*2**3 
#         n=int(binary[13])*2**2 
#         ñ=int(binary[14])*2**1 
#         o=int(binary[15])*2**0
#     ans=int(a+b+c+e+d+f+g+h)
#     print("The base 10 equivalent of the binary number "+binary+" is: "+str(ans))

#8
# n = int(input("Please enter an integer: "))
# a = int(n/16)
# a2 = int(n % 16)
# b = int(a/16)
# b2 = int(a % 16)
# c = int(b/16)
# c2 = int(b % 16)
# d = int(c/16)
# d2 = int(c % 16)

# if a2 == 10:
#     a2 = 'a'
# elif a2 == 11:
#     a2 = 'b'
# elif a2 == 12:
#     a2 = 'c'
# elif a2 == 13:
#     a2 = 'd'
# elif a2 == 14:
#     a2 = 'e'
# elif a2 == 15:
#     a2 = 'f'
# else:
#     a2 == a2

# if b2 == 10:
#     b2 = 'a'
# elif b2 == 11:
#     b2 = 'b'
# elif b2 == 12:
#     b2 = 'c'
# elif b2 == 13:
#     b2 = 'd'
# elif b2 == 14:
#     b2 = 'e'
# elif b2 == 15:
#     b2 = 'f'
# else:
#     b2 = b2

# if c2 == 10:
#     c2 = 'a'
# elif c2 == 11:
#     c2 = 'b'
# elif c2 == 12:
#     c2 = 'c'
# elif c2 == 13:
#     c2 = 'd'
# elif c2 == 14:
#     c2 = 'e'
# elif c2 == 15:
#     c2 = 'f'
# else:
#     c2 = c2

# if d2 == 10:
#     d2 = 'a'
# elif d2 == 11:
#     d2 = 'b'
# elif d2 == 12:
#     d2 = 'c'
# elif d2 == 13:
#     d2 = 'd'
# elif d2 == 14:
#     d2 = 'e'
# elif d2 == 15:
#     d2 = 'f'
# else:
#     d2 = d2
# ans = str(d2)+str(c2)+str(b2)+str(a2)
# print("The hexadecimal equivalent is 0x"+ans)


