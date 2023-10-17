from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas import PatientsSchema
from . import bp 
from .PatientModel import PatientModel
from ..doctors.DoctorModel import DoctorModel

@bp.route('/patients')
class PatientList(MethodView):

    @jwt_required()
    @bp.response(200, PatientsSchema(many=True))
    def get(self):
        user = get_jwt_identity()
        if user in DoctorModel.id:
            patient_profiles = PatientModel.query.filter_by(doctor_id = user).all()
            return patient_profiles
        elif user in PatientModel.id:
            patient_profile = PatientModel.query.filter_by(patient_id = user).all()
            return patient_profile

    @jwt_required()
    @bp.arguments(PatientsSchema)
    @bp.response(201, PatientsSchema)
    def post(self, patient_data):
        user = get_jwt_identity()
        p = PatientModel(**patient_data)
        p.save()
        return p

@bp.route('/patients/<patient_id>')
class Patient(MethodView):

    @jwt_required()
    @bp.arguments(PatientsSchema)
    @bp.response(200, PatientsSchema)
    def put(self, patient_data, patient_id):
        p = PatientModel.query.get(patient_id)
        if p and patient_data['body']:
            user = get_jwt_identity()
            if p.id == user:
                p.body = patient_data['body']
                p.save()
                return p
            elif user in DoctorModel.id:
                p.body.height = patient_data['height']
                p.body.weight = patient_data['weight']
                p.body.history = patient_data['history']
                p.save()
                return p
            else:
                abort(401, message="Unauthorized")
        abort(400, message="Invalid Patient Data")  

    @jwt_required()
    def delete(self, patient_id):
        user_id = get_jwt_identity()
        p = PatientModel.query.get(patient_id)
        if p:
            if p.id == user_id:
                p.delete()
                return {"message":"Patient Deleted"}
            abort(401, message="User doesn't have right to remove")
        abort(400, message="Invalid Patient Id")