from flask import Flask, render_template, request
import hashlib,csv

app = Flask(__name__)

def dictfy(csvFile):
    with open(csvFile, mode="r") as infile:
        reader = csv.reader(infile)
        mydict = dict((rows[0],rows[1]) for rows in reader)
    return mydict

@app.route("/")
def login():
    return render_template("basic.html")

#requires another landing page
@app.route("/auth",methods=['POST'])
def authenticate():
    print "\n::DIAG:: print app"
    print app
    print "\n:: DIAG:: print request"
    print request
    print "\n:: DIAG:: print form - from POST"
    print request.form
    if(request.form): # empty dictionaries evaluate to False
        if(request.form['username'] == "JFreyra"): # username is only possible POST key
            return render_template("validated.html")
    return render_template("invalidated.html")

def checker(userStr,passStr):
    return 0

if(__name__ == "__main__"):
    app.debug = True
    app.run()
