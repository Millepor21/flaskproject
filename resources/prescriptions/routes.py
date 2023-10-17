from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas import PrescriptionsSchema
from . import bp 
from .PrescriptionModel import PrescriptionModel
from ..doctors.DoctorModel import DoctorModel
from ..patients.PatientModel import PatientModel

@bp.route('/prescriptions')
class PrescriptionList(MethodView):

    @jwt_required()
    @bp.response(200, PrescriptionsSchema)
    def get(self):
        current_user = get_jwt_identity()
        if current_user in DoctorModel.id:
            given_prescriptions = PrescriptionModel.query.filter_by(doctor_id = current_user).all()
            return given_prescriptions
        elif current_user in PatientModel.id:
            your_prescriptions = PrescriptionModel.query.filter_by(patient_id = current_user)
            return your_prescriptions

    @jwt_required()
    @bp.arguments(PrescriptionsSchema)
    @bp.response(201, PrescriptionsSchema)
    def post(self, prescription_data):
        current_user = get_jwt_identity()
        if current_user in DoctorModel.id:
            p = PrescriptionModel(**prescription_data, doctor_id = current_user)
            p.save()
            return p
        abort(401, message="User Cannot Make Prescription")
        

@bp.route('/prescriptions/<prescription_id>')
class Prescription(MethodView):

    @jwt_required()
    @bp.arguments(PrescriptionsSchema)
    @bp.response(200, PrescriptionsSchema)
    def put(self, prescription_data, prescription_id):
        p = PrescriptionModel.query.get(prescription_id)
        if p and prescription_data['body']:
            current_user = get_jwt_identity()
            if p.doctor_id == current_user:
                p.body = prescription_data['body']
                p.save()
                return p
            else:
                abort(401, message="Unauthorized")
        abort(400, message="Invalid Prescription Data")

    @jwt_required()
    def delete(self, prescription_id):
        current_user = get_jwt_identity()
        p = PrescriptionModel.query.get(prescription_id)
        if p:
            if p.doctor_id == current_user:
                p.delete()
                return {"message":"Prescription No Longer Prescribed"}
            abort(401, message="User doesn't have the right to remove")
        abort(400, message="Invalid Prescription Id")