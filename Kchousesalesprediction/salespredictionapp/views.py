from django.shortcuts import render
from django.conf import settings
import os
import pickle
from scipy import integrate
# Create your views here.

def mlbankloanprediction(request):
    d=True
    ans=NotImplemented 
    if request.method == "POST":
        a=[]
        print(type(a))
        print(request.POST)
        print(len(request.POST))
        for key,value in request.POST.items():
            print(type(value))
            a.append(value)
        del a[0]
        del a[18]

        print(a)
        pi = pickle.load(open('log_model.pkl','rb'))
        b=pi.predict([a])
        print(a)
        ans=b
        d=False
    return render(request,'mlbankloanprediction.html',{'d':d,'ans':ans})