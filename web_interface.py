from flask import Flask, render_template, request, abort
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from wtforms.form import Form
from nav import nav
from forms import *
from flask_wtf.csrf import CSRFProtect

import pyodbc

SERVER_NAME = 'LAPTOP-JVD1T1M5'

connection = pyodbc.connect(driver='{SQL Server}', server=SERVER_NAME,
                            database='WHOLESALE_CLOTHING_VENDOR_DATABASE_SYSTEM',
                            trusted_connection='yes')

app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)
app.secret_key = 'secret key'
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


@app.route('/employee/delete_employee', methods=['GET', 'POST'])
def delete_employee():
    form = DeleteEmployeeForm()
    if request.method == 'GET':
        return render_template('delete_employee.html', form=form)
    if request.method == 'POST':
        ssn = form.Ssn.raw_data[0]
        print(ssn)
        cursor = connection.cursor()
        cursor.execute(f"exec sp_DeleteEmployee {ssn}")
        cursor.commit()
        return redirect('/employee/delete_employee')


def execute_sp_create_employee(form):
    birthdateindex = 3
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()  # csrf token is not used
    arguments[birthdateindex] += " 00:00:00"  # hour info is required

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


@app.route('/clothing/read_clothing')
def read_clothing():
    cursor = connection.cursor()
    cursor.execute('select * from CLOTHING')
    clothing_info = cursor.fetchall()
    return render_template('read_clothing.html', clothing_info=clothing_info)


@app.route("/clothing/read_clothing_inventory")
def read_clothing_inventory():
    cursor = connection.cursor()
    cursor.execute('select * from ClothingInventory')
    clothing_info = cursor.fetchall()
    return render_template('read_clothing_inventory.html', clothing_info=clothing_info)


@app.route("/department/read_managers")
def read_managers():
    cursor = connection.cursor()
    cursor.execute('select * from Managers')
    manager_info = cursor.fetchall()
    return render_template('read_managers.html', manager_info=manager_info)


@app.route("/clothing/read_clothing_types")
def read_clothing_types():
    cursor = connection.cursor()
    cursor.execute('select * from ClothingTypes')
    clothing_info = cursor.fetchall()
    return render_template('read_clothing_types.html', clothing_info=clothing_info)


@app.route('/department/averageAgeOfDepartment', methods=['GET', 'POST'])
def averageAgeOfDepartment():
    form = AverageAgeOfDeparment()
    if request.method == 'GET':
        return render_template('averageAgeOfDepartment.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            table = execute_sp_averageAgeOfDepartment(form)
            return render_template('showAverageAge.html', table=table)
        return 'invalid form'


def execute_sp_averageAgeOfDepartment(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()  # csrf token is not used

    string_arg = str(arguments)[1:-1]
    print((f'exec sp_AverageAgeOfDepartment{string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_AverageAgeOfDepartment{string_arg}')
    return cursor.fetchall()


@app.route('/department/create_department', methods=['GET', 'POST'])
def create_department():
    form = CreateDepartmentForm()
    if request.method == 'GET':
        return render_template('create_department.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_create_department(form)
            return redirect('/department/create_department')
        return 'invalid form'


def execute_sp_create_department(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()  # csrf token is not used

    string_arg = str(arguments)[1:-1]
    print((f'exec sp_CreateDepartment {string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_CreateDepartment{string_arg}')
    cursor.commit()


@app.route("/clothing/read_clothing_profit")
def read_clothing_profit():
    cursor = connection.cursor()
    cursor.execute('select * from ProfitOfClothes')
    clothing_info = cursor.fetchall()
    return render_template('read_clothing_profit.html', clothing_info=clothing_info)


@app.route("/clothing/create_clothing", methods=['GET', 'POST'])
def create_clothing():
    form = CreateClothingForm()
    if request.method == 'GET':
        return render_template('create_clothing.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_create_clothing(form)
            return redirect("/clothing/create_clothing")
        return 'invalid form'


def execute_sp_create_clothing(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()
    arguments_str = str(arguments)[1:-1]

    cursor = connection.cursor()
    cursor.execute(f'exec sp_CreateClothing {arguments_str}')
    cursor.commit()


@app.route('/department/empty_manager', methods=['GET', 'POST'])
def empty_manager():
    form = EmptyManagerForm()
    if request.method == 'GET':
        return render_template('empty_manager.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_empty_manager(form)
            return redirect('/department/empty_manager')
        return 'invalid form'


def execute_sp_empty_manager(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()  # csrf token is not used

    string_arg = str(arguments)[1:-1]
    print((f'exec sp_EmptyManager {string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_EmptyManager{string_arg}')
    cursor.commit()


@app.route("/producer/read_producer")
def read_producer():
    cursor = connection.cursor()
    cursor.execute('select c.TaxNumber, c.CompanyName, c.Country, c.City, c.PostalCode, c.BankAccountNumber from PRODUCER p inner join COMPANY c on p.TaxNumber = c.TaxNumber')
    read_producer_info = cursor.fetchall()
    return render_template('read_producer.html', read_producer_info=read_producer_info)


@app.route("/shop/read_shop")
def read_shop():
    cursor = connection.cursor()
    cursor.execute('select c.TaxNumber, c.CompanyName, c.Country, c.City, c.PostalCode, c.BankAccountNumber from SHOP s inner join COMPANY c on s.TaxNumber = c.TaxNumber')
    read_shop_info = cursor.fetchall()
    return render_template('read_shop.html', read_shop_info=read_shop_info)


@app.route('/producer/create_producer', methods=['GET', 'POST'])
def create_producer():
    form = CreateProducerForm()
    if request.method == 'GET':
        return render_template('create_producer.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_create_producer(form)
            return redirect('/producer/create_producer')
        return 'invalid form'


def execute_sp_create_producer(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()  # csrf token is not used

    string_arg = str(arguments)[1:-1]
    print((f'exec sp_CreateProducer {string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_CreateProducer{string_arg}')
    cursor.commit()


@app.route('/department/set_manager', methods=['GET', 'POST'])
def set_manager():
    form = SetManagerForm()
    if request.method == 'GET':
        return render_template('set_manager.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_set_manager(form)
            return redirect('/department/set_manager')
        return 'invalid form'


def execute_sp_set_manager(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()  # csrf token is not used

    string_arg = str(arguments[::-1])[1:-1]
    print((f'exec sp_SetManager {string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_SetManager {string_arg}')
    cursor.commit()


@app.route('/shipment/read_incoming_shipments')
def read_incoming_shipments():
    cursor = connection.cursor()
    cursor.execute('select * from IncomingShipments')
    shipment_info = cursor.fetchall()
    return render_template('read_incoming_shipments.html', shipment_info=shipment_info)


@app.route('/shipment/read_outgoing_shipments')
def read_outgoing_shipments():
    cursor = connection.cursor()
    cursor.execute('select * from OutgoingShipments')
    shipment_info = cursor.fetchall()
    return render_template('read_outgoing_shipments.html', shipment_info=shipment_info)


@app.route('/shipment/read_name_of_logistics')
def read_name_of_logistics():
    cursor = connection.cursor()
    cursor.execute('select * from NameOfContractedLogistics')
    logistics_info = cursor.fetchall()
    return render_template('read_name_of_logistics.html', logistics_info=logistics_info)

@app.route('/shipment/create_incoming_shipment', methods=['GET', 'POST'])
def create_incoming_shipment():
    form = CreateIncomingShipmentForm()
    if request.method == 'GET':
        return render_template('create_incoming_shipment.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_create_incoming_shipment(form)
            return redirect('/shipment/create_incoming_shipment')
        return 'invalid form'

def execute_sp_create_incoming_shipment(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop() # csrf token is not used

    string_arg = str(arguments)[1:-1]
    cursor = connection.cursor()
    cursor.execute(f'exec sp_CreateIncomingShipment {string_arg}')
    cursor.commit()
    
@app.route('/shipment/create_outgoing_shipment', methods=['GET', 'POST'])
def create_outgoing_shipment():
    form = CreateOutgoingShipmentForm()
    if request.method == 'GET':
        return render_template('create_outgoing_shipment.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_create_outgoing_shipment(form)
            return redirect('/shipment/create_outgoing_shipment')

def execute_sp_create_outgoing_shipment(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop() # csrf token is not used

    string_arg = str(arguments)[1:-1]
    cursor = connection.cursor()
    cursor.execute(f'exec sp_CreateOutgoingShipment {string_arg}')
    cursor.commit()

################################################################################

@app.route('/producer/delete_producer', methods=['GET', 'POST'])
def delete_producer():
    form = DeleteProducerForm()
    if request.method == 'GET':
        return render_template('delete_producer.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_delete_producer(form)
            return redirect('/producer/delete_producer')
        return 'invalid form'

def execute_sp_delete_producer(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop() # csrf token is not used

    string_arg = str(arguments)[1:-1]
    print((f'exec sp_DeleteProducer {string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_DeleteProducer{string_arg}')
    cursor.commit()

##############################################################################


@app.route('/shop/create_shop', methods=['GET', 'POST'])
def create_shop():
    form = CreateShopForm()
    if request.method == 'GET':
        return render_template('create_shop.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_create_shop(form)
            return redirect('/shop/create_shop')
        return 'invalid form'


def execute_sp_create_shop(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()  # csrf token is not used

    string_arg = str(arguments)[1:-1]
    print((f'exec sp_CreateShop {string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_CreateShop{string_arg}')
    cursor.commit()


@app.route('/shop/delete_shop', methods=['GET', 'POST'])
def delete_shop():
    form = DeleteShopForm()
    if request.method == 'GET':
        return render_template('delete_shop.html', form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
            execute_sp_delete_shop(form)
            return redirect('/shop/delete_shop')
        return 'invalid form'


def execute_sp_delete_shop(form):
    arguments = []
    for item in list(form):
        arguments.append(str(item.raw_data[0]))
    arguments.pop()  # csrf token is not used

    string_arg = str(arguments)[1:-1]
    print((f'exec sp_DeleteShop {string_arg}'))
    cursor = connection.cursor()
    cursor.execute(f'exec sp_DeleteShop{string_arg}')
    cursor.commit()



def print_form(form):
    for item in list(form):
        print(item)

@app.errorhandler(500)
def error_handler_http500(error):
    return render_template('error_handler_http500.html', error=error)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
