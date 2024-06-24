import pickle
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd

def home(request):
    print("test function is called from view")
    return render(request,"home.html")

def index(request):
    print("test function is called from view")
    return render(request,"index.html")

def result(request):
        if request.method=="POST":
                temp={}
                temp['temp1']=request.POST.get("temp")
                temp['humi1']=request.POST.get("humidity")
                temp['exe1']=request.POST.get("exe")
                temp['step1']=request.POST.get("step")
                model=pickle.load(open("model\classifier.pkl",'rb'))
                testdata=pd.DataFrame({'x':temp}).transpose()

                pred=model.predict(testdata)[0]
                
                if(pred==0):
                        result="Don't need Water !"
                else:
                        result='Drink the Water immediately !'
                print(pred)
                return render(request,"result.html",{'result':result})
                
        return render(request,"result.html")
