from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

@app.route("/hi")
def hi_world():
    return "<b>Hi world</b>"

@app.route("/about")
def about():
    return "<p>we are a youth based and youth-driven organization determined to provide low-cost and effective services to our clients</p>"


@app.route("/home")
def home():
    return "<p>Providing efficient, effective and cost-saving services is what we do best</p>"

@app.route("/contact")
def contact():
    return "<p> Our contacts:<p> Email: tokkitdadauda@gmail.com <li>Phone no: 07035963936</li></p>"


@app.route("/services")
def services():
    return "<p>Recruitment || Training || counselling || Placement</p>"

