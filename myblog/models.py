from django.db import models

class User(models.Model):
    """
    用户实体类
    """
    username = models.CharField(max_length=50) # 用户名
    password = models.CharField(max_length=50) # 密码
    email = models.CharField(max_length=320) # 邮箱
    create_date = models.DateTimeField('Date created') # 创建时间
    
    def __str__(self):
        return self.username