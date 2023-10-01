from flask_smorest import Blueprint

bp = Blueprint('doctors',__name__)

from . import routes