import adminapp.views as adminapp
from django.urls import re_path, path

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^users/create/', adminapp.user_create, name='user_create'),
    # path('users/read/', adminapp.users, name='users'),
    re_path(r'^users/read/', adminapp.UsersListView.as_view(), name='users'),
    re_path(r'^users/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path(r'^users/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),

    # path('categories/create/', adminapp.category_create, name='category_create'),
    re_path(r'^categories/create/', adminapp.CategoryCreateView.as_view(), name='category_create'),
    re_path(r'^categories/read/', adminapp.categories, name='categories'),
    # path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    re_path(r'^categories/update/(?P<pk>\d+)/$', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    re_path(r'^categories/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),

    re_path(r'^params/create/', adminapp.params_create, name='params_create'),
    re_path(r'^params/read/', adminapp.params, name='params'),
    re_path(r'^params/update/(?P<pk>\d+)/$', adminapp.params_update, name='params_update'),
    re_path(r'^params/delete/(?P<pk>\d+)/$', adminapp.params_delete, name='params_delete'),

    re_path(r'^products/create/category/(?P<pk>\d+)/$', adminapp.product_create, name='product_create'),
    re_path(r'^products/read/category/(?P<pk>\d+)/$', adminapp.products, name='products'),
    path('products/read/category/<int:pk>/page/<int:page>', adminapp.products, name='products'),
    # path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    re_path(r'^products/read/(?P<pk>\d+)/$', adminapp.ProductDetailView.as_view(), name='product_read'),
    re_path(r'^products/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path(r'^products/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),

    re_path(r'^prodparams/create/products/(?P<pk>\d+)/$', adminapp.prodparams_create, name='prodparams_create'),
    re_path(r'^prodparams/read/products/(?P<pk>\d+)/$', adminapp.prodparams, name='prodparams'),
    re_path(r'^prodparams/read/(?P<pk>\d+)/$', adminapp.prodparams_read, name='prodparams_read'),
    re_path(r'^prodparams/update/(?P<pk>\d+)/$', adminapp.prodparams_update, name='prodparams_update'),
    re_path(r'^prodparams/delete/(?P<pk>\d+)/$', adminapp.prodparams_delete, name='prodparams_delete')
]
