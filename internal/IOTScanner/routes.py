from IOTScanner import app,external
from flask import render_template


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scanner", methods=['POST'])
def scanner():
    x = external.testing()
    return render_template("scannerresults.html")


