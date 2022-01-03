from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from nav import nav
from forms import *
from flask_wtf.csrf import CSRFProtect

import pyodbc

SERVER_NAME = 'LAPTOP-JVD1T1M5'

connection = pyodbc.connect(driver='{SQL Server}', server=SERVER_NAME, database='WHOLESALE_CLOTHING_VENDOR_DATABASE_SYSTEM',               
               trusted_connection='yes')


app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)
app.secret_key = 'DFASUYUH2341'
csrf = CSRFProtect(app)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee/read_employees')
def read_employees():
    cursor = connection.cursor()
    cursor.execute('Select * From EMPLOYEE')
    employee_info = cursor.fetchall()

    return render_template('read_employees.html', employee_info=employee_info)

@app.route('/employee/top_five_employees')
def top_five_employees():
    cursor = connection.cursor()
    cursor.execute('select * from TopFiveEarnerEmployee')
    top_five_earners = cursor.fetchall()

    return render_template('top_five_earner_employees.html', top_five_earners=top_five_earners)

@app.route('/employee/department_of_employees')
def department_of_employees():
    cursor = connection.cursor()
    cursor.execute('select * from DepartmentsOfEmployees')
    employee_info = cursor.fetchall()

    return render_template('department_of_employees.html', employee_info=employee_info)


@app.route('/employee/create_employee', methods=['GET', 'POST'])
def create_employee():
    form = CreateEmployeeForm()
    if request.method == 'GET':
        return render_template('create_employee.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_create_employee(form)
            return redirect('/employee/create_employee')
        return 'invalid form'

def execute_sp_create_employee(form):
    birthdateindex = 3
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop() # csrf token is not used
    arguments[birthdateindex] += " 00:00:00" # hour info is required

    string_arg = str(arguments)[1:-1]
    print((f'exec sp_CreateEmployee {string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_CreateEmployee{string_arg}')
    cursor.commit()

@app.route('/department/read_department')
def read_department():
    cursor = connection.cursor()
    cursor.execute('select * from DEPARTMENT')
    department_info = cursor.fetchall()
    return render_template('read_department.html', department_info=department_info)


def print_form(form):
    for item in list(form):
        print(item)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
