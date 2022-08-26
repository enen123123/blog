from django.shortcuts import render

# Create your views here.
from django.views import View
from post.models import Category,Tag,Post
# 分页
from django.core.paginator import Paginator




class Indexview(View):
    def get(self,request,num=1):
        num=int(num)
        # 查询所有帖子信息
        postlist=Post.objects.all().order_by('-created')
        # 创建分页器对象
        page_obj=Paginator(postlist,1)
        # 获取某一页数据
        pagepost=page_obj.page(num)
        # 页码数
        begin=num-int(3)
        if begin<1:
            begin=1;
        end=begin+5
        if end>page_obj.num_pages:
            end=page_obj.num_pages+1
        if end<6:
            begin=1;
        else:
            begin=end-5
        page_list=range(begin,end)

        return render(request,'index.html',{'postlist':pagepost,'page_list':page_list,'current_num':num})


class Detailview(View):
    def get(self,request,postid):
        postid=int(postid)
        post_obj=Post.objects.get(id=postid)

        return render(request,'detail.html',{'post_obj':post_obj})


def getpostbyid(request,categoryid):
    categoryid=int(categoryid)
    c_post=Post.objects.filter(category_id=categoryid)
    return render(request,'postlist.html',{'c_post':c_post})


def getpostbycreated(request,year,month):
    year=int(year)
    month=int(month)
    if year==0 and month==0:
        c_post=Post.objects.all()
    else:
        c_post=Post.objects.filter(created__year=year,created__month=month)
    return render(request,'postlist.html',{'c_post':c_post})


def getabout(request):
    return render(request,'about.html')