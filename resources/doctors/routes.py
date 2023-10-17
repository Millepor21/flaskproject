from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas import DoctorsSchema
from . import bp 
from .DoctorModel import DoctorModel

@bp.route('/doctors')
class DoctorList(MethodView):

    @jwt_required()
    @bp.response(200, DoctorsSchema(many=True))
    def get(self):
        return DoctorModel.query.all()

    @jwt_required()
    @bp.arguments(DoctorsSchema)
    @bp.response(201, DoctorsSchema)
    def post(self, doctor_data):
        doctor_id = get_jwt_identity()
        d = DoctorModel(**doctor_data)
        d.save()
        return d

@bp.route('/doctors/<doctor_id>')
class Doctor(MethodView):

    @jwt_required()
    @bp.arguments(DoctorsSchema)
    @bp.response(200, DoctorsSchema)
    def put(self, doctor_data, doctor_id):
        d = DoctorModel.query.get(doctor_id)
        if d and doctor_data['body']:
            editor_id = get_jwt_identity()
            if editor_id in DoctorModel.id:
                d.body = doctor_data['body']
                d.save()
                return d
            else:
                abort(401, message="Unauthorized")
        abort(400, message="Invalid Post Data")

    @jwt_required()
    def delete(self, doctor_id):
        deleter_id = get_jwt_identity()
        d = DoctorModel.query.get(doctor_id)
        if d:
            if deleter_id in DoctorModel.id:
                d.save()
                return {'message':"Doctor Profile Removed"}
            abort(401, message="User doesn't have right to remove")
        abort(400, message="Invalid Doctor Id")