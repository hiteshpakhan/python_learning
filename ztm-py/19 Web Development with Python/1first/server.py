from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')     #here you can create any url you want to make for your page
def hello_world():
    return render_template("index.html")       #here if your linking th epage by render_template() it will only catch th epage from the templaes folder

@app.route("/about.html")   #you can name your url any you want
def about():
    return render_template("about.html")

@app.route('/blog') 
def hello_world2():
    return 'Hello, this is my blog hope you enjoy it'     #this is the simple sentence


# @app.route('/favicon.ico') 
# def hello_world2():
#     return 'Hello, this is my blog hope you enjoy it' 