from django.contrib import admin

from .models import User, UserInfo, Article, Tag, Category

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'create_date')
    list_filter = ['create_date']
    search_fields = ['username']

admin.site.register(UserInfo)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Category)
