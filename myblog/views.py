from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import User

def index(request):
    """
    主页
    """
    return render(request, 'myblog/index.html')

def register(request):
    """
    注册页面
    """
    return render(request, 'myblog/register.html')

def register_suc(request):
    """
    注册成功页面
    """
    return render(request, 'myblog/register_suc.html')

def register_fail(request):
    """
    注册失败页面
    """
    return render(request, 'myblog/register_fail.html')

def do_register(request):
    """
    注册
    """
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User(username=username, password=password, email=email, create_date=timezone.now())
        user.save()
        request.session['logged_in_user'] = user
    except KeyError as e:
        print(e)
        return HttpResponseRedirect(reverse('myblog:register_fail'))
    else:
        return HttpResponseRedirect(reverse('myblog:register_suc'))
    
def do_logout(request):
    """
    注销
    """
    try:
        del request.session['logged_in_user']
    except KeyError as e:
        print(e)
    return HttpResponseRedirect(reverse('myblog:index'))

def login(request):
    """
    登录页面
    """
    return render(request, 'myblog/login.html')

def do_login(request):
    """
    登录
    """
    try:
        user = User.objects.get(username=request.POST['username'])
        if user.password == request.POST['password']:
            request.session['logged_in_user'] = user
            return HttpResponseRedirect(reverse('myblog:index'))
        else:
            return render(request, 'myblog/login.html', {'username' : user.username,
                                                         'error_message': "登录失败，用户名或密码错误"})
    except (KeyError, User.DoesNotExist):
        return render(request, 'myblog/login.html', {'error_message': "登录失败，用户名不存在"})