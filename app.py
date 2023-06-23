from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Display():  # put application's code here
    return render_template('showData.html')


if __name__ == '__main__':
    app.run()
