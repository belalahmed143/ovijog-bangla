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
    news_cate = get_object_or_404(NewsCategory,name=name)
    posts =News.objects.filter(news_category=news_cate.id).order_by('-date')

    return render(request,'news_category.html', {'posts':posts, 'news_cate':news_cate})


def NewsDetails(request,pk):
    news =News.objects.all().order_by('-id')
    news_categorise = NewsCategory.objects.all()

    newsdetails = News.objects.get(pk=pk)
    newsdetails.news_view_count = newsdetails.news_view_count + 1
    newsdetails.save()
    context={
        'newsdetails':newsdetails,
        'news':news,
        'news_categorise':news_categorise
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