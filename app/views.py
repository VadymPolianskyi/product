# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from app.models import Category, Product
from app.service.date_service import check_datetime

ADDRESS_MAIN_HTML = 'app/main.html'
ADDRESS_LAST_ADDED_HTML = 'app/last_added.html'
DETAIL_CATEGORY_ADDRESS = 'app/detail_category.html'
DETAIL_PRODUCT_ADDRESS = 'app/detail_product.html'
ADDRESS_CREATE_CATEGORY = 'app/create_category.html'

CATEGORY_FIELDS = ['name', 'slug', 'description']


class CategoriesView(generic.ListView):
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


class CategoryCreate(CreateView):
    template_name = ADDRESS_CREATE_CATEGORY
    model = Category
    fields = CATEGORY_FIELDS


class CategoryUpdate(UpdateView):
    template_name = ADDRESS_CREATE_CATEGORY
    model = Category
    fields = CATEGORY_FIELDS
    success_url = reverse_lazy('app:main')


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('app:main')


class ProductsView(generic.ListView):
    template_name = ADDRESS_LAST_ADDED_HTML
    context_object_name = 'all_products'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductsView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        products = Product.objects.all()
        result= set()
        for product in products:
            if check_datetime(product.created_at):
                result.add(product)
        return result


