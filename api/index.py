from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('static/index.html')

@app.route('/about')
def about():
    return 'About'
