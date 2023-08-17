from django.shortcuts import render

def index(request):
    title = 'universidad Pepito Perez'
    return render(request,'index.html',{
        'title' : title
    })
