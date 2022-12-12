from flask import Flask,render_template,request,flash,redirect,session
from dbhelper import *

app = Flask(__name__)
app.secret_key="@#klarke"
upload_folder="static/imgs"
app.config["UPLOAD_FOLDER"]=upload_folder

@app.route("/upload",methods=['POST','GET'])
def upload():
    if request.method=="POST":
        
        file=request.files['webcam']
        idno=request.args.get("idno")
        lastname=request.args.get("lastname")
        firstname=request.args.get("firstname")
        course=request.args.get("course")
        level=request.args.get("level")
        imagename=upload_folder+"/"+idno+".jpg"
      
        file.save(imagename)
        okey:bool=addrecord('students',idno=idno,lastname=lastname,firstname=firstname,course=course,level=level,image=imagename)
        return redirect("/")

@app.route("/savedata",methods=['POST'])
def savedata():
    idno: str = request.form["idno"]
    lastname: str = request.form["lastname"]
    firstname: str = request.form["firstname"]
    course: str = request.form["course"]
    level: str = request.form["level"]
    flag: str = request.form["flag"]

    if idno!=None and lastname!=None and firstname!=None and course!=None and level!=None:        
        okey: bool = addrecord('students',idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
        if okey:
            flash("New Student Added")
            return redirect("/main")
    else:
        if flag == 1:
            okey: bool = updaterecord('students',idno=idno,lastname=lastname,firstname=firstname,course=course,level=level)
            if okey:
                flash("New Student Updated")
                return redirect("/main")


@app.route("/deletedata")
def deletedata():
    idnumber: str = request.args.get("idno")
    okey: bool = deleterecord('students',idno=idnumber)
    if okey:
        flash("Data Deleted")
        return redirect("/main")
    else:
        flash("Error Deleteting Data")
        return redirect("/main")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"]="no-cache,no-store,must-revalidate"
    return response

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged Out")
    return redirect("/")

@app.route("/main")
def main():
    if "logged_user" in session:
        header: list = ['idno','lastname','firstname','course','level','action']
        stlist: list = getallrecord('students')
        return render_template("main.html",headername='student list',studentlist=stlist,head = header)
    else:
        flash("Login Properly!")
        return redirect("/")

@app.route("/login", methods=['POST'])
def login():
    uname: str = request.form["username"]
    pword: str = request.form["password"]
    user: dict = userlogin('users',username=uname,password=pword)
    if user!=None:
        session["logged_user"]=user["username"]
        flash("Login Accepted!")
        return redirect("/main")
    else:
        flash("Login Failed!")
        return redirect("/")


@app.route("/")
def index():
    return render_template("login.html",headername='user login')

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)