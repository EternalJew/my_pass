from api import db, ma, jsonify, Blueprint
from flask_restful import abort, request
from api.models.it_college import IT_College_members
from api.models.it_college_type import IT_College_Type
from api.utils.get_id_from_db_object_for_relation import get_id

main = Blueprint('it_college_blueprint', __name__)

class ItCollegeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'unique_code', 'type_id', 'registered')


it_college_schema = ItCollegeSchema()
it_college_schema = ItCollegeSchema(many=True)


@main.route('/get_all', methods=['GET'])
def get_members():
    all_members = IT_College_members.query.all()
    result = it_college_schema.dump(all_members)

    if not result:
        abort(404, message="student exist!!")

    return jsonify(result)


@main.route('/get/<id>', methods=['GET'])
def get_member(id):
    result = IT_College_members.query.get(id)

    if not result:
        abort(404, message="student with that 'id' exist!!")

    return jsonify(result)


@main.route('/add', methods=['POST'])
def add_member():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    unique_code = request.json['student']
    type = request.json['type']
    type_id = get_id(IT_College_Type, type)

    new_member = IT_College_members(first_name, last_name, email, unique_code, type_id)

    db.session.add(new_member)
    db.session.commit()

    return it_college_schema.jsonify(new_member)


@main.route('/update/<id>', methods=['PUT'])
def update_member(id):
    member = IT_College_members.query.get(id)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    unique_code = request.json['student']
    email = request.json['email']
    type = request.json['type']
    type_id = get_id(IT_College_Type, type)

    member.first_name = first_name
    member.last_name = last_name
    member.email = email
    member.unique_code = unique_code
    member.type_id = type_id

    db.session.commit()

    return it_college_schema.jsonify(member)


@main.route('/delete/<id>', methods=['DELETE'])
def delete_member(id):
    member = IT_College_members.query.get(id)
    db.session.delete(member)
    db.session.commit()
    return(member)