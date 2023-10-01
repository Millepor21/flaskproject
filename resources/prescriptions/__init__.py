from flask_smorest import Blueprint

bp = Blueprint('prescriptions',__name__)

from . import routes