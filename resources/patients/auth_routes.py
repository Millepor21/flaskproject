from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token

from schemas import PatientsSchema, AuthPatientsSchema
from . import bp 
from .PatientModel import PatientModel

@bp.post('/register/patient')
@bp.arguments(PatientsSchema)
@bp.response(201, PatientsSchema)
def register(patient_data):
    patient = PatientModel()
    patient.from_dict(patient_data)
    try:
        patient.save()
        return patient_data
    except IntegrityError:
        abort(400, message="Username or email already in use")

@bp.post('/login/patient')
@bp.arguments(AuthPatientsSchema)
def login(login_info):
    patient = PatientModel.query.filter_by(username=login_info['username']).first()
    if patient and patient.check_password(login_info['password']):
        access_token = create_access_token(identity=patient.id)
        return {'access_token':access_token}
    abort(400, message="Invalid Username or Password")