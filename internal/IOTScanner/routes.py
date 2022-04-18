from tkinter import N
from IOTScanner import app
from IOTScanner import scanner
from flask import render_template


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scanner", methods=['POST'])
def scannerRoute():
    devices = scanner.main()
    return render_template("scannerresults.html", results=devices)

@app.route("/64d42a0081addc9bd303ccf4bd598046")
def endpoint():
    return ""

