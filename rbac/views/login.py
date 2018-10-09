import json

from rbac import models
from django.conf import settings
from rbac.services.init_permission import init_permission

from django.shortcuts import render ,redirect,HttpResponse


def login(request):
    """
    用户登陆
    :param request:
    :return:
    """

    if request.method == "GET":
        return render(request, "login.html")

    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    obj = models.UserInfo.objects.filter(name=user, password=pwd).first()

    if not obj:  # 用户不存在的时候
        return render(request, "login.html", {"msg": "用户名或密码错误"})

    # 获取这个用户的权限信息 一定要尽量的少去查询数据库并且要记得一个用户的角色可能有空也可能有重复的全限 的要去重

    # permissions_list = obj.roles.filter(permissions__url__isnull = False).values("permissions__url").distinct()

    # 必须要进行__isnull 因为可能它的权限是有为空的  我们以url来当多权限
    # 一个人有多个角色 多个角色的权限可能冲突所以要用去重

    request.session["user_info"] = {"id":obj.id,"name":obj.name}
    # request.session[settings.PERMISSION_SESSION_KEY] = list(permissions_list)  # 因为上面求出的你的url是一个 queryset不能放入session需要进行list强转
    init_permission(request,obj)  # 调用你的rbac中的设置的获取你的定义的内容值
    return redirect("/customer/list/")  # 登陆成功跳转到 课程界面
