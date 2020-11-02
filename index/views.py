from django.shortcuts import render
from user.models import User

# Create your views here.

def index_view(request):
    #检查cookie
    if request.COOKIES.get('u_id'):
        # 数据库查找出用户信息，并显示在主页上
        u_id = request.COOKIES.get('u_id')
        user = User.objects.get(id=u_id)
        username = user.username
        print('user shi '+username)
        return render(request,'index/index.html',locals())

    return render(request,'index/index.html')