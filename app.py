import requests
from flask import Flask,render_template,request,url_for
import pickle
import os
import joblib

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/",methods=['POST','GET'])
def hello():
    if request.method=="POST":
        content=request.form.get('content')
    
        model_path = "models\\spam_prediction_model"
        vectorizer_path = "models\\vectorizer"

        model=joblib.load(model_path)
        v=joblib.load(vectorizer_path)
    
        arr=[]
        arr.append(content)

        converted=v.transform(arr)
        ans=model.predict(converted)

        percent=model.predict_proba(converted)

        percentage_spam=round(percent[0][1],2)*100
        percentage_notspam=round(percent[0][0],2)*100

        if(ans[0]==1):
            result="Spam"
        else:
            result="Not Spam"
        
        return render_template("index.html",result=result,percentage_spam=percentage_spam,percentage_notspam=percentage_notspam)



if(__name__)=="__main__":
    app.run(debug=True)