from django.shortcuts import render

# Create your views here.

def register(request):

    if request.method == "POST":
        first_name = request.POST("First_name")
        Password = request.POST("Password")
    
    else:

        return render(request , "register.html")