from flask import Flask, render_template, request, jsonify
from ai21_integration import utils

app = Flask(__name__)

UNKNOWN_ERROR = 'Oops! Something went wrong. Try again'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['q']
        is_valid, error_msg = utils.is_valid_profession(query)
        if not is_valid:
            return render_template("index.html", title="Proficiō: Error",
                                    error=True, error_msg=error_msg or UNKNOWN_ERROR)

        roadmap = utils.roadmap(query)
        books = utils.books(query)
        interview_q = utils.interview_q(query)
        tip = utils.tip(query)

        return render_template("index.html", title="Proficiō: Home",
                               roadmap=roadmap,
                               books=books,
                               questions=interview_q,
                               tip=tip)

    return render_template("index.html", title="Proficiō: Home")

@app.route('/find_profession')
def find_profession():
    return render_template("find_profession.html", title="Proficiō: Find Profession")


if __name__ == '__main__':
    app.run()
