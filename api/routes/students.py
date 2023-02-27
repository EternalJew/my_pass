from api import db, ma, jsonify, Blueprint
from flask_restful import abort, request
from api.models.students import Students

main = Blueprint('student_blueprint', __name__)

class StudentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'student_unique_code', 'registered')


student_schema = StudentSchema()
student_schema = StudentSchema(many=True)


@main.route('/students/get_all', methods=['GET'])
def get_students():
    all_students = Students.query.all()
    result = student_schema.dump(all_students)

    if not result:
        abort(404, message="student exist!!")

    return jsonify(result)


@main.route('/student/get/<id>', methods=['GET'])
def get_student(id):
    result = Students.query.get(id)

    if not result:
        abort(404, message="student with that 'id' exist!!")

    return jsonify(result)


@main.route('/student/add', methods=['POST'])
def add_student():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    student_unique_code = request.json['student']
    email = request.json['email']

    new_client = Students(first_name, last_name, email, student_unique_code)

    db.session.add(new_client)
    db.session.commit()

    return student_schema.jsonify(new_client)


@main.route('/student/update/<id>', methods=['PUT'])
def update_student(id):
    result = Students.query.get(id)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    student_unique_code = request.json['student']
    email = request.json['email']

    result.first_name = first_name
    result.last_name = last_name
    result.email = email
    result.student_unique_code = student_unique_code

    db.session.commit()

    return student_schema.jsonify(result)


@main.route('/student/delete/<id>', methods=['DELETE'])
def delete_student(id):
    result = Students.query.get(id)
    db.session.delete(result)
    db.session.commit()
    return(result)