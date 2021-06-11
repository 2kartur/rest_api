from .models import Person
from app import db
from flask_restful import Resource, Api, fields, marshal_with, reqparse
from app.api import api_bp
from flask import jsonify, request, make_response
import datetime


api = Api(api_bp)
resource_fields = {
    'id' : fields.Integer,
    'first_name' : fields.String,
    'last_name': fields.String,
    'phone_number' : fields.String,
    'sex' : fields.Boolean,
    'birthday' : db.Column(db.Date),
    'state' : fields.String,
    'hobby' : fields.Integer,
}

person_create = reqparse.RequestParser()
person_create.add_argument('first_name', type=str, help='First name is required!', required=True)
person_create.add_argument('last_name', type=str, help='Last name is required!', required=True)
person_create.add_argument('phone_number', type=str, help='Phone number is required!', required=True)
person_create.add_argument('sex', type=str, help='Sex is required!', required=True)
person_create.add_argument('birthday', type=str, help='Birthday is required!', required=True)
person_create.add_argument('hobby', type=str, help='Hobby is required!', required=True)

person_update = reqparse.RequestParser()
person_update.add_argument('first_name', type=str, help='First name is required!', required=True)
person_update.add_argument('last_name', type=str, help='Last name is required!', required=True)
person_update.add_argument('phone_number', type=str, help='Phone number is required!', required=True)
person_update.add_argument('sex', type=str, help='Sex is required!', required=True)
person_update.add_argument('birthday', type=str, help='Birthday is required!', required=True)
person_update.add_argument('state', type=str, help='State is required!', required=True)
person_update.add_argument('hobby', type=str, help='Hobby is required!', required=True)



class TaskItem(Resource):

    def post(self):
        args = person_create.parse_args()
        try:
            person = Person(first_name=args['first_name'], last_name=args['last_name'], phone_number=args['phone_number'], sex=args['sex'], birthday=args['birthday'], hobby=args['hobby'])
            db.session.add(person)
            db.session.commit()
            return make_response(jsonify({'message': 'Data add in db!'}))
        except:
            db.session.rollback()
            return make_response(jsonify({'message': 'Error when adding data!'}), 201)



    @marshal_with(resource_fields, envelope='resource')
    def get(self, id=None):
        if id is None:
            tasks_all = Person.query.all()
            return tasks_all
        else:
            task = Person.query.filter_by(id=id).first()
            if not task:
                return make_response(jsonify({'message': 'Person not found!'}))
            return task


    def delete(self, id):
        task = Person.query.filter_by(id=id).first()
        if not task:
            return make_response(jsonify({'message': 'Person not found!'}), 404)
        db.session.delete(task)
        db.session.commit()
        return  make_response(jsonify({'message': 'The person has been deleted'}))


    def put(self, id):
        subject = Person.query.filter_by(id=id).first()
        if not subject:
            return make_response(jsonify({'message': 'Subject not found!'}), 404)
        args = person_update.parse_args()

        subject.first_name = args['first_name']
        subject.last_name = args['last_name']
        subject.phone_number = args['phone_number']
        subject.sex = args['sex']
        subject.birthday = args['birthday']
        subject.state = args['state']
        subject.hobby = args['hobby']
        try:
            db.session.commit()
            return make_response(jsonify({"message": "Person succesfully update!"}))
        except:
            db.session.rollback()
            return make_response(jsonify({'message': 'Error when updating data!'}), 201)




api.add_resource(TaskItem, '/person', '/person/<int:id>')