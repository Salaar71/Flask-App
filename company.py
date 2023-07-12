from flask import Flask, jsonify
from mysql.connector import (connection)


app=Flask(__name__) 
mydb = connection.MySQLConnection(user='root', password='sp224466',
                                 host='127.0.0.1',
                                 database='sys')
cursor = mydb.cursor()

@app.route('/')
def company():
    # Show database
    cursor.execute('''SHOW TABLES''')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/employees')
def employees():
    # Show database
    cursor.execute('''SELECT * FROM employee''')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/clients')
def clients():
    # Show database
    cursor.execute('''SELECT * FROM client''')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/branches')
def branches():
    # Show database
    cursor.execute('''SELECT * FROM branch''')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/branchsuppliers')
def branchsuppliers():
    # Show database
    cursor.execute('''SELECT * FROM branch_supplier''')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)

@app.route('/workswith')
def workswith():
    # Show database
    cursor.execute('''SELECT * FROM works_with''')
    row_headers=[x[0] for x in cursor.description] #this will extract row headers
    rv = cursor.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))
    return jsonify(json_data)
   

