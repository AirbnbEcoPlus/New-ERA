from flask import Flask, render_template
from database import databaseConnector
app = Flask(__name__)




@app.route('/')
def panel():
    if databaseConnector.get_option("setup") == "false":
        return render_template("setup.html")
    elif databaseConnector.get_option("setup") == "true":
        return render_template("index.html")

@app.route('/addoption/<name>/<value>')
def addoption(name, value):
        databaseConnector.add_option(name, value)
        return "done"

@app.route('/changeoption/<name>/<value>')
def changeoption(name, value):
    databaseConnector.change_option(name, value)
    return "done"

@app.route('/addcommand/<command>')
def addcommand(command):
    databaseConnector.add_command(command)

@app.route('/addevent/<event>')
def addevent(event):
    databaseConnector.add_event(event)

app.run(host='0.0.0.0', port='8000', debug=True)
