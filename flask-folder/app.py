#######################################
# FLASK APPLICATION
#######################################

# extensions that allow specific classes and functions
from flask import Flask, Blueprint, render_template, url_for, redirect

# a 'blueprint' of the website structure
views = Blueprint(__name__, "views")

# the website is defined as a flask app and the url prefix is set to '/'.
app = Flask(__name__)
app.register_blueprint(views, url_prefix = "/") # this a is flask application and every single page has a / prefix which seperates each page to flask.

#######################################
# APPLICATION PAGES
#######################################
# @ symbol is a decorator
# this is how the home page is accessed (only /)
@app.route("/")
def home():   # here is the location of the html file
    return render_template("index.html") # this is where to put the name of file)

@app.route("/ibrahim")
def ibrahim_page():
    return render_template("ibrahim.html", favourite_drink = "not coffee") 

#######################################
@app.route("/home")
def home_redirect():
    return redirect(url_for("home"))

#######################################

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html") , 404

#######################################

# debugging is activated and the project is set to be hosted on port 8000 (debug only in tetsing)
if __name__ == "__main__":
    app.run(debug = True, port = 8000)

#######################################