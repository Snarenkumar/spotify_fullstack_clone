from django.shortcuts import render,HttpResponse
from home.models import Logindetails
# Create your views here.
def login(request):
    if (request.method == "POST" )  :
        username =request.POST.get('username')
        password =  request.POST.get('password')
        
        none =Logindetails(username=username,password=password)
        none.save()
        print ("guys it is working ")
        print (username)
        print (password)
    

    return render (request,'login.html',)
    