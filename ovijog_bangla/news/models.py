from django.db import models
from django.utils import timezone
# Create your models here.

class NewsCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class News(models.Model):
    news_category =models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Picture',blank='True')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    news_view_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.news_category.name + ' // ' +self.title

class HeadingDate(models.Model):
    date = models.CharField(max_length=50)


    def __str__(self):
        return self.date



    

