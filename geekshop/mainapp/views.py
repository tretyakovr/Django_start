from django.shortcuts import render
from .models import Products, Params, ProdParams, Category

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    params = Params.objects.all()
    category = Category.objects.all()
    products = Products.objects.all()
    prodparams = ProdParams.objects.all()

    return render(request, 'mainapp/products.html', {'params': params, 'products': products, 'prodparams': prodparams,
                                                     'category': category})


def contacts(request):
    return render(request, 'mainapp/contact.html')