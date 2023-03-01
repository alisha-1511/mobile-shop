from django.shortcuts import render, redirect
from product.models import detail
from register.models import user_detail
from django.contrib import messages
from contacted.models import contacted_detail


def home(request):
    pro_details = detail.objects.all()
    data = {
        "product" : pro_details
    }
    return render(request, "index.html", data)

def profile(request):
    return render(request, "profile.html")

def contact(request):
    if request.method=="POST":
        fname = request.POST['fullname']
        email = request.POST['email']
        query = request.POST['query']
        user = contacted_detail.objects.create(fullname=fname,email=email,query=query)
        user.save()
        messages.info(request, "successfully sent")
    return render(request, "contact.html")



def register(request):
    if request.method=="POST":
        fname = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        number = request.POST['number']
        address = request.POST['address']
        if password==cpassword:
            if len(password) >=8:
                if user_detail.objects.filter(email=email).exists():
                    
                    messages.info(request, "email already exist please login.")
                    return render(request, "login.html")
                    
                else:
                    if user_detail.objects.filter(number=number).exists():
                        messages.info(request, "number already exist.")
                        return render(request, "login.html")
                        
                    else:
                        user = user_detail.objects.create(fullname=fname,email=email,password=password,number=number,address=address)
                        user.save()
                        return redirect('/login')
            else:
                messages.info(request, "password must be of 8 character")
                return render(request, "register.html")
             

        else:
            messages.info(request, "Please enter same password")
            return render(request, "register.html")
    else:
        return render(request, "register.html")
    
    return render(request, "register.html")



def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        if user_detail.objects.filter(email=email).exists() and user_detail.objects.filter(password=password).exists():
                data = {
                    'data':user_detail.objects.all().filter(email=email)
                }
                return render(request,"profile.html", data)
        else:
            messages.info(request, "Invalid")
    return render(request, "login.html")


