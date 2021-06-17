import os
from flask import (
        Flask, flash, render_template,
        redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about-us")
def about_us():
    return render_template("about.html")


@app.route("/programme")
def programme():
    return render_template("programme.html")


@app.route("/testmonials")
def get_testimonials():
    testimonials = mongo.db.testimonials.find()
    return render_template("testimonials.html", testimonials=testimonials)


@app.route("/contact-us")
def contact_us():
    return render_template("contact-us.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
