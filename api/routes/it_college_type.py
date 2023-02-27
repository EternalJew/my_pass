from api import db, ma, jsonify, Blueprint
from flask_restful import abort, request
from api.models.it_college_type import IT_College_Type

main = Blueprint('it_college_type_blueprint', __name__)


class ItCollegeTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


it_college_type_schema = ItCollegeTypeSchema()
it_college_type_schema = ItCollegeTypeSchema(many=True)


@main.route('/get_all', methods=['GET'])
def get_members_types():
    all_types = IT_College_Type.query.all()
    result = it_college_type_schema.dump(all_types)

    if not result:
        abort(404, message="user types exist!!")

    return jsonify(result)


@main.route('/<id>', methods=['GET'])
def get_member_type(id):
    member = IT_College_Type.query.get(id)

    if not member:
        abort(404, message="user type with that 'id' exist!!")

    return jsonify(member)

@main.route('/add', methods=['POST'])
def add_member_type():
    name = request.json['name']

    new_user_type = IT_College_Type(name)

    db.session.add(new_user_type)
    db.session.commit()

    return it_college_type_schema.jsonify(new_user_type)

@main.route('/update/<id>', methods=['PUT'])
def update_member_type(id):
    member = IT_College_Type.query.get(id)
    name = request.json['name']

    member.name = name

    db.session.commit()

    return it_college_type_schema.jsonify(member)


@main.route('/delete/<id>', methods=['DELETE'])
def delete_member_type(id):
    member = IT_College_Type.query.get(id)
    db.session.delete(member)
    db.session.commit()
    return it_college_type_schema.jsonify(member)