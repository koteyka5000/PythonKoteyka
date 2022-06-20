from flask import Flask, render_template, request
from database import add_user, read_from_db

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        add_user(name)

        _data = read_from_db()
        return render_template('index.html', data=_data)


















name = 'Noname'
    if request.method == 'POST':
        name = request.form['name']
    return render_template('index.html', name=name)
        
