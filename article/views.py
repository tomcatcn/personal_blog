from django.shortcuts import render,redirect
from index.models import *
from user.models import User
# Create your views here.

#检查用户权限装饰器
def check_user(func):
    def wrapper(request,*args,**kwargs):
        u_id = request.COOKIES.get('u_id')
        print('u_id',u_id)
        if u_id:
            return func(request, *args, **kwargs)
        return redirect('/')

    return wrapper

#处理显示文章列表请求
def list_views(request):
    # 文章类型列
    categorys = Category.objects.all()

    #查找所有的文章列表
    articles = Article.objects.all()

    # 特别推荐内容,选取数据库阅读数量最多的5个文章
    sp_articles = Article.objects.order_by('-read_nums')[:5]

    # 检查cookie
    if request.COOKIES.get('u_id'):
        # 数据库查找出用户信息，并显示在主页上
        u_id = request.COOKIES.get('u_id')
        user = User.objects.get(id=u_id)
        username = user.username

        return render(request, 'article/list.html', locals())

    print(locals())
    return render(request,'article/list.html',locals())

#处理写请求
@check_user
def write_view(request):
    # 文章类型列
    categorys = Category.objects.all()

    # 特别推荐内容,选取数据库阅读数量最多的5个文章
    sp_articles = Article.objects.order_by('-read_nums')[:3]

    # 数据库查找出用户信息，并显示在主页上
    u_id = request.COOKIES.get('u_id')

    user = User.objects.get(id=u_id)
    username = user.username
    print('user shi ' + username)

    return render(request,'article/write.html',locals())



#处理写内容,等待异步处理
def write_submit_view(request):
    #写完成功后，返回文章列表
    # TODO
    return redirect('/article/list')

#处理显示内容请求
def details_view(request,article_id):
    # 文章类型列
    categorys = Category.objects.all()
    # 特别推荐内容,选取数据库阅读数量最多的5个文章
    sp_articles = Article.objects.order_by('-read_nums')[:5]
    #数据库找出要显示的文章
    article_one = Article.objects.get(id=article_id)
    if request.COOKIES.get('u_id'):
        # 数据库查找出用户信息，并显示在主页上
        u_id = request.COOKIES.get('u_id')
        user = User.objects.get(id=u_id)
        username = user.username
        print('user shi ' + username)
        return render(request, 'article/details.html', locals())
    return render(request,'article/details.html',locals())







