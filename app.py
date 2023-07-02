from flask import Flask, render_template, request
from ai21_integration import utils

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    roadmap = ''
    books = ''
    interview_q = ''
    if request.method == 'POST':
        query = request.form['q']
        is_valid = utils.is_valid_profession(query)
        roadmap = utils.roadmap(query)
        books = utils.books(query)
        interview_q = utils.interview_q(query)
    return render_template("index.html", title="Proficiō: Home",
                           roadmap=roadmap,
                           books=books,
                           questions=interview_q)

@app.route('/find_profession')
def find_profession():
    return render_template("find_profession.html", title="Proficiō: Find Profession")


if __name__ == '__main__':
    app.run()
