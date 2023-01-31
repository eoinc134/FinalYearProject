
def getAvailability():
    CAL = open("DataFiles\CAL.lst", "r")
    colours = (CAL.readline())

    for lecturer in CAL:
        availability = lecturer.split(' ')
        L.append(list(int(x) for x in availability))

    return colours

#Variables#
L = []                              #Colour Availability List
TOTAL_COLOURS = getAvailability()   #Total Number of Colours


#Print CAL
print ("Total time slots:", TOTAL_COLOURS)
for x in L:
    print("Total Availability:", x[0])
    print("Available Times:", x[1:])
