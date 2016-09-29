from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    print app
    print request
    print request.args
    print request.headers
    return render_template("basic.html")

#requires another landing page
@app.route("/auth",methods=['POST'])
def authenticate():
    print app
    print request
    print request.args
    print request.headers
    return "hi there"

if(__name__ == "__main__"):
    app.debug = True
    app.run()
