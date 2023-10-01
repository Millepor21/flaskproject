from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas import PrescriptionsSchema
from . import bp 
from .PrescriptionModel import PrescriptionModel

@bp.route('/Prescriptions')
class PrescriptionList(MethodView):

    
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass