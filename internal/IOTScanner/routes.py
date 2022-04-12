from IOTScanner import app
from IOTScanner import external
from flask import render_template


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scanner", methods=['POST'])
def scanner():
    devices = external.main()
    return render_template("scannerresults.html", results=devices)
