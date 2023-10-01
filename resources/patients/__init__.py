from flask_smorest import Blueprint

bp = Blueprint('patients',__name__)

from . import routes