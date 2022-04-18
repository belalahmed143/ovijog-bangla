from django.shortcuts import render,get_object_or_404
from .models import *
from django.views.generic import DetailView
from django.db.models import Count
# Create your views here.
def index(request):
    news_categorise = NewsCategory.objects.all()
    news =News.objects.all().order_by('-id')
    headingdate=HeadingDate.objects.all().order_by('-id')[:1]

    context={
        'news_categorise':news_categorise,
        'news':news,
    }
    return render(request, 'index.html',context)

def news(request, name):
    news_categorise = NewsCategory.objects.all()
    ads = Ads.objects.filter(ads_show_page='categorypage')[:1]
    ads2 = Ads.objects.filter(ads_show_page='categorypage')[1:2]
    news_cate = get_object_or_404(NewsCategory,name=name)
    posts =News.objects.filter(news_category=news_cate.id)[:1]
    posts1 =News.objects.filter(news_category=news_cate.id)[2:13]
    posts2 =News.objects.filter(news_category=news_cate.id)[13:15]
    posts3 =News.objects.filter(news_category=news_cate.id)[15:27]
    latest_news =News.objects.all().exclude(news_category=news_cate.id)
    top_view_news =News.objects.all().order_by('-news_view_count')


    context={
        'ads':ads,
        'ads2':ads2,
        'posts3':posts3,
        'posts2':posts2,
        'posts1':posts1,
        'posts':posts,
        'news_cate':news_cate, 
        'news_categorise':news_categorise,
        'latest_news':latest_news,
        'top_view_news':top_view_news
    }

    return render(request,'news_category.html',context)


def NewsDetails(request,pk):
    ads = Ads.objects.filter(ads_show_page='detailpage')[:1]
    ads2 = Ads.objects.filter(ads_show_page='detailpage')[1:2]
    top_view_news =News.objects.all().exclude(pk=pk).order_by('-news_view_count')[:50]
    news_categorise = NewsCategory.objects.all()
    newsdetails = News.objects.get(pk=pk)
    related_news =News.objects.filter(news_category=newsdetails.news_category).exclude(pk=pk)[:6] 
    news =News.objects.all().exclude(pk=pk)

    new_news = []
    for i in news:
        if i not in related_news:
            new_news.append(i)
    # print(new_news)
    
    newsdetails.news_view_count = newsdetails.news_view_count + 1
    newsdetails.save()
    context={
        'newsdetails':newsdetails,
        'news':news,
        'ads':ads,
        'ads2':ads2,
        'top_view_news': top_view_news,
        'related_news':related_news,
        'news_categorise':news_categorise,
        'new_news':new_news,
    }

    return render(request, 'news_detail.html',context)
    
def aboutus(request):
    return render(request, 'aboutus.html')


def privecy(request):

    return render(request, 'privecy.html')

def contact(request):

#     # if request.method == 'POST':
#     #     name = request.POST['name']
#     #     email = request.POST['email']
#     #     phone = request.POST['phone']
#     #     subject = request.POST['subject']
#     #     message = request.POST['message']
#     #     submit = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
#     #     messages.success(request, f'Successfully Submit')
#     #     submit.save()
#     #     return redirect('contact')
    return render(request, 'contact.html')