from flask import Flask,render_template,redirect,request

app=Flask(__name__)
paras=[]
key=""
ind=[]
@app.route("/",methods=["GET","POST"])

def home():
    if request.method=="GET":
        return render_template("index.html")
    else:
        global paras,key
        paras=request.form["para"].split("\r\n\r\n")
        key =request.form["key"]
        return redirect('/y')
        

@app.route("/y",methods=["GET"])
def y():
    global ind
    for i,para in enumerate(paras):
        if key in para.split():
            ind.append(i+1)
    return ' '.join(str(ind))

