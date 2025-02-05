from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader 

# Create your views here.


def index(request):
    return HttpResponse("Hello world")

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 

def pathview(request, name, id): 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name: {}, UserID: {}".format(name, id))

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse("Name:{}, UserID:{}".format(name, id))

def login(request):
    return render(request, "form.html")


# def index(request): 
#     template = loader.get_template('template/index.html') 
#     context={}  
#     return HttpResponse(template.render(context, request)) 