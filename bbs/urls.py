from django.urls import path
from bbs import views


urlpatterns = [
    path('', views.index, name='index'),
    path('adverts/', views.AdvertListView.as_view(), name='adverts'),
    path('advert/<int:pk>', views.AdvertDetailView.as_view(), name='advert_detail'),
]
