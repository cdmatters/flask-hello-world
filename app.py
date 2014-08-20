# ---- Flask Hello World ---- #

#import the Flask class from the flask module
from flask import Flask

#create the application object

app = Flask(__name__)

#error handling
app.config["DEBUG"] = True


#use decorators to link the function to and url
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

#dynamic routes coming now
@app.route("/test/<search_query>")
def search(search_query):
    return "Hello, were you looking for {}".format(search_query)

@app.route("/integer/<int:value>")
def valueprint(value):
    print value + 1
    return "correct"

@app.route("/float/<float:value>")
def floatprint(value):
    print value + 1.2
    return "correct"

@app.route("/path/<path:bathtime>")
def pathprint(bathtime):
    print "looks like you're trying to get to>>>  {}".format(bathtime)
    return bathtime

@app.route("/name/<name>")
def index(name):
    if name.lower() == "eric":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404




#start the development server using the run() method
if __name__ == "__main__":
        app.run()

