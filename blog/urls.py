"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

from blog.settings import DEBUG, MEDIA_ROOT

urlpatterns = [
    # 后台admin地址
    path('admin/', admin.site.urls),
    # 根目录下创建的次地址
    path('',include('post.urls')),
    # 配置项目包映射路径
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # 配置搜索地址
    path('search/', include('haystack.urls')),

]

from django.views.static import serve
if DEBUG:
    urlpatterns+=re_path(r'^media/(?P<path>.*)/$',serve,{'document_root':MEDIA_ROOT}),


