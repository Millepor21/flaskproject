from app import db 

class PatientModel(db.Model):
    id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    dob = db.Column(db.String, nullable=False)
    height = db.Column(db.String, nullable=False)
    weight = db.Column(db.String, nullable=False)
    history = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Name: {PatientModel.first_name + " " + PatientModel.last_name}>\n<DOB: {PatientModel.dob}>\n<History: {PatientModel.history}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()