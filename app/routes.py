from app import app
from flask import render_template

asd = [
    {
        "temperature": 25
    },
    {
        "temperature": 35
    }
]

@app.route('/')
def hello():
    return render_template("test.html", lista=asd)
