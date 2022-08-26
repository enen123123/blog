from django.db import models

# Create your models here.

class Category(models.Model):
    cname=models.CharField(max_length=20,unique=True,verbose_name='类别名')

    def __str__(self):
        return self.cname

    class Meta:
        db_table='t_category'
        verbose_name_plural='类别'


class Tag(models.Model):
    tname=models.CharField(max_length=20,unique=True,verbose_name='标签名')

    def __str__(self):
        return self.tname

    class Meta:
        db_table='t_tag'
        verbose_name_plural='标签'

# 富文本编辑器，可以将丰富上传的内容格式，配合markdown文件可实现图片，代码的形式转化
from ckeditor_uploader.fields import  RichTextUploadingField
class Post(models.Model):
    # 标题,简介,正文,日期
    title=models.CharField(max_length=20,unique=True,verbose_name='标题')
    desc=models.CharField(max_length=200,verbose_name='简介')
    # content=models.TextField(verbose_name='内容')
    # 修改模型类
    content = RichTextUploadingField(verbose_name='内容')
    # 创立时间和修改时间
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    # 删除字段
    isdelete=models.BooleanField(default=False,verbose_name='是否删除')
    # 外键
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='所属标签')
    # 多对多
    tag=models.ManyToManyField(Tag,verbose_name='所属类别')

    def __str__(self):
        return self.title

    class Meta:
        # 设置别名
        db_table='t_post'
        verbose_name_plural='帖子'









