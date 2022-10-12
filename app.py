from flask import render_template
from flask import request
from flask import Flask
from flask import redirect, make_response, jsonify
import json
import os
app = Flask(__name__)
# login
config = {}

# outlook


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == "POST":
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    # config
    with open("config.json") as f:
        config = json.load(f)
    # runcode
    app.run(host="0.0.0.0", port=config["port"], debug=True)
