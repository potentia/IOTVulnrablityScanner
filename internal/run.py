from flask import Flask
from IOTScanner import app

if __name__ == '__main__':
    app.run(host='192.168.1.2', port=5000, debug=True)
