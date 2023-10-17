from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from psycopg2 import IntegrityError
from schemas import AppointmentsSchema
from . import bp 
from .AppointmentsModel import AppointmentModel
from resources.doctors.DoctorModel import DoctorModel
from resources.patients.PatientModel import PatientModel

@bp.route('/appointments')
class AppointmentList(MethodView):

    @jwt_required()
    @bp.response(200, AppointmentsSchema(many=True))
    def get(self):
        current_user = get_jwt_identity()
        if current_user in DoctorModel.id:
            user_appointments = AppointmentModel.query.filter_by(doctor_id=current_user).all()
            return user_appointments
        elif current_user in PatientModel.id:
            user_appointments = AppointmentModel.query.filter_by(patient_id=current_user).all()
            return user_appointments
        else:
            abort(400, message='No account found')

    @jwt_required()
    @bp.arguments(AppointmentsSchema)
    @bp.response(201, AppointmentsSchema)
    def post(self, appointment_data):
        patient_id = get_jwt_identity()
        a = AppointmentModel(**appointment_data, patient_id = patient_id)
        try:
            a.save()
            return a
        except IntegrityError:
            abort(400,message="Invalid User Id")


@bp.route('/appointments/<appointment_id>')
class Apointment(MethodView):

    @jwt_required()
    @bp.arguments(AppointmentsSchema)
    @bp.response(200, AppointmentsSchema)
    def put(self, appointment_data, appointment_id):
        a = AppointmentModel.query.get(appointment_id)
        if a and appointment_data['body']:
            patient_id = get_jwt_identity()
            if a.patient_id == patient_id:
                a.body = appointment_data['body']
                a.save()
                return a
            else:
                abort(401, message="Unauthorized")
        abort(400, message="Invalid Appointment Data")

    @jwt_required()
    def delete(self, appointment_id):
        patient_id = get_jwt_identity()
        a = AppointmentModel.query.get(appointment_id)
        if a:
            if a.patient_id == patient_id:
                a.delete()
                return {'message': 'Appointment Canceled'}, 202
            abort(401, message="User doesn't have right to remove")
        abort(400, message="Invalid Appointment Id")