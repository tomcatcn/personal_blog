from django.shortcuts import render
from user.models import User
from index.models import *
from django.views.decorators.cache import cache_page

# Create your views here.

# @cache_page(30)
def index_view(request):
    #从数据库中加载内容
    #文章类型列
    categorys = Category.objects.all()


    #文章内容,加载10个
    articles = Article.objects.all()[:10]

    #特别推荐内容,选取数据库阅读数量最多的5个文章
    sp_articles = Article.objects.order_by('-read_nums')[:5]

    #首页右侧推荐内容，选取阅读数量最多的两个
    right_articles = Article.objects.order_by('-read_nums')[:2]

    #首页左侧的内容，选取阅读量对多的三个
    left_articles = Article.objects.order_by('-read_nums')[:3]

    import time
    t1 = time.time()
    #检查cookie
    if request.COOKIES.get('u_id'):
        # 数据库查找出用户信息，并显示在主页上
        u_id = request.COOKIES.get('u_id')
        user = User.objects.get(id=u_id)
        username = user.username
        print('user shi '+username)
        return render(request,'index/index.html',locals())

    return render(request,'index/index.html',locals())