from django.http import HttpResponse
from django.shortcuts import render

from ajax.models import User
from . import models


# from django.http import HttpResponse


# Create your views here.

def create_view(request):
    return render(request, '01-createxhr.html')


# 快捷键alt+Enter
def server02_view(request):
    return HttpResponse("这只server02的响应内容")


def ajaxget_view(request):
    return HttpResponse(request, "02-ajax-get.html")
    # return HttpResponse("02-ajax-get.html")


def getparams_view(request):
    return render(request, '03-ajax-get-params.html')


def server03_view(request):
    # 1. 接收前端传递过来的两个参数
    name = request.GET.get('name', '')
    # age  = request.GET['age']
    age = request.GET['age']
    # 2.响应数据给前段
    s = "姓名：%s,年龄：%s" % (name, age)
    return render(s)


def register_view(request):
    return render(request, '04-register.html')


def checkuname_view(request):
    # 1.接收前端传递过来的参数　uname
    uname = request.GET['uname']
    # 2.判断uname在数据库Users实体中是否存在[查询操作]
    # filter没有数据返回空，不会报错
    print('uname:' + uname)
    users = models.User.objects.filter(uname=uname)
    # 根据查询结果做出响应
    if users:
        return HttpResponse('1')  # 具体显示由前端自行处理

    return HttpResponse('0')


def reguser_view(request):
    # １．接收前端传过来的数据
    uname = request.GET['uname']
    upwd = request.GET['upwd']
    uemail = request.GET['uemail']
    nickname = request.GET['nickname']
    # ２．通过实体类实现增加操作(通过异常处理，处理增加失败的问题)
    try:
        User.objects.create(uname=uname,upwd=upwd,
                            uemail=uemail,nickname=nickname)
        return HttpResponse("1")
    except Exception as e:
        print(e)
        return HttpResponse("0")

def post_view(request):
    return render(request,"05-post.html")

def server05_view(request):
    # 拿数据做出响应
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    msg = "用户名：%s,密码：%s"%(uname,upwd)
    return HttpResponse(msg)

def regpost_view(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    uemail = request.POST['uemail']
    nickname = request.POST['nickname']
    # msg = "用户名：%s,密码：%s,邮箱：%s,昵称：%s" % (uname, upwd,uemail,nickname)
    try:
        User.objects.create(uname=uname,upwd=upwd,
                            uemail=uemail,nickname=nickname)
        return HttpResponse("1")
    except Exception as e:
        print(e)
        return HttpResponse("0")

def users_view(request):
    return render(request,'06-ajax-users.html')

def server06_view(request):
    users = User.objects.all()
    msg = ''
    for u in users:
        msg += "%s_%s_%s_%s_%s|"%(u.id,u.uname,u.upwd,u.uemail,u.nickname)
        msg = msg[0:-1]
    return HttpResponse(msg)
