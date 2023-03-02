"""


"""

from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__, template_folder='templates')


@app.route("/index")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
