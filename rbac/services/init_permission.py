from django.conf import settings


def init_permission(request,user,*args,**kwargs):
    """
    权限和菜单的信息初始化，以后使用时，需要在登陆成功后调用该方法将权限和菜单信息放入session中
    :param request:
    :param user:
    :return:
    """

    # 3 获取用户的信息和权限写入session中

    permission_queryset = user.roles.filter(permissions__url__isnull = False).values("permissions__url",
                                                                                    # "permissions__is_menu",
                                                                                    # "permissions__icon",
                                                                                    "permissions__title",
                                                                                     'permissions__name',
                                                                                     "permissions__id",
                                                                                     # 获取自己关联的信息
                                                                                     "permissions__parent_id",
                                                                                     'permissions__parent__name', # 跨到你的父级中的内容
                                                                                     
                                                                                     #获取一级菜单的信息
                                                                                     "permissions__menu__title",
                                                                                     "permissions__menu_id",  # 外键在建立的时候就会自定生成的一个外键字段_id 所以可以直接这样查到这个关联的表中的id
                                                                                     "permissions__menu__icon"
    ).distinct()  # 获取你的权限表中的 信息

    """
    {
        菜单id:{
            "titile":,
            icon
            children:{
                id,
                name,
                url
            }
        }
    }
    """

    permission_dict = {}  # 这个是用来存放二级菜单的信息
    menu_dict = {}  #最外面我们构造的大字典
    for item in permission_queryset:
        permission_dict[item['permissions__name']] = {
            "id":item["permissions__id"],
            "url":item["permissions__url"],
            "title":item["permissions__title"],
            "pid":item["permissions__parent_id"],  # 如果这个存在这个就是三级的
            'pname':item['permissions__parent__name'],

        }

        if not item["permissions__menu_id"]:  #如果菜单的信息不存在就不添加了
            continue
        if item["permissions__menu_id"] not in menu_dict:  #如果不存在就创建 整个字典内部的内容 如果存在就跟新它里面的二级菜单的信息
            menu_dict[item["permissions__menu_id"]] = {   # 让你的内部字典的key就是你的菜单的id作为字典的键
                "title": item["permissions__menu__title"],
                "icon": item["permissions__menu__icon"],
                "children":[  #二级菜单
                    {
                        "id":item["permissions__menu_id"],
                        "title": item["permissions__title"],
                        "url":item["permissions__url"]
                    },
                ]

            }
        else:  #如果存在的时候,只更新二级菜单中的内容
            menu_dict[item["permissions__menu_id"]]["children"] .append({
                        "id":item["permissions__menu_id"],
                        "title": item["permissions__title"],
                        "url":item["permissions__url"]
                    })
            print(permission_dict)

    request.session[settings.PERMISSION_SESSION_KEY] = permission_dict
    request.session[settings.MENU_SESSION_KEY] = menu_dict











    # permission_list = []  # 存放你的二级菜单的信息  以便于和你的settings中的信息进行匹配
    # menu_dict = {}  #大字典
    # for item in permission_queryset :
    #     permission_list.append({"permissions__url": item['permissions__url']})
    #     #如果一级菜单存在就更新不存在就创建
    #     if item["permissions__menu_id"] in menu_dict:
    #         # 存在就更新内容 跟新的应该是你的二级菜单的内容 因为1级的已经不变了
    #         menu_dict[item["permissions__menu__id"]]["menus"].append(
    #             {
    #                 "id":item["permissions__id"],
    #                 "title":item["permissions__title"],
    #                 "url":item["permissions__url"]
    #             }
    #         )
    #     else:  # 如果你的一级菜单不存在你的 字典中 创建
    #         if item["permissions__menu_id"]:
    #             menu_dict[item["permissions__menu_id"]] ={
    #                 "menu_title":item["permissions__menu__title"],
    #                 "menu_icon":item["permissions__menu__icon"],
    #                 "menus":{
    #                     "id":item["permissions__id"],
    #                     "title":item["permissions__title"],
    #                     "url":item["permissions__url"]
    #                 }
    #
    #             }
    #
    # request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    # request.session[settings.MENU_SESSION_KEY] = menu_dict
    # menu_list = []  #只是用来放置 你的菜单的信息
    # permission_list = [] # 放置你的所有的所有的url 就是你的所有的去权限
    # # 把你的菜单的信息和权限的信息分开放置 方便以后的取值
    # print(permission_queryset)
    # for row in permission_queryset:
    #     permission_list.append({"permissions__url": row['permissions__url',"id":"permissions__menu__id"],"title": "permissions__menu__title",})
    #     # permission_list.append({"permissions__url":row['permissions__url'],"permissions__menu__title":row["permissions__menu__title"]})  #把你获得的对象中的权限加入权限列表
    #
    #     if row["permissions__is_menu"]: #如果是可以做菜单的就取出你们对应的信息 然后加入menu_list 列表中
    #         menu_list.append({"id":row["permissions__id"],"title":row["permissions__title"],"icon":row["permissions__icon"],"url":row["permissions__url"]})
    #
    #
    #
    # request.session[settings.PERMISSION_SESSION_KEY] = permission_list  # 把你的权限信息放进去
    # request.session[settings.MENU_SESSION_KEY] = menu_list  # 把你的菜单放进session
    # print(request.session[settings.PERMISSION_SESSION_KEY])










