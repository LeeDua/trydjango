from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'prop1': obj.prop1,
        'title': obj.title
    }
    return render(request, "product/detail.html", context )