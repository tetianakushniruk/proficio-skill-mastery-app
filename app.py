from flask import Flask, render_template, request, jsonify, session
from ai21_integration import utils

import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/validate', methods=['POST'])
def validate():
    query = request.form['query']
    is_valid, error_msg = utils.is_valid_profession(query)
    print(error_msg)
    if not is_valid:
        return jsonify({'error': True, 'error_msg': error_msg}), 400
    return jsonify({'success': True}), 200

@app.route('/roadmap', methods=['POST'])
def roadmap():
    query = request.form['query']
    try:
        session['roadmap'] = utils.roadmap(query)
    except Exception:
        return jsonify({'error': True}), 400
    return jsonify({'success': True}), 200

@app.route('/books', methods=['POST'])
def books():
    query = request.form['query']
    try:
        session['books'] = utils.books(query)
    except Exception:
        return jsonify({'error': True}), 400
    return jsonify({'success': True}), 200

@app.route('/questions', methods=['POST'])
def questions():
    query = request.form['query']
    try:
        session['questions'] = utils.interview_q(query)
    except Exception:
        return jsonify({'error': True}), 400
    return jsonify({'success': True}), 200

@app.route('/tip', methods=['POST'])
def tip():
    query = request.form['query']
    try:
        session['tip'] = utils.tip(query)
    except Exception:
        return jsonify({'error': True}), 400
    return jsonify({'success': True}), 200

@app.route('/', methods=['GET'])
def home():
    roadmap = session.get('roadmap')
    books = session.get('books')
    questions = session.get('questions')
    tip = session.get('tip')

    return render_template("index.html", title="Proficiō: Home",
                           roadmap=roadmap,
                           books=books,
                           questions=questions,
                           tip=tip)

@app.route('/find_profession')
def find_profession():
    return render_template("find_profession.html", title="Proficiō: Find Profession")


if __name__ == '__main__':
    app.run()
