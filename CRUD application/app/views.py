from django.shortcuts import render
from .models import *
# Create your views here.
def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    # Data come from HTML to View
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    # creating object of model class
    #Inserting data into table
    newuser = student.objects.create(Firstname=fname,Lastname=lname,
                                        Email=email,Contact=contact)
    
    # After Insert render on show.html
    return render(request,"app/show.html")