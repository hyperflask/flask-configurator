from flask import Flask, jsonify
from flask_configurator import FlaskConfigurator


app = Flask(__name__)
config = FlaskConfigurator(app)


@app.route("/")
def index():
    return jsonify(config)
