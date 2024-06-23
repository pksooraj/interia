import os
from flask import *
from werkzeug.utils import secure_filename

obj = Flask(__name__)
from src.dbconnector import *

obj.secret_key = "aaaaaa"


@obj.route('/')
def main():
    return render_template('mod.html')


@obj.route("/login", methods=['post'])
def login():
    username = request.form['textfield']
    password = request.form['textfield2']
    query = "select*from login where username=%s and password=%s"
    value = (username, password)
    result = selectone(query, value)
    if result is None:
        return '''<script>alert("Please Enter valid usename&password");
        window.location="/" </script>'''
    elif result[3] == "admin":
        session['lid'] = result[0]
        return redirect('/adminhome')
    elif result[3] == "architect":
        session['lid'] = result[0]
        return redirect('/architectuploadeddesign')
    else:
        '''<script>alert("invalid username/password");
        window.location="/" </script>'''


@obj.route("/uploadplan", methods=['post'])
def uploadplan():
    Curtain = request.form['textfield']
    choosefile = request.files['file']
    choosefile1 = secure_filename(choosefile.filename)
    choosefile.save(os.path.join('static/upcurtain', choosefile1))
    query2 = "insert into upload_plans values(null,%s,%s,curdate(),%s)"
    value2 = (Curtain, choosefile1, session['lid'])
    iud(query2, value2)
    return '''<script>alert("uploaded successfully");
               window.location="/architectuploadeddesign" </script>'''


@obj.route('/editaechitectreg')
def editaechitectreg():
    id = request.args.get('id')
    session['arc'] = id
    qry = "select*from architect where logid=%s"
    val = str(id)
    res = selectone(qry, val)

    return render_template("editarch.html", val=res)


@obj.route('/adminhome')
def adminhome():
    id=session['lid']
    query = "select * from login where id=%s"
    result = selectone(query,id)
    print(result[1])
    return render_template('indexadmin.html', v=result[1])


@obj.route('/edit', methods=['post'])
def edit():
    firstname = request.form['textfield4']
    lastname = request.form['textfield5']
    email = request.form['textfield6']
    gender = request.form['radiobutton']
    phoneno = request.form['textfield2']
    place = request.form['textfield7']
    dob = request.form['textfield8']
    qualification = request.form.getlist('checkbox')
    q = str(','.join(qualification))

    query1 = "update architect set fname=%s,lname=%s,dob=%s,gender=%s,place=%s,qualification=%s,email=%s,phone=%s where logid=%s"
    value1 = (firstname, lastname, dob, gender, place, q, email, phoneno, session['arc'])
    iud(query1, value1)
    return '''<script>alert("Updated succesful");
           window.location="/managearchitect" </script>'''


@obj.route('/delete')
def delete():
    id = request.args.get('id')
    query1 = "delete from architect where logid=%s"
    value1 = (id)
    iud(query1, value1)

    qr2="DELETE FROM login WHERE id=%s"
    iud(qr2,str(id))

    return '''<script>alert("deleted succesful");
           window.location="/managearchitect" </script>'''


@obj.route('/reg1', methods=['post'])
def reg1():
    try:
        username = request.form['textfield']
        password = request.form['textfield3']
        firstname = request.form['textfield4']
        lastname = request.form['textfield5']
        email = request.form['textfield6']
        gender = request.form['radiobutton']
        phoneno = request.form['textfield2']
        place = request.form['textfield7']
        dob = request.form['textfield8']
        qualification = request.form.getlist('checkbox')
        q = str(','.join(qualification))
        query = "insert into login values(null,%s,%s,'architect')"
        value = (username, password)
        lid = iud(query, value)
        query1 = "insert into architect values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value1 = (lid, firstname, lastname, dob, gender, place, q, email, phoneno)
        iud(query1, value1)
        return '''<script>alert("Registation succesful");
               window.location="/managearchitect" </script>'''
    except Exception as e:
        return '''<script>alert("Duplicate Entry please Try Again!!!");
                       window.location="/managearchitect" </script>'''



@obj.route('/reg', methods=['post'])
def reg():
    return render_template('reg.html')


@obj.route('/managearchitect')
def managearchitect():
    query = "select * from architect"
    result = select(query)

    return render_template('mang archi.html', value=result)


@obj.route('/viewusers')
def viewusers():
    query = "select * from user"
    result = select(query)
    return render_template('view user.html', value=result)


@obj.route('/uploadcurtaindesign', methods=['post'])
def uploadcurtaindesign():
    Curtain = request.form['textfield']
    choosefile = request.files['file']
    choosefile1 = secure_filename(choosefile.filename)
    choosefile.save(os.path.join('static/upcurtain', choosefile1))
    Description = request.form['textfield2']
    Price = request.form['textfield3']
    query2 = "insert into curtaindesigns values(null,%s,%s,%s,%s,curdate())"
    value2 = (Curtain, choosefile1, Description, Price)
    iud(query2, value2)
    return '''<script>alert("uploaded successfully");
               window.location="/adminhome" </script>'''


@obj.route('/uploadcurtaindesign1')
def uploadcurtaindesign1():
    return render_template('upload  curtain desn.html')


@obj.route('/managecurtaindesign')
def managecurtaindesign():
    return render_template('mang curtain design.html')


@obj.route('/uploadfurnituredesign')
def uploadfurnituredesign():
    return render_template('uplod furniture desn.html')


@obj.route('/uploadfurnituredesign1', methods=['post'])
def uploadfurnituredesign1():
    Curtain = request.form['textfield']
    choosefile = request.files['file']
    choosefile1 = secure_filename(choosefile.filename)
    choosefile.save(os.path.join('static/upfurni', choosefile1))
    Description = request.form['textfield2']
    Price = request.form['textfield3']
    query3 = "insert into uploadoor values(null,%s,%s,%s,%s,curdate())"
    value3 = (Curtain, choosefile1, Price, Description)
    iud(query3, value3)
    return '''<script>alert("uploaded successfully");window.location="/adminhome" </script>'''


@obj.route('/deletearchitecture')
def deletearchitecture():
    return '''<script>alert("deleted");window.location="/managearchitect" </script>'''


@obj.route('/managefurnituredesign')
def managefurnituredesign():
    return render_template('mang furniture design.html')


@obj.route('/viewcomplaints')
def viewcomplaints():
    query = "SELECT complaints.*,user.fname,lname FROM USER JOIN complaints ON complaints.userid=user.userid WHERE complaints.reply='pending'"
    result = select(query)

    return render_template('viewcomplaint.html', value=result)


@obj.route('/viewfeedback')
def viewfeedback():
    query = "SELECT feedbacks.*,user.fname,lname FROM USER JOIN feedbacks ON feedbacks.userid=user.userid"
    result = select(query)
    return render_template('viewfeedback.html', value=result)


@obj.route('/architectuploadeddesign')
def architectuploadeddesign():
    return render_template('indexarchitect.html')


@obj.route('/uploadplans')
def uploadplans():
    return render_template('upload plan.html')


@obj.route('/manageplans')
def manageplans():
    return render_template('mng plan.html')


@obj.route('/viewdesign')
def viewdesign():
    query = "select *,login.* from upload_plans JOIN `login` ON `login`.`id`=`upload_plans`.`arch_lid`"
    result = select(query)
    return render_template('View Design.html', value=result)

@obj.route('/viewuseruploadeddesign')
def viewuseruploadeddesign():
    query = "SELECT `user`.*,`user_uploaded_designs`.* FROM `user_uploaded_designs` JOIN `user` ON `user`.`userid`=`user_uploaded_designs`.`uid`"
    result = select(query)
    return render_template('View User Uploaded Design.html', value=result)


@obj.route('/viewuseruploadeddesign1')
def viewuseruploadeddesign1():
    query = "select * from upload_plans"
    result = select(query)
    return render_template('view user.html', value=result)

@obj.route('/discussionwithuser')
def discussionwithuser():
    query = "SELECT discussion.*,user.* FROM USER JOIN discussion ON discussion.user_id=user.userid WHERE discussion.status='pending'"
    result = select(query)
    return render_template('descriptiom with user.html', value=result)

@obj.route('/discussionreply')
def discussionreply():
    id1 = request.args.get('id1')
    session['did'] = id1
    # print('sads')
    return render_template('disc reply.html')


@obj.route('/sendreply')
def sendreply():
    id1 = request.args.get('id1')
    session['cid'] = id1
    # print('asdasdadasdsadsads')
    print(id1)
    return render_template('send reply.html')

@obj.route('/discreply', methods=['post'])
def discreply():
    reply = request.form['textfield']

    query1 = "update discussion set status=%s where id=%s"
    val = (reply, session['did'])
    iud(query1, val)
    return '''<script>alert("Replied succesful");
               window.location="/discussionwithuser" </script>'''

@obj.route('/reply', methods=['post'])
def reply():
    reply = request.form['textfield']

    query1 = "update complaints set reply=%s where compid=%s"
    val = (reply, session['cid'])
    iud(query1, val)
    return '''<script>alert("Replied succesful");
               window.location="/viewcomplaints" </script>'''


obj.run(debug=True)
