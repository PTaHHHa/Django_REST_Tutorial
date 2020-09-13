from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from article.models import Article, Author
from .serializers import ArticleSerializer, AuthorSerializer
# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({'articles': serializer.data})


class AuthorView(APIView):
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response({'authors': serializer.data})