from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from dishes.models import Product, Category
from .models import *
from django.views.decorators.http import require_GET, require_POST


class Dishes:
    def __init__(self, name, year, author, country, desc, image):
        self.name = name
        self.year = year
        self.author = author
        self.country = country
        self.description = desc
        self.image = image


def dishes_index(request):
    dish = Dishes('Яйцо «Бенедикт»', '1894', 'Лемюэль Бенедикт', 'США (Нью-Йорк)', 'Еще одно знаковое блюдо, родившееся в отеле Waldorf Astoria, обязано появлению на свет... похмелью. '
                  'Одним ясным утром 1894 года биржевой брокер с Уолл-стрит Лемюэль Бенедикт брел по улицам Нью-Йорка. '
                   'Настроение у него было отнюдь не безоблачным, так как мистер Бенедикт пил всю ночь и мучился от страшного '
                   'похмелья. В поисках еды он забрел в отель, где заказал на завтрак «тосты с маслом, два вареных яйца без скорлупы,'
                   ' бекон и голландский соус». Блюдо впечатлило уже известного нам метрдотеля ресторана Оскара Чирки, который '
                   'впоследствии внес блюдо в утреннее и обеденное меню, заменив тосты на хрустящие булочки, а бекон на ветчину. '
                   'Но имя брокера осталось увековечено в названии.', 'image/1.jpg')
    return render(request, 'dishes/index.html', {'dish': dish})


def queryset_to_json(some_objects):
    some_objects = serializers.serialize("json", some_objects)
    return json.loads(some_objects)


# ------------------------------- get all objects -------------------------------------
@require_GET
def product_list(request):
    return JsonResponse({"all_products": queryset_to_json(Product.objects.all())})


@require_GET
def category_list(request):
    return JsonResponse({"all_categories": queryset_to_json(Category.objects.all())})
# ------------------------------------------------------------------------------------


# ------------------------------- search by name -------------------------------------
@require_GET
def product_search(request, param):
    filtered_products = (Product.objects.filter(product_name__icontains=param) |
                         Product.objects.filter(ingredients__icontains=param) |
                         Product.objects.filter(description__icontains=param)).all()
    return JsonResponse({"products": queryset_to_json(filtered_products)})


@require_GET
def category_search(request, param):
    filtered_categories = Category.objects.filer(category_name__icontains=param).all()
    return JsonResponse({"categories": queryset_to_json(filtered_categories)})
# ------------------------------------------------------------------------------------


# --------------------------------- create object ------------------------------------
@csrf_exempt
@require_POST
def create_product(request):
    data = json.loads(request.body)
    product = Product.objects.create(product_name=data["product_name"],
                                     ingredients=data["ingredients"],
                                     description=data["description"],
                                     category=Category.objects.get(id=data["category"]))
    product.save()
    return JsonResponse({"status": "201 Created"})


@csrf_exempt
@require_POST
def create_category(request):
    data = json.loads(request.body)
    category = Category.objects.create(category_name=data["category_name"])
    category.save()
    return JsonResponse({"status": "201 Created"})
# ------------------------------------------------------------------------------------


@require_GET
def products_in_category(request, cat_id):
    filtered_products = (Product.objects.filter(category=cat_id)).all()
    return JsonResponse({"products_in_category": queryset_to_json(filtered_products)})


