from django.contrib import admin

from page.models import MyUser, Post

admin.site.register(MyUser)
admin.site.register(Post)
