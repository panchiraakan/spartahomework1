import sqlite3

def init_db():
    with sqlite3.connect('comments.db') as db:
        db.execute('CREATE TABLE IF NOT EXISTS comments (comment TEXT)')

def add_comment(comment: str):
    with sqlite3.connect('comments.db') as db:
        db.execute('INSERT INTO comments (comment) VALUES (?)', (comment,))

def get_comments():
    with sqlite3.connect('comments.db') as db:
        return db.execute('SELECT comment FROM comments').fetchall()

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form['comment']
        add_comment(comment)
    comments = get_comments()
    return render_template('index.html', comments=comments)
