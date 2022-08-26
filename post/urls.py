from django.contrib import admin
from django.urls import path,re_path, include

from post import views

urlpatterns = [
    path('', views.Indexview.as_view()),
    # 正则可以带返回值,方便获取第几页之类
    re_path(r'^page/(\d+)$',views.Indexview.as_view()),
    re_path(r'^post/(\d+)$',views.Detailview.as_view()),
    re_path(r'^category/(\d+)$', views.getpostbyid),
    re_path(r'^archive/(?P<year>\d+)/(?P<month>\d+)$', views.getpostbycreated),
    re_path(r'^about/$', views.getabout),

]
