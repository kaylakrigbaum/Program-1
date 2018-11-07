#Kayla Krigbaum
#Program 5
#CS101 11am
#May Zein el Din
#Due: 11/04/18

import csv

#needed lists and datatypes
all = {} 
convertedlist = []
copyconverted = convertedlist[:]

#Functions
def importfile():
    '''this function opens the file and returns the value of it opened and read'''
    try:   
        sunspots = open('sunspots.csv','r')
        sunreader = csv.reader(sunspots, delimiter =',')
        return sunreader
        
    except FileNotFoundError:
        print("There is a problem opening the file. (IE. The file is not in the correct directory.)")


def format(file):
    '''this function takes the open and read file and formats it to year, month, total format'''
    try:
        for row in file:
            if row[0] not in all:
                all[row[0]] = {row[1]: int(row[4])}  
            else:
                if int(row[4]) == -1:
                    adder = 0
                else:
                    adder = int(row[4])
                if row[1] in all[row[0]]:
                    all[row[0]][row[1]] += adder      
                else:
                    all[row[0]][row[1]] = adder
                    
    except ValueError:
        row[4] = 0

def converted(dictionary):
    '''this function takes the created dictionary and puts it in the format of a (year, month, sunspots) tuple saved in a list'''
    for (year, month) in dictionary.items():
        for (month, sunspots) in month.items():    
            convertedlist.append((year,month,sunspots))
    
def smoothed(copylist, original):
    '''this function takes the original list (year, month, total) and calculates the smoothed average and replaces the total section with the smoothed average. Copylist: (year, month, smoothed average).'''
    t = []
    position = 0
    for line in original:
        t.append(line[2])
    for tuples in original:
        if(((int(tuples[0]) == 1818 and int(tuples[1]) <= 6)) or (int(tuples[0]) == 2015) or ((int(tuples[0]) == 2014) and (int(tuples[1]) == 12))):
            position += 1
            continue
        else:
            smooth = (t[position-6]/2 + t[position-5] + t[position-4] + t[position-3] + t[position-2] + t[position-1] + t[position] + t[position+1] + t[position + 2] + t[position + 3] + t[position + 4] + t[position + 5] + t[position + 6]/2) / 12
            new_tuple = (tuples[0],tuples[1],smooth)
            copylist.append(new_tuple)
        position += 1
    return copylist

def writemonthtotal(orignallist):
    '''this takes the orignallist (year, month, total) and formats it and writes it to a new file'''
    with open('monthtotal.txt','w') as monthtotal:
        for line in orignallist:
            counter = 1
            for element in line:
                if counter <= 2:
                    monthtotal.write("{}," .format(element))
                    counter += 1
                else:
                    monthtotal.write("{}\n" .format(element))

def writemonthsmoothed(listcopy):
    '''this takes the listcopy (year, month, smoothed average) and formats it and writes it to a new file'''
    with open('monthsmoothed.txt', 'w') as monthsmoothed:
        for line in listcopy:
            counter = 1
            for element in line:
                if counter <= 2:
                    monthsmoothed.write("{},".format(element))
                    counter += 1
                else:
                    monthsmoothed.write("{}\n" .format(element))

#Main Body (function calls)
format(importfile())
converted(all)
new_list = smoothed(copyconverted, convertedlist)
writemonthtotal(convertedlist)
writemonthsmoothed(copyconverted)

