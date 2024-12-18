madisonsBank = "$10"

print("Madison I hope you are not mad!")
angerStatus = True
response1 = input("Are you? Type 'yes' or 'no': ")
if response1 == "yes":
    pass
else:
    angerStatus = False
    print("Thank god!")

if angerStatus:
    print("What do I need to do to make you not mad?")
    response2 = input("Type '1' if you need money, type '2' if you need another python program: ")
    if response2 == "1":
        print(f"Madisons starting bank balance: {madisonsBank}")
        while(True):
            madisonsBank += "0"
            print(f"Madisons new bank balance: {madisonsBank}")
            response3 = input("Are you still mad? Type 'yes' or 'no': ")
            if response3 == "yes":
                pass
            else:
                print("I am glad you are no longer mad :D")
                break
    else:
        print("That will take a while give me some time.")