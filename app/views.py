# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from app.models import Category, Product

ADDRESS_MAIN_HTML = 'app/main.html'
DETAIL_CATEGORY_ADDRESS = 'app/detail_category.html'
DETAIL_PRODUCT_ADDRESS = 'app/detail_product.html'


class MainView(generic.ListView):
    template_name = ADDRESS_MAIN_HTML
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()


class DetailCategoryView(generic.DetailView):
    model = Category
    template_name = DETAIL_CATEGORY_ADDRESS


class DetailProductView(generic.DetailView):
    model = Product
    template_name = DETAIL_PRODUCT_ADDRESS
