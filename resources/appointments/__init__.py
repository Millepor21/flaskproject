from flask_smorest import Blueprint

bp = Blueprint('appointments',__name__)

from . import routes