from django.shortcuts import render
from mysite.models import *
# Create your views here.

def home(request):
    orders = OrderProduct.objects.all()
    return render(request, 'mysite/index.html', {'orders': orders})