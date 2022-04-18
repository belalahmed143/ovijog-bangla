from django.urls import path
from . import views
# from .views import NewsDetailsView

urlpatterns = [
    path('',views.index,name='index'),
    path('newscategory/<name>/',views.news, name='news'),
    path('newsdetails/<int:pk>',views.NewsDetails, name='news-details'),

    path('aboutus/',views.aboutus,name='aboutus'),
    path('privecy/',views.privecy,name='privecy'),
    path('contact/',views.contact,name='contact'),

]