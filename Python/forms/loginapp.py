from flask import Flask, render_template, request
import cgi,cgitb,os
cgitb.enable()

app = Flask(__name__)

@app.route("/auth")
def home():
    print request.headers
    print request.method
    print request
    return app.send_static_file("forms.html")

if(__name__ == "__main__"):
    app.debug = True
    app.run()
