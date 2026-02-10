from flask import Flask
from flask import render_template
 # Create an instance of Flask
app = Flask(__name__)

#Functions that returns content
#using app.route decorator totmap the URL

@app.route("/")
def index():
    name_data = None
    return render_template("index.html", name=name_data)


# To run YOUR APP enter "FLASK run" into the TERMINAL
# (if you closed your teminal, open it agai. with CTRL + ')
# TO STOP click CTRL + C in the terminal