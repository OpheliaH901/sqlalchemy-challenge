# Import dependencies
from flask import Flask, request, redirect, jsonify
import numpy as np 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# SET UP DATABASE & DB REFERENCES
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Coming Home AGAIN?!"


@app.route("/contact")
def contact():
    name = 'Ophelia'
    contact = 'phellyh@gmail.com'
    return(f"My name is {name} and please email me at {contact}")

if __name__ == "__main__":
     app.run(debug=True)

# print(__name__)     
