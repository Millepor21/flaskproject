from marshmallow import Schema, fields

class AppointmentsSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    doctor_id = fields.Str(required=True)
    patient_id = fields.Str(required=True)
    reason_for_appointment = fields.Str(required=True)
    time = fields.Str(required=True)
    date = fields.Str(required=True)
    address = fields.Str(required=True)

class DoctorsSchema(Schema):
    id = fields.Int(dump_only=True)
    last_name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    specialty  = fields.Str(required=True)

class PatientsSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    dob = fields.Str(required=True)
    height = fields.Str()
    weight = fields.Str()
    history = fields.Str()

class PrescriptionsSchema(Schema):
    id = fields.Int(dump_only=True)
    patient_id = fields.Str(required=True)
    doctor_id = fields.Str(required=True)
    medication = fields.Str(required=True)
    dosage = fields.Str(required=True)
    num_refil = fields.Str(required=True)
    directions = fields.Str(required=True)
    price = fields.Str(required=True)