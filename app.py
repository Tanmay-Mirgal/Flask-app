from flask import Flask, redirect, url_for, render_template
from employees import employees_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/<int:num>')
def about(num):
    return render_template('about.html', title="about", num=num)

@app.route('/employees')
def employees():
    return render_template('employees.html', title='employees', emp=employees_data)

@app.route('/employees/manager')
def manager():
    return render_template('manager.html', title='managers', emp=employees_data)

@app.route('/discover')
def discover():
    return render_template('discover.html', title="discover")

@app.route('/user/<name>')
def user(name):
    return f'Hello {name}'

@app.route('/pass/<sname>/<int:marks>')
def user_pass(sname, marks):
    return f'<h1>{sname}, You passed with {marks} marks</h1>'

@app.route('/fail/<sname>/<int:marks>')
def user_fail(sname, marks):
    return f'<h1>{sname}, You failed with {marks} marks</h1>'

@app.route('/score/<name>/<int:score>')
def score(name, score):
    if score < 30:
        return redirect(url_for("user_fail", sname=name, marks=score))
    else:
        return redirect(url_for("user_pass", sname=name, marks=score))

if __name__ == "__main__":
    app.run(debug=True)
