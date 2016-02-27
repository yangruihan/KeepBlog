from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    """
    用户账号类
    """
    username = models.CharField(max_length=50)  # 用户名
    password = models.CharField(max_length=50)  # 密码
    email = models.EmailField()  # 邮箱
    create_date = models.DateTimeField(auto_now_add=True)  # 创建时间
     
    def __str__(self):
        return self.username
     
class UserInfo(models.Model):
    """
    用户信息类
    """
    GENDER_CHOICES = (
        ('M', '男'),
        ('F', '女'),
    )
     
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userinfo',)
    nickname = models.CharField(max_length=50)  # 昵称
    realname = models.CharField(max_length=50, blank=True)  # 实名
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')  # 性别
    birthday = models.DateField()  # 生日
    area = models.CharField(max_length=100, null=True)  # 地区
    description = models.TextField(null=True)  # 简述
     
    def __str__(self):
        return self.nickname
 
    def get_gender(self):
        i = 0 if self.gender == 'M' else 1
        return self.GENDER_CHOICES[i][1]
     
class Tag(models.Model):
    """
    博文标签类
    """
    tag_name = models.CharField(max_length=64)
 
    def __unicode__(self):
        return self.tag_name
     
class Article(models.Model):
    """
    博文
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 博主
    title = models.CharField(max_length=100)  # 博客题目
    category = models.CharField(max_length=50, blank=True)  # 博客分类 可为空
    tag = models.ManyToManyField(Tag, blank=True)  # 博客标签 可为空
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = models.TextField(blank=True, null=True)  # 博客文章正文
 
    def get_absolute_url(self):
        path = reverse('myblog:detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path
     
    def __str__(self) :
        return self.title
 
    class Meta:
        ordering = ['-date_time']
