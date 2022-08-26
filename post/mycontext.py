from django.db.models import Count

from .models import *
# 原生查询
from django.db import connection

def getrightinfo(request):
    # 分类、获取记录数、排序
    r_cate_post=Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')
    # 近期文章
    r_recent_post=Post.objects.order_by('-created')[2:]
    # 获取游标
    cursor=connection.cursor()
    # 获取时间、表、年份月份排序、传参降序排序
    filepost=cursor.execute("select created,count('*') count from t_post GROUP by strftime('%Y-%m',created) order by count desc")
    # 获取对象，归档结果、通过控制台需要fetchall
    r_file_post=filepost.fetchall()
    print(r_file_post)
    return {'r_cate_post':r_cate_post,'r_recent_post':r_recent_post,'r_file_post':r_file_post}

# update t_post set created='2018-07-23 11-11-11.111111'where id=4;
# 数据控制台更改数据
