from IOTScanner import app
from flask import render_template
from time import sleep


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scanner", methods=['POST'])
def scanner():
    sleep(10)
    return render_template("scannerresults.html")


