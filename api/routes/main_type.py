from api import db, ma, jsonify, Blueprint
from flask_restful import abort, request
from api.models.main_type import Main_Type

main = Blueprint('main_type_blueprint', __name__)


class MainTypeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


main_type_schema = MainTypeSchema()
main_type_schema = MainTypeSchema(many=True)


@main.route('/get_all', methods=['GET'])
def get_members_types():
    all_types = Main_Type.query.all()
    result = main_type_schema.dump(all_types)

    if not result:
        abort(404, message="main types exist!!")

    return jsonify(result)


@main.route('/<id>', methods=['GET'])
def get_member_type(id):
    member = Main_Type.query.get(id)

    if not member:
        abort(404, message="main type with that 'id' exist!!")

    return jsonify(member)

@main.route('/add', methods=['POST'])
def add_member_type():
    name = request.json['name']

    new_user_type = Main_Type(name)

    db.session.add(new_user_type)
    db.session.commit()

    return main_type_schema.jsonify(new_user_type)

@main.route('/update/<id>', methods=['PUT'])
def update_member_type(id):
    member = Main_Type.query.get(id)
    name = request.json['name']

    member.name = name

    db.session.commit()

    return main_type_schema.jsonify(member)


@main.route('/delete/<id>', methods=['DELETE'])
def delete_member_type(id):
    member = Main_Type.query.get(id)
    db.session.delete(member)
    db.session.commit()
    return main_type_schema.jsonify(member)