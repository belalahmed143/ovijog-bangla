from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Ovijog Bangla' 
admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(NewsLocation)
admin.site.register(Ads)
admin.site.register(HeadingDate)
