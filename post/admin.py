from django.contrib import admin

# Register your models here.

# 注册表中的信息，在站点中查看
from post.models import Category,Tag,Post
# 后台中的将三个模型表导入
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)




