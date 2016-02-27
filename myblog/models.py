from django.db import models

class User(models.Model):
    """
    用户账号类
    """
    username = models.CharField(max_length=50) # 用户名
    password = models.CharField(max_length=50) # 密码
    email = models.EmailField() # 邮箱
    create_date = models.DateTimeField(auto_now_add=True) # 创建时间
    
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
    nickname = models.CharField(max_length=50) # 昵称
    realname = models.CharField(max_length=50, default="") # 实名
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')  # 性别
    birthday = models.DateField() #生日
    area = models.CharField(max_length=100, default="") # 地区
    description = models.TextField(default="") # 简述
    
    def __str__(self):
        return self.nickname

    def get_gender(self):
        i = 0 if self.gender == 'M' else 1
        return self.GENDER_CHOICES[i][1]