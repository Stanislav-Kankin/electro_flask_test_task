from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
db_uri = 'sqlite:///c:\\dev\\test_task\\electro_flask_test_task\\users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self,  password):
        return check_password_hash(self.password, password)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return 'Пользователь зарегистрирован'
    return render_template('register_form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                return f'Welcome, {username}'
            else:
                return 'Неправильное имя пользователя или пароль'
    return render_template('confirm_form.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
