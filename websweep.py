#Kayla Krigbaum
#CS101, May Zein El Din, 11am
#Program 4

#create all needed lists and variables
headers = []
readyHeaders = []
inputFile = 0
x = True
y = True

#LOOPS:
#this loop gets the user's input for the file to read from
while x == True:
    try:
        inputFile = input("Enter a file to read:")
        inputStream = open(inputFile, "r")
        x = False
    except FileNotFoundError:
        print("The file you entered does not exist. Try entering a new file.")

#this loop gets the user's input for the file to output to
while y == True:
    try:
        outputFile = input("Name the file you want to output to:")

        outputStream = open(outputFile , 'w')
        if outputFile[-4:] != ".txt":
            raise Exception
        y = False
    except IOError:
        print("The name chosen is invalid. Try another name.")
    except Exception:
        print("The file can only be a .txt file.")

#FUNCTIONS
def headerFinder():
    '''this function finds all of the headers inside of the user's chosen file and appends them to a list'''
    inputLines = inputStream.readlines()
    for line in inputLines:
        if (line[:2] == "<h") and (line[2].isdigit() == True):
            headers.append(line)

def headerFormatter():
    '''this function uses the headers in the headerFinder list and formats them for output'''
    for header in headers:
        formatheader = ""
        formatheader = "*"+ header[4:-6]+ "\n"
        if int(header[2]) == 1:
            readyHeader = "".join(formatheader)
            readyHeaders.append(readyHeader)
        if int(header[2]) > 1:
            formatheader = formatheader.split()
            formatheader.insert(0, "\t" * (int(header[2]) - 1))
            readyHeader = "".join(formatheader) + '\n'
            readyHeaders.append(readyHeader)

def output():
    '''this function writes all of the formatted headers to the user's chosen file'''
    outputStream.writelines(readyHeaders)

#MAIN BODY
    
#step one is to call headerFinder
headerFinder()
#step two is to call headerFormatter
headerFormatter()
#step three is to call output
output()
#step four is to tell the user that the file was created
print("Your file was created. Goodbye") 

#the final step is to close all of the open files 
outputStream.close()
inputStream.close()

