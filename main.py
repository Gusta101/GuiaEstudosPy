from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile("config.py")

def main():
    app.run(port=8080, debug=True)

from views import *

if __name__ == '__main__':
    main()