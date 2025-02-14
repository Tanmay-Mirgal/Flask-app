from flask_wtf import FlaskForm
from wtforms import (StringField,SelectField,DateField)
from wtforms.validators import (
    DataRequired,
    length,
    Email,
    Optional
)

class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(),length(2,30)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(),Email()]
    )
    gender = SelectField(
        "Gender",
        choices=["Males","Females","Others"],
        validators=[Optional()]
    )
    dob = DateField(
        "Date of birth",
        validators=[Optional]
    )

class LoginForm(FlaskForm):
    pass
