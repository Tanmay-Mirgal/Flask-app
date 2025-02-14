from flask import Flask,render_template,url_for,redirect
import time 

app = Flask(__name__)

@app.route('/' )
@app.route('/home')
def home():
    return render_template("home2.html",title="Home")

@app.route('/signup')
def signup():
    return render_template('signup.html',title="Sign up")

@app.route('/login')
def login():
    return render_template('login.html',title="login")

if __name__ == "__main__":
    app.run(debug=True)