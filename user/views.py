from django.shortcuts import render,redirect
from user.models import *

# Create your views here.

#处理登录请求
def log_view(request):
    #如果是get方法，返回登录页面
    if request.method == "GET":
        return render(request,'user/login.html')
    #如果是post方法，与数据库对比，如果正确就返回主页，错误继续返回登录页面
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('pwd')
        #如果查找返回空，重定向回登录
        user = User.objects.filter(username=username,password=password)

        if user:
            #登录成功，自动加上cookie
            resp = render(request,'user/login_success.html')
            resp.set_cookie('u_id',user[0].id)
            return resp
        #不成功重回登录界面
        return redirect('/user/login')

#处理注册请求
def reg_view(request):
    # 如果是get方法，返回注册页面
    if request.method == "GET":
        return render(request, 'user/register.html')
    # 如果是post方法，插入数据库，错误继续返回登录页面
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('pwd')
        # 如果创建用户成功，返回注册成功页面
        user = User.objects.create(username=username, password=password)

        if user:
            # 注册，自动加上cookie
            resp = render(request, 'user/register_success.html')
            resp.set_cookie('u_id', user.id)
            return resp
        # 不成功重回登录界面
        return redirect('/user/reg')


