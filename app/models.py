
from flask.ext.login import UserMixin
from . import db, lm


@lm.user_loader
def load_user(username):
    return User.query(username)


class User(UserMixin, db.Document):
    username = db.StringField(required=True, max_length=15)
    email = db.StringField(max_length=40)
    password = db.StringField(max_length=15)
    # avatar_url = db.FileFiled(max_length=100)
    html_url = db.StringField(max_length=100)

    @property
    def is_active(self):
        return True

    @property
    def get_id(self):
        return self.uniqueID

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        # False as we do not support annonymity
        return False

    @classmethod
    def uniqueID(cls):
        return unicode(cls.id)

    @staticmethod
    def query(username):
        result = User.objects(username=username)
        if len(result) != 0:
            value = result[0].id
            return value
        else:
            return None

    def verify_password(self, pswd):
        if self.password == pswd:
            return True
        return False


class Profile(db.Document):
    username = db.ReferenceField(User)
    location = db.StringField(max_length=100)
    job = db.StringField(max_length=30)
    position = db.StringField(max_length=30)
    filed = db.StringField(max_length=20)
