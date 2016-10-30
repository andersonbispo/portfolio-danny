from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projeto_um')
def project_one():
    return render_template('project_one.html')
