import csv

#removes only one entry whose key does not have an a castable float value
#must optimize for multiple removals
#good for removing headers in csv file
#takes String csvFile (csv filename)
def occDict(csvFile):
    with open(csvFile, mode="r") as infile:
        reader = csv.reader(infile)
        mydict = dict((rows[0],rows[1]) for rows in reader)
    for key in mydict:
        try:
            float(mydict[key])
        except ValueError:
            mydict.pop(key, mydict[key])
            break
    return mydict
