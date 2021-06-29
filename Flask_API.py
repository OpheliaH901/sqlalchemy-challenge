# 1. import Flask
from flask import Flask
# from test_function import *

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

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
