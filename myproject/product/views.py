from django.shortcuts import render
from product.models import category


# Create your views here.
def index(request):
    list_category = category.objects.all()
    context = {
        'list_category': list_category
    }
    return render(request, "index.html", context)


def detail(request, category_id):
    cate = category.objects.get(pk=category_id) #pk=primary_key hoac ten truong trong model
    context = {
        'cate123': cate #key=value
    }
    return render(request, "detail.html", context)
