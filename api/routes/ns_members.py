from api import db, ma, jsonify, Blueprint
from flask_restful import abort, request
from api.models.ns_members import NS_members
from api.models.ns_members_type import NS_Members_Type
from api.utils.get_id_from_db_object_for_relation import get_id

main = Blueprint('ns_members_blueprint', __name__)

class NsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'ns_unique_code', 'type_id', 'registered')


ns_schema = NsSchema()
ns_schema = NsSchema(many=True)


@main.route('/ns_members/get_all', methods=['GET'])
def get_ns_members():
    all_members = NS_members.query.all()
    result = ns_schema.dump(all_members)

    if not result:
        abort(404, message="student exist!!")

    return jsonify(result)


@main.route('/ns_member/get/<id>', methods=['GET'])
def get_student(id):
    result = NS_members.query.get(id)

    if not result:
        abort(404, message="ns member with that 'id' exist!!")

    return jsonify(result)


@main.route('/ns_member/add', methods=['POST'])
def add_ns_member():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    email = request.json['email']
    ns_unique_code = request.json['student']
    type = request.json['type']
    type_id = get_id(NS_Members_Type, type)

    new_client = NS_members(first_name, last_name, email, ns_unique_code, type_id)

    db.session.add(new_client)
    db.session.commit()

    return ns_schema.jsonify(new_client)


@main.route('/ns_member/update/<id>', methods=['PUT'])
def update_student(id):
    member = NS_members.query.get(id)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    ns_unique_code = request.json['student']
    email = request.json['email']
    type = request.json['type']
    type_id = get_id(NS_Members_Type, type)

    member.first_name = first_name
    member.last_name = last_name
    member.email = email
    member.ns_unique_code = ns_unique_code
    member.type_id = type_id

    db.session.commit()

    return ns_schema.jsonify(member)


@main.route('/ns_member/delete/<id>', methods=['DELETE'])
def delete_student(id):
    result = NS_members.query.get(id)
    db.session.delete(result)
    db.session.commit()
    return(result)