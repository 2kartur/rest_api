from app import db
import enum
from datetime import datetime

class MyEnum(enum.Enum):
    acquaintance = 1
    good_acquaintance = 2
    friend = 3


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    birthday = db.Column(db.Date)
    state = db.Column(db.Enum(MyEnum), default='acquaintance')
    hobby = db.Column(db.String(80), nullable=False)


    def __repr__(self):
        return f'<Task {self.id} {self.name} {self.teacher} {self.type} {self.is_exam} {self.specialty} {self.semester}>'