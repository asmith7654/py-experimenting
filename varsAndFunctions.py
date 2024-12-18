#create variables
age = 21
weight = 165.5
name = "Andrew"
male = True

#create function that prints attributes nicely
def printAttributes(age: int,weight: float,name: str,gender: bool) -> None:
    output = f"The subject's age and weight are {age}, {weight}. "
    if gender:
        output += f"The subject is male, and his name is {name}. "
    else:
        output += f"The subject is female, and her name is {name}. "
    return print(output)

#print variables
printAttributes(age,weight,name,male)

#use user input in function
userAge = int(input("Enter your age: "))
userWeight = float(input("Enter your weight in lbs: "))
userName = input("Enter your name: ")
tempGender = input("Type 'Male' or 'Female' according to your gender: ")
userGender = True
if tempGender == "Male":
    pass
else:
    userGender = False

printAttributes(userAge,userWeight,userName,userGender)

#use modulus by checking if age is even
if userAge%2==0:
    print("Age is even. ")
else:
    print("Age is odd. ")

#practice converting variables
dogAge = userAge * 7
kilos = userWeight * 0.454
if userGender:
    spanishName = "La " + userName
else:
    spanishName = "El " + userName

oppositeGender = not userGender

print("The following is your description in dog years, kilos, your spanish name, and the opposite gender.")
printAttributes(dogAge,kilos,spanishName,oppositeGender)


