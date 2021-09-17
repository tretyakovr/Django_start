from django.shortcuts import render
from .models import Products, Params, ProdParams, Category
from basketapp.models import Basket
from django.shortcuts import get_object_or_404
import random


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Products.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Products.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    title = 'главная'

    products = Products.objects.all()[:6]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    params = Params.objects.all()
    prodparams = ProdParams.objects.all()

    title = 'продукты'
    links_menu = Category.objects.all()
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Products.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products = Products.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'params': params,
            'prodparams': prodparams,
        }

        return render(request, 'mainapp/products_list.html', content)

    # same_products = Products.objects.all()[3:5]
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    category = Category.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'params': params,
        'prodparams': prodparams,
        'category': category,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)

    # products = Products.objects.all()

    # return render(request, 'mainapp/products.html', {'params': params, 'products': products, 'prodparams': prodparams,
    #                                                  'category': category})


def contacts(request):
    return render(request, 'mainapp/contact.html')


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': Category.objects.all(),
        'product': get_object_or_404(Products, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)
