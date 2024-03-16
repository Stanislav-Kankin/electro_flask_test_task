from flask import Flask, render_template, request, redirect, url_for

from models import db, User

app = Flask(__name__)
db_uri = 'sqlite:///c:\\dev\\test_task\\electro_flask_test_task\\users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db.init_app(app)


@app.route('/register', methods=['GET', 'POST'])
def register() -> str:
    """Регистрируем нового пользователя"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register_form.html')


@app.route('/login', methods=['GET', 'POST'])
def login() -> str:
    """Аутентификация пользователя"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                return render_template('welcome.html', username=username)
            else:
                return 'Неправильное имя пользователя или пароль'
    return render_template('login_form.html')


@app.route('/users')
def users() -> str:
    """Выводим список всех пользователей"""
    all_users = User.query.all()
    return render_template('users.html', users=all_users)


@app.route('/users/create', methods=['GET', 'POST'])
def create_user() -> str:
    """Создаем нового пользователя"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('users'))
    return render_template('create_user.html')


@app.route('/users/<int:user_id>/update', methods=['GET', 'POST'])
def update_user(user_id: int) -> str:
    """Обновление данных пользователя имя/пароль"""
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user.username = username
            user.set_password(password)
            db.session.commit()
            return redirect(url_for('users'))
    return render_template('update_user.html', user=user)


@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id: int) -> str:
    """Удаление пользователя с БД"""
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
