from datetime import datetime

print("Please enter your name and age:")
localName = input("Name: ")
localAge = input("Age: ")
localAge = int(localAge)
print("Your name is " + localName)

def hundredWhen(age):
    calcOne = 100 - age
    yearNow = datetime.now().year
    calcFinal = calcOne + yearNow
    print("Your will be 100 in " + str(calcFinal))

hundredWhen(localAge)

