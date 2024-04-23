from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route('/run_script')
def run_script():
    subprocess.call(['python', 'your_script.py'])
    return render_template("index.html", title="Hello")
