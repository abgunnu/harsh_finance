from multiprocessing import context
from datetime import datetime
from home.models import Contact
from django.shortcuts import render, HttpResponse
from django.contrib import messages 

# Create your views here.
def index(request):
    context = {
        'variable1' : 'gunnu is great',
        'variable2' : 'ram' 
    }

    return render(request,'index.html')
    #return HttpResponse('this is homepage')

def about(request):
    #return HttpResponse('this is about page')
    return render(request,'about.html',context) 

def services(request):
    #return HttpResponse('this is services page')
    return render(request,'services.html',context)

def contact(request):
    #return HttpResponse('this is contact page')
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        desc = request.POST.get('desc')
        contact = Contact(name=name, email= email, phone =phone, desc =desc, date = datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent!')

    return render(request,'contact.html')