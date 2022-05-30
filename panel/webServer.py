from flask import Flask, render_template
from database import databaseConnector
app = Flask(__name__)

if databaseConnector.get_option("setup") == "false":
    @app.route('/')
    def setup():
        return render_template("setup.html")
elif databaseConnector.get_option("setup") == "true":
    @app.route('/')
    def start():
        return render_template("index.html")
app.run(host='0.0.0.0', port='8000', debug=True)


