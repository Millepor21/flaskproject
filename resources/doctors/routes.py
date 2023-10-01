from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas import DoctorsSchema
from . import bp 
from .DoctorModel import DoctorModel

@bp.route('/Doctors')
class DoctorList(MethodView):

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass