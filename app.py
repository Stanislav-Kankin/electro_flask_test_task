from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL(app)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return login()
    return render_template('register_form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return f'Welcome, {username}'
        else:
            return 'ERORR BLEAD'
    return render_template('confirm_form.html')


if __name__ == '__main__':
    app.run(debug=True)
