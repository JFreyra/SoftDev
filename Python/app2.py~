from flask import Flask
#python can be object oriented

app = Flask(__name__)
#creates instance of Flask and passes env variable __name__

@app.route("/")
def hello_world():
    return '''<html>
              <head>
              <title>Flask Pages!!!</title>
              </head>
              <body>
              <a href="http://127.0.0.1:5000/anotherone">Another One!</a><br>
              <a href="http://127.0.0.1:5000/anotherone2">Another another One!</a><br>
              </body>
              </html> '''

@app.route("/anotherone")
def hello_world2():
    return '''another one<br>
              <a href="http://127.0.0.1:5000/">back</a>'''

@app.route("/anotherone2")
def hello_world3():
    return '''another one again<br>
              <a href="http://127.0.0.1:5000/">back</a>'''

if(__name__ == "__main__"):
    app.run()
