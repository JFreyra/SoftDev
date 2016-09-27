import random

#returns random weighted selection from a dictionary based on float values
#takes dictionary myDict with keys with float values
#takes String totalKey that is key in myDict that has value of total percentage
def randDictSelection(myDict,totalKey):
    selectjob = random.random()*float(myDict[totalKey])
    counter = 0.0;
    for key in myDict:
        counter+=float(myDict[key])
        if(selectjob<=counter):
            return(key)
