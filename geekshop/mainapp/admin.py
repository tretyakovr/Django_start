from django.contrib import admin
from .models import Category, Params, Products, ProdParams

admin.site.register(Category)
admin.site.register(Params)
admin.site.register(Products)
admin.site.register(ProdParams)

