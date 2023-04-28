from flask import render_template
from main import app
from models import Estudo

@app.route("/")
def index():
    return render_template("index.html")