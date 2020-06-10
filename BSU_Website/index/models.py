from django.db import models

# Create your models here.
class Articles(models.Model):
    article_title = models.CharField(max_length= 100)
    article_author = models.CharField(max_length = 25)
    article_body = models.TextField()
    article_date = models.DateTimeField("date_published")