data = [{'permissions__menu_id': 1, 'permissions__url': '/customer/list/', 'permissions__title': '客户列表', 'permissions__menu__title': '信息管理', 'permissions__menu__icon': 'fa-coffee'},
{'permissions__menu_id': None, 'permissions__url': '/customer/add/', 'permissions__title': '添加客户', 'permissions__menu__title': None, 'permissions__menu__icon': None},
{'permissions__menu_id': 1, 'permissions__url': '/payment/list/', 'permissions__title': '账单列表', 'permissions__menu__title': '信息管理', 'permissions__menu__icon': 'fa-coffee'}]



# menu_dict = {}  # 大字典

# permission_list = []
# for item in data:
#
#     # 判断你的信息是否已经存在了大字典中如果存在就把你的二级菜单的信息跟新
#     if item["permissions__menu_id"] in menu_dict:
#         # 更新
#         permission_list.append(
#             {
#                 "title":'permissions__url',
#                 "icon":'permissions__title'
#             }
#         )
#     else:
#         # 创建所有的新的
#         menu_dict = {
#             "icon":'permissions__menu__icon',
#             "title":'permissions__menu__title',
#             "children":
#                 {
#                     "title": 'permissions__menu__title',
#                     "icon": 'permissions__menu__icon'
#                 }
#
#         }
#
# print(menu_dict)


permission_list = []
menu_dict = {}  # 大字典
for item in data:
    permission_list.append(item['permissions__url'])  # 把你的权限的url加入其中
    if not item['permissions__menu_id']:
        continue  #是空就返回

    if item['permissions__menu_id'] in menu_dict:
        menu_dict["children"].append(
            {
                "title":'permissions__title',
                "url":'permissions__url',
            }
        )
    else:
        menu_dict = {
            "id":""
        }



