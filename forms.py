from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.fields.datetime import *
from wtforms.fields.simple import *
from wtforms.validators import *

class CreateEmployeeForm(FlaskForm):
    Ssn = IntegerField('Ssn', validators=[DataRequired()])
    FirstName = StringField('FirstName', validators=[DataRequired()])
    LastName = StringField('LastName', validators=[DataRequired()])
    BirthDate = DateField('BirthDate', validators=[DataRequired()])
    Dno = IntegerField('Dno', validators=[DataRequired()])
    Gender = StringField('Gender', validators=[Length(min=1, max=1, message='Gender can be either M or F'), DataRequired()])
    Country = StringField('Country', validators=[DataRequired()])
    City = StringField('City', validators=[DataRequired()])
    PostalCode = StringField('PostalCode', validators=[Length(min=5, max=5), DataRequired()])
    Salary = IntegerField('Salary', validators=[DataRequired()])