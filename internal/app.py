from flask import Flask
import scanner
app=Flask(__name__)


@app.route("/")
def home():
    x = scanner.test()
    return x

app.run(debug=True)

