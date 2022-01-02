from flask import Flask
import pyodbc

SERVER_NAME = 'LAPTOP-JVD1T1M5'

connection = pyodbc.connect(driver='{SQL Server}', server=SERVER_NAME, database='WHOLESALE_CLOTHING_VENDOR_DATABASE_SYSTEM',               
               trusted_connection='yes')


app = Flask(__name__)

@app.route('/hello/', methods=['GET'])
def hello():
    return 'HELLO WORLD'

@app.route('/')
def index():
    cursor = connection.cursor()
    cursor.execute('Select * From EMPLOYEE')
    
    return str(cursor.fetchall())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
