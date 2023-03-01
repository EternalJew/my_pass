from wtforms import Form, StringField, SubmitField, validators
from api.models.it_college import IT_College_members
from api.models.it_college_type import IT_College_Type


class RegForm(Form):
    first_name = StringField("First Name", validators=[
        validators.DataRequired(),
        validators.Length(min=4, message="First Name must be at least 6 characters long.")
    ])
    last_name = StringField("Last Name", validators=[
        validators.DataRequired(),
        validators.Length(min=4, message="Last Name must be at least 6 characters long.")
    ])
    email = StringField("E-Mail", validators=[
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, message="Email Address must be at least 6 characters long.")
    ])
    name = StringField("Type", validators=[
        validators.DataRequired(),
        validators.Length(min=4, message="Type must be at least 4 characters long.")
    ])
    submit = SubmitField("Sign Up")

    # def validate_username(self, username):
    #     present = User.query.filter_by(username=username.data).first()
    #     if present:
    #         raise validators.ValidationError("This username has already been taken, please choose a different one.")

    def validate_email(self, email):
        present = IT_College_members.query.filter_by(email=email.data).first()
        if present:
            raise validators.ValidationError(
                "This email has already been registered with us, please enter a different one.")

    def validate_type(self, name):
        present = IT_College_Type.query.filter_by(name=name.data).first()
        if not present:
            raise validators.ValidationError(
                "This type exist. Choose again.")



