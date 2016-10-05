# Imports

from flask import Flask, render_template, request
import hashlib,csv


# Object Instantiations

app = Flask(__name__)
hashObj = hashlib.sha224()


### Helper Functions ###

# Reads a given csv file into a dictionary
def dictify(csvFile):
    with open(csvFile, mode="r") as infile:
        reader = csv.reader(infile)
        mydict = dict((rows[0],rows[1]) for rows in reader)
    return mydict

# Returns hash sha224 of a string in hex
def myHash(value):
    hashObj.update(value)
    return hashObj.hexdigest()

# Writes a key and hashed value to a given csv file
def writeTo(csvFile,key,value):
    with open(csvFile, mode="w") as outfile:
        outfile.write(key+","+hash(value)+"\n")

# Verifies form input for three cases:
#
# Username is not in csv : directs user to account creation
# Username and password are in csv and match : directs user to success message
# Username is in csv but password does not match : directs user to failure message
def checker(userStr,passStr):
    tempDict = dictify("data/userpass.csv")
    if(not tempDict.has_key(userStr)):
        return addAcc("Login Failed: Username not in System")
    elif(tempDict[userStr] == myHash(passStr)):
        return render_template("validation.html",
                               validated = 1)
    return render_template("validation.html",
                           validated = 0)

#-------------------------------------------------------------------------------------#

### Main Functions ###

# Main Page
# Either sends user to authentication or account creation
# Login button -> authentication (authenticate() method)
# Register button -> account creation (addAcc() method)
@app.route("/")
def login():
    return render_template("basic.html",
                           message = 'Sign Up or Log in!')

# If form input is left blank, sends user to and emptyArgError page
# else runs checker and returns output
@app.route("/auth",methods=['POST']) # requires another landing page
def authenticate():
    user = request.form['username']
    passW = request.form['password'] 
    if(user != '' and passW != ''):
        return checker(user,passW)
    return app.send_static_file("emptyArgError.html")

# Displays account creation form then directs to signup()
@app.route("/addAcc")
def addAcc(msg):
    return render_template("addAcc.html",
                           message = msg)

# Adds new user
# Does not add new user if: any field is left blank or username is already taken
# If not added, user is directed to account creation or emptyArgError depending on infraction
@app.route("/signup",methods=['POST'])
def signup():
    user = request.form['username']
    passW = request.form['password'] 
    if(user != '' and passW != ''):
        tempDict = dictify("data/userpass.csv")
        if(tempDict.has_key(user)):
            return addAcc("Sign Up Failed! Username already taken")
        writeTo("data/userpass.csv",user,passW)
        return render_template("basic.html",
                               message = "Sign Up Complete! Please Login")
    return app.send_static_file("emptyArgError.html")

#--------------------------------------------------------------------------------------#

# Flask thingie
if(__name__ == "__main__"):
    app.debug = True
    app.run()
