from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from resources.appointments import bp as appointments_bp
api.register_blueprint(appointments_bp)
from resources.doctors import bp as doctors_bp
api.register_blueprint(doctors_bp)
from resources.patients import bp as patients_bp
api.register_blueprint(patients_bp)
from resources.prescriptions import bp as prescriptions_bp
api.register_blueprint(prescriptions_bp)

from resources.appointments import routes
from resources.doctors import routes
from resources.patients import routes
from resources.prescriptions import routes

from resources.appointments.AppointmentsModel import AppointmentModel
from resources.doctors.DoctorModel import DoctorModel
from resources.patients.PatientModel import PatientModel
from resources.prescriptions.PrescriptionModel import PrescriptionModel
