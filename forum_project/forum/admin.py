from django.contrib import admin
from .models import Tag, Post, Comment  # 导入你的实体模型

# 注册模型
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
