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
    Gender = StringField('Gender',
                         validators=[Length(min=1, max=1, message='Gender can be either M or F'), DataRequired()])
    Country = StringField('Country', validators=[DataRequired()])
    City = StringField('City', validators=[DataRequired()])
    PostalCode = StringField('PostalCode', validators=[Length(min=5, max=5), DataRequired()])
    Salary = IntegerField('Salary', validators=[DataRequired()])

class AverageAgeOfDeparment(FlaskForm):
    Dno = IntegerField('Dno', validators=[DataRequired()])


class CreateDepartmentForm(FlaskForm):
    Dno = IntegerField('Dno', validators=[DataRequired()])
    Name = StringField('Name', validators=[DataRequired()])


class CreateClothingForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    PTax = IntegerField('PTax', validators=[DataRequired()])
    Type = StringField('Type', validators=[DataRequired()])
    Gender = StringField('Gender',
                         validators=[Length(min=1, max=1, message='Gender can be either M or F'), DataRequired()])
    Size = StringField('Size', validators=[DataRequired()])
    Color = StringField('Color', validators=[DataRequired()])
    BPrice = IntegerField('BPrice', validators=[DataRequired()])
    SPrice = IntegerField('SPrice', validators=[DataRequired()])
    ShipmentId = IntegerField('ShipmentId', validators=[DataRequired()])


class EmptyManagerForm(FlaskForm):
    Dno = IntegerField('Dno', validators=[DataRequired()])


class DeleteEmployeeForm(FlaskForm):
    Ssn = IntegerField('Ssn', validators=[DataRequired()])


class CreateProducerForm(FlaskForm):
    TaxNumber = IntegerField('TaxNumber', validators=[DataRequired()])
    CompanyName = StringField('CompanyName', validators=[DataRequired()])
    Country = StringField('Country', validators=[DataRequired()])
    City = StringField('City', validators=[DataRequired()])
    PostalCode = StringField('PostalCode', validators=[DataRequired()])
    BankAccountNumber = StringField('BankAccountNumber', validators=[DataRequired()])


class SetManagerForm(FlaskForm):
    Dno = IntegerField('Dno', validators=[DataRequired()])
    Ssn = IntegerField('Ssn', validators=[DataRequired()])

class DeleteProducerForm(FlaskForm):
    TaxNumber = IntegerField('TaxNumber', validators=[DataRequired()])