from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import User

def index(request):
    return render(request, 'myblog/index.html')

def register(request):
    return render(request, 'myblog/register.html')

def register_suc(request):
    return render(request, 'myblog/register_suc.html')

def register_fail(request):
    return render(request, 'myblog/register_fail.html')

def do_register(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User(username=username, password=password, email=email, create_date=timezone.now())
        user.save()
    except KeyError as e:
        # return render(request, 'myblog/register.html', {
        #         'error_message': u"你必须将信息填写完整",
        #     })
        print(e)
        return HttpResponseRedirect(reverse('myblog:register_fail'))
    else:
        return HttpResponseRedirect(reverse('myblog:register_suc'))