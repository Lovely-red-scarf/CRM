# CRM
这是一个权限控制到按钮级别的crm权限组件




####################################

首先组件是本人自定义的
操作系统:windows10+python3.5+Django1.11

此权限就是能访问的url  能进入的url愈来愈多就是权限越来越大

1：如果要登陆后台管理文件登陆账号：root 密码：root1234

2:首页的登陆比较简便 如有感觉简陋者 自行补充吧 
    登陆人的账号有三个
    登陆人1：赵云,密码：123456(此人有所有的权限)
    登陆人2：zyl，密码：123456（权限只有班主任的）
    登陆人3：操场小妹妹，密码：123456（权限是秘书）
    登陆人4：雷锋，密码：123456（学生）
    
    
 3：内部一共有两个app有rbac和web这两个app
    其中数据库放在web中的models.py文件中 并且前端的大部分界面都是在web中
    rbac中放置的是 所有的逻辑代码
    rbac中的middleware中的文件是中间件
    templatetags 是为了动态生成模板自定义的文件夹
    
    
