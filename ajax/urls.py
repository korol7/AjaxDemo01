from django.conf.urls import url
from . import views

urlpatterns=[
    # 演示创建xhr
    url(r'^01-createxhr$',views.create_view),
    #演示使用ajax发送get请求的步骤
    url(r'^02-server/$',views.server02_view),
    url(r'^02-ajax-get/$',views.ajaxget_view),
    #演示使用ajax发送请求并附带参数
    url(r'^03-ajax-get-params/$',views.getparams_view),
    url(r'^03-server/$',views.server03_view),

    #使用AJAX完成注册操作
    url(r'^04-register',views.register_view),
    url(r'^04-checkuname',views.checkuname_view),
    url(r'^04-reguser/$',views.reguser_view),
    # post请求
    url(r'^04-regpost/$', views.regpost_view),

    #     使用AJAX发送POST请求
    url(r'^05-ajax-post/$',views.post_view),
    url(r"^05-server/$",views.server05_view),

#     06使用ＡＪＡＸ读取数据
    url(r'^06-server',views.server06_view),
#     在前端中处理JSON格式字符串
    url("^07-json/$",views.json_view),

]