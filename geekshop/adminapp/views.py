from django.shortcuts import get_object_or_404, render
from authapp.models import ShopUser
from mainapp.models import Category, Params, Products, ProdParams
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm
from mainapp.forms import CategoryRegisterForm
from adminapp.forms import CategoryEditForm


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)


def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)


#-------------------------------------------------------
def categories(request):
    title = 'админка/категории'

    categories_list = Category.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


def category_create(request):
    title = 'категории товаров/создание'

    if request.method == 'POST':
        category_form = CategoryRegisterForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = CategoryRegisterForm()

    content = {'title': title, 'update_form': category_form}

    return render(request, 'adminapp/category_update.html', content)


def category_update(request, pk):
    title = 'категории товаров/редактирование'

    edit_category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        edit_form = CategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[edit_category.pk]))
    else:
        edit_form = CategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/category_update.html', content)


def category_delete(request, pk):
    title = 'категории товаров/удаление'

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        # вместо удаления лучше сделаем неактивным
        # user.is_active = False
        # user.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)


#-------------------------------------------------------
def params(request):
    title = 'админка/параметры товаров'

    params_list = Params.objects.all()

    content = {
        'title': title,
        'objects': params_list
    }

    return render(request, 'adminapp/params.html', content)


def params_create(request):
    pass


def params_update(request, pk):
    pass


def params_delete(request, pk):
    pass


#-------------------------------------------------------
def products(request, pk): # здесь pk - это id категории товара
    title = 'админка/продукт'

    category = get_object_or_404(Category, pk=pk)
    products_list = Products.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


def products_create(request, pk):
    pass


def products_read(request, pk):
    pass


def products_update(request, pk):
    pass


def products_delete(request, pk):
    pass


#-------------------------------------------------------
def prodparams(request, pk): # здесь pk - это id товара(!)
    title = 'админка/параметры товара'

    # params_list = get_object_or_404(Params, pk=pk)
    product = get_object_or_404(Products, pk=pk)
    prodparams_list = ProdParams.objects.filter(product__pk=pk).order_by('param_name')

    content = {
        'title': title,
        'product': product,
        'objects': prodparams_list,
    }

    return render(request, 'adminapp/prodparams.html', content)


def prodparams_create(request, pk):
    pass


def prodparams_read(request, pk):
    pass


def prodparams_update(request, pk):
    pass


def prodparams_delete(request, pk):
    pass
