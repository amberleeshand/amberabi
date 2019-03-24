from flask import Flask, render_template, request

app = Flask(__name__)

#defining pages
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/lesson")
def lesson():
    return render_template("lesson.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/sign_up")
def sign_up():
  return render_template("sign_up.html")

@app.route("/successful",methods = ["POST"])
def successful():
    return render_template('successful.html')

# quiz python

@app.route('/quiz', methods=['GET', 'POST'])
def startthequiz():
	return render_template('quiz.html')

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
