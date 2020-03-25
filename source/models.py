from source import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from source import login
from hashlib import md5


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/' \
               '{}?d=identicon&s={}'.format(digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

    # @classmethod
    # def create(cls, session, **kwargs):
    #     """
    #     Метод добавления попытки авторизации
    #     :param session: сессия базы данных
    #     :param kwargs: словарь атрибутовы класса User
    #     :return: True||False, описание
    #     """
    #     user = User(**kwargs)
    #     session.add(user)
    #     try:
    #         session.commit()
    #     except:
    #         session.rollback()
    #         return False, 'Ошибка добавления пользователя'
    #     return True, 'Пользователь успешно добавлен', user.id
    #
    # @classmethod
    # def read(cls, session):
    #     """
    #     Метод чтения всех записей пользователей
    #     :param session: сессия базы данных
    #     :return: словарь {id: [last_name, first_name, patronymic, post_id, access_id, creation_time, updating_time,
    #      images_path]}
    #     """
    #     return {i.id: [i.last_name, i.first_name, i.patronymic, i.post_id, i.access_id, i.creation_time,
    #                    i.updating_time, i.images_path] for i in session.query(User).all()}
    #
    # @classmethod
    # def read_id(cls, session, id):
    #     """
    #     Метод чтения записи пользователя
    #     :param session: сессия базы данных
    #     :return: объект записи выбранного пользователя
    #     """
    #     return session.query(User).filter(User.id == id).first()
    #
    # @classmethod
    # def read_faces(cls, session):
    #     """
    #     Метод чтения всех путей до изображений лиц пользователей
    #     :param session:
    #     :return: словарь {id: images_path}
    #     """
    #     return {i.id: i.images_path for i in session.query(User).all()}
    #
    # @classmethod
    # def update(cls, session, id, **kwargs):
    #     """
    #      Метод обновления выбранной записи пользователя
    #     :param session: сессия базы данных
    #     :return kwargs: словарь, который может включать в себя следуюище пары "ключ: значение":
    #     {'last_name': , 'first_name': '', 'patronymic': '', 'post_id': n, 'access_id': n,
    #     'creation_time': datetime.now(), 'updating_time': datetime.now(),'images_path': ''}
    #     :return: True||False, описание
    #     """
    #     try:
    #         user = session.query(User).get(id)
    #         for key, value in kwargs.items():
    #             setattr(user, key, value)
    #     except:
    #         return False, 'Ошибка обновления информации пользователя'
    #     return True, 'Информация пользователя успешно обновлена'
    #
    # @classmethod
    # def delete(cls, session, id):
    #     """
    #     Метод удаления пользователя
    #     :param session: сессия базы данных
    #     :param id: идентификатор пользователя
    #     :return: True||False, описание
    #     """
    #     try:
    #         session.query(User).filter(User.id == id).delete()
    #     except IntegrityError:
    #         return False, 'Ошибка удаления пользователя'
    #     return True, 'Пользователь успешно удален'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

