from django.db import models
from django.utils import timezone
# Create your models here.

class NewsCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class NewsLocation(models.Model):
    district = models.CharField(max_length = 150)
    division  = models.ForeignKey('self', related_name='chaild', on_delete=models.CASCADE,blank=True, null=True)
    division_status  = models.BooleanField( default=False)
    
    def __str__(self):
        return self.district 

class News(models.Model):
    news_category =models.ForeignKey(NewsCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Picture',blank='True')
    title = models.CharField(max_length=200)
    news_location = models.ForeignKey(NewsLocation, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    news_view_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.news_category.name + ' // ' +self.title



class Ads(models.Model):
    PAGE_NAME=(
        ('homepage', 'homepage'),
        ('detailpage', 'detailpage'),
        ('categorypage', 'categorypage'),
    )
    title = models.CharField(max_length = 150)
    image = models.FileField(upload_to='ads_img')
    ads_show_page = models.CharField(max_length = 100, choices=PAGE_NAME)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-id']
    
class HeadingDate(models.Model):
    date = models.CharField(max_length=50)


    def __str__(self):
        return self.date



    

