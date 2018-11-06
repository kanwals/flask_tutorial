from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/gk')
def gk():
    name = "aman"

    return render_template('test.html', name=name)


if __name__ == '__main__':
    app.run()
