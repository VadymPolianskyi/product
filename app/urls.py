from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [
    # user urls
    url(r'^registration/$', views.UserFormView.as_view(), name='registration'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),

    #product urls
    url(r'^(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)$', views.DetailProductView.as_view(), name='detail_product'),
    url(r'^(?P<category_slug>[\w-]+)/product/add/$', views.create_song, name='product_create'),
    url(r'^last-added/24/$', views.ProductsView.as_view(), name='last_added'),

    #category urls
    url(r'^$', views.CategoriesView.as_view(), name='main'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailCategoryView.as_view(), name='detail_category'),
    url(r'^category/add/$', views.CategoryCreate.as_view(), name='category_create'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.CategoryUpdate.as_view(), name='category_update'),
    url(r'^category/(?P<slug>[\w-]+)/delete/$', views.CategoryDelete.as_view(), name='category_delete'),

]