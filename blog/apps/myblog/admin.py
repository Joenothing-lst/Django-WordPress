from django.contrib import admin
from .models import BigCategory
from .models import Article
from .models import Tag
from .models import Keyword
from .models import FriendLink
from .models import Activate
from .models import Category
from .models import Carousel

# Register your models here.
admin.site.register((BigCategory, Category, Activate, Article, Tag, Keyword, FriendLink, Carousel))