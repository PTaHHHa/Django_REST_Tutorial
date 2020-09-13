from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    # увеличивается за каждую публикацию, сделаю потом
    count_of_articles = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='author', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author}: {self.title}'
