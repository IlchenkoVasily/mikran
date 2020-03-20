from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import loader

from .models import Profile

def index(request):
    return render(request,'main/index.html')
def profile(request):
    profiles = User.objects.all()
    template = loader.get_template('main/index.html')
    context = {
        'user_list': profiles,
    }
    return HttpResponse(template.render(context, request))


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         ...