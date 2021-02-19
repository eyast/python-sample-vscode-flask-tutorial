from datetime import datetime
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import time
from . import app

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
def get_temp():
    pageloc = "https://www.weatherzone.com.au/vic/melbourne/melbourne"
    page = requests.request(method='GET', url=pageloc)
    soup = BeautifulSoup(page.content, "html.parser")
    attention = soup.find(class_ = "tempnow")
    attention = attention.text
    attention = str.split(attention, ".")
    attention = attention[0]
    print(attention)
    return attention

def test_answer():
    assert type(get_temp) == int