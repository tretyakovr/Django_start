from django.shortcuts import render
from .models import Products, Params, ProdParams, Category
from basketapp.models import Basket
from django.shortcuts import get_object_or_404
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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


def products(request, pk=None, page=1):

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    params = Params.objects.all()
    prodparams = ProdParams.objects.all()

    title = 'продукты'
    links_menu = Category.objects.filter(is_active=True)
    basket = get_basket(request.user)

    if pk is not None:
        if pk is not None:
            if pk == 0:
                category = {
                    'pk': 0,
                    'name': 'все'
                }
                # products = Products.objects.filter(is_active=True, category__is_active=True).order_by('price')
                products = Products.objects.filter(category__is_active=True).order_by('price')
            else:
                category = get_object_or_404(Category, pk=pk)
                # products = Products.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
                products = Products.objects.filter(category__pk=pk, category__is_active=True).order_by('price')

            paginator = Paginator(products, 2)
            try:
                products_paginator = paginator.page(page)
            except PageNotAnInteger:
                products_paginator = paginator.page(1)
            except EmptyPage:
                products_paginator = paginator.page(paginator.num_pages)

            content = {
                'title': title,
                'links_menu': links_menu,
                'category': category,
                'products': products_paginator,
                'basket': basket,
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
