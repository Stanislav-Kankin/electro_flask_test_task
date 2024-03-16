from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
    """Модель базы данных"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password: str) -> None:
        """Хэшируем пароль пользователя"""
        self.password = generate_password_hash(password)

    def check_password(self,  password: str) -> bool:
        """Проверка пароля пользователя"""
        return check_password_hash(self.password, password)
