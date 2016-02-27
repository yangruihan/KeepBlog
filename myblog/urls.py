from django.conf.urls import url

from . import views

app_name = 'myblog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^do_register/$', views.do_register, name='do_register'),
    url(r'^register_suc/$', views.register_suc, name='register_suc'),
    url(r'^register_fail/$', views.register_fail, name='register_fail'),
    url(r'^do_logout/$', views.do_logout, name='do_logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^do_login/$', views.do_login, name='do_login'),
]