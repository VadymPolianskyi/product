from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [

    url(r'^$', views.CategoriesView.as_view(), name='main'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailCategoryView.as_view(), name='detail_category'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)$', views.DetailProductView.as_view(), name='detail_product'),
    url(r'^category/add/$', views.CategoryCreate.as_view(), name='category_create'),
    url(r'^last-added/24/$', views.ProductsView.as_view(), name='last_added'),
]