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
    url(r'^username_check/$', views.username_check, name='username_check'),
    url(r'^jump_personal_page/$', views.jump_personal_page,
        name='jump_personal_page'),
    url(r'^improve_userinfo/$', views.improve_userinfo,
        name='improve_userinfo'),
    url(r'^do_create_userinfo/$', views.do_create_userinfo,
        name='do_create_userinfo'),
    url(r'^user_home/$', views.user_home, name="user_home"),
    url(r'^article_detail/(?P<article_id>[0-9]+)/$',
        views.article_detail, name='article_detail'),
    url(r'^user_home/category/(?P<category_id>[0-9]+)/$',
        views.user_home_category, name="user_home_category"),
    url(r'^user_home/tag/(?P<tag_id>[0-9]+)/$',
        views.user_home_tag, name="user_home_tag"),
]
