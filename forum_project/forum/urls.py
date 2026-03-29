from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # 首页
    path('', views.index, name='index'),
    path('index/', views.index),  # 保持兼容性

    # 帖子操作
    path('post/new/', views.create_post, name='create_post'),  # 统一使用这个名称
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # 互动功能
    path('post/<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('post/<int:pk>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('post/<int:post_pk>/comment/', views.add_comment, name='add_comment'),

    # 用户系统
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='forum/login.html'), name='login'),
    # 注意：LogoutView 在 Django 5.x 中通常需要 POST 请求，或者在 settings 中配置
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/', views.profile, name='profile'),

    # 找回密码：确保 views.simple_password_reset 渲染的是正确的 html 文件
    path('password-reset/', views.simple_password_reset, name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='forum/password_reset_done.html'),
         name='password_reset_done'),
]