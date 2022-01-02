from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from nav import nav
import pyodbc

SERVER_NAME = 'LAPTOP-JVD1T1M5'

connection = pyodbc.connect(driver='{SQL Server}', server=SERVER_NAME, database='WHOLESALE_CLOTHING_VENDOR_DATABASE_SYSTEM',               
               trusted_connection='yes')


app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read_employees')
def read_employees():
    cursor = connection.cursor()
    cursor.execute('Select * From EMPLOYEE')
    employee_info = cursor.fetchall()

    return render_template('read_employees.html', employee_info=employee_info)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
