from app import db 

from werkzeug.security import generate_password_hash, check_password_hash

class AppointmentModel(db.Model):
    
    __tablename__ = 'appointments'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    reason_for_appointment = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)

    def __repr__(self):
        return f'<Username: {AppointmentModel.username}>\n<Date: {AppointmentModel.time}>\n<Address: {AppointmentModel.address}>'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def from_dict(self, dict):
        password = dict.pop('password')
        self.hash_password(password)
        for k,v in dict.items():
            setattr(self, k, v)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()