from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q

class EmailOrUsernameModelBackend(ModelBackend):
    """自定义认证后端：支持用户名或邮箱登录"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 查找用户名或邮箱匹配的用户
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None