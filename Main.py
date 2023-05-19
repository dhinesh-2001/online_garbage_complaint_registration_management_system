from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from werkzeug.utils import secure_filename
import datetime
import mysql.connector
import sys
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():

    return render_template('index.html')

@app.route("/admin")
def admin():

    return render_template('adlog.html')
@app.route("/reports")
def reports():

    return render_template('reports.html')
@app.route("/ratview")
def ratview():
    id = request.args.get('id')
    session['ris']=id

    return render_template('rating.html')
@app.route("/userregister")
def userregister():

    return render_template('usreregister.html')
@app.route("/login")
def emp():
    return render_template('login.html')
@app.route("/userlogin")
def userlogin():
    return render_template('userlogin.html')
@app.route("/adminhome")
def adminhome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee ")
    data = cur.fetchall()


    return render_template('adminhome.html', data=data)
@app.route("/emphome")
def emphome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaint where status='complaint sent to officer'")
    data = cur.fetchall()
    return render_template('emphome.html',data=data)
@app.route("/userhome")
def userhome():
    return render_template('userhome.html')
@app.route("/empregister")
def empregister():
    return render_template('register.html')
@app.route("/viewuser")
def viewuser():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register ")
    data = cur.fetchall()

    return render_template('viewuser.html',data=data)



@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

           conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
           # cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM employee ")
           data = cur.fetchall()

           return render_template('adminhome.html',data=data)

       else:
        return render_template('index.html', error=error)


@app.route("/emplogin", methods=['GET', 'POST'])
def emplogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['fname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute("SELECT * from employee where uname='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM complaint where status='complaint sent to officer'")
            data = cur.fetchall()

            return render_template('emphome.html', data=data)

@app.route("/uslogin", methods=['GET', 'POST'])
def uslogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:
            print(data[0])
            session['usid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM register where uname='" + username + "' and password='" + password + "'")
            data = cur.fetchall()

            return render_template('userhome.html', data=data)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name1 = request.form['name']
        gender = request.form['gender']

        email = request.form['email']

        phone = request.form['phone']



        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']
        dept = request.form['dept']
        place = request.form['place']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employee VALUES ('','" + name1 + "','" + gender + "','"+ email+"','"+phone+"','" + dept + "','"+address+"','"+place+"','"+uname+"','"+password+"')")
        conn.commit()
        conn.close()


    return render_template('login.html')
@app.route("/usregister", methods=['GET', 'POST'])
def usregister():
    if request.method == 'POST':

        name1 = request.form['name']
        gender = request.form['gender']

        email = request.form['email']

        phone = request.form['phone']



        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']

        place = request.form['place']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO register VALUES ('','" + name1 + "','" + gender + "','"+ email+"','"+phone+"','"+address+"','"+place+"','"+uname+"','"+password+"')")
        conn.commit()
        conn.close()


    return render_template('userlogin.html')


@app.route("/complaint", methods=['GET', 'POST'])
def complaint():
    if request.method == 'POST':

        dept = request.form['dept']
        cctype = request.form['ctype']

        location = request.form['location']

        date = request.form['date']
        uname= session['uname']



        details = request.form['details']
        file = request.files['file']
        file.save("static/upload/" + file.filename)


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO complaint VALUES ('','" + uname + "','" + dept + "','"+ cctype+"','"+location+"','" + date + "','" + details + "','"+file.filename+"','','','')")
        conn.commit()
        conn.close()


    return render_template('userhome.html')

@app.route("/cview")
def cview():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaint where uname='"+uname+"'")
    data = cur.fetchall()

    return render_template('cview.html', data=data)
@app.route("/viewcomplaint")
def viewcomplaint():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaint where status=''")
    data = cur.fetchall()

    return render_template('viewcomplaint.html', data=data)
@app.route("/action")
def action():


         #categories=request.form['id']
         id=request.args.get('id')

         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
         cursor = conn.cursor()
         cursor.execute("select * from complaint where id='"+id+"'")
         data = cursor.fetchall()
         print(data)
         return render_template("action.html", data=data)
@app.route("/action1", methods=['GET', 'POST'])
def action1():
    if request.method == 'POST':


         #categories=request.form['id']
         id = request.form['id']
         cctype = request.form['ataken']

         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
         cursor = conn.cursor()
         cursor.execute("update complaint set status='"+ cctype +"' where id='"+ id +"'")
         conn.commit()
         conn.close()
         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')

         cursor1 = conn1.cursor()
         cursor1.execute("select * from complaint ")
         data = cursor1.fetchall()
         return render_template("emphome.html", data=data)
@app.route("/view1")
def view1():


         #categories=request.form['id']
         id=request.args.get('id')

         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
         cursor = conn.cursor()
         cursor.execute("select * from complaint")
         data = cursor.fetchall()
         print(data)
         return render_template("view1.html", data=data)
@app.route("/actionass")
def actionass():


         #categories=request.form['id']
         id=request.args.get('id')



         print(id)
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
         cursor = conn.cursor()
         cursor.execute("update complaint set status='complaint sent to officer' where id='" + id + "'")
         conn.commit()
         conn.close()
         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')

         cursor1 = conn1.cursor()
         cursor1.execute("select * from complaint where status='' ")
         data = cursor1.fetchall()
         return render_template("viewcomplaint.html", data=data)
@app.route("/cview1")
def cview1():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM complaint where uname='"+uname+"'")
    data = cur.fetchall()

    return render_template('cview1.html', data=data)
@app.route("/feed", methods=['GET', 'POST'])
def feed():
    error = None
    if request.method == 'POST':
        id=session['ris']
        urate = request.form['rate']
        feed = request.form['feed']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute(
            "update complaint set urate='"+urate+"',feed='"+feed+"' where id='"+id+"'")
        conn.commit()
        conn.close()
        return render_template('cview.html')
@app.route("/datereports", methods=['GET', 'POST'])
def datereports():
    error = None
    if request.method == 'POST':
        sdate = request.form['sdate']
        edate = request.form['edate']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='empcomp')
        cursor = conn.cursor()
        cursor.execute("SELECT * from complaint where date BETWEEN '"+sdate+"' and '"+edate+"'")
        data = cursor.fetchall()

        return render_template('reports.html', data=data)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)