from django.urls import path

from products.views import ListProductsView, RegisterProductView, FilterProductsByCategoryView

urlpatterns = [
    path('products/list/', ListProductsView.as_view(), name='list-products'),
    path('products/register/', RegisterProductView.as_view(), name='register-product'),
    path('products/filter/', FilterProductsByCategoryView.as_view(), name='filter-products'),
]