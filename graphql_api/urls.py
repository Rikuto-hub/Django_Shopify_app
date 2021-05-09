from django.urls import path

from . import views


urlpatterns = [
    path('shop', views.ShopView.as_view()),
    path('product', views.ProductView.as_view()),
    path('collection', views.CollectionView.as_view()),
    path('customer', views.CustomerView.as_view()),
]
