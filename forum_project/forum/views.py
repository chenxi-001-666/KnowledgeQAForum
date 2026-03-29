import markdown
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PostForm
from .models import Post, Tag, Comment


# --- 内容展示逻辑 ---
@login_required(login_url='login')
def index(request):
    # 基础查询集
    posts = Post.objects.all().order_by('-created_at')
    tags = Tag.objects.all()

    # 获取筛选参数
    current_tag = request.GET.get('tag')
    search_query = request.GET.get('search')

    # 执行标签过滤
    if current_tag:
        posts = posts.filter(tags__name=current_tag)

    # 执行关键词搜索
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    context = {
        'posts': posts,
        'tags': tags,
        'current_tag': current_tag,
    }
    return render(request, 'forum/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Markdown 渲染逻辑（保持你之前的设置）
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
    post_html = md.convert(post.content)

    # 核心：只获取没有父评论的顶级评论，子评论通过模板递归或属性获取
    comments = post.comments.filter(parent=None).order_by('-created_at')

    return render(request, 'forum/post_detail.html', {
        'post': post,
        'post_html': post_html,
        'comments': comments,
    })
# --- 用户系统逻辑 ---

@login_required
def add_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')  # 获取父评论 ID（楼中楼关键）

        if content:
            parent_comment = None
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)

            # 创建评论
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content,
                parent=parent_comment
            )
    return redirect('post_detail', pk=post_pk)

def register(request):
    """注册视图"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'forum/register.html', {'form': form})


@login_required
def profile(request):
    # 核心：使用 request.user 过滤作者
    user_posts = Post.objects.filter(author=request.user).order_by('-created_at')

    # 如果你有收藏功能，也需要在这里获取
    # user_favorites = Favorite.objects.filter(user=request.user)

    return render(request, 'forum/profile.html', {
        'user_posts': user_posts,
        # 'user_favorites': user_favorites,
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m() # 必须写这一行，否则标签(Tags)存不进去
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form})

@login_required
def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=pk)

@login_required
def toggle_favorite(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.favorites.filter(id=request.user.id).exists():
        post.favorites.remove(request.user)
    else:
        post.favorites.add(request.user)
    return redirect('post_detail', pk=pk)

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 权限检查：只有作者本人才能删除
    if post.author != request.user:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('index')  # 删除后返回首页

    # 如果是 GET 请求，可以跳转到一个确认页面，或者直接在前端用 JS 弹窗拦截
    return render(request, 'forum/post_confirm_delete.html', {'post': post})

def password_reset(request):
    # 确保这里的路径和你修改的文件路径完全一致
    return render(request, 'forum/password_reset.html')

def simple_password_reset(request):
    error_msg = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        try:
            user = User.objects.get(username=username)
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password successfully reset, turn to login！")
                return redirect('login')
            else:
                error_msg = "Two passwords do not match"
        except User.DoesNotExist:
            error_msg = "User does not exist"

    return render(request, 'forum/password_reset.html', {'error_msg': error_msg})

# --- 找回密码补充说明 ---
# 找回密码通常直接在 urls.py 中调用 django.contrib.auth.views
# 除非需要自定义逻辑，否则不需要在 views.py 中重写。