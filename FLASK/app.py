from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)
app.secret_key = "]xf7x9fxabxcfx87{xadjxd3exea4RYA"


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)