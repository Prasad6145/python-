#Add parentheses to the following expression so that it evaluates to 0. 8 - 3 * 2 - 1 + 1
a=(0.8-3)*(2-(1+1))
a
#Implement Simple Interest Formula : S.I. = P × R × T

P = 1500
R = 9.5
T = 20
SI=P*R*T
SI

#Try to implement Compound Interest Formula : V = P(1+r/n)^nt

P = 1500
r = 0.043
n = 4
t = 6
V=P*(1+r/n)**(n*t)
V

#Try to implement Compound Interest Formula : V = P(1+r/n)^nt

P = 1500
r = 0.043
n = 4
t = 6
V=P*(1+r/n)**(n*t)
V

#Implement Fahrenheit to Celsius conversion formula : F = ( C x 9 / 5 ) + 32
C = 253
F=(C*9/5)+32
C

#Create 2 variables and assign values like name and surname from the user. Then concatenate these 2 variables and display using print function.
name=input('enter your name : ')
surname=input('enter your surname : ')
print(name+" "+surname)

#Create 2 variables and assign values like birth month and birth year from the user. Display these 2 variables and the length of these variables inside a single print function.
birth_month=input()
birth_year=input()
print(birth_month+"-"+birth_year, len(birth_month),len(birth_year))


#Create 2 variables and assign values of user's favourite IPL team and any number between 1 - 10. Display the name of this favourite IPL team as many times as the number they pick from 1 - 10.
#Note : Pass the message in the input function for taking information from the user.
favourite_team=input()
number=int(input())
print(favourite_team*number)

#Create 4 variables and take input from user for information like height, weight, age and a number from 1 - 10. Display the results of true division, floor division and exponentiation of height, weight and age with the number selected from 1 - 10 concatenated together inside a print function respectively.
#Note : Pass the message in the input function for taking information from the user. Hint : Concatenate string \n to display output on new line.
height=int(input())
weight=int(input())
age=int(input())
number=int(input())
print(height/number,"\n",height//number,"\n",height**number,"\n",weight/number,"\n",weight//number,"\n",weight**number,"\n",age/number,"\n",age//number,"\n",age**number)
