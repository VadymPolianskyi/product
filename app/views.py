# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from app.models import Category

ADDRESS_MAIN_HTML = 'app/main.html'


class MainView(generic.ListView):
    template_name = ADDRESS_MAIN_HTML
    context_object_name = 'all_categories'

    def get_queryset(self):
        return Category.objects.all()
