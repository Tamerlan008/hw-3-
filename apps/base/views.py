from django.shortcuts import render
from apps.base.models import Base, Peopular_category, Our_chef, News
# Create your views here.

def index(request):
    base = Base.objects.latest('id')
    category = Peopular_category.objects.all()
    chef = Our_chef.objects.all().order_by('?')[:3]
    news_all = News.objects.all().order_by('?')[:2]
    return render(request, 'base/index-dark.html', locals())