from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token

from schemas import AuthDoctorsSchema, DoctorsSchema
from . import bp 
from .DoctorModel import DoctorModel

@bp.post('/register/doctor')
@bp.arguments(DoctorsSchema)
@bp.response(201, DoctorsSchema)
def register(doctor_data):
    doctor = DoctorModel()
    doctor.from_dict(doctor_data)
    try:
        doctor.save()
        return doctor_data
    except IntegrityError:
        abort(400, message="Username or email already in use")

@bp.post('/login/doctor')
@bp.arguments(AuthDoctorsSchema)
def login(login_info):
    doctor = DoctorModel.query.filter_by(email=login_info['email']).first()
    if doctor and doctor.check_password(login_info['password']):
        access_token = create_access_token()
        return {'access_token':access_token}
    abort(400, message="Invalid Email or Password")