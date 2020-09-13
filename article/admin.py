from django.contrib import admin
from article.models import Article, Author
# Register your models here.

admin.site.register(Author)
admin.site.register(Article)

