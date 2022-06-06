from flask import Flask, render_template
app = Flask(__name__)

TEMPLATES_AUTO_RELOAD = True

@app.route('/')
def home():
    return render_template('index.html')
