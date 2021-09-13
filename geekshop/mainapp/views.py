from django.shortcuts import render
from .models import Products, Params, ProdParams, Category
from basketapp.models import Basket
from django.shortcuts import get_object_or_404

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    print(pk)

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    params = Params.objects.all()
    prodparams = ProdParams.objects.all()

    title = 'продукты'
    links_menu = Category.objects.all()

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
            'prodparams': prodparams
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = Products.objects.all()[3:5]
    category = Category.objects.all()

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'params': params,
        'prodparams': prodparams,
        'category': category
    }

    return render(request, 'mainapp/products.html', content)

    # products = Products.objects.all()

    # return render(request, 'mainapp/products.html', {'params': params, 'products': products, 'prodparams': prodparams,
    #                                                  'category': category})


def contacts(request):
    return render(request, 'mainapp/contact.html')
