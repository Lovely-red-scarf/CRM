import re

from django.template import Library
from django.conf import settings

register = Library()


@register.inclusion_tag('rbac/menu.html')   # 这个装饰器式先加载这个html界面然后再去下面拿到数据进行渲染这个界面
def menu(request):
    """
    生成菜单
    :param request:
    :return:
    """
    permission_dict = request.session[settings.PERMISSION_SESSION_KEY]  #取出所有的权限的 、url
    menu_dict = request.session[settings.MENU_SESSION_KEY]   # 获取菜单的信息

    # print(menu_list)
    # for item in menu_list:
    #     print(item)
    #     reg = "^%s$"%item['permissions__url']
    #     if re.match(reg,request.path_info):
    #         item["class"] = "active"  #如果这个菜单式存在的就设置一个默认选中的项
    print(menu_dict,)

    return {"menu_dict":menu_dict }  # 把你的这个菜单信息返回出去

@register.inclusion_tag("rbac/breadcrumb.html")
def breadcrumb(request,*args,**kwargs):
    return {"breadcrumb_list":request.breadcrumb_list}  # 取到你在中间件中返回的信息



@register.filter()

def has_permission(request,name):
    permission_dict = request.session.get(settings.PERMISSION_SESSION_KEY)
    if name in permission_dict:
        return True
