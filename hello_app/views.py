from datetime import datetime
from flask import Flask, render_template
from . import app
import requests
from bs4 import BeautifulSoup
import time

def get_temp_melb():
    url = "https://www.weatherzone.com.au/vic/melbourne/melbourne"
    page = requests.get(url)
    print(page.content)
    time.sleep(1)
    return "eyas"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/temp")
def temp():
    result = get_temp_melb()
    return result