#Kayla Krigbaum
#CS101
#Program 3
#Due 10/07/2018

#All functions are in the order they are called in the main loop; this will help you understand which things are being executed first

#The first thing the main loop does is check if the length of the string is valid
def length(string):
    '''This function checks if the length of the string valid'''
    if len(string) != 13:
        '''If the length of the string is not equal to 13, then it is invalid and returns false'''
        return False
    else:
        '''If the length of the string is equal to 13, then it is valid and returns true'''
        return True

#The second thing the main loop does is check if all of the characters in the string are in the correct range of letters and numbers
def validCharacter(string):
    '''This function checks to make sure that only valid letters and numbers are included in the string'''
    validLetters = ['A','B','C','D','E','F']
    validNumbers = ['0','1','2','3','4','5','6','7','8','9']
    for char in string:
        '''This looks at each character in the string'''
        if (char in validLetters) or (char in validNumbers):
            '''If the character is a valid letter and number, then it will check the next character'''
            continue
        else:
            '''If the character is not a valid letter or number, then it will return the character so the output will tell the user which character was bad'''
            return char
#The third thing the main loop does is check if the first character is in the valid range of letters
def firstCharValid(string):
    '''This checks to make sure that the first letter in the string is A-D'''
    validLetters = ['A','B','C','D']
    if string[0] not in validLetters:
        '''If the first letter is not in the validLetters list, then it will return false'''
        return False
    else:
        '''If the first letter is in the list, then it will return true'''
        return True        

#The fourth thing the main loop does is check if the second character is in the valid range of letters
def secondCharValid(string):
    '''This checks to make sure that the second letter in the string is A-E'''
    validLetters = ['A','B','C','D','E']
    if string[1] not in validLetters:
        '''If the second letter is not in the validLetters list, then it will return false'''
        return False
    else:
        '''If the second letter is in the validLetters list, then it will return true'''
        return True

#The fifth thing the main loop does is check if the last character is a number
def lastchar(string):
    '''This checks to make sure that the last character of the user entry is a number'''
    if string[12].isdigit == False:
        '''If the last character is not a digit, it will return false'''
        return False
    else:
        '''If the last character is a digit, it will return true'''
        return True

#The sixth thing the main loop does is check the modulus of the last character
def mod(string):
    '''This function gets the modulus of the product sum and compares it to the last number of the given string'''
    value = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
        }
    
    productSum = 0
    
    for index in range(len(string)-1):
        '''This checks each index in the string, excluding the last number'''
        if string[index].isalpha() == True:
            '''If the index is a letter, the product sum is the index multiplied by the value for that letter (which is in the dictionary)'''
            productSum += (index * value[string[index]])
        else:
            '''If the index is a number, the product sum is the index multiplied by the value for that number'''
            productSum += (int(string[index]) * index)

    remainder = productSum % 10
    
    if int(string[12]) == remainder:
        '''If the last number is equal to the modulus of the product sum by ten, then it is valid and returns true'''
        return True
    else:
        '''If the last number is not equal to the modulus of the product sum by ten, then it is invalid and returns false'''
        return False            

#The seventh thing the main loop does is check the class and assignment types of the entry:

#class:
def firstChar(string):
    '''This returns a value for the first letter in the string'''
    for x in string:
        '''This looks at x in the string'''
        if string[0] == "A":
            '''If the first letter is A, then it will return CS101'''
            return "CS101"
        if string[0] == "B":
            '''If the first letter is B, then it will return CS191'''
            return "CS191"
        if string[0] == "C":
            '''If the first letter is C, then it will return CS201'''
            return "CS201"
        if string[0] == "D":
            '''If the first letter is D, then it will return CS291'''
            return "CS291"

#assignment:
def secondChar(string):
    '''This returns a value for the second letter in the string'''
    for x in string:
        if string[1] == "A":
            '''If the second letter is A, then it will return Test'''
            return "Test"
        if string[1] == "B":
            '''If the second letter is B, then it will return Program'''
            return "Program"
        if string[1] == "C":
            '''If the second letter is C, then it will return Quiz'''
            return "Quiz"
        if string[1] == "D":
            '''If the second letter is D, then it will return Final'''
            return "Final"
        if string[1] == "E":
            '''If the second letter is E, then it will return Other'''
            return "Other"

#This is now the main body of code which references all of the above functions
print("Welcome to the assignment # validator")

while True:
    '''This will allow the program to run on an infinite loop unless the user breaks it'''
    userInput = input("Enter the assignment number ==>")
    userInput = userInput.upper()
    if userInput == '':
        '''If the user presses enter, the program will break'''
        break
    elif length(userInput) == False:
        '''If the length function returns false, this will be the output'''
        print("Incorrect, the value has to be 13 characters in length")
    elif validCharacter(userInput) != None:
        '''If the validCharacter function returns x, then the output will tell the user which character is wrong'''
        print("Incorrect, there is an illegal character {} in the value".format(validCharacter(userInput)))
    elif firstCharValid(userInput) == False:
        '''If the firstCharValid function returns false, it will tell the user that the first character is wrong'''
        print("Incorrect, the first character cannot be {}, only A-D.".format(userInput[0]))
    elif secondCharValid(userInput) == False:
        '''If the secondCharValid function returns false, it will tell the user that the second character is wrong'''
        print("Incorrect, the second character cannot be {}, only A-E.".format(userInput[1]))
    elif lastchar(userInput) == False:
        '''If the lastchar function returns false, it will tell the user that the last character must be a number'''
        print("Incorrect, the last character must be a number.")
    elif mod(userInput) != True:
        '''If the mod function does not return true, it will tell the user that the last digit of the entry is not correct'''
        print("Invalid, the last digit of your entry is not correct.")
    else:
        '''If none of the above conditions display an error message, this will tell the user that their input is valid and which class and assignment it is'''
        print("Valid, class is {} and assignment is a {}".format(firstChar(userInput),secondChar(userInput)))

print("You have chosen to stop the program. Goodbye.")

                      
