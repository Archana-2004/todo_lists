from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context={'success':False}
    if request.method == "POST":
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(taskTitle=title, desc=desc)
        ins.save()
        context={'success':True}

    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')


