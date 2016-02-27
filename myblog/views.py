from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from myblog.models import UserInfo

from .models import User, Article, Tag, UserInfo


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
    
def username_check(request):
    """
    用户名检测
    """
    try:
        if request.GET['username'].strip() == '':
            return HttpResponse("请输入用户名")
        else:
            User.objects.get(username=request.GET['username'])
            return HttpResponse("用户名已存在，请重新输入")
    except User.DoesNotExist:
        return HttpResponse("")
    
def improve_userinfo(request):
    """
    完善个人信息页面
    """
    return render(request, 'myblog/improve_userinfo.html')
    
def jump_personal_page(request):
    """
    判断用户是否填写个人信息，如果填写则跳转到个人主页，如果未填写，则提示用户填写
    """
    try:
        user = request.session['logged_in_user']
        if (hasattr(user, "userinfo")):
            return HttpResponseRedirect(reverse('myblog:user_home'))
        else:
            return HttpResponseRedirect(reverse('myblog:improve_userinfo'))
    except KeyError as e:
        print(e)
        return HttpResponse("个人主页功能出现异常")
        
def do_create_userinfo(request):
    """
    创建用户个人信息
    """
    try:
        user = request.session['logged_in_user']
        nickname = request.POST['nickname']
        realname = request.POST['realname']
        gender = request.POST['gender']
        birthday = request.POST['birthday']
        city = request.POST['s_city'] if request.POST['s_city'] != "地级市" else ""
        province = request.POST['s_province'] if request.POST['s_province'] != "省份" else ""
        area = province + '_' + city
        if province == "":
            area = ""
        description = request.POST['description']
        userinfo = UserInfo(user=user, nickname=nickname, realname=realname, gender=gender, birthday=birthday, area=area, description=description)
        userinfo.save()
        return HttpResponseRedirect(reverse('myblog:user_home'))
    except KeyError as e:
        print(e)
        return HttpResponse("创建个人信息失败")
    
def user_home(request):
    """
    个人主页
    """
    try:
        user = request.session['logged_in_user']
        articles = Article.objects.filter(user=user).order_by('-date_time')
        paginator = Paginator(articles, 10) # 每页显示个数
        page = request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except PageNotAnInteger :
            article_list = paginator.page(1)
        except EmptyPage :
            article_list = paginator.paginator(paginator.num_pages)
        return render(request, 'myblog/user_home.html', {'article_list' : article_list})
    except KeyError as e:
        print(e)
        return HttpResponse("获得个人博文失败")