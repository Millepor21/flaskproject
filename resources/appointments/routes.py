from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from schemas import AppointmentsSchema
from . import bp 
from .AppointmentsModel import AppointmentModel
from resources.doctors.DoctorModel import DoctorModel
from resources.patients.PatientModel import PatientModel

@bp.route('/Appointments')
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

    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass