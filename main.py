from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    return f'Hola <username>{escape(username)}</username>'