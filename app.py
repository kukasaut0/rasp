from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
<<<<<<< HEAD
    return "Hello World!"
=======
    return "Hello World?"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)
>>>>>>> parent of 13fe88f... going dash

if __name__ == '__main__':
    app.run()
