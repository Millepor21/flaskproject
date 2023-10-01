from app import db 

class PrescriptionModel(db.Model):
    
    __tablename__ = 'prescriptions'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    medication = db.Column(db.String, nullable=False)
    dosage = db.Column(db.String, nullable=False)
    num_refil = db.Column(db.String, nullable=False)
    directions = db.Column(db.String, nullable=False)
    price = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Medication: {PrescriptionModel.medication}>\n<Dosage: {PrescriptionModel.dosage}>\n<Directions: {PrescriptionModel.directions}>\n<Number of Refills: {PrescriptionModel.num_refil}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()