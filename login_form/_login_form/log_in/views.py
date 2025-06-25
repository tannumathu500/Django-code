from django.shortcuts import render, render 
from log_in.forms import CustomLoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view (request):
    # return HttpResponse("HI, you are going to login soon , fill the information as needed in login form, thanks")
    # return render ()
    if request.method == "POST":
        form = CustomLoginForm (request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            print("username :- " ,username)
            print("password :- " ,password)

            user = authenticate(username=username, password=password)

            if user is not None :
                login (request, user)
                return render(request, "welcome.html")
            else:
                form.add_error(None, "Inavlid username and password")
    else:
        form = CustomLoginForm()
    return render (request, 'login.html', {"form": form})


