from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
#@login_required(login_url="login/")
def index(request):
    print(request.user.username)
    return render(request, 'dashboard/index.html')

