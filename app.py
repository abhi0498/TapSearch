from flask import Flask,render_template,redirect,request
import PyPDF2
import re
app=Flask(__name__)
paras=[]
key=""
ind=list()
@app.route("/",methods=["GET","POST"])

def home():
    if request.method=="GET":
        return render_template("index.html")
    else:
        global paras,key
        paras=request.form["para"].split("\r\n\r\n")
       
        i=[j for j in range(len(paras)) if paras[j]=='']
        for d in i:
            paras.remove('')
        key =request.form["key"]
        return redirect('/y')
        

@app.route("/y",methods=["GET"])
def y():
    global ind
    ind=[]
    new_para=[]
    for i,para in enumerate(paras):
        new_para=[p.lower() for p in para.split()]
        new_para=[re.sub('[^A-Za-z0-9]+', '', p) for p in new_para]
        if key.lower() in new_para:
            ind.append(i+1)
    ind=ind[:10]
    if len(ind)==0:
        ind="Not found"
    data={
        'key':key,
        'ind':ind,
        'paras':paras
    }
    return render_template('results.html',data=data)

@app.route("/pdf",methods=["GET","POST"])
def pdf():
    if request.method=="GET":
        return render_template('pdf.html')
    else:
        global paras,key
        pages=[]
        paras=[]
        f=request.files['files']
        f.save(f.filename)
        pdfFileObj = open(f.filename, 'rb') 
  
 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        
        key = request.form["key"]
        
  
        for i in range(pdfReader.numPages):
            pages.append(pdfReader.getPage(i))
        for page in pages:
            paras.append(page.extractText())
      
        
        
        return redirect('/y')
        
     
        



if __name__ == "__main__":
    app.run(debug=True)

