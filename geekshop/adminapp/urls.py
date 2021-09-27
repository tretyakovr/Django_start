import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users, name='users'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),

    path('params/create/', adminapp.params_create, name='params_create'),
    path('params/read/', adminapp.params, name='params'),
    path('params/update/<int:pk>', adminapp.params_update, name='params_update'),
    path('params/delete/<int:pk>', adminapp.params_delete, name='params_delete'),

    path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    path('products/read/category/<int:pk>/page/<int:page>', adminapp.products, name='products'),
    path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),

    path('prodparams/create/products/<int:pk>/', adminapp.prodparams_create, name='prodparams_create'),
    path('prodparams/read/products/<int:pk>/', adminapp.prodparams, name='prodparams'),
    path('prodparams/read/<int:pk>/', adminapp.prodparams_read, name='prodparams_read'),
    path('prodparams/update/<int:pk>/', adminapp.prodparams_update, name='prodparams_update'),
    path('prodparams/delete/<int:pk>/', adminapp.prodparams_delete, name='prodparams_delete')
]
