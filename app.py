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
    testimonials = mongo.db.testimonials.find().sort("created_on", -1)
    return render_template("testimonials.html", testimonials=testimonials)


@app.route("/contact-us", methods=["GET", "POST"])
def contact_us():
    """ Insert new contact us record to database """
    if request.method == "POST":
        new_contact = {
            "full_name": request.form.get("full_name"),
            "email": request.form.get("email"),
            "phone": request.form.get("phone"),
            "message": request.form.get("message"),
        }
        mongo.db.contactUs.insert_one(new_contact)
        return redirect(url_for("thank_you"))

    return render_template("contact-us.html")


@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
