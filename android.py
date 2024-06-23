import os
import flask
from werkzeug.utils import secure_filename
from src.dbconnector import *
obj = flask.Flask(__name__)

@obj.route("/loginA",methods=['post'])
def loginA():
    username = flask.request.form['Username']
    password = flask.request.form['Password']
    query = "select*from login where username=%s and password=%s"
    value = (username, password)
    result = selectone(query, value)
    if result is None:
        return flask.jsonify({'task':'invalid'})
    else:
        return flask.jsonify({'task':'valid','lid':result[0]})

@obj.route('/signupA', methods=['post'])
def signupA():
    try:
        fname = flask.request.form['fname']
        lname = flask.request.form['lname']
        age = flask.request.form['age']
        place = flask.request.form['place']
        pin = flask.request.form['pin']
        email = flask.request.form['email']
        phone = flask.request.form['phone']
        uname = flask.request.form['uname']
        pwd = flask.request.form['pwd']
        gender = flask.request.form['gender']
        query1 = "insert into login values(null,%s,%s,'user')"
        val=uname,pwd
        lid=iud(query1,val)
        query2 = "insert into user values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value1 = (lid, fname, lname,age, gender, place, pin, email, phone)
        iud(query2, value1)
        return flask.jsonify({'task':'success'})
    except Exception as e:
        print(e)
        return flask.jsonify({'task':'Error'})

@obj.route("/viewplanA", methods=['post'])
def viewplanA():
    query = "select * from upload_plans JOIN architect on upload_plans.arch_lid=architect.logid"
    result = androidselectallnew(query)
    print(result)
    return flask.jsonify(result)

@obj.route("/curtaindesignA", methods=['post'])
def curtaindesignA():
    query = "select * from curtaindesigns"
    result = androidselectallnew(query)
    return flask.jsonify(result)

@obj.route("/furnituredesignA", methods=['post'])
def furnituredesignA():
    query = "select * from uploadoor"
    result = androidselectallnew(query)
    return flask.jsonify(result)

@obj.route("/useruploadeddesignA", methods=['post'])
def useruploadeddesignA():
    designname=flask.request.form['designname']
    uid=flask.request.form['lid']
    file=flask.request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/upcurtain', filename))
    query1 = "insert into user_uploaded_designs values(null,%s,%s,%s)"
    val=(designname,filename,uid)
    print(iud(query1,val))
    return flask.jsonify({'task':'success'})

@obj.route("/discussionuserA", methods=['post'])
def discussionuserA():
    query = "select fname,lname from architect"
    result = androidselectallnew(query)
    return flask.jsonify(result)

@obj.route("/viewreplyA", methods=['post'])
def viewreplyA():
    query = "select * from discussion JOIN architect on discussion.aid=architect.id"
    result = androidselectallnew(query)
    return flask.jsonify(result)

@obj.route("/viewfeedbackA", methods=['post'])
def viewfeedbackA():
    try:
        f = flask.request.form['feedback']
        uid = flask.request.form['lid']
        query1 = "insert into feedbacks values(null,%s,%s,curdate())"
        val = (uid, f)
        print(iud(query1, val))
        return flask.jsonify({'task': 'success'})
    except Exception as e:
        print(e)
        return flask.jsonify({'task': 'Error'})

@obj.route("/complaintA", methods=['post'])
def complaintA():
    query = "select * from complaints"
    result = androidselectallnew(query)
    return flask.jsonify(result)

@obj.route("/sendcomplaintA", methods=['post'])
def sendcomplaintA():
    try:
        qst = flask.request.form['complaint']
        lid = flask.request.form['lid']
        value = (lid, qst)
        query = "insert into complaints values(null,%s,%s,'pending',curdate())"
        iud(query, value)
        return flask.jsonify({'task': 'valid'})
    except Exception as e:
        print(e)
        return flask.jsonify({'task': 'Error'})

@obj.route("/archnameA", methods=['post'])
def archnameA():
    query = "select fname,lname,logid,id from architect"
    result = androidselectallnew(query)
    return flask.jsonify(result)

@obj.route("/questionA", methods=['post'])
def questionA():
    try:
        qst = flask.request.form['qst']
        lid = flask.request.form['lid']
        aid = flask.request.form['aid']
        value = (lid, qst,aid)
        query = "insert into discussion values(null,%s,%s,%s,'pending')"
        iud(query, value)
        # iud("insert into discussion values(null,%s,%s,%s,'pending')", (1, "sdsa",1))
        return flask.jsonify({'task': 'valid'})
    except Exception as e:
        print(e)
        return flask.jsonify({'task': 'Error'})


obj.run(host="0.0.0.0",port=5000)