from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import oauth, oauthLogin, userView
