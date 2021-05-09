from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductView.as_view(), name='product_path'),
    path('collection/', views.CollectionView.as_view(), name='collection_path'),
    path('order/', views.OrderView.as_view(), name='order_path'),
]