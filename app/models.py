import bson
from flask.ext.login import UserMixin
from . import db, lm


@lm.user_loader
def load_user(uid):
    return User.query(bson.objectid.ObjectId(str(uid)))


class User(UserMixin, db.Document):
    username = db.StringField(required=True, max_length=15)
    email = db.StringField(max_length=40)
    password = db.StringField(max_length=15)
    avatar = db.FileField()
    html_url = db.StringField(max_length=100)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        # False as we do not support annonymity
        return False

    @staticmethod
    def query(uid):
        result = User.objects(id=uid)
        if len(result) != 0:
            value = result[0]
            return value
        else:
            return None

    def verify_password(self, pswd):
        if self.password == pswd:
            return True
        return False


class Profile(db.Document):
    user = db.ReferenceField(User)
    location = db.StringField(max_length=100)
    job = db.StringField(max_length=30)
    position = db.StringField(max_length=30)
    filed = db.StringField(max_length=20)
