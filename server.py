from flask import Flask,render_template

server = Flask(__name__)

@server.route('/')
def root():
    return render_template('root.html')