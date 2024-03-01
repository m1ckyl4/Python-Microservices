from flask import Flask, request,  redirect, jsonify 
import mysql.connector as mysql

conn = mysql.connect(
    host= "localhost",
    user = "root",
    password = "12345678",
    port = 3306,
    database = "mymemo"
)

app = Flask(name)

@app.route('/adduser', methods=["POST"])
def adduser():
    cur = conn.reconnect()

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')

    sql = "INSERT INTO memo(firstname, lastname, email)"
    sql += "VALUES(%s,%s,%s)"
    data = (firstname, lastname, email)

    cur = conn.cursor()
    cur.execute(sql,data)
    conn.commit()
    conn.close()
    return redirect('http://localhost:5001/getuser')

if name == "_main":
    app.run(host='0.0.0.0', port=5003, debug=True)