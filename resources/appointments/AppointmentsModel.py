from app import db 

class AppointmentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, db.ForeignKey('patients.username'), nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    reason_for_appointment = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)

    def __repr__(self):
        return f'<Username: {AppointmentModel.username}>\n<Date: {AppointmentModel.time}>\n<Address: {AppointmentModel.address}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()