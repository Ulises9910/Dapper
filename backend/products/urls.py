from django.urls import path
from .views import (ProductListCreateView, ProductRetrieveUpdateDestroyView, 
                    CategoryListCreateView, CategoryRetrieveUpdateDestroyView)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
]