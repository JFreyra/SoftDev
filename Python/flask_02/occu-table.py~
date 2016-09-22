from flask import Flask, render_template

app = Flask(__name__)

links = ["\"http://127.0.0.1:5000/jobs\"",
         "\"http://127.0.0.1:5000/tables\"",
         "\"http://127.0.0.1:5000/occupations\""]

linksT = ["Jobs!",
          "Tables!",
          "Occupation Table!"]

@app.route("/")
def home():
    return render_template("basic.html",
                           title = "Homepage",
                           heading = "Links: jobs, tables, occupation table!",
                           varL = links)

if(__name__ == "__main__"):
    app.debug = True
    app.run()
