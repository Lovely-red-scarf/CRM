
import re
from django.conf import settings
from django.shortcuts import HttpResponse,redirect
from django.utils.deprecation import MiddlewareMixin

from rbac import models

# 定义一个中间件对你的内容进行校验

class RbacMiddleware(MiddlewareMixin):
    '''
    权限控制中间件
    '''

    # def process_request(self,request):
    #     #获取当前的url
    #     current_url = request.path_info
    #
    #     # 白名单处理
    #     for reg in settings.VALID_URL:  #循环我们在settings中配置的路由
    #         if re.match(reg,current_url):  #和你请求的路径进行匹配
    #             return   # 满足条件就跳过
    #
    #     # 2. 获取当前用户session中所有的权限  如果权限没有就返回
    #     permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
    #
    #     flag = None
    #     for item in permission_list:
    #         reg = "^%s/"%item.get('permissions__url')  # 给你的请求的权限设置正则匹配的符号
    #
    #
    #         re.match(reg,current_url)
    #         flag = True
    #         break
    #     if not flag:  #没有一个权限
    #         return HttpResponse("无权访问")


    def process_request(self,request):

        #首先获取你的当前请求的路径 url
        current_url = request.path_info

        # 白名单处理
        for reg in settings.VALID_URL:
            if re.match(reg,current_url):   #如果匹配上了 存在的时候
                return
        request.breadcrumb_list = [
            {'title': '首页', 'url': '/customer/list/$'},
        ]

        permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
        print(permission_dict)
        if not permission_dict:
            return redirect("/login/")  #重新去登陆
        flag = None
        for item in permission_dict.values():  # 对你最后的构造的字典中值进行循环
            id = item["id"]
            url = item["url"]
            title=item["title"]
            pid = item["pid"]
            pname = item["pname"]

            reg = "^%s$"%item.get("url") # 对你的url进行拼接加上正则的符号
            # reg = "^%s$" % item.get('url')
            if re.match(reg,current_url):
                flag = 1
                if pid:  # 父级id存在的话就是三级的菜单 你就要把二级和三级都加进去为了渲染
                    request.current_menu_id = pid
                    request.breadcrumb_list.extend([
                        {"title":permission_dict[pname]["title"],"url":permission_dict[pname]["url"]},  # 获取二级菜单
                        {"title":item["title"],"url":item["url"]}  # 获取的是三级的
                    ])
                else:  # 仅仅是二级菜单的时候 就直接添加进去
                    request.current_menu_id = id
                    request.breadcrumb_list.extend([

                        {"title": item["title"], "url": item["url"]}
                    ])

                break
        if not flag:
            return HttpResponse("没有权限")







