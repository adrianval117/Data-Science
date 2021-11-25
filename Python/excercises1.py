#1
# name=input("Enter your name: ")
# print(str(name[0]),"ASCII value IS", ord(name[0]))
# print(str(name[1]),"ASCII value IS", ord(name[1]))
# print(str(name[2]),"ASCII value IS", ord(name[2]))
# print(str(name[3]),"ASCII value IS", ord(name[3]))

#2
# name=input("Enter your name in downcase: ")
# a=chr(ord(name[0]) - 32)
# b=chr(ord(name[1]) - 32)
# c=chr(ord(name[2]) - 32)
# d=chr(ord(name[3]) - 32)
# print("The string capitalized IS ", a+b+c+d)

#3
# miles=float(input("Please enter the number of miles you drove: "))
# gal_gas=float(input("Please enter the number of gas you put in the tank: "))
# print("You got %1.15f mpg on that tank of gas"%(miles/gal_gas))

#4
# dollars=float(input("What is the amount of US Dollars you want to convert? "))
# excRate=float(input("What is the current exchange rate (1 US Dollar equals what in the Foreig Currency)? "))
# ans=dollars*excRate
# print("The amount IN the Foreign Currency IS", round(ans, 2))

#5
# cms=float(input("How many centimeters do you want to convert? "))
# inches=cms/2.54
# yards=int(inches/36)
# inches=inches-(yards*36)
# feet=int(inches/12)
# inches=inches-(feet*12)
# print("This is",yards,"yards,",feet,"feet, %1.6f "%(inches))

#6
# cost=float(input("How much did the item cost: "))
# pay=float(input("How much did the person give to you: "))
# change=pay-cost
# pennies=change*100
# twenties=int(pennies/2000)
# pennies=pennies-(twenties*2000)
# tens=int(pennies/1000)
# pennies=pennies-(tens*1000)
# fives=int(pennies/500)
# pennies=pennies-(fives*500)
# ones=int(pennies/100)
# pennies=pennies-(ones*100)
# quarters=int(pennies/25)
# pennies=pennies-(quarters*25)
# dimes=int(pennies/10)
# pennies=pennies-(dimes*10)
# nickels=int(pennies/5)
# pennies=int(pennies-(nickels*5))
# print("The person's change is: $"+str(change))
# print("The bills or the change should be: ")
# print(twenties, "twenties")
# print(tens, "tens")
# print(fives, "fives")
# print(ones, "ones")
# print(quarters, "quarters")
# print(dimes, "dimes")
# print(nickels, "nickels")
# print(pennies, "pennies")

#7
# binary=input("Please enter an eight digit binary number: ")
# a=int(binary[0])*2**7
# b=int(binary[1])*2**6
# c=int(binary[2])*2**5
# d=int(binary[3])*2**4
# e=int(binary[4])*2**3
# f=int(binary[5])*2**2
# g=int(binary[6])*2**1
# h=int(binary[7])*2**0
# ans=(a+b+c+e+d+f+g+h)
# print("The decimal equivalent of "+binary+" is:", ans)

#9
# sideA=float(input("Please enter the leg of the first leg: "))
# sideB=float(input("Please enter the leg of the second leg: "))
# sideC=(sideA**2+sideB**2)**(1/2)
# print("The length of the hypotenuse IS",sideC)

