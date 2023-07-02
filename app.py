from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", title="Proficiō: Home")

@app.route('/find_profession')
def find_profession():
    return render_template("find_profession.html", title="Proficiō: Find Profession")


if __name__ == '__main__':
    app.run()
