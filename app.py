from flask import Flask
from flask import render_template
 # Create an instance of Flask
app = Flask(__name__)

#Functions that returns content
#using app.route decorator totmap the URL

@app.route("/")
def index():
    name_data = 'None'
    year_data = 2026
    #Can also use lists & dictionaries
    favorite_list = ['Terraria', 'Cloverpit', 'Balatro', 'Tiny Rogues']
    rating_dict ={
        'Terraria' : 'Too. Many. Acheviements.',
        'Cloverpit' : 'LETS GO GAMBLING',
        'Balatro' : 'Poker.',
        'Tiny Rouges' : 'ENDLESS COMBOS'
    }
    return render_template("index.html", name=name_data, favorites=favorite_list, rating=rating_dict)


# To run YOUR APP enter "FLASK run" into the TERMINAL
# (if you closed your teminal, open it agai. with CTRL + ')
# TO STOP click CTRL + C in the terminal