from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def user_login(request):
    form = LoginForm()
    return render(request, "user/login.html", {'form':form})
