from flask import Flask, render_template, request

app = Flask(__name__)

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
    print "\n:: DIAG:: print args - from GET"
    print request.args
    print "\n:: DIAG:: print form - from POST"
    print request.form
    print "\n:: DIAG:: print headers"
    print request.headers
    if(request.form): # empty dictionaries evaluate to False
        print "\n\n\n :::: DIAG :::: checks for request form \n\n\n"
        if(request.form['username'] == "JFreyra"): # username is only possible POST key
            return render_template("validated.html")
    return render_template("invalidated.html")

if(__name__ == "__main__"):
    app.debug = True
    app.run()
