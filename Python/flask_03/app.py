from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "you're home!"

@app.route("/page1")
def test():
    return app.send_static_file("test.html")

if(__name__ == "__main__"):
    app.debug = True
    app.run()
