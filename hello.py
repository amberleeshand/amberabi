from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/")
def sign_up():
  return render_template("sign_up.html")

@app.route("/successful",methods = ["POST"])
def result():
     #result = request.form
    return render_template('successful.html')

app.run(debug = True)
