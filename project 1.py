#project 1:

print("welcome to personal data collector")
print()

name = input("Please Enter Your Name: ")
age = int(input("Please Enter Your Age: "))
height = float(input("Please Enter your height in meters: "))
number = int(input("Please Enter your favourite number: "))

print()
print("Thank you!here is the information we collected:")
print()



print("Name:", name ,("Type:" ,type(name),"Memory Address:",id(name)))

print("Age:",age ,("Type:",type(age),"Memory Address:",id(age)))

print("height:",height,("Type:",type(height),"Memory Address:",id(height)))

print("number:",number,("Type:",type(number),"Memory Address:",id(number)))

print()

birth_year = 2026 -age
print()

print("Your birth year is aproximately:",birth_year,"(based on your age of ",age,")")

print()
print("thank you for using the personal data collector.Goodbye!")
