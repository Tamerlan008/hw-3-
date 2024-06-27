from django.shortcuts import render
from apps.base.models import Base
# Create your views here.

def index(request):
    base = Base.objects.latest('id')
    return render(request, 'base/index-dark.html', locals())