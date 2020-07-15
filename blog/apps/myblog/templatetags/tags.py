# 创建了新的tags标签文件后必须重启服务器

from django import template
from ..models import Article, Category, Tag, Carousel, FriendLink, BigCategory, Activate, Keyword
from django.db.models.aggregates import Count
from django.utils.html import mark_safe
import re

# 注册自定义标签函数
register = template.Library()


# 获取公告查询集
@register.simple_tag
def get_activate_text():
    """返回最新公告"""
    a = [i for i in Activate.objects.order_by('-add_date') if i.is_active]
    return a[0]


# 获取导航条大分类查询集
@register.simple_tag
def get_bigcategory_list():
    """返回大分类列表"""
    return BigCategory.objects.all()


# 返回文章分类查询集
@register.simple_tag
def get_category_list(id):
    """返回小分类列表"""
    return Category.objects.filter(bigcategory_id=id)


# 获取滚动的大幻灯片查询集、获取左侧的幻灯片查询集，这两个部分用的图片是一样的
@register.simple_tag
def get_carousel_index():
    return Carousel.objects.filter(number__lte=5)


# 获取右侧栏热门专题幻灯片查询集
@register.simple_tag
def get_carousel_right():
    return Carousel.objects.filter(number__gt=5, number__lte=10)


# 获取归档文章查询集
@register.simple_tag
def get_data_date():
    """获取文章发表的不同月份"""
    article_dates = Article.objects.datetimes('create_date', 'month', order='DESC')
    return article_dates


# 获取热门排行数据查询集，参数：sort 文章类型， num 数量
@register.simple_tag
def get_article_list(sort=None, num=None):
    """获取指定排序方式和指定数量的文章"""
    if sort:
        if num:
            return Article.objects.order_by(sort)[:num]
        return Article.objects.order_by(sort)
    if num:
        return Article.objects.all()[:num]
    return Article.objects.all()


# 获取文章标签信息，参数文章ID
@register.simple_tag
def get_tag_list():
    return Tag.objects.all()


# 获取友链
@register.simple_tag
def get_friends():
    return FriendLink.objects.all()


# 获取文章大分类
@register.simple_tag
def get_title(category):
    c = BigCategory.objects.filter(slug=category)
    if c:
        return c[0]