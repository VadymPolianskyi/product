from django.conf.urls import url

from . import views

app_name = 'app'

urlpatterns = [

    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailCategoryView.as_view(), name='detail_category'),
    url(r'^detail/(?P<category_id>[0-9]+)/(?P<pk>[0-9]+)$', views.DetailProductView.as_view(), name='detail_product'),
]