from api import db, ma, jsonify, Blueprint, app
from api.models.it_college import IT_College_members
from api.models.it_college_type import IT_College_Type
from api.utils.get_id_from_db_object_for_relation import get_id, get_name_from_type
from api.utils.generate_client_code import generate_code
from flask import flash, request, render_template
from api.auth.forms import RegForm


main = Blueprint('it_college_blueprint', __name__)


class ItCollegeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'unique_code', 'type_id', 'registered')


it_college_schema = ItCollegeSchema()
it_college_schema = ItCollegeSchema(many=True)


@main.route('/get_all', methods=['GET'])
def get_members():
    members = IT_College_members.query.all()

    output = []

    for member in members:
        member_data = {}

        member_data['id'] = member.id
        member_data['first_name'] = member.first_name
        member_data['last_name'] = member.last_name
        member_data['email'] = member.email
        member_data['unique_code'] = member.unique_code
        member_data['type_name'] = get_name_from_type(IT_College_Type, member.type_id)

        output.append(member_data)

    return jsonify({'college members': output})


@main.route('/get/<id>', methods=['GET'])
def get_member(id):
    member = IT_College_members.query.get(id)
    if not member:
        return {"message": "client with that id not found"}, 404

    output = []

    member_data = {}

    member_data['id'] = member.id
    member_data['first_name'] = member.first_name
    member_data['last_name'] = member.last_name
    member_data['email'] = member.email
    member_data['unique_code'] = member.unique_code
    member_data['type_name'] = get_name_from_type(IT_College_Type, member.type_id)

    output.append(member_data)

    return jsonify({'college members': output})



@main.route('/signup', methods=['GET', 'POST'])
def add_member():
    form = RegForm(request.form)
    if request.method == "POST" and form.validate():
        new_college_member = IT_College_members(first_name=form.first_name.data,
                                                last_name=form.last_name.data,
                                                email=form.email.data,
                                                unique_code=generate_code(),
                                                type_id=get_id(IT_College_Type, form.name.data))
        db.session.add(new_college_member)
        db.session.commit()
        flash("Account created for %s!" % (form.first_name.data), "success")
    return it_college_schema.jsonify(new_college_member)


@main.route('/update/<id>', methods=['PUT'])
def update_member(id):
    college_member = IT_College_members.query.get(id)
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    unique_code = request.json['student']
    email = request.json['email']
    type = request.json['type']
    type_id = get_id(IT_College_Type, type)

    college_member.first_name = first_name
    college_member.last_name = last_name
    college_member.email = email
    college_member.unique_code = unique_code
    college_member.type_id = type_id

    db.session.commit()

    return it_college_schema.jsonify(college_member)


@main.route('/delete/<id>', methods=['DELETE'])
def delete_member(id):
    college_member = IT_College_members.query.get(id)
    db.session.delete(college_member)
    db.session.commit()
    return(college_member)


import pandas
from fileinput import filename
# Root endpoint
@app.get('/upload_excel')
def upload():
    return render_template('upload-excel.html')


@app.post('/upload_clients')
def upload_clients_from_excel(): #EXCEL PARSER
    if request.method == 'POST':
        # Read the File using Flask request
        file = request.files['file']
        # Save file in local directory
        file.save(file.filename)

        # Parse the data as a Pandas DataFrame type
        data = pandas.read_excel(file)

        # Iterate over the rows in the DataFrame and insert them into the database
        for row in data.itertuples(index=False):
            new_member = IT_College_members(
                first_name=row.first_name,
                last_name=row.last_name,
                email=row.email,
                unique_code=generate_code(),
                type_id=get_id(IT_College_Type, row.type),
            )

            db.session.add(new_member)

        # Commit the changes to the database
        db.session.commit()

        # Return HTML snippet that will render the table
        return data.to_html()
