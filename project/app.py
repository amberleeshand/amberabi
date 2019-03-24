from flask import Flask, render_template, request

app = Flask(__name__)

#defining pages
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/lesson1")
def lesson1():
    return render_template("lesson1.html")

@app.route("/lesson2")
def lesson2():
    return render_template("lesson2.html")

@app.route("/lesson3")
def lesson3():
    return render_template("lesson3.html")

@app.route("/lesson4")
def lesson4():
    return render_template("lesson4.html")

@app.route("/sign_up")
def sign_up():
  return render_template("sign_up.html")

@app.route("/successful",methods = ["POST"])
def successful():
    return render_template('successful.html')

# quiz python

@app.route('/lesson1', methods=['GET', 'POST'])
def startthequiz():
	return render_template('lesson1.html')

@app.route('/<question>', methods=['GET', 'POST'])
def question(question):
	# Selecting the relevant data from the quiz dictionary
	phrase = quiz.get(question)[0]
	next_question = quiz.get(question)[2]

	return render_template('question.html', phrase=phrase, next_question=next_question)

@app.route('/result/<question>', methods=['GET', 'POST'])
def result(question):
	# Selecting the relevant data from the quiz dictionary
	answer = quiz.get(question)[1]
	next_question = quiz.get(question)[2]

	# The user inputted data
	form_data = request.form
	user_answer = form_data["Answer"]

	# Checking the answer
	if answer==user_answer.lower():
		result = "correct"
	else:
		result = "incorrect"

	return render_template("result.html", result=result, next_question=next_question, answer=answer)

# Dictionary of our quiz data. The key is the question code, used in the URLs
# The value of the dictionary is an array:
# The first element of the array is the phrase, the second the answer, and the third is the next question so the page loops round
quiz = {
	"hello":["hello","hola","howareyou"],
	"howareyou":["how are you", "como estas","whatisyourname"],
	"whatisyourname":["what is your name","como te llamas","end"]
}



app.run(debug = True)
