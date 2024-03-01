from flask import Flask, request, redirect, jsonify 
import mysql.connector as mysql

conn = mysql.connect(
    host= "localhost",
    user = "root",
    password = "12345678",
    port = 3306,
    database = "mymemo"
)

app = Flask(name)

@app.route('/putuser', methods=["PUT"])
def putuser():
    response = request.getjson()
    idmemo = response['idmemo']
    firstname = response['firstname']
    lastname = response['lastname']
    email = response['email']

    #UPDATE DATA TO DB 
    cur = conn.reconnect()
    cur = conn.cursor()
    sql = "UPDATE  memo SET firstname=%s, lastname=%s, email=%s"
    sql += "WHERE idmemo=%s"
    data = (firstname, lastname, email, idmemo)
    cur.execute(sql, data)
    conn.commit()
    conn.close()
    return redirect('http://localhost:5001/getuser')

    return jsonify(idmemo)


if __name == '__main':
    app.run(host='0.0.0.0', port=5004, debug=True)