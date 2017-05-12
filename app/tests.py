# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase, Client

from app.models import Category, Product
from app.service.datetime_service import check_datetime

SUCCESS_STATUS_CODE = 200
FOUND_STATUS_CODE = 302
CLIENT = Client()

class BaseTestCase(TestCase):
    def setUp(self):
        Category.objects.create(id=1, name='First category', slug='first-category',
                                description='Some description of the category..').save()
        Product.objects.create(name='First product', slug='first-product', description='Some description of the product..',
                               price=1000, category_id=1, created_at=datetime.datetime.now(), modified_at = datetime.datetime.now()).save()
        self.first_category = Category.objects.get(name='First category')
        self.first_product = Product.objects.get(name='First product')


class CategoryTestCase(BaseTestCase):

    def test_category_get_all(self):
        response = CLIENT.get('/products/')
        assert response.status_code == SUCCESS_STATUS_CODE

    def test_category_detail(self):
        response = CLIENT.get('/products/' + self.first_category.slug + '/')
        assert response.status_code == SUCCESS_STATUS_CODE

    def test_category_add(self):
        response = CLIENT.post('/products/category/add/')
        assert response.status_code == SUCCESS_STATUS_CODE

    def test_category_delete(self):
        category_slug = 'second-category'
        Category.objects.create(id=2, name='Secong category', slug=category_slug,
                                description='Some description of the category..').save()
        response = CLIENT.post('/products/category/' + category_slug + '/delete/', {'slug': category_slug})
        # find and redirect to '/products' if success
        assert response.status_code == FOUND_STATUS_CODE

    def test_category_update(self):
        response = CLIENT.get('/products/category/' + self.first_category.slug + '/')
        assert response.status_code == SUCCESS_STATUS_CODE


class ProductTestCase(BaseTestCase):

    def test_product_unregistered_user_get_last_for_24(self):
        CLIENT.get('/products/logout/')
        assert CLIENT.get('/products/last-added/24/').status_code == FOUND_STATUS_CODE

    def test_product_detail(self):
        response = CLIENT.get('/products/' + self.first_category.slug + '/' + self.first_product.slug)
        assert response.status_code == SUCCESS_STATUS_CODE

    def test_product_add(self):
        response = CLIENT.get('/products/' + self.first_category.slug + '/product/add/')
        assert response.status_code == SUCCESS_STATUS_CODE


class UserTestCase(BaseTestCase):

    def test_user_logout(self):
        assert CLIENT.get('/products/logout/').status_code == SUCCESS_STATUS_CODE

    def test_user_login(self):
        assert CLIENT.get('/products/login/').status_code == SUCCESS_STATUS_CODE

    def test_user_registration(self):
        assert CLIENT.get('/products/registration/').status_code == SUCCESS_STATUS_CODE


class DateTimeServiceTestCase(TestCase):

    def test_datatime_include(self):
        now = datetime.datetime.now()
        assert check_datetime(now) == True

    def test_datatime_dont_include(self):
        now = datetime.datetime.now()
        compared = datetime.datetime(now.year, now.month, now.day - 3, now.hour, now.minute, now.second)
        assert check_datetime(compared) == False