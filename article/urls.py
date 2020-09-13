from django.contrib import admin
from django.urls import path
from article.views import ArticleView, AuthorView

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('authors/', AuthorView.as_view())
]