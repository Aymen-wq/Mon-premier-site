from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Bienvenue</h1>
    <p>Site de test Python</p>
    """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Bienvenue</h1>
    <p>Site de test Python</p>
    """

app.run(debug=True)