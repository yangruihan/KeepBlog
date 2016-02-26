from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import User

def index(request):
    return render(request, 'myblog/index.html')

def register(request):
    return render(request, 'myblog/register.html')

def do_register(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User(username=username, password=password, email=email, create_date=timezone.now())
        user.save()
        request.session['logged_in_user'] = user
        return render(request, 'myblog/register_suc.html')
    except KeyError as e:
        print(e)
        return render(request, 'myblog/register_fail.html')