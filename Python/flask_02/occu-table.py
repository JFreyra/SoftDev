from flask import Flask, render_template

app = Flask(__name__)

links = ["jobs",
         "tables",
         "occupations"]

linksT = ["Jobs!",
          "Tables!",
          "Occupation Table!"]

@app.route("/")
def home():
    return render_template("basic.html",
                           title = "Homepage",
                           heading = "Links: jobs, tables, occupation table!",
                           links = True,
                           varL = links)

@app.route("/jobs")
def jobs():
    return "hello"
    #return render_template

@app.route("/tables")
def tables():
    return "hello"

@app.route("/occupations")
def occupations():
    return "hello"

if(__name__ == "__main__"):
    app.debug = True
    app.run()
