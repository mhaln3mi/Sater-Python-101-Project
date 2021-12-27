
data = {
    "Amal": 1111111111,
    "Mohammed": 2222222222,
    "Khadijah": 3333333333,
    "Abdullah": 4444444444,
    "Rawan": 5555555555,
    "Faisal": 6666666666,
    "Layla": 7777777777,

}

def main():
    user_input = input("Enter 1 to look up by phone number, 2 to look up by name, and 3 to add a number: ")
    if user_input == "1":
        lookUpPhoneNumber()
    elif user_input == "2":
        lookByName()
    elif user_input == "3":
        addNumber()
    else:
        print("invalid input")




def lookUpPhoneNumber():
    user_input = input("Enter phone number: ")
    digits = len(user_input)
    if digits != 10 or user_input.isnumeric() == False:
        print("This is invalid number")
    else:
        for name, number in data.items():
            if number == int(user_input):
                print(name)
                break
        else:
            print("Sorry, the number is not found ")


def lookByName():
    user_input = input("enter the name: ")
    if user_input.isalpha() == False:
        print("This is invalid number")
    else:
        for name, number in data.items():
            if name == user_input:
                print(number)
                break
        else:
            print("Sorry, the name is not found ")


def addNumber():
    user_input = input("Please enter a name to add: ")
    user_input2 = input("Please enter a phone number to add: ")

    if user_input.isalpha() == True and len(user_input2) == 10:
        data[user_input] = int(user_input2)
        print("The number is added")
    else:
        print("This is invalid input")


main()
