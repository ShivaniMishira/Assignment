from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Xusers
from django.contrib import messages

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
        messages.success(request, "New User Added." )
    return render(request, 'new_users.html')

# show data of single user from database
def info_users(request,id):
    info = Xusers.objects.get(id=id)
    return render(request, 'users_info.html', {'i':info})


def edit(request,id):
    A = Xusers.objects.get(id=id)
    return render(request, 'update.html', {'A':A})


# Updates information Specific id from database
def update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        update = Xusers.objects.get(id=id)
        update.Name = name
        update.Email = email
        update.Role = role
        update.save()
        messages.success(request, " User Info Updated." )
    return render(request, 'users.html')
pass


# Delete Specific id from database
def delete(request,id):
    user = Xusers.objects.get(id=id)
    user.delete()
    messages.warning(request, "User Delete.")
    return render(request,'users.html')

# error handling when a user or resource is not found
def error_404(request, exception):
    return render(request,'404.html')


# search bar 
def search(request):
    if request.method=="POST":
        S = request.POST.get("search")
        if Xusers.objects.filter(Name=S):   
            con = Xusers.objects.filter(Name=S)
            context={"con":con}             
            return render(request,'search.html',context)
        else:
            return render(request, '404.html' )
    return render(request, 'search.html')    