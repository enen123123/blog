from django.template import Library

register=Library()

@register.filter
def md(value):
    # 需要settings安装Markdown
    import markdown
    # 解析数据,将txt转化成html格式,将代码结构化展示
    return markdown.markdown(value)

