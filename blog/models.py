from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    genre_choices = (
        ('education','Education'),
        ('politcs','Politics'),
        ('movie','Movie'),
        ('scifi','Science Ficiton'),
        
    )
    title=models.CharField(max_length=200)
    genre=models.CharField(max_length=50,choices=genre_choices,default='education')
    content=models.TextField()
    cover_image = models.ImageField(upload_to='article_image/',null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.title

class Comment(models.Model):
    text = models.CharField(max_length=300)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


