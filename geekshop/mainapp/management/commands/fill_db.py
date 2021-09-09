from django.core.management.base import BaseCommand
import json, os
from mainapp.models import Category, Params, Products, ProdParams

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Так как на удаление родительской записи наложен RESTRICT при наличии дочерних,
        # то очищаем таблицы снизу вверх
        ProdParams.objects.all().delete()
        Products.objects.all().delete()
        Params.objects.all().delete()
        Category.objects.all().delete()

        categories = load_from_json('categories')

        for category in categories:
            new_category = Category(**category)
            new_category.save()

        params = load_from_json('params')

        for param in params:
            new_param = Params(**param)
            new_param.save()

        products = load_from_json('products')

        for product in products:
            # Получаем категорию по имени
            _category = Category.objects.get(name=product["category"])
            new_product = Products(category=_category, name=product["name"])
            new_product.save()

            for param in product["params"]:
                # Получаем параметр по имени
                _param = Params.objects.get(name=param["param_name"])
                new_prodparams = ProdParams(prod_name=new_product, param_name=_param, value=param["value"])
                new_prodparams.save()
