from django.urls import path
from .views import (product_list, category_list, product_search, category_search, create_product, create_category,
                    products_in_category, dishes_index)

urlpatterns = [
    path('', dishes_index, name='dishes_index'),
    path('products/', product_list, name='product_list'),
    path('categories/', category_list, name='category_list'),
    path('product/search/q=<str:param>', product_search, name='product_search'),
    path('category/search/q=<str:param>', category_search, name='category_search'),
    path('product/create/', create_product, name='create_product'),
    path('category/create/', create_category, name='create_category'),
    path('category/n=<int:cat_id>', products_in_category, name='products_in_category'),
]
