from django.conf.urls import url
from django.urls import path
from api import views

urlpatterns = [
    path('', views.api_root),
    url(r'^adverts/$', views.AdvertsListView.as_view(), name='api_adverts_list'),
    url(r'^advert/(?P<pk>\d+)/$', views.AdvertDetailView.as_view(), name='api_advert_detail'),
    url(r'^advert/create/$', views.AdvertCreateView.as_view(), name='api_advert_create'),
    url(r'^categories/$', views.CategoryListView.as_view(), name='api_categories_list'),
]
