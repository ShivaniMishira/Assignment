from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Xusers

# front web page
def index(request):
    return render(request, 'index.html')


# returns the string 'Hello Word' 
def hello(request):
    return HttpResponse('HELLO WORLD !!!')


# A list of users from a MySQL database and display as a list in users.html page
def users(request):
    record = Xusers.objects.all()
    context = {'record':record}
    return render(request, 'users.html', context)


# Adds new data in 'users' table in database
def new_users(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Role = request.POST.get('role')
        new = Xusers(Name=Name, Email=Email, Role=Role)
        new.save()
    return render(request, 'new_users.html')

# show data of single user from database
def info_users(request,id):
    info = Xusers.objects.get(id=id)
    return render(request, 'users_info.html', {'i':info})
